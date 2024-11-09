import time
import webbrowser
from flask import Flask
from views import views
import subprocess
import argparse

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Enable Flask Debug", action="store_true")
    return parser.parse_args()

if __name__ == '__main__':
    py_args = get_args()
    # Run the app in a separate process
    cli_args = ["python", "-m", "flask", "run", "--port=8000"]
    if py_args.debug:
        cli_args.append("--debug")
    else:
        cli_args.append("--no-reload")

    process = subprocess.Popen(cli_args)

    # Wait in case of unexpected lag
    time.sleep(1)

    # Open the URL in the default web browser
    webbrowser.open("http://127.0.0.1:8000/views/")

    try:
        # Wait for the user to press Ctrl+C
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the Flask server
        process.terminate()
