import base64
print(base64.b64encode(b"hello"))
print(base64.b64decode(b"aGVsbG8="))

import hashlib
data="hello"

m=hashlib.md5()
m.update(data.encode("utf-8"))
h=m.hexdigest()
print(h)

s=hashlib.sha256()
s.update(data.encode("utf-8"))
h=s.hexdigest()
print(h)
