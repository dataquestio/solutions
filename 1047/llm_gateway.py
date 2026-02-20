# llm_gateway.py

import os
import requests

import constants


class LLMGatewayError(Exception):
    """Raised when the gateway cannot return a valid response."""
    pass


def generate(provider, model, messages, max_tokens=constants.DEFAULT_MAX_TOKENS):
    """
    Send a chat-style request to either Together or Anthropic
    and return a normalized response.

    Returns:
        {
            "provider": "...",
            "model": "...",
            "text": "..."
        }
    """
    provider = provider.strip().lower()

    if provider == "together":
        text = _call_together(model, messages, max_tokens)

    elif provider == "anthropic":
        text = _call_anthropic(model, messages, max_tokens)

    else:
        raise LLMGatewayError("Unsupported provider. Use 'together' or 'anthropic'.")

    return {
        "provider": provider,
        "model": model,
        "text": text,
    }


def _call_together(model, messages, max_tokens):
    api_key = os.getenv("TOGETHER_API_KEY")
    if not api_key:
        raise LLMGatewayError("Missing TOGETHER_API_KEY.")

    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
    }

    response = requests.post(
        constants.TOGETHER_URL,
        headers=headers,
        json=payload,
        timeout=constants.DEFAULT_TIMEOUT,
    )

    if response.status_code != 200:
        raise LLMGatewayError("Together API error: " + response.text)

    data = response.json()
    choices = data.get("choices", [])
    return choices[0].get("message", {}).get("content") if choices else None


def _call_anthropic(model, messages, max_tokens):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise LLMGatewayError("Missing ANTHROPIC_API_KEY.")

    headers = {
        "x-api-key": api_key,
        "anthropic-version": constants.ANTHROPIC_VERSION,
        "Content-Type": "application/json",
    }

    system_text = None
    non_system_messages = []

    for msg in messages:
        if msg.get("role") == "system":
            system_text = msg.get("content")
        else:
            non_system_messages.append(msg)

    payload = {
        "model": model,
        "messages": non_system_messages,
        "max_tokens": max_tokens,
    }

    if system_text:
        payload["system"] = system_text

    response = requests.post(
        constants.ANTHROPIC_URL,
        headers=headers,
        json=payload,
        timeout=constants.DEFAULT_TIMEOUT,
    )

    if response.status_code != 200:
        raise LLMGatewayError("Anthropic API error: " + response.text)

    data = response.json()
    content = data.get("content", [])
    text_block = next((block for block in content if block.get("type") == "text"), None)
    return text_block.get("text") if text_block else None
