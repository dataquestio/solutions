import csv
from datetime import datetime
import io
import psycopg2
from urllib import request


conn = psycopg2.connect(dbname='postgres', user='postgres')
cur = conn.cursor()
# Autocommit instead of commiting every transaction.
conn.autocommit = True

# Create database and users.
cur.execute('CREATE DATABASE ihw')
cur.execute("CREATE USER production WITH PASSWORD 'abc123'")
cur.execute("CREATE USER analyst WITH PASSWORD 'def456'")

# Reconnect to ihw database.
conn = psycopg2.connect(dbname='ihw', user='postgres')
conn.autocommit = True
cur = conn.cursor()

# Create the table.
cur.execute(
    """
    CREATE TABLE hurricanes (
        fid INTEGER PRIMARY KEY,
        recorded_at TIMESTAMP,
        btid INTEGER,
        name VARCHAR(10),
        lat DECIMAL(4, 1),
        long DECIMAL(4, 1),
        wind_kts SMALLINT,
        pressure INTEGER,
        category VARCHAR(2),
        basin VARCHAR(16),
        shape_length DECIMAL(8, 6)
    )
    """
)

# Manage privileges.
cur.execute("REVOKE ALL ON hurricanes FROM production")
cur.execute("REVOKE ALL ON hurricanes FROM analyst")
cur.execute("GRANT SELECT, INSERT, UPDATE ON hurricanes TO production")
cur.execute("GRANT SELECT ON hurricanes TO analyst")
conn.close()

# Reconnect with production user.
conn = psycopg2.connect(dbname='ihw', user='production', password='abc123')
cur = conn.cursor()
conn.autocommit = True

# Insert the data.
response = request.urlopen('https://dq-content.s3.amazonaws.com/251/storm_data.csv')
reader = csv.reader(io.TextIOWrapper(response))
# Skip the header.
_ = next(reader)
rows = []
for line in reader:
    recorded_at = datetime(int(line[1]), int(line[2]), int(line[3]), hour=int(line[4][:2]), minute=int(line[4][2:-1]))

    new_line = [line[0], recorded_at] + line[5:]
    rows.append(
        cur.mogrify(
            "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            new_line
        ).decode('utf-8')
    )
cur.execute('INSERT INTO hurricanes VALUES ' + ",".join(rows))
