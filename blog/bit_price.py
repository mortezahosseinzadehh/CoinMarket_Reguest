import json
import requests
from requests import Session, Request




url = "https://api.coinmarketcap.com/asset/v3/watchlist/query"
payload = {
'json':  { "watchListType": "ORDINARY",
  "aux": "5",
  "cryptoAux": "ath,atl,high24h,low24h,max_supply,self_reported_circulating_supply,self_reported_market_cap,circulating_supply,total_supply,volume_7d,volume_30d,tvl,audit,cmc_rank",
  "convertIds": "1,1027,2781"}
}
headers = {
    'Authorization': "Bearer eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJyb2xlcyI6ImFjY291bnRXZWIsYWNjb3VudE1vYmlsZSIsImlzcyI6ImNtYy1hdXRoIiwiaWF0IjoxNjQwODE4NTM1LCJzdWIiOiI2MWNjYWY2NmZiNmYyZTUxYWYzYjU4OGMiLCJleHAiOjE2NDM0MTA1MzV9.HEFMRfEp5xuPxeIgC37sv1vlLCYwmlSQSFLGgEzfFFU",

  }

sessions = Session()

sessions.headers.update(headers)


response = requests.request("POST", url, json=payload, headers=headers)



file_json = json.loads(response.text)

#doge_elon_mars

#vol_24

doge_elon_24h = (file_json['data']['watchLists'][0]['cryptoCurrencies'][0]['quotes'][0]['volume24h'])
#change7d
doge_elon_7d = (file_json['data']['watchLists'][0]['cryptoCurrencies'][0]['quotes'][0]['percentChange7d'])

#baby_doge_coin
#vol_24

baby_coin_24 = (file_json['data']['watchLists'][0]['cryptoCurrencies'][1]['quotes'][0]['volume24h'])



#change7d

baby_coin_7d = (file_json['data']['watchLists'][0]['cryptoCurrencies'][1]['quotes'][0]['percentChange7d'])



#holder



#dogelon_holder





response2 = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/holders/count?id=9436&range=7d")

json_data = json.loads( response2.text)
mori = (json_data['data']['points'])
mori_2 = str(mori)
mori_3 = mori_2.replace("}", "")
json_data2 = mori_3.replace("{", "")


# print(json_data2.split(',', 10)[6])


doge_hold_w1 = (json_data2.split(',', 10)[5])
doge_hold_w2 = (json_data2.split(',', 10)[3])
doge_hold_w3 = (json_data2.split(',', 10)[0])
doge_hold_w4 = (json_data2.split(',', 10)[6])
doge_hold_w5 = (json_data2.split(',', 10)[1])
doge_hold_w6 = (json_data2.split(',', 10)[2])
doge_hold_w7 = (json_data2.split(',', 10)[4])

#baby_dog_holder
response_m = requests.get("https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/holders/count?id=10407&range=7d")

json_data3 = json.loads(response_m.text)
morix = (json_data3['data']['points'])

morix2 = str(morix)

morix3 = morix2.replace("}", "")
json_mori = morix3.replace("{", "")

# print(json_mori.split(',', 10)[6])

# print(json_mori)

baby_hold_w1 = (json_mori.split(',', 10)[5])
baby_hold_w2 = (json_mori.split(',', 10)[3])
baby_hold_w3 = (json_mori.split(',', 10)[0])
baby_hold_w4 = (json_mori.split(',', 10)[6])
baby_hold_w5 = (json_mori.split(',', 10)[1])
baby_hold_w6 = (json_mori.split(',', 10)[2])
baby_hold_w7 = (json_mori.split(',', 10)[4])
# print(baby_hold_w6)

context = {


            "doge_24": doge_elon_24h,
            "doge7d": doge_elon_7d,
            "baby24": baby_coin_24,
            "baby7": baby_coin_7d,
            "d_h_1": doge_hold_w1,
            "d_h_2": doge_hold_w2,
            "d_h_3": doge_hold_w3,
            "d_h_4": doge_hold_w4,
            "d_h_5": doge_hold_w5,
            "d_h_6": doge_hold_w6,
            "d_h_7": doge_hold_w7,
            "b_h_1": baby_hold_w1,
            "b_h_2": baby_hold_w2,
            "b_h_3": baby_hold_w3,
            "b_h_4": baby_hold_w4,
            "b_h_5": baby_hold_w5,
            "b_h_6": baby_hold_w6,
            "b_h_7": baby_hold_w7,




}
# print(context["b_h_7"])