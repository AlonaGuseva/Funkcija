#Izveidot funkciju, kas izvada asraksta elemenyus
def izdruka(daudzums, sari):
  for elem in range(0,daudzums):
    print(sar[elem])
  return 0

saraksts = [2,4,5,6,1,2,34,5]  
dudzums = int(input("Ievadi elementu skaitu: "))
rez = izdruka(daudzums, saraksts)