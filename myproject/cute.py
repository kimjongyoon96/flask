import mojito
import pprint
from flask import Flask, jsonify

key = "d"
secret = "d"
acc_no = "00000000-01"

broker = mojito.KoreaInvestment(
    api_key = key,
    api_secret = secret,
    acc_no = acc_no
)
symbols = broker.fetch_kospi_symbols()   
    # 코스피
symbols.head()  # 0부터 모든것을 출력시킨다.

filtered_symbols = symbols[symbols['그룹코드'] == 'ST']
print(filtered_symbols)




