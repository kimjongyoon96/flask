from flask import Flask, jsonify
import mojito
import pprint
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')  # 몽고DB 연결 설정

@app.route('/symbols', methods=['GET'])
def get_symbols():
    key = "PSVT5oQXN4N39r3jhoLtrCiVen4fcJ3p7zOh"
    secret = "OeeQY05O9OEfjuOP2KEtVpbP77p8WKaClPqgOEdSAVdH/FazfG51bqSc97t16uYOsvjb5DzrbqB11cfuMfBXPtwDB2BQqg7otSZAHo61OkobqBGPWJHGOHE/lt+X4WPNhyDiDu06EMiC6t+lvcIrG50t4/alJf7qhfL/dkg8sfOJgC66SDA="
    acc_no = "00000000-01"

    broker = mojito.KoreaInvestment(
        api_key=key,
        api_secret=secret,
        acc_no=acc_no
    )
    symbols = broker.fetch_symbols()   
    filtered_symbols = symbols[symbols['KRX은행'] == 'Y']
    pprint.pprint(filtered_symbols)

    # 몽고DB에 데이터 저장
    db = client['mydatabase']  # 사용할 데이터베이스 선택
    collection = db['cutee']  # 사용할 컬렉션 선택
    collection.insert_many(filtered_symbols.to_dict('records'))

    return jsonify(filtered_symbols.to_dict('records'))

if __name__ == '__main__':
    app.run()
