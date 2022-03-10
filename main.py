import random
print("Sa jeszcze zadania dodatkowe aby je wyswietlic wpisz dodatkowe i nr zadania np dodatkowe1\n")
print("Aby sprawdzic poprawnosc zadania wpisz zd z numerem ktory chcesz sprawdzic np: zd1, zd2 ...")
zadanie = input()
# Zadanie 1
if(zadanie == "zd1"):
  print("\nOdpowiedzi: ")
  print("0 > 1", 0 > 1)
  print("0 <= 1", 0 <= 1)
  print("0 >= 1", 0 >= 1)
  print("1 == 0", 1 == 0)
  print("1 == 1", 1 == 1)
  print("1 !=0", 1 != 0)
  print("1 != 1", 1 != 1)
# Zadanie 2
if(zadanie == "zd2"):
  print("\nPodaj liczbe x: ")
  x = int(input())
  print("Podaj liczbe y: ")
  y = int(input())
  print("Wynik wyrazenia 2x+5y to:", 2*x + 5*y)
# Zadanie 3
if(zadanie == "zd3"):
  z = 'Ala'
  x = "ma"
  y = "kota"
  zdanie = y + x + z
  print(z + " " + x + " " + y)
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
    print(a + b)
  if(x=="-"):
    print("Wynik odejmowania to: ")
    print(a - b)
  if(x=="*"):
    print("Wynik mnozenia to: ")
    print(a * b)
  if(x=="/"):
    print("Wynik dzielenia to: ")
    print(a / b)
  if(x=="**"):
    print("Wynik potegowania to: ")
    print(a ** b)
  if(x=="//"):
    print("Wynik dzielenia calkowitego: ")
    print(a // b)
  if(x=="%"):
    print("Reszta z dzielenia a//b to: ")
    print(a % b)
# Zadanie 8
if(zadanie == "zd8"):
  print("Podaj liczbe x: ")
  x = int(input())
  print("Wynik x > 1 i x < 13 to: ", x > 1 and x < 13)
  print("Wynik dla x != 5 lub x < 0 to: ", x != 5 or x < 0)
if(zadanie == "dodatkowe1"):
  print("Podaj imie: ")
  imie = input()
  print("Podaj nazwisko: ")
  nazwisko = input()
  print("Podaj wiek: ")
  wiek = int(input())
  print("\nTeraz zostanie zadanych ci 5 pytania sa to pytania w stylu tak / nie\n")
  print("Czy zdrowo sie odżywiasz ? ")
  p1 = input()
  print("\nCzy lubisz sport ? ")
  p2 = input()
  print("\nCzy pijesz dziennie 3 szklanki wody ? ")
  p3 = input()
  print("\nCzy spożywasz alkohol częściej niz 2-3 razy w miesiącu ? ")
  p4 = input()
  print("\nOstatnie pytanie.")
  print("\nCzy często zastępujesz samochód rowerem ? ")
  p5 = input()
  if(p1 == "tak" and p2 == "tak" and p3 == "tak" and p4 == "nie" and p5 == "tak"):
    print("Pan " + imie + " " + nazwisko + " mając " + str(wiek) + " lat jest jedna z najzdrowiej żyjących osób jakie znam.")
  if(p1 == "nie" and p2 == "nie" and p3 == "nie" and p4 == "tak" and p5 == "nie"):
    print("Pan " + imie + " " + nazwisko + " mając " + str(wiek) + " lat jest jedna z najgorzej żyjących osób jakie znam.")
  else:
    print("Mogło być lepiej ale nie jest najgorzej")
if(zadanie == "dodatkowe2"):
  print("Podaj imie: ")
  imie = input()
  print("Podaj nazwisko: ")
  nazwisko = input()
  print("Podaj wiek: ")
  wiek = int(input())
  print("Podaj swój zawód: ")
  zawod = input()
  print("Podaj miejsce urodzenia: ")
  miejsce_urodzenia = input()
  print("Podaj swoje zainteresowania: ")
  zainteresowania = input()
  print("\n")
  print(imie + " " + nazwisko + " lat "+ str(wiek) + " urodzony w " + miejsce_urodzenia + " z zawodu " + zawod + " jego/jej zainteresowania to: " + zainteresowania)
if(zadanie == "dodatkowe3"):
  print("Nie umiem zrobic sylab do nauki nie wiem jak sie za to zabrać to zrobiłem losowanie liczby od 1-1000 i użytkownik musi ja odgadnąc taka zabawa ma 10 prób.\n")
  liczba_prob = 0;
  liczba = random.randint(1,1000)
  while(liczba_prob != 10):
    print("Podaj liczbe z zakresu 1-1000: ")
    los = int(input())
    if(los == liczba):
      print("Brawo!! Zgadłes wylosowaną liczbę. Była to ", liczba)
      break;
    if(los < liczba):
      print("Podana liczba jest mniejsza niż wylosowana. ")
      liczba_prob += 1
    if(los > liczba):
      print("Podana liczba jest większa niż wylosowana. ")
      liczba_prob += 1
  print("\nNiestety nie udało ci się odgadnąć wylosowanej liczby. Wylosowana liczba to ", liczba)
if(zadanie == "dodatkowe4"):
  print("Podaj imie z polskimi znakami: ")
  imie = input()
  if(imie == "Janusz" or imie == "Grażyna"):
    print("Witam Janusza lub Grażynę")
  else:
    print("Liczyłem ze poznam Janusz lub Grażynę")