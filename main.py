from flask import Flask, render_template, request
import mariadb
import sys

app = Flask(__name__)
# main service reservation search

def get_conn():
    conn = mariadb.connect(
            user="root",
            password="000000",
            host="193.123.233.236",
            port=3306,
            database="petland"
            )
    return conn

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

