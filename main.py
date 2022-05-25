import cust
import json
import phe as paillier
import servercalc

if __name__=='__main':
    cust.storeKeys()
    pub_key, priv_key = cust.getKeys()
    data = age, he, al, gen = [24,4,6,1]
    datafile = cust.serializeData(pub_key, data)
    with open('data.json', 'w') as file:
        json.dump(datafile,file)

    answer_file = cust.loadAnswer()
    answer_key = paillier.PaillierPublicKey(n=int(answer_file['pubkey']['n']))
    answer = paillier.EncryptedNumber(answer_key,int(answer_file['values'][0]), int(answer_file['values'][1]))
    if answer_key==pub_key:
        print(priv_key.decrypt(answer))