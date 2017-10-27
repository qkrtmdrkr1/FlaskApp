from flask import Flask, render_template
import MySQLdb


def connection():
    conn = MySQLdb.connect(host="192.168.123.122",
                            user = "park",
                            passwd = "ubuntu",
                            db = "sushi")
    c = conn.cursor()

    return c, conn

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/Show_Me_The_Sushi')
def show_me_the_sushi():
    return render_template("show_me_the_sushi.html")

@app.route('/header.html')
def header():
    return render_template("header.html")

@app.route('/owner/header.html')
def owner_header():
    return render_template("header.html")

@app.route('/owner')
def owner():
    return render_template("owner.html")

@app.route('/owner/hyun')
def hyun():
    return render_template('owner_hyun.html')

@app.route('/owner/gak')
def gak():
    return render_template('owner_gak.html')

@app.route('/owner/bae')
def bae():
    return render_template('owner_bae.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/list')
def lists():
    cnt = 0
    c, conn = connection()
    c.execute("SELECT * FROM data")
    d = c.fetchall()
 
    templist = []
    for element in d:
        templist.append(list(element))
        cnt += 1
    conn.commit()
    conn.close()

    return render_template('list.html', row = templist, cnt = cnt)

#############################
@app.route('/check')
def check():
    try:
        c, conn = connection()
        return "Okay!!"
    except Exception as e:
        return "Error"
##############################
if __name__ == '__main__':
    app.run()



