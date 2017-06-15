import psycopg2


def connect():
    """Connect to the PostgreSQL database. Returns a database connection."""
    return psycopg2.connect("dbname=news")


def question_1():
    db = connect()
    c = db.cursor()
    query = "select * from total_views limit 3;"
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print ("Q1. What are the most popular three articles of all time? : ")
    print ("1. {} - {} views".format(rows[0][0], rows[0][2]))
    print ("2. {} - {} views".format(rows[1][0], rows[1][2]))
    print ("3. {} - {} views".format(rows[2][0], rows[2][2]))
    print ("\n")


def question_2():
    db = connect()
    c = db.cursor()
    query = "select * from authors_total_views limit 3;"
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print ("Q2. Who are the most popular article authors of all time? : ")
    print ("1. {} - {} views".format(rows[0][0], rows[0][1]))
    print ("2. {} - {} views".format(rows[1][0], rows[1][1]))
    print ("3. {} - {} views".format(rows[2][0], rows[2][1]))
    print ("\n")


def question_3():
    db = connect()
    c = db.cursor()
    query = "select * from error_percentage where error_percentage > 1.0;"
    c.execute(query)
    rows = c.fetchall()
    db.close()
    print ("Q3. On which days did more than 1% of requests lead to errors? : ")
    print ("1. {}/ {} - {}% errors".format(
        int(rows[0][0]), int(rows[0][1]), rows[0][2]))
    print ("\n")


question_1()
question_2()
question_3()
