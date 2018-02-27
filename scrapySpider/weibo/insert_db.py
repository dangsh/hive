import pymysql
import json

def read_data():
    with open('2_23.json' , encoding='utf-8') as f:
        for i in range(3066):
            line = f.readline()
            d = json.loads(line)
            userid = d["userid"]
            username = d["username"]
            make_insert(userid , username)
    f.close()

def make_insert(userid , username):
    cursor = conn.cursor()
    cursor.execute("select id from weibouser where userid = %s" % userid)
    a = cursor.fetchall()
    print(a)
    if len(a) > 0:
        pass
    else:
        cursor.execute("insert into weibouser (userid,username) VALUES ('%s','%s')"%(userid , username))
    conn.commit()

if __name__ == "__main__":
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='5801200zxg',
        db='weibo',
        charset='utf8'
    )
    read_data()

