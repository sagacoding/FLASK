from flask import *
import psycopg2

app = Flask(__name__)
app.config['POSTGRES_USER'] = 'postgres'
app.config['POSTGRES_PASSWORD'] = '12345678'
app.config['POSTGRES_DB'] = 'postgres'
app.config['POSTGRES_HOST'] = 'localhost'

@app.route('/')
def index():
    connection = psycopg2.connect(
        user=app.config['POSTGRES_USER'],
        password=app.config['POSTGRES_PASSWORD'],
        host=app.config['POSTGRES_HOST'],
        database=app.config['POSTGRES_DB']
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM student_info.student_hobbies  WHERE studid=183")
    # data = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    # return render_template('dbdata.html', data=data)
    return "data successfully DELETED"
    

if __name__ == '__main__':
    app.run(debug=True)

