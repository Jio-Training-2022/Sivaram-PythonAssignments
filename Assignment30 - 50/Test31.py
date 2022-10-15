import hashlib
result = hashlib.md5(b'AI is awesome')
print("The byte equivalent of hash is : ", end ="")
print(result.digest())