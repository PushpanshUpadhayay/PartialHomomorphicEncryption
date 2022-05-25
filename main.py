import cust
import json
import phe as paillier
import servercalc
import pandas as pd
cust.storeKeys()
pub_key, priv_key = cust.getKeys()
df = pd.read_csv('employee_data.csv')
l = []
for i in df.head().index:
    a = list(df.iloc[i, 0:4])
    l.append(a)
for i in l:
    data = i
    datafile = cust.serializeData(pub_key, data)
    with open('data.json', 'w') as file:
        json.dump(datafile,file)
    servercalc.writeToAnswer()
    answer_file = cust.loadAnswer()
    answer_key = paillier.PaillierPublicKey(n=int(answer_file['pubkey']['n']))
    answer = paillier.EncryptedNumber(answer_key,int(answer_file['values'][0]), int(answer_file['values'][1]))
    if answer_key==pub_key:
        print(priv_key.decrypt(answer))
