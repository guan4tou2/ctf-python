from Crypto.Util import number

P=bin(number.bytes_to_long(b'hello world'))[2:]
key=bin(number.bytes_to_long(b'ctf'))[2:]

# print(number.long_to_bytes(P^key))
C=''
for i in range(len(P)):
    if int(P[i])^int(key[i%len(key)]):
        C+='1'
    else:
        C+='0'

print(number.long_to_bytes(int(C,2)))

p=''
for i in range(len(C)):
    if int(C[i])^int(key[i%len(key)]):
        p+='1'
    else:
        p+='0'

print(number.long_to_bytes(int(p,2)))
