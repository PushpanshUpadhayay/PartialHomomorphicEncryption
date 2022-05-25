# PartialHomomorphicEncryption
In traditional cryptography, a public key is used to encrypt the data. And a secret private key is exchanged between the two parties for decrypting it. When this processing happens on the cloud, the cloud server must have access to the secret key to unlock the data for processing purposes. Homomorphic encryption simplifies and secures this process by allowing the cloud to perform computations on ciphertext or the encrypted data. And then return those encrypted results to the owner of the data. So, the data is never decrypted at any point in time, and complete privacy is maintained, regardless of where data is stored.

For any encryption to fall under Partially Homomorphic Encryption two properties need to be true:
1) D(E(A)+E(B)) = A+B, where D()-> Decrypt(), E()-> Encrypt(), A & B-> cipher text
2) D(E(A)*scaler) = A*scaler, scaler here refers to a constant value (exponent of the value in accordance with this project)
