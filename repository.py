import psycopg2
import os


conn = psycopg2.connect(
    host=os.environ.get("DATABASE_HOST", "localhost"),
    database=os.environ.get("DATABASE_NAME", "diversify_db"),
    user=os.environ.get("DATABASE_USER", "admin"),
    password=os.environ.get("DATABASE_PASSWORD", "mypassword"))


def retrive_users():
    '''retrive_all_users'''
    results = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM volunteer.volunteers")
    records = cur.fetchall()
    columns = [column[0] for column in cur.description]
    for row in records:
        results.append(dict(zip(columns, row)))

    return results


def create_volunteer_db(name, surname, city, country):
    '''creating a volunteer'''
    insert_query = """INSERT INTO volunteer.volunteers (v_name,v_surname,v_creation_date, v_id, v_city,v_country)
    VALUES (%s,%s,current_timestamp, nextval('volunteer.v_volunteer_seq'),%s,%s) RETURNING v_id"""
    values = (name, surname, city, country)
    cur = conn.cursor()
    cur.execute(insert_query, values)
    row_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return row_id


def retrive_one_user(user_id):
    '''retrive_all_users'''
    results = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM volunteer.volunteers where v_id=" + str(user_id))
    records = cur.fetchall()
    columns = [column[0] for column in cur.description]
    for row in records:
        results.append(dict(zip(columns, row)))

    return results
