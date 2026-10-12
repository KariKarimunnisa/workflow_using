from flask import Flask

app = Flask(__name__)

# Static route
@app.route("/")
def home():
    return "GoodMorning!"

# Dynamic route
@app.route("/user/<username>")
def get_user(username):
    return f"Hello, {username}!"
#typed dynamic route
@app.route("/price/<float:amount>")
def getBill(amount):
    return f"Total: {amount}"

# HTTP methods & render template
@app.route("/home", methods=["GET", "POST"])
def home_page():
if __name__ == "__main__":
    app.run(debug=True)