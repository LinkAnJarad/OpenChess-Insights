import time
import webbrowser
from flask import Flask
from views import views
import subprocess

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    # Run the app in a separate process
    process = subprocess.Popen(["python", "-m", "flask", "run", "--no-reload", "--port=8000"])

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
