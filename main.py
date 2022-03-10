print("Aby sprawdzic poprawnosc zadania wpisz zd z numerem ktory chcesz sprawdzic np: zd1, zd2 ...")
zadanie = input()
# Zadanie 1
if(zadanie == "zd1"):
  print("Odpowiedzi: ")
  print("0 > 1", 0 > 1)
  print("0 <= 1", 0 <= 1)
  print("0 >= 1", 0 >= 1)
  print("1 == 0", 1 == 0)
  print("1 == 1", 1 == 1)
  print("1 !=0", 1 != 0)
  print("1 != 1", 1 != 1)
# Zadanie 2
if(zadanie == "zd2"):
  print("Podaj liczbe x: ")
  x = int(input())
  print("Podaj liczbe y: ")
  y = int(input())
  print("Wynik wyrazenia 2x+5y to:", 2*x + 5*y)
# Zadanie 3
if(zadanie == "zd3"):
  z = 'Ala'
  x = "ma"
  y = "kota"
  zdanie = y + " " + x + " " + z
  print(zdanie)
  print(y, x, z)
# Zadanie 4
if(zadanie == "zd4"):
  print("Podaj imie i nazwisko: ")
  a = input()
  print("Podaj wiek: ")
  c = int(input())
  print("Podaj kierunek studiow: ")
  d = input()
  print("Jestem " + a + " mam " + str(c) + " studiuje " + d)
# Zadanie 5
if(zadanie == "zd5"):
  suma = 1 + 2 + 10 + 20000001 + 4 + 347586970885
  if(suma == 321784560456434534646):
    print("Suma liczb 1 + 2 + 10 + 20000001 + 4 + 347586970885 jest rowna     321784560456434534646")
  if(suma < 321784560456434534646):
    print("Suma liczb 1 + 2 + 10 + 20000001 + 4 + 347586970885 jest mniejsza od 321784560456434534646")
  if(suma > 321784560456434534646):
    print("Suma liczb 1 + 2 + 10 + 20000001 + 4 + 347586970885 jest wieksza od 321784560456434534646")
# Zadanie 6
if(zadanie == "zd6"):
  print("Podaj liczbe a: ")
  a = int(input())
  print("Podaj liczbe b: ")
  b = int(input())
  if((a+b) % 2 == 0):
    print("Suma liczb", a,"i", b, "jest parzysta")
  if((a+b) % 2 != 0):
    print("Suma liczb", a, "i", b, "jest nie parzysta")
# Zadanie 7
if(zadanie == "zd7"):
  print("Podaj liczbe a: ")
  a = int(input())
  print("Podaj liczbe b: ")
  b = int(input())
  print("\n+ to dodawanie, - to odejmowanie, * to mnozenie, / to dzielenie, ** to potegowanie, // to dzielenie bez reszty, % to reszta z dzielenia\n")
  print("Podaj znakiem matematycznym jakie dzialanie ma zostac wykonane: ")
  x = input()
  if(x=="+"):
    print("Wynik dodawania to: ")
    print(a+b)
  if(x=="-"):
    print("Wynik odejmowania to: ")
    print(a-b)
  if(x=="*"):
    print("Wynik mnozenia to: ")
    print(a*b)
  if(x=="/"):
    print("Wynik dzielenia to: ")
    print(a/b)
  if(x=="**"):
    print("Wynik potegowania to: ")
    print(a**b)
  if(x=="//"):
    print("Wynik dzielenia calkowitego: ")
    print(a//b)
  if(x=="%"):
    print("Reszta z dzielenia a//b to: ")
    print(a%b)
# Zadanie 8
if(zadanie == "zd8"):
  print("Podaj liczbe x: ")
  x = int(input())
  print("Wynik x > 1 i x < 13 to: ", x > 1 and x < 13)
  print("Wynik dla x != 5 lub x < 0 to: ", x != 5 or x < 0)