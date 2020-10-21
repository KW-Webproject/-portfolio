# 총 4가지의 메서드가 있다
# 데이터베이스 사용 권한이 있는 메서드
# 사용자의 주소와 DB의 펫시터의 주소를 체크하는 메서드
# 예약정보 조회시 사용자 이름과, 번호를 DB에서 조회하여 검색하는 메서드
# 최종 결제하기 클릭시 DB reservation 테이블에 사용자 정보를 입력한다.
import mariadb
import sys


def get_conn():
    conn = mariadb.connect(user="root",
                           password="000000",
                           host="193.123.233.236",
                           port=3306,
                           database="petland")
    return conn


def check_add(search_local):
    # 입력된 주소로 펫시터가 있는지 체크한다.
    r_id = ""
    # 근로자의 예약여부는 possible 0 or 1 로 구분한다.
    sql = """
        SELECT p_id, p_name FROM pet_sitter WHERE p_local = "{}" AND possible = 0
    """.format(search_local)
    print(sql)
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        r_id = cur.fetchone()
        print(r_id)
    except mariadb.Error as e:
        print("ERR : {}".format(e))
    except TypeError as e:
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
    result = ""
    # sql = """
    #     SELECT * FROM reservation WHERE phone = "{}" AND name= "{}"
    #     """.format(user_phone, user_name)
    sql = """
        SELECT r.c_id , r.name, r.phone, r.pet, r.service, r.r_date, r.r_time, p.p_name 
        FROM reservation r
        INNER JOIN pet_sitter p 
        ON r.r_p_id = p.p_id 
        WHERE r.phone = "{}" AND r.name= "{}"
    """.format(user_phone, user_name)
    print(sql)
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        for c_id, name, phone, pet, service, r_date, r_time, p_name in cur:
            result += "<tr>"
            result += "<td>"+str(c_id)+"</td>"
            result += "<td>"+name+"</td>"
            result += "<td>"+phone+"</td>"
            result += "<td>"+pet+"</td>"
            result += "<td>"+service+"</td>"
            result += "<td>"+str(r_date)+"</td>"
            result += "<td>"+r_time+"</td>"
            result += "<td>"+p_name+"</td>"
            result += "</tr>"
        # print(result)
    except mariadb.Error as e:
        print("ERR : {}".format(e))
    finally:
        if conn:
            conn.close()
    return result


# 결제하기 했을 때 예약자의 데이터를 저장
def payment_save(info):
    # 예약정보를 리스트형식으로 가지고있다. 최종 결제시 db에 입력
    # name, phone, pet, service, date, time, postcode, roadaddress, detailaddress
    full_address = ""
    # print(info)
    # print(len(info))
    full_address = info[6] + " " + info[7] + " " + info[8]
    # print(full_address)
    err = ""
    sql = """INSERT INTO reservation
        (name, phone, pet, service, r_date, r_time, address, r_p_id)
        values ("{}","{}","{}","{}","{}","{}", "{}", "{}")
    """.format(info[0], info[1], info[2], info[3], info[4], info[5], full_address, info[9])
    # print(sql)
    # 펫시터 예약시 possible

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
