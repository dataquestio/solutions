{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "BbNlkiA8dw2i"
   },
   "source": [
    "# Profitable App Profiles for the App Store and Google Play Markets\n",
    "\n",
    "Our aim in this project is to find mobile app profiles that are profitable for the App Store and Google Play markets. We're working as data analysts for a company that builds Android and iOS mobile apps, and our job is to enable our team of developers to make data-driven decisions with respect to the kind of apps they build. \n",
    "\n",
    "At our company, we only build apps that are free to download and install, and our main source of revenue consists of in-app ads. This means that our revenue for any given app is mostly influenced by the number of users that use our app. Our goal for this project is to analyze data to help our developers understand what kinds of apps are likely to attract more users.\n",
    "\n",
    "## Opening and Exploring the Data\n",
    "\n",
    "As of September 2018, there were approximately 2 million iOS apps available on the App Store, and 2.1 million Android apps on Google Play.\n",
    "\n",
    "<center>\n",
    "![img](https://s3.amazonaws.com/dq-content/350/py1m8_statista.png)\n",
    "Source: [Statista](https://www.statista.com/statistics/276623/number-of-apps-available-in-leading-app-stores/)\n",
    "</center>\n",
    "\n",
    "Collecting data for over four million apps requires a significant amount of time and money, so we'll try to analyze a sample of data instead. To avoid spending resources with collecting new data ourselves, we should first try to see whether we can find any relevant existing data at no cost. Luckily, these are two data sets that seem suitable for our purpose:\n",
    "\n",
    "- [A data set](https://www.kaggle.com/lava18/google-play-store-apps) containing data about approximately ten thousand Android apps from Google Play. You can download the data set directly from [this link](https://dq-content.s3.amazonaws.com/350/googleplaystore.csv).\n",
    "- [A data set](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps) containing data about approximately seven thousand iOS apps from the App Store. You can download the data set directly from [this link](https://dq-content.s3.amazonaws.com/350/AppleStore.csv).\n",
    "\n",
    "Let's start by opening the two data sets and then continue with exploring the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "g5xdxIaYdw2j"
   },
   "outputs": [],
   "source": [
    "from csv import reader\n",
    "\n",
    "### The Google Play data set ###\n",
    "opened_file = open('googleplaystore.csv')\n",
    "read_file = reader(opened_file)\n",
    "android = list(read_file)\n",
    "android_header = android[0]\n",
    "android = android[1:]\n",
    "\n",
    "### The App Store data set ###\n",
    "opened_file = open('AppleStore.csv')\n",
    "read_file = reader(opened_file)\n",
    "ios = list(read_file)\n",
    "ios_header = ios[0]\n",
    "ios = ios[1:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "FeTuoAYVdw2n"
   },
   "source": [
    "To make it easier to explore the two data sets, we'll first write a function named `explore_data()` that we can use repeatedly to explore rows in a more readable way. We'll also add an option for our function to show the number of rows and columns for any data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "h22cRL40dw2p",
    "outputId": "21e603e4-b988-48dc-f8ec-069949de1e84"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']\n",
      "\n",
      "\n",
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['Coloring book moana', 'ART_AND_DESIGN', '3.9', '967', '14M', '500,000+', 'Free', '0', 'Everyone', 'Art & Design;Pretend Play', 'January 15, 2018', '2.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']\n",
      "\n",
      "\n",
      "Number of rows: 10841\n",
      "Number of columns: 13\n"
     ]
    }
   ],
   "source": [
    "def explore_data(dataset, start, end, rows_and_columns=False):\n",
    "    dataset_slice = dataset[start:end]    \n",
    "    for row in dataset_slice:\n",
    "        print(row)\n",
    "        print('\\n') # adds a new (empty) line between rows\n",
    "        \n",
    "    if rows_and_columns:\n",
    "        print('Number of rows:', len(dataset))\n",
    "        print('Number of columns:', len(dataset[0]))\n",
    "\n",
    "print(android_header)\n",
    "print('\\n')\n",
    "explore_data(android, 0, 3, True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "O1yZOnuXdw2x"
   },
   "source": [
    "We see that the Google Play data set has 10841 apps and 13 columns. At a quick glance, the columns that might be useful for the purpose of our analysis are `'App'`, `'Category'`, `'Reviews'`, `'Installs'`, `'Type'`, `'Price'`, and `'Genres'`.\n",
    "\n",
    "Now let's take a look at the App Store data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "8Gb1lsaAdw2y",
    "outputId": "715331b0-6c15-4e28-8f0c-e876f16c3e29"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']\n",
      "\n",
      "\n",
      "['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']\n",
      "\n",
      "\n",
      "['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']\n",
      "\n",
      "\n",
      "['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1']\n",
      "\n",
      "\n",
      "Number of rows: 7197\n",
      "Number of columns: 16\n"
     ]
    }
   ],
   "source": [
    "print(ios_header)\n",
    "print('\\n')\n",
    "explore_data(ios, 0, 3, True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "4nJCxwvydw22"
   },
   "source": [
    "We have 7197 iOS apps in this data set, and the columns that seem interesting are: `'track_name'`, `'currency'`, `'price'`, `'rating_count_tot'`, `'rating_count_ver'`, and `'prime_genre'`. Not all column names are self-explanatory in this case, but details about each column can be found in the data set [documentation](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps/home).\n",
    "\n",
    "\n",
    "## Deleting Wrong Data\n",
    "\n",
    "The Google Play data set has a dedicated [discussion section](https://www.kaggle.com/lava18/google-play-store-apps/discussion), and we can see that [one of the discussions](https://www.kaggle.com/lava18/google-play-store-apps/discussion/66015) outlines an error for row 10472. Let's print this row and compare it against the header and another row that is correct."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "cJxTPUn2dw23",
    "outputId": "1b752112-0fca-4303-d573-b18d1fb3d17a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']\n",
      "\n",
      "\n",
      "['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']\n",
      "\n",
      "\n",
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n"
     ]
    }
   ],
   "source": [
    "print(android[10472])  # incorrect row\n",
    "print('\\n')\n",
    "print(android_header)  # header\n",
    "print('\\n')\n",
    "print(android[0])      # correct row"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "quFWJnigdw2_"
   },
   "source": [
    "The row 10472 corresponds to the app _Life Made WI-Fi Touchscreen Photo Frame_, and we can see that the rating is 19. This is clearly off because the maximum rating for a Google Play app is 5 (as mentioned in the [discussions section](https://www.kaggle.com/lava18/google-play-store-apps/discussion/66015), this problem is caused by a missing value in the `'Category'` column). As a consequence, we'll delete this row. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "qjH4wG67dw3B",
    "outputId": "0dde0972-18a5-4784-d19d-c36eb9553652"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10841\n",
      "10840\n"
     ]
    }
   ],
   "source": [
    "print(len(android))\n",
    "del android[10472]  # don't run this more than once\n",
    "print(len(android))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "dE2D3beidw3G"
   },
   "source": [
    "## Removing Duplicate Entries\n",
    "\n",
    "### Part One\n",
    "If we explore the Google Play data set long enough, we'll find that some apps have more than one entry. For instance, the application Instagram has four entries:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "EqXZrUdNdw3G",
    "outputId": "2a625721-c86c-4913-ebb0-48be73303bf7"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "['Instagram', 'SOCIAL', '4.5', '66577446', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n",
      "['Instagram', 'SOCIAL', '4.5', '66509917', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']\n"
     ]
    }
   ],
   "source": [
    "for app in android:\n",
    "    name = app[0]\n",
    "    if name == 'Instagram':\n",
    "        print(app)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "c2GlTsJedw3L"
   },
   "source": [
    "In total, there are 1,181 cases where an app occurs more than once:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "BDUzP8jRdw3M",
    "outputId": "db3dce62-70db-42b0-cd7c-0f2ba2c84403"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of duplicate apps: 1181\n",
      "\n",
      "\n",
      "Examples of duplicate apps: ['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business', 'ZOOM Cloud Meetings', 'join.me - Simple Meetings', 'Box', 'Zenefits', 'Google Ads', 'Google My Business', 'Slack', 'FreshBooks Classic', 'Insightly CRM', 'QuickBooks Accounting: Invoicing & Expenses', 'HipChat - Chat Built for Teams', 'Xero Accounting Software']\n"
     ]
    }
   ],
   "source": [
    "duplicate_apps = []\n",
    "unique_apps = []\n",
    "\n",
    "for app in android:\n",
    "    name = app[0]\n",
    "    if name in unique_apps:\n",
    "        duplicate_apps.append(name)\n",
    "    else:\n",
    "        unique_apps.append(name)\n",
    "    \n",
    "print('Number of duplicate apps:', len(duplicate_apps))\n",
    "print('\\n')\n",
    "print('Examples of duplicate apps:', duplicate_apps[:15])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "xnPJT7Xmdw3R"
   },
   "source": [
    "We don't want to count certain apps more than once when we analyze data, so we need to remove the duplicate entries and keep only one entry per app. One thing we could do is remove the duplicate rows randomly, but we could probably find a better way.\n",
    "\n",
    "If you examine the rows we printed two cells above for the Instagram app, the main difference happens on the fourth position of each row, which corresponds to the number of reviews. The different numbers show that the data was collected at different times. We can use this to build a criterion for keeping rows. We won't remove rows randomly, but rather we'll keep the rows that have the highest number of reviews because the higher the number of reviews, the more reliable the ratings.\n",
    "\n",
    "To do that, we will:\n",
    "\n",
    "- Create a dictionary where each key is a unique app name, and the value is the highest number of reviews of that app\n",
    "- Use the dictionary to create a new data set, which will have only one entry per app (and we only select the apps with the highest number of reviews)\n",
    "\n",
    "### Part Two\n",
    "\n",
    "Let's start by building the dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "TYBPi8d9dw3T"
   },
   "outputs": [],
   "source": [
    "reviews_max = {}\n",
    "\n",
    "for app in android:\n",
    "    name = app[0]\n",
    "    n_reviews = float(app[3])\n",
    "    \n",
    "    if name in reviews_max and reviews_max[name] < n_reviews:\n",
    "        reviews_max[name] = n_reviews\n",
    "        \n",
    "    elif name not in reviews_max:\n",
    "        reviews_max[name] = n_reviews"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "r_T5VYoIdw3V"
   },
   "source": [
    "In a previous code cell, we found that there are 1,181 cases where an app occurs more than once, so the length of our dictionary (of unique apps) should be equal to the difference between the length of our data set and 1,181."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "wtGBkHKBdw3V",
    "outputId": "6a9c1c68-9ee5-4463-b4c2-797e8c705f78"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Expected length: 9659\n",
      "Actual length: 9659\n"
     ]
    }
   ],
   "source": [
    "print('Expected length:', len(android) - 1181)\n",
    "print('Actual length:', len(reviews_max))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "d27SheWrdw3Z"
   },
   "source": [
    "Now, let's use the `reviews_max` dictionary to remove the duplicates. For the duplicate cases, we'll only keep the entries with the highest number of reviews. In the code cell below:\n",
    "\n",
    "- We start by initializing two empty lists, `android_clean` and `already_added`.\n",
    "- We loop through the `android` data set, and for every iteration:\n",
    "    - We isolate the name of the app and the number of reviews.\n",
    "    - We add the current row (`app`) to the `android_clean` list, and the app name (`name`) to the `already_added` list if:\n",
    "        - The number of reviews of the current app matches the number of reviews of that app as described in the `reviews_max` dictionary; and\n",
    "        - The name of the app is not already in the `already_added` list. We need to add this supplementary condition to account for those cases where the highest number of reviews of a duplicate app is the same for more than one entry (for example, the Box app has three entries, and the number of reviews is the same). If we just check for `reviews_max[name] == n_reviews`, we'll still end up with duplicate entries for some apps."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "pRuxSg3Ddw3Z"
   },
   "outputs": [],
   "source": [
    "android_clean = []\n",
    "already_added = []\n",
    "\n",
    "for app in android:\n",
    "    name = app[0]\n",
    "    n_reviews = float(app[3])\n",
    "    \n",
    "    if (reviews_max[name] == n_reviews) and (name not in already_added):\n",
    "        android_clean.append(app)\n",
    "        already_added.append(name) # make sure this is inside the if block"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "KCyBLNlBdw3c"
   },
   "source": [
    "Now let's quickly explore the new data set, and confirm that the number of rows is 9,659."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "8xMT6nWtdw3c",
    "outputId": "498cc044-c355-4a65-9d2e-9e6c07923d24"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up']\n",
      "\n",
      "\n",
      "Number of rows: 9659\n",
      "Number of columns: 13\n"
     ]
    }
   ],
   "source": [
    "explore_data(android_clean, 0, 3, True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "JcdI8lpbdw3g"
   },
   "source": [
    "We have 9659 rows, just as expected.\n",
    "\n",
    "## Removing Non-English Apps\n",
    "\n",
    "### Part One\n",
    "\n",
    "If you explore the data sets enough, you'll notice the names of some of the apps suggest they are not directed toward an English-speaking audience. Below, we see a couple of examples from both data sets:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "mh8pNstMdw3h",
    "outputId": "32641067-3ccc-4232-87b9-5d8a56271e67"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "爱奇艺PPS -《欢乐颂2》电视剧热播\n",
      "【脱出ゲーム】絶対に最後までプレイしないで 〜謎解き＆ブロックパズル〜\n",
      "中国語 AQリスニング\n",
      "لعبة تقدر تربح DZ\n"
     ]
    }
   ],
   "source": [
    "print(ios[813][1])\n",
    "print(ios[6731][1])\n",
    "\n",
    "print(android_clean[4412][0])\n",
    "print(android_clean[7940][0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "KRvDytrbdw3m"
   },
   "source": [
    "We're not interested in keeping these kind of apps, so we'll remove them. One way to go about this is to remove each app whose name contains a symbol that is not commonly used in English text — English text usually includes letters from the English alphabet, numbers composed of digits from 0 to 9, punctuation marks (., !, ?, ;, etc.), and other symbols (+, *, /, etc.).\n",
    "\n",
    "All these characters that are specific to English texts are encoded using the ASCII standard. Each ASCII character has a corresponding number between 0 and 127 associated with it, and we can take advantage of that to build a function that checks an app name and tells us whether it contains non-ASCII characters.\n",
    "\n",
    "We built this function below, and we use the built-in `ord()` function to find out the corresponding encoding number of each character."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "AJ2xPuuDdw3n",
    "outputId": "cd533d78-9fc4-45d5-861d-b8af8528707f"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def is_english(string):\n",
    "    \n",
    "    for character in string:\n",
    "        if ord(character) > 127:\n",
    "            return False\n",
    "    \n",
    "    return True\n",
    "\n",
    "print(is_english('Instagram'))\n",
    "print(is_english('爱奇艺PPS -《欢乐颂2》电视剧热播'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "ghq_QFtbdw3q"
   },
   "source": [
    "The function seems to work fine, but some English app names use emojis or other symbols (™, — (em dash), – (en dash), etc.) that fall outside of the ASCII range. Because of this, we'll remove useful apps if we use the function in its current form."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "9n57U2gSdw3s",
    "outputId": "58570323-bd37-4969-9e68-9e2bd0f58708"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "False\n",
      "8482\n",
      "128540\n"
     ]
    }
   ],
   "source": [
    "print(is_english('Docs To Go™ Free Office Suite'))\n",
    "print(is_english('Instachat 😜'))\n",
    "\n",
    "print(ord('™'))\n",
    "print(ord('😜'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "5n_pvR_vdw3x"
   },
   "source": [
    "### Part Two\n",
    "\n",
    "To minimize the impact of data loss, we'll only remove an app if its name has more than three non-ASCII characters:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "moN9tdiQdw3x",
    "outputId": "a1e6aef7-2b8d-4c13-cced-ad24933f035a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def is_english(string):\n",
    "    non_ascii = 0\n",
    "    \n",
    "    for character in string:\n",
    "        if ord(character) > 127:\n",
    "            non_ascii += 1\n",
    "    \n",
    "    if non_ascii > 3:\n",
    "        return False\n",
    "    else:\n",
    "        return True\n",
    "\n",
    "print(is_english('Docs To Go™ Free Office Suite'))\n",
    "print(is_english('Instachat 😜'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Igmzo8IJdw31"
   },
   "source": [
    "The function is still not perfect, and very few non-English apps might get past our filter, but this seems good enough at this point in our analysis — we shouldn't spend too much time on optimization at this point.\n",
    "\n",
    "Below, we use the `is_english()` function to filter out the non-English apps for both data sets:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "sLb6Ncavdw32",
    "outputId": "6637a501-1e77-4c7b-a6b6-6f4c1914e325"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']\n",
      "\n",
      "\n",
      "['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up']\n",
      "\n",
      "\n",
      "Number of rows: 9614\n",
      "Number of columns: 13\n",
      "\n",
      "\n",
      "['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']\n",
      "\n",
      "\n",
      "['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']\n",
      "\n",
      "\n",
      "['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1']\n",
      "\n",
      "\n",
      "Number of rows: 6183\n",
      "Number of columns: 16\n"
     ]
    }
   ],
   "source": [
    "android_english = []\n",
    "ios_english = []\n",
    "\n",
    "for app in android_clean:\n",
    "    name = app[0]\n",
    "    if is_english(name):\n",
    "        android_english.append(app)\n",
    "        \n",
    "for app in ios:\n",
    "    name = app[1]\n",
    "    if is_english(name):\n",
    "        ios_english.append(app)\n",
    "        \n",
    "explore_data(android_english, 0, 3, True)\n",
    "print('\\n')\n",
    "explore_data(ios_english, 0, 3, True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "X1meBiKtdw36"
   },
   "source": [
    "We can see that we're left with 9614 Android apps and 6183 iOS apps.\n",
    "\n",
    "## Isolating the Free Apps\n",
    "\n",
    "As we mentioned in the introduction, we only build apps that are free to download and install, and our main source of revenue consists of in-app ads. Our data sets contain both free and non-free apps, and we'll need to isolate only the free apps for our analysis. Below, we isolate the free apps for both our data sets."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "4TXBzJVwdw38",
    "outputId": "f1c6694d-b2c1-4f89-a455-52ce2f1da0cf"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8864\n",
      "3222\n"
     ]
    }
   ],
   "source": [
    "android_final = []\n",
    "ios_final = []\n",
    "\n",
    "for app in android_english:\n",
    "    price = app[7]\n",
    "    if price == '0':\n",
    "        android_final.append(app)\n",
    "        \n",
    "for app in ios_english:\n",
    "    price = app[4]\n",
    "    if price == '0.0':\n",
    "        ios_final.append(app)\n",
    "        \n",
    "print(len(android_final))\n",
    "print(len(ios_final))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "wQhOlVV0dw3-"
   },
   "source": [
    "We're left with 8864 Android apps and 3222 iOS apps, which should be enough for our analysis.\n",
    "\n",
    "## Most Common Apps by Genre\n",
    "\n",
    "### Part One\n",
    "\n",
    "As we mentioned in the introduction, our aim is to determine the kinds of apps that are likely to attract more users because our revenue is highly influenced by the number of people using our apps.\n",
    "\n",
    "To minimize risks and overhead, our validation strategy for an app idea is comprised of three steps:\n",
    "\n",
    "1. Build a minimal Android version of the app, and add it to Google Play.\n",
    "2. If the app has a good response from users, we then develop it further.\n",
    "3. If the app is profitable after six months, we also build an iOS version of the app and add it to the App Store.\n",
    "\n",
    "Because our end goal is to add the app on both the App Store and Google Play, we need to find app profiles that are successful on both markets. For instance, a profile that might work well for both markets might be a productivity app that makes use of gamification.\n",
    "\n",
    "Let's begin the analysis by getting a sense of the most common genres for each market. For this, we'll build a frequency table for the `prime_genre` column of the App Store data set, and the `Genres` and `Category` columns of the Google Play data set.\n",
    "\n",
    "### Part Two\n",
    "\n",
    "We'll build two functions we can use to analyze the frequency tables:\n",
    "\n",
    "- One function to generate frequency tables that show percentages\n",
    "- Another function that we can use to display the percentages in a descending order"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "7CTAV3ULdw3_"
   },
   "outputs": [],
   "source": [
    "def freq_table(dataset, index):\n",
    "    table = {}\n",
    "    total = 0\n",
    "    \n",
    "    for row in dataset:\n",
    "        total += 1\n",
    "        value = row[index]\n",
    "        if value in table:\n",
    "            table[value] += 1\n",
    "        else:\n",
    "            table[value] = 1\n",
    "    \n",
    "    table_percentages = {}\n",
    "    for key in table:\n",
    "        percentage = (table[key] / total) * 100\n",
    "        table_percentages[key] = percentage \n",
    "    \n",
    "    return table_percentages\n",
    "\n",
    "\n",
    "def display_table(dataset, index):\n",
    "    table = freq_table(dataset, index)\n",
    "    table_display = []\n",
    "    for key in table:\n",
    "        key_val_as_tuple = (table[key], key)\n",
    "        table_display.append(key_val_as_tuple)\n",
    "        \n",
    "    table_sorted = sorted(table_display, reverse = True)\n",
    "    for entry in table_sorted:\n",
    "        print(entry[1], ':', entry[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "nxHDmzy-dw4B"
   },
   "source": [
    "### Part Three\n",
    "\n",
    "We start by examining the frequency table for the `prime_genre` column of the App Store data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "DdCoVYyndw4C",
    "outputId": "2027422a-3f94-4260-e298-545cfefafe6f"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Games : 58.16263190564867\n",
      "Entertainment : 7.883302296710118\n",
      "Photo & Video : 4.9658597144630665\n",
      "Education : 3.662321539416512\n",
      "Social Networking : 3.2898820608317814\n",
      "Shopping : 2.60707635009311\n",
      "Utilities : 2.5139664804469275\n",
      "Sports : 2.1415270018621975\n",
      "Music : 2.0484171322160147\n",
      "Health & Fitness : 2.0173805090006205\n",
      "Productivity : 1.7380509000620732\n",
      "Lifestyle : 1.5828677839851024\n",
      "News : 1.3345747982619491\n",
      "Travel : 1.2414649286157666\n",
      "Finance : 1.1173184357541899\n",
      "Weather : 0.8690254500310366\n",
      "Food & Drink : 0.8069522036002483\n",
      "Reference : 0.5586592178770949\n",
      "Business : 0.5276225946617008\n",
      "Book : 0.4345127250155183\n",
      "Navigation : 0.186219739292365\n",
      "Medical : 0.186219739292365\n",
      "Catalogs : 0.12414649286157665\n"
     ]
    }
   ],
   "source": [
    "display_table(ios_final, -5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "PJ46gVj1dw4G"
   },
   "source": [
    "We can see that among the free English apps, more than a half (58.16%) are games. Entertainment apps are close to 8%, followed by photo and video apps, which are close to 5%. Only 3.66% of the apps are designed for education, followed by social networking apps which amount for 3.29% of the apps in our data set. \n",
    "\n",
    "The general impression is that App Store (at least the part containing free English apps) is dominated by apps that are designed for fun (games, entertainment, photo and video, social networking, sports, music, etc.), while apps with practical purposes (education, shopping, utilities, productivity, lifestyle, etc.) are more rare. However, the fact that fun apps are the most numerous doesn't also imply that they also have the greatest number of users — the demand might not be the same as the offer. \n",
    "\n",
    "Let's continue by examining the `Genres` and `Category` columns of the Google Play data set (two columns which seem to be related)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "OjWHtqPIdw4H",
    "outputId": "1a7ee405-4f72-4086-9120-4256f8a6dfc0"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FAMILY : 18.907942238267147\n",
      "GAME : 9.724729241877256\n",
      "TOOLS : 8.461191335740072\n",
      "BUSINESS : 4.591606498194946\n",
      "LIFESTYLE : 3.9034296028880866\n",
      "PRODUCTIVITY : 3.892148014440433\n",
      "FINANCE : 3.7003610108303246\n",
      "MEDICAL : 3.531137184115524\n",
      "SPORTS : 3.395758122743682\n",
      "PERSONALIZATION : 3.3167870036101084\n",
      "COMMUNICATION : 3.2378158844765346\n",
      "HEALTH_AND_FITNESS : 3.0798736462093865\n",
      "PHOTOGRAPHY : 2.944494584837545\n",
      "NEWS_AND_MAGAZINES : 2.7978339350180503\n",
      "SOCIAL : 2.6624548736462095\n",
      "TRAVEL_AND_LOCAL : 2.33528880866426\n",
      "SHOPPING : 2.2450361010830324\n",
      "BOOKS_AND_REFERENCE : 2.1435018050541514\n",
      "DATING : 1.861462093862816\n",
      "VIDEO_PLAYERS : 1.7937725631768955\n",
      "MAPS_AND_NAVIGATION : 1.3989169675090252\n",
      "FOOD_AND_DRINK : 1.2409747292418771\n",
      "EDUCATION : 1.1620036101083033\n",
      "ENTERTAINMENT : 0.9589350180505415\n",
      "LIBRARIES_AND_DEMO : 0.9363718411552346\n",
      "AUTO_AND_VEHICLES : 0.9250902527075812\n",
      "HOUSE_AND_HOME : 0.8235559566787004\n",
      "WEATHER : 0.8009927797833934\n",
      "EVENTS : 0.7107400722021661\n",
      "PARENTING : 0.6543321299638989\n",
      "ART_AND_DESIGN : 0.6430505415162455\n",
      "COMICS : 0.6204873646209386\n",
      "BEAUTY : 0.5979241877256317\n"
     ]
    }
   ],
   "source": [
    "display_table(android_final, 1) # Category"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "PJR2QdJqdw4J"
   },
   "source": [
    "The landscape seems significantly different on Google Play: there are not that many apps designed for fun, and it seems that a good number of apps are designed for practical purposes (family, tools, business, lifestyle, productivity, etc.). However, if we investigate this further, we can see that the family category (which accounts for almost 19% of the apps) means mostly games for kids.\n",
    "\n",
    "\n",
    "[![img](https://s3.amazonaws.com/dq-content/350/py1m8_family.png)](https://play.google.com/store/apps/category/FAMILY?hl=en)\n",
    "\n",
    "\n",
    "Even so, practical apps seem to have a better representation on Google Play compared to App Store. This picture is also confirmed by the frequency table we see for the `Genres` column:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "pra8hj7_dw4K",
    "outputId": "e096aafb-c4cd-44c7-b6a1-061059f4079b"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tools : 8.449909747292418\n",
      "Entertainment : 6.069494584837545\n",
      "Education : 5.347472924187725\n",
      "Business : 4.591606498194946\n",
      "Productivity : 3.892148014440433\n",
      "Lifestyle : 3.892148014440433\n",
      "Finance : 3.7003610108303246\n",
      "Medical : 3.531137184115524\n",
      "Sports : 3.463447653429603\n",
      "Personalization : 3.3167870036101084\n",
      "Communication : 3.2378158844765346\n",
      "Action : 3.1024368231046933\n",
      "Health & Fitness : 3.0798736462093865\n",
      "Photography : 2.944494584837545\n",
      "News & Magazines : 2.7978339350180503\n",
      "Social : 2.6624548736462095\n",
      "Travel & Local : 2.3240072202166067\n",
      "Shopping : 2.2450361010830324\n",
      "Books & Reference : 2.1435018050541514\n",
      "Simulation : 2.0419675090252705\n",
      "Dating : 1.861462093862816\n",
      "Arcade : 1.8501805054151623\n",
      "Video Players & Editors : 1.7712093862815883\n",
      "Casual : 1.7599277978339352\n",
      "Maps & Navigation : 1.3989169675090252\n",
      "Food & Drink : 1.2409747292418771\n",
      "Puzzle : 1.128158844765343\n",
      "Racing : 0.9927797833935018\n",
      "Role Playing : 0.9363718411552346\n",
      "Libraries & Demo : 0.9363718411552346\n",
      "Auto & Vehicles : 0.9250902527075812\n",
      "Strategy : 0.9138086642599278\n",
      "House & Home : 0.8235559566787004\n",
      "Weather : 0.8009927797833934\n",
      "Events : 0.7107400722021661\n",
      "Adventure : 0.6768953068592057\n",
      "Comics : 0.6092057761732852\n",
      "Beauty : 0.5979241877256317\n",
      "Art & Design : 0.5979241877256317\n",
      "Parenting : 0.4963898916967509\n",
      "Card : 0.45126353790613716\n",
      "Casino : 0.42870036101083037\n",
      "Trivia : 0.41741877256317694\n",
      "Educational;Education : 0.39485559566787\n",
      "Board : 0.3835740072202166\n",
      "Educational : 0.3722924187725632\n",
      "Education;Education : 0.33844765342960287\n",
      "Word : 0.2594765342960289\n",
      "Casual;Pretend Play : 0.236913357400722\n",
      "Music : 0.2030685920577617\n",
      "Racing;Action & Adventure : 0.16922382671480143\n",
      "Puzzle;Brain Games : 0.16922382671480143\n",
      "Entertainment;Music & Video : 0.16922382671480143\n",
      "Casual;Brain Games : 0.13537906137184114\n",
      "Casual;Action & Adventure : 0.13537906137184114\n",
      "Arcade;Action & Adventure : 0.12409747292418773\n",
      "Action;Action & Adventure : 0.10153429602888085\n",
      "Educational;Pretend Play : 0.09025270758122744\n",
      "Simulation;Action & Adventure : 0.078971119133574\n",
      "Parenting;Education : 0.078971119133574\n",
      "Entertainment;Brain Games : 0.078971119133574\n",
      "Board;Brain Games : 0.078971119133574\n",
      "Parenting;Music & Video : 0.06768953068592057\n",
      "Educational;Brain Games : 0.06768953068592057\n",
      "Casual;Creativity : 0.06768953068592057\n",
      "Art & Design;Creativity : 0.06768953068592057\n",
      "Education;Pretend Play : 0.056407942238267145\n",
      "Role Playing;Pretend Play : 0.04512635379061372\n",
      "Education;Creativity : 0.04512635379061372\n",
      "Role Playing;Action & Adventure : 0.033844765342960284\n",
      "Puzzle;Action & Adventure : 0.033844765342960284\n",
      "Entertainment;Creativity : 0.033844765342960284\n",
      "Entertainment;Action & Adventure : 0.033844765342960284\n",
      "Educational;Creativity : 0.033844765342960284\n",
      "Educational;Action & Adventure : 0.033844765342960284\n",
      "Education;Music & Video : 0.033844765342960284\n",
      "Education;Brain Games : 0.033844765342960284\n",
      "Education;Action & Adventure : 0.033844765342960284\n",
      "Adventure;Action & Adventure : 0.033844765342960284\n",
      "Video Players & Editors;Music & Video : 0.02256317689530686\n",
      "Sports;Action & Adventure : 0.02256317689530686\n",
      "Simulation;Pretend Play : 0.02256317689530686\n",
      "Puzzle;Creativity : 0.02256317689530686\n",
      "Music;Music & Video : 0.02256317689530686\n",
      "Entertainment;Pretend Play : 0.02256317689530686\n",
      "Casual;Education : 0.02256317689530686\n",
      "Board;Action & Adventure : 0.02256317689530686\n",
      "Video Players & Editors;Creativity : 0.01128158844765343\n",
      "Trivia;Education : 0.01128158844765343\n",
      "Travel & Local;Action & Adventure : 0.01128158844765343\n",
      "Tools;Education : 0.01128158844765343\n",
      "Strategy;Education : 0.01128158844765343\n",
      "Strategy;Creativity : 0.01128158844765343\n",
      "Strategy;Action & Adventure : 0.01128158844765343\n",
      "Simulation;Education : 0.01128158844765343\n",
      "Role Playing;Brain Games : 0.01128158844765343\n",
      "Racing;Pretend Play : 0.01128158844765343\n",
      "Puzzle;Education : 0.01128158844765343\n",
      "Parenting;Brain Games : 0.01128158844765343\n",
      "Music & Audio;Music & Video : 0.01128158844765343\n",
      "Lifestyle;Pretend Play : 0.01128158844765343\n",
      "Lifestyle;Education : 0.01128158844765343\n",
      "Health & Fitness;Education : 0.01128158844765343\n",
      "Health & Fitness;Action & Adventure : 0.01128158844765343\n",
      "Entertainment;Education : 0.01128158844765343\n",
      "Communication;Creativity : 0.01128158844765343\n",
      "Comics;Creativity : 0.01128158844765343\n",
      "Casual;Music & Video : 0.01128158844765343\n",
      "Card;Action & Adventure : 0.01128158844765343\n",
      "Books & Reference;Education : 0.01128158844765343\n",
      "Art & Design;Pretend Play : 0.01128158844765343\n",
      "Art & Design;Action & Adventure : 0.01128158844765343\n",
      "Arcade;Pretend Play : 0.01128158844765343\n",
      "Adventure;Education : 0.01128158844765343\n"
     ]
    }
   ],
   "source": [
    "display_table(android_final, -4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "k7x0Mwv_dw4N"
   },
   "source": [
    "The difference between the `Genres` and the `Category` columns is not crystal clear, but one thing we can notice is that the `Genres` column is much more granular (it has more categories). We're only looking for the bigger picture at the moment, so we'll only work with the `Category` column moving forward.\n",
    "\n",
    "Up to this point, we found that the App Store is dominated by apps designed for fun, while Google Play shows a more balanced landscape of both practical and for-fun apps. Now we'd like to get an idea about the kind of apps that have most users.\n",
    "\n",
    "## Most Popular Apps by Genre on the App Store\n",
    "\n",
    "One way to find out what genres are the most popular (have the most users) is to calculate the average number of installs for each app genre. For the Google Play data set, we can find this information in the `Installs` column, but for the App Store data set this information is missing. As a workaround, we'll take the total number of user ratings as a proxy, which we can find in the `rating_count_tot` app."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "ET9Gx6Sadw4O"
   },
   "source": [
    "Below, we calculate the average number of user ratings per app genre on the App Store:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "J_5ACupHdw4T",
    "outputId": "af0fc1fe-a241-4390-f786-3a784b29c7fa"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Social Networking : 71548.34905660378\n",
      "Photo & Video : 28441.54375\n",
      "Games : 22788.6696905016\n",
      "Music : 57326.530303030304\n",
      "Reference : 74942.11111111111\n",
      "Health & Fitness : 23298.015384615384\n",
      "Weather : 52279.892857142855\n",
      "Utilities : 18684.456790123455\n",
      "Travel : 28243.8\n",
      "Shopping : 26919.690476190477\n",
      "News : 21248.023255813954\n",
      "Navigation : 86090.33333333333\n",
      "Lifestyle : 16485.764705882353\n",
      "Entertainment : 14029.830708661417\n",
      "Food & Drink : 33333.92307692308\n",
      "Sports : 23008.898550724636\n",
      "Book : 39758.5\n",
      "Finance : 31467.944444444445\n",
      "Education : 7003.983050847458\n",
      "Productivity : 21028.410714285714\n",
      "Business : 7491.117647058823\n",
      "Catalogs : 4004.0\n",
      "Medical : 612.0\n"
     ]
    }
   ],
   "source": [
    "genres_ios = freq_table(ios_final, -5)\n",
    "\n",
    "for genre in genres_ios:\n",
    "    total = 0\n",
    "    len_genre = 0\n",
    "    for app in ios_final:\n",
    "        genre_app = app[-5]\n",
    "        if genre_app == genre:            \n",
    "            n_ratings = float(app[5])\n",
    "            total += n_ratings\n",
    "            len_genre += 1\n",
    "    avg_n_ratings = total / len_genre\n",
    "    print(genre, ':', avg_n_ratings)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "SwA1S8Uadw4X"
   },
   "source": [
    "On average, navigation apps have the highest number of user reviews, but this figure is heavily influenced by Waze and Google Maps, which have close to half a million user reviews together:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "rdNDNVbVdw4X",
    "outputId": "21032c92-d8cf-4736-ff17-8f7d386d8dcb"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Waze - GPS Navigation, Maps & Real-time Traffic : 345046\n",
      "Google Maps - Navigation & Transit : 154911\n",
      "Geocaching® : 12811\n",
      "CoPilot GPS – Car Navigation & Offline Maps : 3582\n",
      "ImmobilienScout24: Real Estate Search in Germany : 187\n",
      "Railway Route Search : 5\n"
     ]
    }
   ],
   "source": [
    "for app in ios_final:\n",
    "    if app[-5] == 'Navigation':\n",
    "        print(app[1], ':', app[5]) # print name and number of ratings"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "55kQqN_qdw4Z"
   },
   "source": [
    "The same pattern applies to social networking apps, where the average number is heavily influenced by a few giants like Facebook, Pinterest, Skype, etc. Same applies to music apps, where a few big players like Pandora, Spotify, and Shazam heavily influence the average number.\n",
    "\n",
    "Our aim is to find popular genres, but navigation, social networking or music apps might seem more popular than they really are. The average number of ratings seem to be skewed by very few apps which have hundreds of thousands of user ratings, while the other apps may struggle to get past the 10,000 threshold. We could get a better picture by removing these extremely popular apps for each genre and then rework the averages, but we'll leave this level of detail for later.\n",
    "\n",
    "Reference apps have 74,942 user ratings on average, but it's actually the Bible and Dictionary.com which skew up the average rating:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "T2H7TxY6dw4a",
    "outputId": "70aba60f-bc0a-4547-fa5b-966bb457a7c4"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bible : 985920\n",
      "Dictionary.com Dictionary & Thesaurus : 200047\n",
      "Dictionary.com Dictionary & Thesaurus for iPad : 54175\n",
      "Google Translate : 26786\n",
      "Muslim Pro: Ramadan 2017 Prayer Times, Azan, Quran : 18418\n",
      "New Furniture Mods - Pocket Wiki & Game Tools for Minecraft PC Edition : 17588\n",
      "Merriam-Webster Dictionary : 16849\n",
      "Night Sky : 12122\n",
      "City Maps for Minecraft PE - The Best Maps for Minecraft Pocket Edition (MCPE) : 8535\n",
      "LUCKY BLOCK MOD ™ for Minecraft PC Edition - The Best Pocket Wiki & Mods Installer Tools : 4693\n",
      "GUNS MODS for Minecraft PC Edition - Mods Tools : 1497\n",
      "Guides for Pokémon GO - Pokemon GO News and Cheats : 826\n",
      "WWDC : 762\n",
      "Horror Maps for Minecraft PE - Download The Scariest Maps for Minecraft Pocket Edition (MCPE) Free : 718\n",
      "VPN Express : 14\n",
      "Real Bike Traffic Rider Virtual Reality Glasses : 8\n",
      "教えて!goo : 0\n",
      "Jishokun-Japanese English Dictionary & Translator : 0\n"
     ]
    }
   ],
   "source": [
    "for app in ios_final:\n",
    "    if app[-5] == 'Reference':\n",
    "        print(app[1], ':', app[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "RClnbNGSdw4d"
   },
   "source": [
    "However, this niche seems to show some potential. One thing we could do is take another popular book and turn it into an app where we could add different features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes about the book, etc. On top of that, we could also embed a dictionary within the app, so users don't need to exit our app to look up words in an external app.\n",
    "\n",
    "This idea seems to fit well with the fact that the App Store is dominated by for-fun apps. This suggests the market might be a bit saturated with for-fun apps, which means a practical app might have more of a chance to stand out among the huge number of apps on the App Store.\n",
    "\n",
    "Other genres that seem popular include weather, book, food and drink, or finance. The book genre seem to overlap a bit with the app idea we described above, but the other genres don't seem too interesting to us:\n",
    "\n",
    "- Weather apps — people generally don't spend too much time in-app, and the chances of making profit from in-app adds are low. Also, getting reliable live weather data may require us to connect our apps to non-free APIs.\n",
    "\n",
    "- Food and drink — examples here include Starbucks, Dunkin' Donuts, McDonald's, etc. So making a popular food and drink app requires actual cooking and a delivery service, which is outside the scope of our company.\n",
    "\n",
    "- Finance apps — these apps involve banking, paying bills, money transfer, etc. Building a finance app requires domain knowledge, and we don't want to hire a finance expert just to build an app.\n",
    "\n",
    "Now let's analyze the Google Play market a bit.\n",
    "\n",
    "## Most Popular Apps by Genre on Google Play\n",
    "\n",
    "For the Google Play market, we actually have data about the number of installs, so we should be able to get a clearer picture about genre popularity. However, the install numbers don't seem precise enough — we can see that most values are open-ended (100+, 1,000+, 5,000+, etc.):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "k9XN-3Oxdw4e",
    "outputId": "4cf0acfe-8452-4c92-e400-c0c0879ebe1c"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1,000,000+ : 15.726534296028879\n",
      "100,000+ : 11.552346570397113\n",
      "10,000,000+ : 10.548285198555957\n",
      "10,000+ : 10.198555956678701\n",
      "1,000+ : 8.393501805054152\n",
      "100+ : 6.915613718411552\n",
      "5,000,000+ : 6.825361010830325\n",
      "500,000+ : 5.561823104693141\n",
      "50,000+ : 4.7721119133574\n",
      "5,000+ : 4.512635379061372\n",
      "10+ : 3.5424187725631766\n",
      "500+ : 3.2490974729241873\n",
      "50,000,000+ : 2.3014440433213\n",
      "100,000,000+ : 2.1322202166064983\n",
      "50+ : 1.917870036101083\n",
      "5+ : 0.78971119133574\n",
      "1+ : 0.5076714801444043\n",
      "500,000,000+ : 0.2707581227436823\n",
      "1,000,000,000+ : 0.22563176895306858\n",
      "0+ : 0.04512635379061372\n",
      "0 : 0.01128158844765343\n"
     ]
    }
   ],
   "source": [
    "display_table(android_final, 5) # the Installs columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "MS8oEkvcdw4g"
   },
   "source": [
    "One problem with this data is that is not precise. For instance, we don't know whether an app with 100,000+ installs has 100,000 installs, 200,000, or 350,000. However, we don't need very precise data for our purposes — we only want to get an idea which app genres attract the most users, and we don't need perfect precision with respect to the number of users.\n",
    "\n",
    "We're going to leave the numbers as they are, which means that we'll consider that an app with 100,000+ installs has 100,000 installs, and an app with 1,000,000+ installs has 1,000,000 installs, and so on.\n",
    "\n",
    "To perform computations, however, we'll need to convert each install number to `float` — this means that we need to remove the commas and the plus characters, otherwise the conversion will fail and raise an error. We'll do this directly in the loop below, where we also compute the average number of installs for each genre (category)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "qLmoJbd_dw4h",
    "outputId": "484a9775-2a55-4790-9df4-4c3e0a8a031b"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ART_AND_DESIGN : 1986335.0877192982\n",
      "AUTO_AND_VEHICLES : 647317.8170731707\n",
      "BEAUTY : 513151.88679245283\n",
      "BOOKS_AND_REFERENCE : 8767811.894736841\n",
      "BUSINESS : 1712290.1474201474\n",
      "COMICS : 817657.2727272727\n",
      "COMMUNICATION : 38456119.167247385\n",
      "DATING : 854028.8303030303\n",
      "EDUCATION : 1833495.145631068\n",
      "ENTERTAINMENT : 11640705.88235294\n",
      "EVENTS : 253542.22222222222\n",
      "FINANCE : 1387692.475609756\n",
      "FOOD_AND_DRINK : 1924897.7363636363\n",
      "HEALTH_AND_FITNESS : 4188821.9853479853\n",
      "HOUSE_AND_HOME : 1331540.5616438356\n",
      "LIBRARIES_AND_DEMO : 638503.734939759\n",
      "LIFESTYLE : 1437816.2687861272\n",
      "GAME : 15588015.603248259\n",
      "FAMILY : 3695641.8198090694\n",
      "MEDICAL : 120550.61980830671\n",
      "SOCIAL : 23253652.127118643\n",
      "SHOPPING : 7036877.311557789\n",
      "PHOTOGRAPHY : 17840110.40229885\n",
      "SPORTS : 3638640.1428571427\n",
      "TRAVEL_AND_LOCAL : 13984077.710144928\n",
      "TOOLS : 10801391.298666667\n",
      "PERSONALIZATION : 5201482.6122448975\n",
      "PRODUCTIVITY : 16787331.344927534\n",
      "PARENTING : 542603.6206896552\n",
      "WEATHER : 5074486.197183099\n",
      "VIDEO_PLAYERS : 24727872.452830188\n",
      "NEWS_AND_MAGAZINES : 9549178.467741935\n",
      "MAPS_AND_NAVIGATION : 4056941.7741935486\n"
     ]
    }
   ],
   "source": [
    "categories_android = freq_table(android_final, 1)\n",
    "\n",
    "for category in categories_android:\n",
    "    total = 0\n",
    "    len_category = 0\n",
    "    for app in android_final:\n",
    "        category_app = app[1]\n",
    "        if category_app == category:            \n",
    "            n_installs = app[5]\n",
    "            n_installs = n_installs.replace(',', '')\n",
    "            n_installs = n_installs.replace('+', '')\n",
    "            total += float(n_installs)\n",
    "            len_category += 1\n",
    "    avg_n_installs = total / len_category\n",
    "    print(category, ':', avg_n_installs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "jmJZ_ZNAdw4m"
   },
   "source": [
    "On average, communication apps have the most installs: 38,456,119. This number is heavily skewed up by a few apps that have over one billion installs (WhatsApp, Facebook Messenger, Skype, Google Chrome, Gmail, and Hangouts), and a few others with over 100 and 500 million installs:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "yDgqLB3xdw4p",
    "outputId": "020dc10e-5dc0-4983-b4ed-ddb4631fe760"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WhatsApp Messenger : 1,000,000,000+\n",
      "imo beta free calls and text : 100,000,000+\n",
      "Android Messages : 100,000,000+\n",
      "Google Duo - High Quality Video Calls : 500,000,000+\n",
      "Messenger – Text and Video Chat for Free : 1,000,000,000+\n",
      "imo free video calls and chat : 500,000,000+\n",
      "Skype - free IM & video calls : 1,000,000,000+\n",
      "Who : 100,000,000+\n",
      "GO SMS Pro - Messenger, Free Themes, Emoji : 100,000,000+\n",
      "LINE: Free Calls & Messages : 500,000,000+\n",
      "Google Chrome: Fast & Secure : 1,000,000,000+\n",
      "Firefox Browser fast & private : 100,000,000+\n",
      "UC Browser - Fast Download Private & Secure : 500,000,000+\n",
      "Gmail : 1,000,000,000+\n",
      "Hangouts : 1,000,000,000+\n",
      "Messenger Lite: Free Calls & Messages : 100,000,000+\n",
      "Kik : 100,000,000+\n",
      "KakaoTalk: Free Calls & Text : 100,000,000+\n",
      "Opera Mini - fast web browser : 100,000,000+\n",
      "Opera Browser: Fast and Secure : 100,000,000+\n",
      "Telegram : 100,000,000+\n",
      "Truecaller: Caller ID, SMS spam blocking & Dialer : 100,000,000+\n",
      "UC Browser Mini -Tiny Fast Private & Secure : 100,000,000+\n",
      "Viber Messenger : 500,000,000+\n",
      "WeChat : 100,000,000+\n",
      "Yahoo Mail – Stay Organized : 100,000,000+\n",
      "BBM - Free Calls & Messages : 100,000,000+\n"
     ]
    }
   ],
   "source": [
    "for app in android_final:\n",
    "    if app[1] == 'COMMUNICATION' and (app[5] == '1,000,000,000+'\n",
    "                                      or app[5] == '500,000,000+'\n",
    "                                      or app[5] == '100,000,000+'):\n",
    "        print(app[0], ':', app[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "GkB0Ewlsdw47"
   },
   "source": [
    "If we removed all the communication apps that have over 100 million installs, the average would be reduced roughly ten times:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "GVS8X24bdw48",
    "outputId": "864d77ca-7455-46e5-b028-72d81f553da8"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3603485.3884615386"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "under_100_m = []\n",
    "\n",
    "for app in android_final:\n",
    "    n_installs = app[5]\n",
    "    n_installs = n_installs.replace(',', '')\n",
    "    n_installs = n_installs.replace('+', '')\n",
    "    if (app[1] == 'COMMUNICATION') and (float(n_installs) < 100000000):\n",
    "        under_100_m.append(float(n_installs))\n",
    "        \n",
    "sum(under_100_m) / len(under_100_m)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "VGf0n6cydw5A"
   },
   "source": [
    "We see the same pattern for the video players category, which is the runner-up with 24,727,872 installs. The market is dominated by apps like Youtube, Google Play Movies & TV, or MX Player. The pattern is repeated for social apps (where we have giants like Facebook, Instagram, Google+, etc.), photography apps (Google Photos and other popular photo editors), or productivity apps (Microsoft Word, Dropbox, Google Calendar, Evernote, etc.).\n",
    "\n",
    "Again, the main concern is that these app genres might seem more popular than they really are. Moreover, these niches seem to be dominated by a few giants who are hard to compete against.\n",
    "\n",
    "The game genre seems pretty popular, but previously we found out this part of the market seems a bit saturated, so we'd like to come up with a different app recommendation if possible.\n",
    "\n",
    "The books and reference genre looks fairly popular as well, with an average number of installs of 8,767,811. It's interesting to explore this in more depth, since we found this genre has some potential to work well on the App Store, and our aim is to recommend an app genre that shows potential for being profitable on both the App Store and Google Play. \n",
    "\n",
    "Let's take a look at some of the apps from this genre and their number of installs:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "EsjrE2Nudw5B",
    "outputId": "04f55ee7-8355-412d-c43b-8f3b3ebd4db4"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "E-Book Read - Read Book for free : 50,000+\n",
      "Download free book with green book : 100,000+\n",
      "Wikipedia : 10,000,000+\n",
      "Cool Reader : 10,000,000+\n",
      "Free Panda Radio Music : 100,000+\n",
      "Book store : 1,000,000+\n",
      "FBReader: Favorite Book Reader : 10,000,000+\n",
      "English Grammar Complete Handbook : 500,000+\n",
      "Free Books - Spirit Fanfiction and Stories : 1,000,000+\n",
      "Google Play Books : 1,000,000,000+\n",
      "AlReader -any text book reader : 5,000,000+\n",
      "Offline English Dictionary : 100,000+\n",
      "Offline: English to Tagalog Dictionary : 500,000+\n",
      "FamilySearch Tree : 1,000,000+\n",
      "Cloud of Books : 1,000,000+\n",
      "Recipes of Prophetic Medicine for free : 500,000+\n",
      "ReadEra – free ebook reader : 1,000,000+\n",
      "Anonymous caller detection : 10,000+\n",
      "Ebook Reader : 5,000,000+\n",
      "Litnet - E-books : 100,000+\n",
      "Read books online : 5,000,000+\n",
      "English to Urdu Dictionary : 500,000+\n",
      "eBoox: book reader fb2 epub zip : 1,000,000+\n",
      "English Persian Dictionary : 500,000+\n",
      "Flybook : 500,000+\n",
      "All Maths Formulas : 1,000,000+\n",
      "Ancestry : 5,000,000+\n",
      "HTC Help : 10,000,000+\n",
      "English translation from Bengali : 100,000+\n",
      "Pdf Book Download - Read Pdf Book : 100,000+\n",
      "Free Book Reader : 100,000+\n",
      "eBoox new: Reader for fb2 epub zip books : 50,000+\n",
      "Only 30 days in English, the guideline is guaranteed : 500,000+\n",
      "Moon+ Reader : 10,000,000+\n",
      "SH-02J Owner's Manual (Android 8.0) : 50,000+\n",
      "English-Myanmar Dictionary : 1,000,000+\n",
      "Golden Dictionary (EN-AR) : 1,000,000+\n",
      "All Language Translator Free : 1,000,000+\n",
      "Azpen eReader : 500,000+\n",
      "URBANO V 02 instruction manual : 100,000+\n",
      "Bible : 100,000,000+\n",
      "C Programs and Reference : 50,000+\n",
      "C Offline Tutorial : 1,000+\n",
      "C Programs Handbook : 50,000+\n",
      "Amazon Kindle : 100,000,000+\n",
      "Aab e Hayat Full Novel : 100,000+\n",
      "Aldiko Book Reader : 10,000,000+\n",
      "Google I/O 2018 : 500,000+\n",
      "R Language Reference Guide : 10,000+\n",
      "Learn R Programming Full : 5,000+\n",
      "R Programing Offline Tutorial : 1,000+\n",
      "Guide for R Programming : 5+\n",
      "Learn R Programming : 10+\n",
      "R Quick Reference Big Data : 1,000+\n",
      "V Made : 100,000+\n",
      "Wattpad 📖 Free Books : 100,000,000+\n",
      "Dictionary - WordWeb : 5,000,000+\n",
      "Guide (for X-MEN) : 100,000+\n",
      "AC Air condition Troubleshoot,Repair,Maintenance : 5,000+\n",
      "AE Bulletins : 1,000+\n",
      "Ae Allah na Dai (Rasa) : 10,000+\n",
      "50000 Free eBooks & Free AudioBooks : 5,000,000+\n",
      "Ag PhD Field Guide : 10,000+\n",
      "Ag PhD Deficiencies : 10,000+\n",
      "Ag PhD Planting Population Calculator : 1,000+\n",
      "Ag PhD Soybean Diseases : 1,000+\n",
      "Fertilizer Removal By Crop : 50,000+\n",
      "A-J Media Vault : 50+\n",
      "Al-Quran (Free) : 10,000,000+\n",
      "Al Quran (Tafsir & by Word) : 500,000+\n",
      "Al Quran Indonesia : 10,000,000+\n",
      "Al'Quran Bahasa Indonesia : 10,000,000+\n",
      "Al Quran Al karim : 1,000,000+\n",
      "Al-Muhaffiz : 50,000+\n",
      "Al Quran : EAlim - Translations & MP3 Offline : 5,000,000+\n",
      "Al-Quran 30 Juz free copies : 500,000+\n",
      "Koran Read &MP3 30 Juz Offline : 1,000,000+\n",
      "Hafizi Quran 15 lines per page : 1,000,000+\n",
      "Quran for Android : 10,000,000+\n",
      "Surah Al-Waqiah : 100,000+\n",
      "Hisnul Al Muslim - Hisn Invocations & Adhkaar : 100,000+\n",
      "Satellite AR : 1,000,000+\n",
      "Audiobooks from Audible : 100,000,000+\n",
      "Kinot & Eichah for Tisha B'Av : 10,000+\n",
      "AW Tozer Devotionals - Daily : 5,000+\n",
      "Tozer Devotional -Series 1 : 1,000+\n",
      "The Pursuit of God : 1,000+\n",
      "AY Sing : 5,000+\n",
      "Ay Hasnain k Nana Milad Naat : 10,000+\n",
      "Ay Mohabbat Teri Khatir Novel : 10,000+\n",
      "Arizona Statutes, ARS (AZ Law) : 1,000+\n",
      "Oxford A-Z of English Usage : 1,000,000+\n",
      "BD Fishpedia : 1,000+\n",
      "BD All Sim Offer : 10,000+\n",
      "Youboox - Livres, BD et magazines : 500,000+\n",
      "B&H Kids AR : 10,000+\n",
      "B y H Niños ES : 5,000+\n",
      "Dictionary.com: Find Definitions for English Words : 10,000,000+\n",
      "English Dictionary - Offline : 10,000,000+\n",
      "Bible KJV : 5,000,000+\n",
      "Borneo Bible, BM Bible : 10,000+\n",
      "MOD Black for BM : 100+\n",
      "BM Box : 1,000+\n",
      "Anime Mod for BM : 100+\n",
      "NOOK: Read eBooks & Magazines : 10,000,000+\n",
      "NOOK Audiobooks : 500,000+\n",
      "NOOK App for NOOK Devices : 500,000+\n",
      "Browsery by Barnes & Noble : 5,000+\n",
      "bp e-store : 1,000+\n",
      "Brilliant Quotes: Life, Love, Family & Motivation : 1,000,000+\n",
      "BR Ambedkar Biography & Quotes : 10,000+\n",
      "BU Alsace : 100+\n",
      "Catholic La Bu Zo Kam : 500+\n",
      "Khrifa Hla Bu (Solfa) : 10+\n",
      "Kristian Hla Bu : 10,000+\n",
      "SA HLA BU : 1,000+\n",
      "Learn SAP BW : 500+\n",
      "Learn SAP BW on HANA : 500+\n",
      "CA Laws 2018 (California Laws and Codes) : 5,000+\n",
      "Bootable Methods(USB-CD-DVD) : 10,000+\n",
      "cloudLibrary : 100,000+\n",
      "SDA Collegiate Quarterly : 500+\n",
      "Sabbath School : 100,000+\n",
      "Cypress College Library : 100+\n",
      "Stats Royale for Clash Royale : 1,000,000+\n",
      "GATE 21 years CS Papers(2011-2018 Solved) : 50+\n",
      "Learn CT Scan Of Head : 5,000+\n",
      "Easy Cv maker 2018 : 10,000+\n",
      "How to Write CV : 100,000+\n",
      "CW Nuclear : 1,000+\n",
      "CY Spray nozzle : 10+\n",
      "BibleRead En Cy Zh Yue : 5+\n",
      "CZ-Help : 5+\n",
      "Modlitební knížka CZ : 500+\n",
      "Guide for DB Xenoverse : 10,000+\n",
      "Guide for DB Xenoverse 2 : 10,000+\n",
      "Guide for IMS DB : 10+\n",
      "DC HSEMA : 5,000+\n",
      "DC Public Library : 1,000+\n",
      "Painting Lulu DC Super Friends : 1,000+\n",
      "Dictionary : 10,000,000+\n",
      "Fix Error Google Playstore : 1,000+\n",
      "D. H. Lawrence Poems FREE : 1,000+\n",
      "Bilingual Dictionary Audio App : 5,000+\n",
      "DM Screen : 10,000+\n",
      "wikiHow: how to do anything : 1,000,000+\n",
      "Dr. Doug's Tips : 1,000+\n",
      "Bible du Semeur-BDS (French) : 50,000+\n",
      "La citadelle du musulman : 50,000+\n",
      "DV 2019 Entry Guide : 10,000+\n",
      "DV 2019 - EDV Photo & Form : 50,000+\n",
      "DV 2018 Winners Guide : 1,000+\n",
      "EB Annual Meetings : 1,000+\n",
      "EC - AP & Telangana : 5,000+\n",
      "TN Patta Citta & EC : 10,000+\n",
      "AP Stamps and Registration : 10,000+\n",
      "CompactiMa EC pH Calibration : 100+\n",
      "EGW Writings 2 : 100,000+\n",
      "EGW Writings : 1,000,000+\n",
      "Bible with EGW Comments : 100,000+\n",
      "My Little Pony AR Guide : 1,000,000+\n",
      "SDA Sabbath School Quarterly : 500,000+\n",
      "Duaa Ek Ibaadat : 5,000+\n",
      "Spanish English Translator : 10,000,000+\n",
      "Dictionary - Merriam-Webster : 10,000,000+\n",
      "JW Library : 10,000,000+\n",
      "Oxford Dictionary of English : Free : 10,000,000+\n",
      "English Hindi Dictionary : 10,000,000+\n",
      "English to Hindi Dictionary : 5,000,000+\n",
      "EP Research Service : 1,000+\n",
      "Hymnes et Louanges : 100,000+\n",
      "EU Charter : 1,000+\n",
      "EU Data Protection : 1,000+\n",
      "EU IP Codes : 100+\n",
      "EW PDF : 5+\n",
      "BakaReader EX : 100,000+\n",
      "EZ Quran : 50,000+\n",
      "FA Part 1 & 2 Past Papers Solved Free – Offline : 5,000+\n",
      "La Fe de Jesus : 1,000+\n",
      "La Fe de Jesús : 500+\n",
      "Le Fe de Jesus : 500+\n",
      "Florida - Pocket Brainbook : 1,000+\n",
      "Florida Statutes (FL Code) : 1,000+\n",
      "English To Shona Dictionary : 10,000+\n",
      "Greek Bible FP (Audio) : 1,000+\n",
      "Golden Dictionary (FR-AR) : 500,000+\n",
      "Fanfic-FR : 5,000+\n",
      "Bulgarian French Dictionary Fr : 10,000+\n",
      "Chemin (fr) : 1,000+\n",
      "The SCP Foundation DB fr nn5n : 1,000+\n"
     ]
    }
   ],
   "source": [
    "for app in android_final:\n",
    "    if app[1] == 'BOOKS_AND_REFERENCE':\n",
    "        print(app[0], ':', app[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "j4vZcL-Udw5G"
   },
   "source": [
    "The book and reference genre includes a variety of apps: software for processing and reading ebooks, various collections of libraries, dictionaries, tutorials on programming or languages, etc. It seems there's still a small number of extremely popular apps that skew the average:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "sPYrMGhKdw5H",
    "outputId": "98571b49-b279-4e0c-c61c-517939d09ce4"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Google Play Books : 1,000,000,000+\n",
      "Bible : 100,000,000+\n",
      "Amazon Kindle : 100,000,000+\n",
      "Wattpad 📖 Free Books : 100,000,000+\n",
      "Audiobooks from Audible : 100,000,000+\n"
     ]
    }
   ],
   "source": [
    "for app in android_final:\n",
    "    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000,000+'\n",
    "                                            or app[5] == '500,000,000+'\n",
    "                                            or app[5] == '100,000,000+'):\n",
    "        print(app[0], ':', app[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "jGuGD7ODdw5K"
   },
   "source": [
    "However, it looks like there are only a few very popular apps, so this market still shows potential. Let's try to get some app ideas based on the kind of apps that are somewhere in the middle in terms of popularity (between 1,000,000 and 100,000,000 downloads):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "id": "s9pL6QCddw5K",
    "outputId": "cf1d2dc2-8b71-4b84-ad1c-210cbae4e9db"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wikipedia : 10,000,000+\n",
      "Cool Reader : 10,000,000+\n",
      "Book store : 1,000,000+\n",
      "FBReader: Favorite Book Reader : 10,000,000+\n",
      "Free Books - Spirit Fanfiction and Stories : 1,000,000+\n",
      "AlReader -any text book reader : 5,000,000+\n",
      "FamilySearch Tree : 1,000,000+\n",
      "Cloud of Books : 1,000,000+\n",
      "ReadEra – free ebook reader : 1,000,000+\n",
      "Ebook Reader : 5,000,000+\n",
      "Read books online : 5,000,000+\n",
      "eBoox: book reader fb2 epub zip : 1,000,000+\n",
      "All Maths Formulas : 1,000,000+\n",
      "Ancestry : 5,000,000+\n",
      "HTC Help : 10,000,000+\n",
      "Moon+ Reader : 10,000,000+\n",
      "English-Myanmar Dictionary : 1,000,000+\n",
      "Golden Dictionary (EN-AR) : 1,000,000+\n",
      "All Language Translator Free : 1,000,000+\n",
      "Aldiko Book Reader : 10,000,000+\n",
      "Dictionary - WordWeb : 5,000,000+\n",
      "50000 Free eBooks & Free AudioBooks : 5,000,000+\n",
      "Al-Quran (Free) : 10,000,000+\n",
      "Al Quran Indonesia : 10,000,000+\n",
      "Al'Quran Bahasa Indonesia : 10,000,000+\n",
      "Al Quran Al karim : 1,000,000+\n",
      "Al Quran : EAlim - Translations & MP3 Offline : 5,000,000+\n",
      "Koran Read &MP3 30 Juz Offline : 1,000,000+\n",
      "Hafizi Quran 15 lines per page : 1,000,000+\n",
      "Quran for Android : 10,000,000+\n",
      "Satellite AR : 1,000,000+\n",
      "Oxford A-Z of English Usage : 1,000,000+\n",
      "Dictionary.com: Find Definitions for English Words : 10,000,000+\n",
      "English Dictionary - Offline : 10,000,000+\n",
      "Bible KJV : 5,000,000+\n",
      "NOOK: Read eBooks & Magazines : 10,000,000+\n",
      "Brilliant Quotes: Life, Love, Family & Motivation : 1,000,000+\n",
      "Stats Royale for Clash Royale : 1,000,000+\n",
      "Dictionary : 10,000,000+\n",
      "wikiHow: how to do anything : 1,000,000+\n",
      "EGW Writings : 1,000,000+\n",
      "My Little Pony AR Guide : 1,000,000+\n",
      "Spanish English Translator : 10,000,000+\n",
      "Dictionary - Merriam-Webster : 10,000,000+\n",
      "JW Library : 10,000,000+\n",
      "Oxford Dictionary of English : Free : 10,000,000+\n",
      "English Hindi Dictionary : 10,000,000+\n",
      "English to Hindi Dictionary : 5,000,000+\n"
     ]
    }
   ],
   "source": [
    "for app in android_final:\n",
    "    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000+'\n",
    "                                            or app[5] == '5,000,000+'\n",
    "                                            or app[5] == '10,000,000+'\n",
    "                                            or app[5] == '50,000,000+'):\n",
    "        print(app[0], ':', app[5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "MnArt0Mbdw5M"
   },
   "source": [
    "This niche seems to be dominated by software for processing and reading ebooks, as well as various collections of libraries and dictionaries, so it's probably not a good idea to build similar apps since there'll be some significant competition.\n",
    "\n",
    "We also notice there are quite a few apps built around the book Quran, which suggests that building an app around a popular book can be profitable. It seems that taking a popular book (perhaps a more recent book) and turning it into an app could be profitable for both the Google Play and the App Store markets.\n",
    "\n",
    "However, it looks like the market is already full of libraries, so we need to add some special features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes on the book, a forum where people can discuss the book, etc.\n",
    "\n",
    "\n",
    "## Conclusions\n",
    "\n",
    "In this project, we analyzed data about the App Store and Google Play mobile apps with the goal of recommending an app profile that can be profitable for both markets.\n",
    "\n",
    "We concluded that taking a popular book (perhaps a more recent book) and turning it into an app could be profitable for both the Google Play and the App Store markets. The markets are already full of libraries, so we need to add some special features besides the raw version of the book. This might include daily quotes from the book, an audio version of the book, quizzes on the book, a forum where people can discuss the book, etc."
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [
    "nxHDmzy-dw4B"
   ],
   "name": "Mission350Solutions.ipynb",
   "provenance": [],
   "version": "0.3.2"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
