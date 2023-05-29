from flask import Flask, jsonify
import mojito
import pprint

app = Flask(__name__)

@app.route('/symbols', methods=['GET'])
def get_symbols():
    key = "d"
    secret = "d"
    acc_no = "00000000-01"

    broker = mojito.KoreaInvestment(
        api_key=key,
        api_secret=secret,
        acc_no=acc_no
    )
    symbols = broker.fetch_kospi_symbols()
    filtered_symbols = symbols[symbols['그룹코드'] == 'ST']
    pprint.pprint(filtered_symbols) 
    return jsonify(filtered_symbols.to_dict('records'))

if __name__ == '__main__':
    app.run()
