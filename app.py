from flask import Flask, render_template, request, redirect, flash
import pywhatkit
import datetime
import time

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        mobile = request.form["mobile"]
        message = request.form["message"]

        # Get current time + 1 minute to avoid timing issues
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1

        try:
            pywhatkit.sendwhatmsg(mobile, message, hour, minute, wait_time=5)
            flash("✅ Sent to WhatsApp Web!", "success")
        except Exception as e:
            flash(f"❌ Error: {str(e)}", "error")

        return redirect("/")

    return render_template("index.html")

if __name__ == "__main__":
    print("🚀 Flask app is starting...")
    app.run(debug=True)
