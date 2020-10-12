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

@app.route("/test")
def test():
    sql = "SELECT p_name, p_date FROM pet_sitter"
    result = ""

    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
                sql
                )
        result += '<ul>'
        for(p_name, p_date) in cur:
                result += """
                    <li>이름 = {}</li>
                    <li>날짜 = {}</li>
                    """.format(p_name, p_date)
        result += '</ul>'

    except mariadb.Error:
        result = "펫시터 없음"
        sys.exit(1)
    finally:
        if conn:
            conn.close()
    return result
    
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

