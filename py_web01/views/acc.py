from flask import Blueprint,render_template,request,redirect

#蓝图对象
ac = Blueprint("acc",__name__)

@ac.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("/index.html")

    user = request.form.get("user")
    pwd = request.form.get("pwd")
    print(user, pwd)

    import pymysql
    conn = pymysql.connect(host='192.168.2.106', port=3306, user='gzeis', passwd='gz007007*A', charset="utf8", db='web_mysql')
    cursors = conn.cursor()
    cursors.execute("select * from user_info where user=%s and pwd=%s", [user, pwd])
    #cursors.execute(sql, params)
    user_data = cursors.fetchone()
    print(user_data)
  
    cursors.close()
    conn.close()

    if user_data:
        return render_template("main.html")
    return render_template("index.html",error="用户名或密码错误！")



@ac.route('/main')
def main():
    return "list"   