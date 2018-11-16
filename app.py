from flask import Flask, request

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Alsbsdla@16', db='employee_details')

cur = conn.cursor()

cur.execute("SELECT * from employee_table")
k = cur.fetchall()

app = Flask(__name__)


@app.route('/')
def display():
    global cur
    cur.execute("SELECT * from employee_table")
    k = cur.fetchall()
    return 'Data in Employee_database: ' + str(k)


@app.route('/add_employee', methods= ['POST'])
def add_employee():
    global cur
    k = request.get_json()
    cur.execute("INSERT INTO employee_table (employee_id, employee_name, manager_id, employee_age) VALUES ('"+str(k['employee_id'])+"', '"+str(k['employee_name'])+"', '"+str(k['manager_id'])+"', '"+str(k['employee_age'])+"')")
    conn.commit()
    return 'Inserted:'+str(k)

if __name__ == '__main__':
    app.run(debug=True)