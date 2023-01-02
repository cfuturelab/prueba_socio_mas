import hashlib
import requests


sha256 = hashlib.sha256()
sha256.update('heroyf1'.encode('utf-8'))
res1 = sha256.hexdigest()

# sha256.update('heroyf2'.encode('utf-8'))
# res2 = sha256.hexdigest()
# print(res1 ,res2)


def proofOfWork():
    data = 'heroyf'
    