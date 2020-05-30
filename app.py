import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/test")
def test():
    import requests
    res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": "Heo7osVid8IA3PGMBXp2ww", "isbns": "1416949658"})
    return(res.json())

@app.route('/account', methods=['GET'])
def account():
    return 'Account Page'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        #do whatever
        return ('form POST')

    return render_template('register.html') #UPDATE: If user is logged in, dont show register

if __name__ == '__main__':
    app.run()
