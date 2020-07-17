from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
    return 'Dashboard for food provenance supply chain app'

if __name__ == "__main__":
    app.run(debug=True)