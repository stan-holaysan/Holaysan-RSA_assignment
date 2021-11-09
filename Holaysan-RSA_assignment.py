m1 = 'ENCRYPTION'
m2 = 'RASTAMAN'
 
p = 11
q = 13
e = 7
d = 223
 
n = p*q
z = (p-1) * (q-1)

 
def encrypt(m):
    cList = []
    for char in m:
        eChar = (ord(char) ** e) %n
        cList.append(chr(int(eChar)))
    print(cList)
    c = ''.join(cList)
    print("Encrypted Message: ", c)
    return c

def decrypt(c):
    dList = []
    for char in c:
        dChar = (ord(char) ** d) %n
        dList.append(chr(int(dChar)))
    print(dList)
    m = ''.join(dList)
    print("Decrypted Message: ", m)
    return m

def rsa_simulation(message):
    print("Original Message 1: ", message)
    c = encrypt(message)
    m = decrypt(c)


rsa_simulation(m1)
rsa_simulation(m2)