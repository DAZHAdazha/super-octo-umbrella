# 1.导入flask 扩展
from flask import Flask, render_template, flash, request, jsonify, redirect, url_for # 最后两个是用来重定向
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Text
from flask_cors import CORS
from sqlalchemy import or_
import random
import json
import csv

excelFile = r'D:\肺炎\DXY-COVID-19-Data\csv\DXYRumors.csv' # 修改为存放班级的excel位置
csvFile = r'D:\肺炎\DXY-COVID-19-Data\csv\DXYNews.csv' # 修改为存放班级的excel位置



# 2.创建Flask 应用程序实例
# 需要传入__name__, 作用是为了确定资源所在路径
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:fengyunjia@127.0.0.1:3306/肺炎可视化'  # mysql://username:password@hostname/database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'dazha' #加密混淆使用

CORS(app)
# 3.定义路由及视图函数
# Flask中定义路由是通过装饰器实现的



def read_xlrd(excelFile,title,body,summary,time):
  with open(excelFile,'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
      title.append(row[2])
      summary.append(row[3])
      body.append(row[5])
      time.append(row[8])
    title.pop(0)
    summary.pop(0)
    body.pop(0)
    time.pop(0)


def read_csv(csvFile,title,source,summary,time):
  with open(csvFile,'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
      time.append(row[2])
      title.append(row[3])
      summary.append(row[4])
      source.append(row[5])
    title.pop(0)
    summary.pop(0)
    source.pop(0)
    time.pop(0)


class Rumors(db.Model):
  # 定义表名
  __tablename__ = 'rumors'
  # 定义字段
  # db.Column表示是一个字段
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id为主键
  title = db.Column(Text)
  summary = db.Column(Text)
  body = db.Column(Text)
  time = db.Column(Text)
  # 对于一对多模型，在一的一的一方
  # backref='role'表示User要用的属性
  # repr()方法显示一个可读字符串

  def __repr__(self):
    return '<Rumors: %s %s %s %s>' % (self.title, self.summary, self.body, self.time)

  def to_json(self):
    json_data = {
      'id': self.id,
      'title': self.title,
      'summary': self.summary,
      'body': self.body,
      'time': self.time
    }
    return json.dumps(json_data, ensure_ascii=False)

class News(db.Model):
  # 定义表名
  __tablename__ = 'news'
  # 定义字段
  # db.Column表示是一个字段
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # id为主键
  title = db.Column(Text)
  summary = db.Column(Text)
  source = db.Column(Text)
  time = db.Column(Text)
  # 对于一对多模型，在一的一的一方
  # backref='role'表示User要用的属性
  # repr()方法显示一个可读字符串

  def __repr__(self):
    return '<Rumors: %s %s %s %s>' % (self.title, self.summary, self.source, self.time)

  def to_json(self):
    json_data = {
      'id': self.id,
      'title': self.title,
      'summary': self.summary,
      'source': self.source,
      'time': self.time
    }
    return json.dumps(json_data, ensure_ascii=False)


# 用flash给模板传递消息, 模板中需要遍历消息,需要对内容进行加密，因此要设置
# secret_key, 做加密消息的混淆
# @app.route('/', methods=['GET', 'POST'])  # 路由默认只支持GET，如需要增加，需自行指定
# def index():
#     # request 为请求对象-->获取请求方式，数据
#     if request.method == 'POST':
#         # 获取请求的参数
#         username = request.form.get('username')
#         password = request.form.get('password')
#         password2 = request.form.get('password2')
#         print(username, password, password2)
#         if not all([username, password, password2]):
#             flash('缺少参数')
#         elif password != password2:
#             flash('不完整')
#         else:
#             return 'success'
#     url = 'www.baidu.com' # url为变量名
#     my_list = [1, 3, 5, 7]
#     # return 'hello hahdshdasdsada uwq jq fdpqoi fuiog qjg  flask' # 返回字符串
#     return render_template('index.html', url_str=url, this_list=my_list) #注意使用返回模板时jinjia2默认在templates文件夹中寻找 注意s！
#     #url_str 为可在html中使用的变量名（html文件中使用{{url_str}}, url为之前的变量名
#     #通常变量名与传入参数名字一致 如 url_str=url_str,此处为区别分清



# 使用同一个路由函数 来显示不同用户的订单信息 如在根目录的/orders子目录下传入参数（订单号）来取得对于信息：/orders/11111
# <>定义路由的参数，<>内需要自行取名字（如order_id）
@app.route('/orders/<int:order_id>') #注：参数默认类型为字符串，unicode， 此处的“int:”为限定参数类型 作为路由优化 也可为float等
def get_order_id(order_id): #此次参数是为了方便后面return中再次使用
    return 'order_id %s' % order_id

@app.route('/rumors_search',methods=['GET', 'POST']) #注：参数默认类型为字符串，unicode， 此处的“int:”为限定参数类型 作为路由优化 也可为float等
def get_rumor(): #此次参数是为了方便后面return中再次使用
    if request.method == 'POST':
      q = request.get_json()['title']
      # print(q)
      rumor = Rumors.query.filter(or_(Rumors.title.contains(q), Rumors.body.contains(q), Rumors.summary.contains(q), Rumors.time.contains(q)))
      dict = []
      # print(rumor.all())
      for i in rumor.all():
        dict.append(i.to_json())
      # print(dict)
    return json.dumps(dict)


@app.route('/rumors', methods=['GET']) #注：参数默认类型为字符串，unicode， 此处的“int:”为限定参数类型 作为路由优化 也可为float等
def show_rumor(): #此次参数是为了方便后面return中再次使用
      random_list = []
      random_count = 0
      rows = db.session.query(Rumors).count()
      mark = True
      while mark:
        if random_count >= 10:
          break
        else:
          random_num = random.randint(0, rows-1)
          if random_num in random_list:
            continue
          else:
            random_list.append(random_num)
            random_count += 1
      dict = []
      for i in random_list:
        dict.append(Rumors.query.filter_by(id=i).first().to_json())
      # print(dict)
      return json.dumps(dict)



@app.route('/news_search',methods=['GET', 'POST']) #注：参数默认类型为字符串，unicode， 此处的“int:”为限定参数类型 作为路由优化 也可为float等
def get_news(): #此次参数是为了方便后面return中再次使用
    if request.method == 'POST':
      q = request.get_json()['title']
      print(q)
      dict = []
      news = News.query.filter(or_(News.title.contains(q), News.source.contains(q), News.summary.contains(q), News.time.contains(q)))
      print(news.all())
      for i in news.all():
        dict.append(i.to_json())
    return json.dumps(dict)

# 4.启动程序
if __name__ == '__main__':
    # db.drop_all()
    # 创建表
    # db.create_all()

    # body = []
    # time = []
    # title = []
    # summary = []
    # read_xlrd(excelFile, title, body,summary, time)
    # print(title)
    # print(body)
    # print(summary)
    # print(time)
    # source = []
    # time = []
    # title = []
    # summary = []
    # read_csv(csvFile, title, source,summary, time)
    #
    # for i in range(len(title)):
    #   item = News(title=title[i],summary=summary[i],source=source[i],time=time[i])
    #   db.session.add(item)
    # db.session.commit()

    #
    # for i in range(len(title)):
    #   item = Rumors(title=title[i],summary=summary[i],body=body[i],time=time[i])
    #   db.session.add(item)
    # db.session.commit()
    #执行了app.run(),就会将flask程序运行在一个简易的服务器（Flask 提供，用于测试）
    app.run(debug=True)
