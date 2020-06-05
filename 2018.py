# try out all the print statements in the comments for better understanding.

ciphertext = open("2017.txt").read()#open file and store in string

ciphertext = ciphertext.replace(' ',"")#remove all spaces
ciphertext = ciphertext.replace('/n',"")#remove all newwlines
#print(ciphertext)


work = [] #list of consecutive five-character strings, optimize at will.
for i in range(0, len(ciphertext)-4):
    s = ciphertext[i] + ciphertext[i+1] + ciphertext[i+2] + ciphertext[i+3] + ciphertext[i+4]
    work.append(s)

#print(work)


freq = {} #dictionary to store the frequency of all the five-character strings.
for i in work:
    freq[i] = work.count(i)

k = []
val = []
for key,value in freq.items():
    k.append(key)
    val.append(value)

newval = val
newval = sorted(val)#to find the few largest frequencies.
#print(newval)

ex1 = val.index(4)
#print(ex1) == 2092

pent1 = k[2092]
#print(pent1) == DJEEZ, the five-chracter string with largest frequency. 

djeez = []
for i in range(0, len(work)):
    if("DJEEZ" == work[i]):
        djeez.append(i)

#print(djeez)
# diff = 1112, 184, 128
# key_length = 8(check the common factor of diff. values, and take the largest one.)

#print(len(ciphertext)) == 4278 take 4272

first = ""
c = 15 # from 8 to 15
while(c <= 4272): # from 4264 to 4272
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