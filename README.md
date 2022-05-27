![pic](https://user-images.githubusercontent.com/23193659/170720475-234a2095-05d3-45fc-94de-4306e99a3f69.jpg)
# PartialHomomorphicEncryption
In traditional cryptography, a public key is used to encrypt the data. And a secret private key is exchanged between the two parties for decrypting it. When this processing happens on the cloud, the cloud server must have access to the secret key to unlock the data for processing purposes. Homomorphic encryption simplifies and secures this process by allowing the cloud to perform computations on ciphertext or the encrypted data. And then return those encrypted results to the owner of the data. So, the data is never decrypted at any point in time, and complete privacy is maintained, regardless of where data is stored.

For any encryption to fall under Partially Homomorphic Encryption two properties need to be true:
1) D(E(A)+E(B)) = A+B, where D()-> Decrypt(), E()-> Encrypt(), A & B-> cipher text
2) D(E(A)*scaler) = A*scaler, scaler here refers to a constant value (exponent of the value in accordance with this project)

In the code provided, I have implemented Pascal Paillier Homomorphic Encryption. Here, the code is divided into three pages:
1) linmodel.py: This page implements linear regression on the dataset (employee_data.csv) to predict salary of the employee based on the parameters such as age, healthy_eating, active_lifestyle, and gender.

2) cust.py: This page implements Paillier Homomorphic encryption on the customer side generating the public and private keys further, serializing the data by using encrypt() function thus generating a Encrypted number to be saved on the cloud creating a json file to be sent to the server or the cloud. Also, loadAnswer() function loads the answer.json file that customer receives from the server.

3) servercalc.py: This page deserializes the data sent by customer, using EncryptedNumber() function to return EncryptedNumber using public_key and ciphertext as encrypt() was used to generate the EncryptedNumber customer side. Then, the encrypted number is multiplied by the coefficients returned after applying linear regression to the data which returns the predicted salary for the corresponding data which is then serialized at the server side. Finally, writing the serialized predicted data into the answer.json file.
