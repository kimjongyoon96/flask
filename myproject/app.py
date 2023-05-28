from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')  # 몽고DB 연결

@app.route('/')
def hello():
    db = client['mydatabase']  # 데이터베이스 선택
    collection = db['mycollection']  # 컬렉션 선택
    data = {'name': 'John', 'age': 25}  # 새로운 문서 생성
    collection.insert_one(data)  # 문서 삽입
    return 'Hello, Flask! Data inserted.'

if __name__ == '__main__':
    app.run()
