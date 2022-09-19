cislo5=5
print(type(cislo5))


cislo5="5" # a vsude dale v programu uz bude string
print(type(cislo5))

#konkretni situace, jen jednou
print(type(str(cislo5)))

#pretypovani jen 1x, pak uz nefunguje
cislo5=5
str(cislo5)
print(type(cislo5))

jmeno="Petr"
print("Ahoj "+jmeno)
print("Ahoj"+str(cislo5))

#---------------------------------------
print(type(0.123))