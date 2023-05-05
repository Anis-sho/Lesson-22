#Anis


#1.Masalan list va tuple in yakum Qavsho hastand. Badash in ijroishi onho va dokhilu voridkuni ba hamon listho ast

Tuple=('Ali','Foiq','Tabrez','Anis','Ziyo')
List=["Anis","Ato","Foiq","Takhmuraz","Ali","Shahboshah"]


#2.Farqiyat bayni global va local tagiryobandaho on ast ki agar mo global tagiryobanda monem
dar hama joyi kodamon on hamin qimatro megirad. Amo agar mo local tagiryobandaro monem mo metavonem har 
dof onro ivaz namoem.

maslan "Muso" in global tagiryobanda ast

x='Anis'

def MyFunction ():
    global x
    x='Muso'
    print(x)

MyFunction()
print(x)


va dar in jo local tagiryobanda ast

x='tillo'

def MyFunction ():
    x='nuqra'
    print(x)

MyFunction()
print(x)




#3.Operatorhoi cikli dar Python in While va for hastand


while True:
    name = input("Enter you name: ")
    if name != "":
        break

print(name)



for i in range(1,11):
    if i == 5:
        pass
    else:
        print(i)
        


4.String in navi tagiryobandaest ki dar "" - ho joygir meshavad va onro mo dar hisobkuni nametavonem jam kunem.
vay metavonad faqat khudash navista shavad.

nom = "Nomi man Anis"

5. Dar Python mo Functionro bo def muarifi mekunem. Masalan


x='Talaba'

def MyFunction ():
    global x
    x='Donishju'
    print(x)

MyFunction()
print(x)

6.Boplean dar Python in amon komandahoe ki bo >,<, <=, >= muarrifi meshavad

print(3>5)
print(5>=9)



7.Dar Python mo Dictionaryro dar vaqti muharifi kardani tagiryobanda va maqnoi onro medihem va dar lis boshad 
mo faqat guruhro muharifi mekunem

masalan baroi list - 

List=["Anis","Ato","Foiq","Takhmuraz","Ali","Shahboshah"]

va baroi dictionary mo -  

myCarInfo = {
    "name":"Anis",
    "city":"Khorog",
    "education":"master",
    "birth":1994
}

for x,y in myCarInfo.items():

    print(str(x) + " - " + str(y))




8. Konvertkunoniro mo  bo komandai .lower()

Player = input("Playing game? ")

if Player.lower() != "yes":
    quit()
    
print("Lets play!")


9.Az listi Python mo hamin kheli mekunem

myCarInfo = {
    "name":"Anis",
    "city":"Khorog",
    "education":"master",
    "birth":1994
}

#In Muayan tagiryobandaro del mekunad
myCarInfo.pop("birth")

# in boshab o9khironro
myCarInfo.popitem()

print(myCarInfo)