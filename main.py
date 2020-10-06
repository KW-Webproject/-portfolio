from flask import Flask, render_template

app = Flask(__name__)
#main service reservation search

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/service")
def service():
    return render_template('service.html')

@app.route("/reservation")
def reservation():
    return render_template('reservation.html')

@app.route("/search")
def search():
    return

if __name__ == "__main__":
    app.run(host='0.0.0.0')
