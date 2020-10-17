from flask import Flask, render_template, request, redirect, json
import mariadb
import sys

app = Flask(__name__)


def get_conn():
    conn = mariadb.connect(user="root",
                           password="000000",
                           host="193.123.233.236",
                           port=3306,
                           database="petland")
    return conn

# conn = get_conn()
# cur = conn.cursor()

# @app.route("/form", methods=['POST'])
# def form():
#     if request.method == 'POST':
#         reservation_form = request.form
#         name = reservation_form['name']
#         phone = reservation_form['phone']
#         pet = reservation_form['pet']
#         service = reservation_form['service']
#         p_date = reservation_form['date']
#         r_time = reservation_form['time']

#         sql = """INSERT INTO reservation
#             (name, phone, pet, service, p_date, r_time)
#             values ("{}","{}","{}","{}","{}","{}")
#         """.format(name, phone, pet, service, p_date, r_time)
#         print(sql)
#         cur.execute(sql)

#         conn.commit()
#         conn.close()
#         return "예약이 완료되었습니다."
#     return render_template("Form.html")
# @app.route("/test")
# def test():
#     sql = "SELECT p_name, p_date FROM pet_sitter"
#     result = ""

#     try:
#         conn = get_conn()
#         cur = conn.cursor()
#         cur.execute(
#                 sql
#                 )
#         result += '<ul>'
#         for(p_name, p_date) in cur:
#                 result += """
#                     <li>이름 = {}</li>
#                     <li>날짜 = {}</li>
#                     """.format(p_name, p_date)
#         result += '</ul>'

#     except mariadb.Error:
#         result = "펫시터 없음"
#         sys.exit(1)
#     finally:
#         if conn:
#             conn.close()
#     return result


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/reservation")
def reservation():
    return render_template("reservation.html")


@app.route("/reservation", methods=['POST'])
def test():
    name = request.form['name']
    phone = request.form['phone']
    pet = request.form['pet']
    service = request.form.getlist('service')
    date = request.form['date']
    time = request.form.getlist('time')
    postcode = request.form['postcode']
    roadaddress = request.form['roadaddress']
    detailaddress = request.form['detailaddress']

    # 지역(구)를 먼저 빼와서 DB와 비교
    roadaddress = roadaddress.split()
    print(roadaddress)
    str_addr = roadaddress[1]

    # 펫시터가 존재하면 p_id와 p_name을 저장
    check_sitter = check_add(str_addr) 
    if len(service) > 1:
        service = ",".join(service)
    else:
        service = service[0]

    if len(time) > 1:
        time = ",".join(time)
    else:
        time = time[0]

    formData = []
    formData.append(name)
    formData.append(phone)
    formData.append(pet)
    formData.append(service)
    formData.append(date)
    formData.append(time)
    formData.append(postcode)
    formData.append(roadaddress)
    formData.append(detailaddress)

    print(formData)
    if check_sitter != 0:
        return render_template("reservation2.html", 
        name = name, pet = pet,
        service = service, date = date,
        time = time)
    else:
        return "펫시터가 없습니다."

@app.route("/reservation_check")
def reservation_check():
    return render_template("reservation_check.html")

@app.route("/reservation_check", methods=['POST'])
def check_submit():
    name = request.form['name']
    phone = request.form['phone']
    print(name, phone)
    user_info = check_phone(phone, name)
    if len(user_info) == 0:
        return "예약정보가 없습니다."
    else:
        print(user_info)
        return "조회가 되었다"

# 입력된 주소로 펫시터가 있는지 체크한다.
def check_add(search_local):
    r_id = ""
    sql = """
        SELECT p_id, p_name FROM pet_sitter WHERE p_local = "{}"
    """.format(search_local)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    r_id = cur.fetchone()
    if r_id == None:
        return 0 
    else:
        return r_id

def check_phone(user_phone, user_name):
    user_info = [] 
    sql ="""
        SELECT * FROM reservation WHERE phone = "{}" AND name= "{}"
        """.format(user_phone, user_name)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    for i in cur:
        user_info += i
    print(user_info)
    return user_info 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

