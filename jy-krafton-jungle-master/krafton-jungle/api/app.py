from flask import Flask, jsonify, request, render_template
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.jungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items', methods=['POST'])
def post_items():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분


@app.route('/items', methods=['GET'])
def get_items():
  items = list(db.items.find({}, {'_id': 0}))
  return jsonify(items)

@app.route('/items', methods=['POST'])
def get_items():
    # 1. 클라이언트로부터 데이터를 받기
    # 2. meta tag를 스크래핑하기
    # 3. mongoDB에 데이터 넣기
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})

if __name__ == '__main__':  
  app.run('0.0.0.0',port=5001,debug=True)
  


