import random 
puu = """
   /V\    
  / V \
 / V V \  
/VV V VV\   
"""

try:
    n = int(input("kirjuta arv 1-9"))
except:
    print("valed andmet")
for i in range(n):
    print(puu)

2

R = int(input("kirjuta arv"))
summa = 1
if R % 2 == 1:
    for i in range(1, R + 1, 2):
        summa *= i
    print(summa)
else:
    print("vale")

3

N = random.randint(0,100)
print(N)
positivset = 0
mitu = 0
for i in range(N):
    randomNumber = random.randint(-100,100)
    if randomNumber > 0:
         positivset += 1
    mitu += 1
print("positivsed - ", positivset)

4

a = int(input("kirjutage arv"))
paaritu = 0
paaris = 0
for i in a:
    if i % 2 == 0:
        paaris += 1
    else:
        paaritu += 1
print(paaris, paaritu)


5

summa = 0
A = int(input("kirjutage arv A"))
B = int(input("kirjutage arv B"))
for i in range(A,B +1):
    summa += i
print(summa)






