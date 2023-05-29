import mojito
import pprint
from flask import Flask, jsonify

# 단축코드, 표준코드, 한글명, 그룹코드, 시가총액규모, 지수업종대분류, 지수업종중분류, 지수업종소분류, 제조업, 저유동성, 지배구조지수종목, KOSPI200섹터업종, KOSPI100, KOSPI50, KRX, ETP, ELW발행, KRX100, KRX자동차, KRX반도체, KRX바이오, KRX은행, SPAC, KRX에너지화학, KRX철강, 단기과열, KRX미디어통신, KRX건설, Non1, KRX증권, KRX선박, KRX섹터_보험, KRX섹터_운송, SRI, 기준가, 매매수량단위, 시간외수량단위, 거래정지, 정리매매, 관리종목, 시장경고, 경고예고, 불성실공시, 우회상장, 락구분, 액면변경, 증자구분, 증거금비율, 신용가능, 신용기간, 전일거래량, 액면가, 상장일자, 상장주수, 자본금, 결산월, 공모가, 우선주, 공매도과열, 이상급등, KRX300, KOSPI, 매출액, 영업이익, 경상이익, 당기순이익, ROE, 기준년월, 시가총액, 그룹사코드, 회사신용한도초과, 담보대출가능, 대주가능



key = "PSVT5oQXN4N39r3jhoLtrCiVen4fcJ3p7zOh"
secret = "OeeQY05O9OEfjuOP2KEtVpbP77p8WKaClPqgOEdSAVdH/FazfG51bqSc97t16uYOsvjb5DzrbqB11cfuMfBXPtwDB2BQqg7otSZAHo61OkobqBGPWJHGOHE/lt+X4WPNhyDiDu06EMiC6t+lvcIrG50t4/alJf7qhfL/dkg8sfOJgC66SDA="
acc_no = "00000000-01"

broker = mojito.KoreaInvestment(
    api_key = key,
    api_secret = secret,
    acc_no = acc_no
)
# symbols = broker.fetch_kospi_symbols()    
symbols = broker.fetch_symbols()     # 코스피
symbols.head()  # 0부터 모든것을 출력시킨다.
filtered_symbols = symbols[symbols['KRX반도체'] == 'Y'] 
print(filtered_symbols)


