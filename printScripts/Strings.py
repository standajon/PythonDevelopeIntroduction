print("Ahoj svete")

zprava="Mam rad Python"
print(zprava)

zprava2="Tohle je hodne douhy text.Tohle je hodne douhy text.Tohle je hodne douhy text.Tohle je hodne douhy text.Tohle je hodne douhy text.Tohle je hodne douhy text."
print(zprava2)

zprava3="""Tohle je hodne douhy text.
Tohle je hodne douhy text.
Tohle je hodne douhy text.
Tohle je hodne douhy text.
Tohle je hodne douhy text.
Tohle je hodne douhy text."""
print(zprava3)
#delka retezce
print(len(zprava3))

txt="     pes     "
txtShort=txt.strip()
print(txtShort)

neco="AAAAAAAAAAAA"
print(neco.lower())

#indexace konkretniho znaku
textik = "Tohle je nejaka veta"
print(textik[1])

pozdrav = "Ahoj ahoj"
print(pozdrav[0:4])

#spocita vyskyt pismena
print(pozdrav.count("o"))

msg = "Ahoj"
msg2 = "Stando"
print(msg + " " + msg2)

#dostuopne metody co se da s tim delat
print(dir(msg))


