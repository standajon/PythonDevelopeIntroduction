#list uchovava vice hodnot v jedne promenne

mujList = ['pes','kocka','kralik']

print(mujList)

print(len(mujList))
print(type(mujList))

#list je indexovany. Prvni hodnota je 0 a pak 1, 2, atd...

print(mujList[1])

#negativni - od konce
print(mujList[-1])


if mujList[1]=="kocka":
    print('Je to kocka')
else:
    print("je to neco jinyho")


if "pes" in mujList:
    print("Pes je na seznamu")







