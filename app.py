from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "폐의약품 수거함 웹입니다!"

if __name__ == "__main__":
    app.run(debug=True)