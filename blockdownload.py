import  json
import requests
from requests.auth import HTTPDigestAuth
import json

start = 1000000
end = start+100
for block in range(start,end+1):
    blockhex = hex(block)
    url = "https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag="+blockhex+"&boolean=true&apikey=S47AGG7U6NA7BQG1GI5QCDNA9XMN69PW1E"

    myResponse = requests.get(url)
    if(myResponse.ok):

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.content)
        trxlist = jData['result']['transactions']
        for trx in trxlist:
            blockhash = trx['blockHash']
            trxhash = trx['hash']
            filename = '/home/shashi/RenoirExperiment/Block1/' + blockhash
            with open(filename, "a+") as f:
                f.write(trxhash+"\n")
                # print(trxhash)

    else:
      # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()