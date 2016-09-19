from flask import Flask

app = Flask(__name__)
# from app import views

@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()