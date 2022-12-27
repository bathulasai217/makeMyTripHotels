l =[1,2,3,4,5,7,13,17,23,57,80]
l1 = []

for i in l:
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            l1.append(i)

c = 2
l2 = []
for k in l1:
    while k != 0:
        for j in (2,c):
            if c%j == 0:
                break
            else:
                l2.append(c)
                c += 1
        k -= 1

print(l2)





