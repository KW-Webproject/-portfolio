from flask import Flask, render_template, request, redirect, json
import mariadb
import sys

app = Flask(__name__)
# 예약자 정보를 결제하기까지 저장하기위해 전역변수 사용
reservation_info = []


def get_conn():
    conn = mariadb.connect(user="root",
                           password="000000",
                           host="193.123.233.236",
                           port=3306,
                           database="petland")
    return conn


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/reservation")
def reservation():
    return render_template("reservation.html")


@app.route("/reservation", methods=['POST'])
def receive_form():
    name = request.form['name']
    phone = request.form['phone']
    pet = request.form['pet']
    service = request.form.getlist('service')
    date = request.form['date']
    time = request.form.getlist('time')
    postcode = request.form['postcode']
    roadaddress = request.form['roadaddress']
    detailaddress = request.form['detailaddress']

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
    global reservation_info
    reservation_info = formData
    print("전역변수 : ", reservation_info)

    # 지역(구)를 먼저 빼와서 DB와 비교
    roadaddress = roadaddress.split()
    print(roadaddress)
    str_addr = roadaddress[1]
    # 펫시터가 존재하면 p_id와 p_name을 저장
    check_sitter = check_add(str_addr)
    reservation_info.append(check_sitter[0])
    print(reservation_info)
    print(check_sitter)
    if check_sitter != 0:
        return render_template("reservation2.html",
                               name=name, pet=pet,
                               service=service, date=date,
                               time=time)
    else:
        err = "펫시터가 없음"
        return render_template("reservation.html", err=err)

# 결제하기 작동시 /reservation2로 form을 보내고 reservation.html 로 이동

# 결제하기 눌렀을시 db에 데이터 입력


@app.route("/reservation2", methods=['POST'])
def reservation2():
    payment_save(reservation_info)
    # reservation_info = ""
    return render_template("reservation.html")


@app.route("/reservation_check")
def reservation_check():
    return render_template("reservation_check.html")


@app.route("/reservation_check", methods=['POST'])
def check_submit():
    name = request.form['name']
    phone = request.form['phone']
    # 체크 값이 있을 시
    # user_info[p_id, name, phone, pet, service(리스트), p_date, r_time(리스트), r_p_id ]
    user_info = check_phone(phone, name)
    if len(user_info) == 0:
        err = "예약정보가 없습니다."
        return render_template("reservation_check.html", err=err)
    else:
        print(user_info)
        return render_template("reservation_check2.html",
                               id=user_info[0], name=user_info[1], pet=user_info[3], service=user_info[4], date=user_info[5],
                               time=user_info[6], petsitter="냉무")

# 입력된 주소로 펫시터가 있는지 체크한다.


def check_add(search_local):
    r_id = ""
    sql = """
        SELECT p_id, p_name FROM pet_sitter WHERE p_local = "{}" AND possible = 0
    """.format(search_local)
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        r_id = cur.fetchone()
    except mariadb.Error as e:
        print("ERR : {}".format(e))
    finally:
        if conn:
            conn.close()
        if r_id == None:
            return 0
        else:
            return r_id


# 조회가 되었을 시 user_info에 값을 전달한다.
def check_phone(user_phone, user_name):
    user_info = []
    sql = """
        SELECT * FROM reservation WHERE phone = "{}" AND name= "{}"
        """.format(user_phone, user_name)
    print(sql)
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        for i in cur:
            user_info += i
        print(user_info)
        # pet_sitter 테이블에서 possible colum을 빼온다

        # sql = """
        #     SELECT
        # """
        # conn = get_conn()
        # cur = conn.cursor()
        # cur.execute(sql)
        # print(user_info)
    except mariadb.Error as e:
        print("ERR : {}".format(e))
    finally:
        if conn:
            conn.close()
    return user_info


# 결제하기 했을 때 예약자의 데이터를 저장
def payment_save(info):
    # 예약정보를 리스트형식으로 가지고있다. 최종 결제시 db에 입력
    # name, phone, pet, service, date, time, postcode, roadaddress, detailaddress
    full_address = ""
    print(info)
    print(len(info))
    full_address = info[6] + " " + info[7] + " " + info[8]
    print(full_address)
    err = ""
    sql = """INSERT INTO reservation
        (name, phone, pet, service, r_date, r_time, address)
        values ("{}","{}","{}","{}","{}","{}", "{}")
    """.format(info[0], info[1], info[2], info[3], info[4], info[5], full_address)
    print(sql)
    # 펫시터 예약시 possible 업데이트

    sql2 = """
        UPDATE pet_sitter SET possible=1 WHERE p_id = {}
    """.format(info[9])
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.execute(sql2)
        conn.commit()
    except mariadb.Error as err:
        print("ERROR: {}".format(err))
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
