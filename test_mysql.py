import mysql.connector
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)["mysql"]

print("DEBUG CONFIG:", config)  # 👈 show raw values

conn = mysql.connector.connect(
    host=str(config["host"]),        # force string
    user=str(config["user"]),
    password=str(config["password"]),
    database=str(config["name"]),
    port=int(config["port"])         # force int
)

print("✅ Connection successful!")
conn.close()
