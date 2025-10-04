import pymysql
import yaml
import os

def load_config():
    """Load configuration from the YAML file."""
    # Use relative path to the file
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

config = load_config()

def get_mysql_connection():
    """Create a MySQL connection using the configuration."""
    return pymysql.connect(
        host=str(config["mysql"]["host"]),
        port=int(config["mysql"]["port"]),
        user=str(config["mysql"]["user"]),
        password=str(config["mysql"]["password"]),
        db=str(config["mysql"]["database"]),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
