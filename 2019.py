ciphertext = open("2019.txt").read()

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

ex1 = val.index(4)
#print(ex1) == 2360 
pent1 = k[2360]
#print(pent1) == IYRFV

iyrfv = []
for i in range(0, len(work)):
    if("IYRFV" == work[i]):
        iyrfv.append(i)

#print(iyrfv)
# diff = 1112, 184, 128
# key_length = 8 but should have chexked with 4 letters!

#print(len(ciphertext)) == 4531 take 4528

first = ""
c = 15 # from 8 to 15
while(c <= 4527): # from 4520 to 4528
    first += ciphertext[c]
    c += 8

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

# KEY == RODGLBQF