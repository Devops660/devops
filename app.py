from flask import Flask
from pathlib import Path
import os
from waitress import serve


app = Flask(__name__)

# dotenv_path = Path('/mnt/g/env_file/.env')
# load_dotenv(dotenv_path=dotenv_path)
# #load_dotenv()
# DB_NAME = os.getenv('DB_NAME')
# print(DB_NAME)

# config = dotenv_values(".env")
# print("---------------------------", config)
# print(config["DB_NAME"])
# print(config["DB_PASSWORD"])



@app.route("/")
def main():
    return "my flask app for db" + " _"

#app.run(host='0.0.0.0', port=8080, debug=True)
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)