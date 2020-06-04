ciphertext = open("2017.txt").read()

ciphertext = ciphertext.replace(' ',"")
ciphertext = ciphertext.replace('/n',"")
#print(ciphertext)

work = []
for i in range(0, len(ciphertext)-4):
    s = ciphertext[i] + ciphertext[i+1] + ciphertext[i+2] + ciphertext[i+3] + ciphertext[i+4]
    work.append(s)

#print(work)

freq = {}
for i in work:
    freq[i] = work.count(i)

k = []
val = []
for key,value in freq.items():
    k.append(key)
    val.append(value)

newval = val
newval = sorted(val)

#print(newval)

ex1 = val.index(6) #ex1 = 401

pent1 = k[401] # == QPLZX
#print(pent1) 

qplzx = []
for i in range(0, len(work)):
    if("QPLZX" == work[i]):
        qplzx.append(i)

#print(qplzx)
# diff = 811, 1520, 150, 860, 200

#key_length = 10

#print(len(ciphertext)) == 4609
#print(ciphertext)

first = ""
c = 10 # from 10 to 19
while(c <= 4600): # from 4600 to 4609
    first += ciphertext[c]
    c += 10

print(first)
alphabet = {}

for i in list(first):
    alphabet[i] = list(first).count(i)
occ = []
for key, value in alphabet.items():
    
    occ.append(value)

print(alphabet)
occ.sort()
print(occ)


# KEY = STATISTICS