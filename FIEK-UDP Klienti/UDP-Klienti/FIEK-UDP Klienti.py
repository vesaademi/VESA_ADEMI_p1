#klientiudp


import socket
from socket import * 
import sys
UDP_IP="localhost"
UDP_PORT=11000
print ('----------------------------------------------------------------------------------------------------------------------           ')
print ('                                                UNIVERSITETI I PRISHTINES                                                        ')
print ('                                      Fakulteti i Inxhinieris Elektrike dhe Kompjuterike                                         ')
print ('                                                Departamenti i Kompjuterikes                                                     ')
print ('                                                 Lenda:Rrjeta Kompjuterike                                                       ')
print ('----------------------------------------------------------------------------------------------------------------------           ')
print ('\n\n\n\n\n                                             Projekti 1: DIZAJNIMI KLIENT-SERVER                                       ')
print('\n\n\n\n\nProfesori i lendes:Prof.Asoc.Dr Blerim Rexha                                 Asistenti i lendes:Prof.Asoc.Dr Haxhi Lajqi')
print('\n\n\n\n\n                                                    Studentja:Vesa Ademi                                                ')
s=socket(AF_INET,SOCK_DGRAM)
s.connect((UDP_IP,UDP_PORT))

print ("\n\n\nKerkesat e meposhte mund te shqyrtohen nga klienti:                         ")
print("1.IP ADDRESSA E KLIENTIT                                           ")
print("2.PORTI NUMBER I KLIENTIT                                          ")
print("3.ZANORE                                                           ")
print("  -->Shkruani kerkesen tuaj ne formen : 3 fjaliajuaj          ")
print("4.PRINTO                                                           ")
print("  -->Shkruani kerkesen tuaj ne formen : 4 fjaliajuaj          ")
print("5.EMRI I KLIENTIT                                                  ")
print("6.KOHA                                                             ")
print("7.LOJA                                                             ")
print("8.FIBONACCI                                                        ")
print("  -->Shkruani kerkesen tuaj ne formen : 8 numriqedeshironi         ")
print("9.KONVERTO                                                         ")
print("  -->Llojet e konvertimev qe mund te beni: C-to-K,C-to-F,K-to-C,F-to-C,F-to-K,pound-to-kg,kg-to-pound")
print("  --> Shkruani kerkesen ne formen : 9 Llojiikonvertimit numri")
print("10.INCH-CM                                                         ")
print("  -->Llojet e konvertimev: INCH-TO-CM , CM-TO-INCH")
print("  --> Shkruani kerkesen tuaj ne formen : 10 llojikonvertimit numri                                   ")
print("11 BMI-WEIGHT                                                      ")
print("  -->Shkruani kerkesen tuaj ne formen : 11 gjatesia pesha                                       ")
print("Nese doni te perfundoni shtypni PO")
while True:
    nr=input("\n\nKerkesa:")
    if(nr=="3"):
        print("Shkruani 3 fjalia")
        continue
    elif(nr=="4"):
        print("Shkruani 4 fjalia")
        continue
    elif(nr=="8"):
        print("Shkruani 8 numri")
        continue
    elif(nr=="9"):
        print("Shkruani 9 llojiikonvertimit numri")
        continue
    elif (nr=="10"):
        print("Shkruani 10 llojikonvertimit numri")
        continue
    elif(nr=="11"):
        print("Shkruani 11 gjatesia pesha ")
        continue
    elif (nr=="PO"):
       print("Keni perfunduar ketu!")
       break

    try:
        s.send(nr.encode("ASCII"))
    except:
        print("Kerkesa nuk mund te pranohet nga serveri!")

    Rezultati=s.recv(128)
    try:
        print("Rezultati:"+Rezultati.decode("ASCII"))
    except Exception:
        print("Rezultati:"+Rezultati.decode("utf8"))

s.close()

    

