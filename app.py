from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return "Home Page"

@app.route("/home")
def home():
    return render_template("index.html", content="name", names=["hello", "var", "hii"])

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()