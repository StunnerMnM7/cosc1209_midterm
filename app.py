from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>EcoVoyage</h1><p>Developed by: Mihir Mane</p><p>Company ID: 100947380 ID</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)