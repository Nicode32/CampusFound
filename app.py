from datetime import date
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nanhi",   
    database="query"    
)
cursor = mydb.cursor(dictionary=True)

@app.route('/', methods=['GET'])
def index():
    cursor.execute("SELECT * FROM info ORDER BY id DESC")
    records = cursor.fetchall()
    return render_template('index.html', records=records)

@app.route('/submit', methods=['POST'])
def submit():
    # Read form data
    name = request.form.get('Nameofstudent')
    course = request.form.get('course')
    contactno = request.form.get('contactno')
    item = request.form.get('item')
    itemdescription = request.form.get('itemdescription')
    status = request.form.get('status')
    report_date = request.form.get('date') or date.today().isoformat()

    # Insert into database
    sql = """
        INSERT INTO info
        (Nameofstudent, course, contactno, item, itemdescription, status, date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    vals = (name, course, contactno, item, itemdescription, status, report_date)
    cursor.execute(sql, vals)
    mydb.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
