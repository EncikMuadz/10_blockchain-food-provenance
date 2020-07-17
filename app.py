from flask import Flask, render_template # render_template to render html from templates dir
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('rumah.html')

if __name__ == "__main__":
    app.run(debug=True)