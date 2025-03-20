from flask import Flask, render_template
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        username = os.getlogin()
    except:
        username = os.getenv("USER", "Unknown User")  # Fallback for some environments

    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -10")
    except:
        top_output = "Could not retrieve top processes."

    return render_template("index.html", name="Nitesh", username=username, time=formatted_time, top_output=top_output)
