from socket import *
import time
import re
from socket import gethostname;
import random
import datetime
import math
import sys
import string
import _thread
UDP_IP="localhost"
UDP_PORT=11000
serverSocket =socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',UDP_PORT))

print('SERVERI U STARTUA ne:'+str(UDP_PORT))


print ("----------------------------------------------------------------------------------------------------------------------")
print ("                                                UNIVERSITETI I PRISHTINES                                             ")
print ("                                      Fakulteti i Inxhinieris Elektrike dhe Kompjuterike                              ")
print ("                                                Departamenti i Kompjuterikes                                          ")
print ("                                                 Lenda:Rrjeta Kompjuterike                                            ")
print ("----------------------------------------------------------------------------------------------------------------------")
print ("\n\n\n\n\n                                             Projekti 1: DIZAJNIMI KLIENT-SERVER                                 ")
print("\n\n\n\n\nProfesori i lendes:Prof.Asoc.Dr Blerim Rexha                                 Asistenti i lendes:Prof.Asoc.Dr Haxhi Lajqi")
print("\n\n\n\n\n                                                    Studentja:Vesa Ademi                                          ")
print("\n\n\n\n")
print("                                                     Operacionet:                                            ")
print("                                                1.IP ADDRESSA E KLIENTIT                                     ")
print("                                                2.PORTI NUMBER I KLIENTIT                                    ")
print("                                                3.ZANORE                                                     ")
print("                                                4.PRINTO                                                     ")
print("                                                5.EMRI I KLIENTIT                                            ")
print("                                                6.KOHA                                                       ")
print("                                                7.LOJA                                                       ")
print("                                                8.FIBONACCI                                                  ")
print("                                                9.KONVERTO                                                   ")

def clientThread(serverSocket,Clientaddress,next):
    def IP():
        MESSAGE=Clientaddress[0]
        serverSocket.sendto(str(MESSAGE).encode("ASCII"),Clientaddress)

    def PORT():
        MESSAGE=Clientaddress[1]
        serverSocket.sendto(str(MESSAGE).encode("ASCII"),Clientaddress)

    def ZANORE(s):

        i=0
        counter=0
        while i<len(s):
            if s[i] in 'aeiouAEIOU':
                counter=counter+1
            i=i+1
        MESSAGE="Teksti ka "+ str(counter)+" zanore."
        serverSocket.sendto(MESSAGE.encode("ASCII"),Clientaddress)

    def PRINTO(tex):
         splitArray = tex
         i=1
         teksti = ""
         s = len(next)
         if(s <= 128):
             while i<len(splitArray):
              teksti = teksti + splitArray[i] + " "
              i+=1
              MESSAGE = teksti
         serverSocket.sendto(MESSAGE.encode("ASCII"),Clientaddress)
    def KOHA():
        MESSAGE=time.ctime(time.time())
        serverSocket.sendto(MESSAGE.encode("ASCII"),Clientaddress)

    def HOST():
        emri=''
        if gethostname()==None :
            MESSAGE='\Emri i klientit nuk dihet !\n'
        else:
            MESSAGE='Emri i klientit eshte:'+gethostname()
        serverSocket.sendto(MESSAGE.encode("ASCII"),Clientaddress)

    def LOJA():
        m=[]
        for i in range (20):
            m.append(random.randint(1,100))
    
        MESSAGE=str(m)
        serverSocket.sendto(MESSAGE.encode("ASCII"),Clientaddress)

    def FIBONACCI(n):
         first,second =0,1
         for i in range (0,n):
             first,second=second,first+second
         MESSAGE=str(first)
         serverSocket.sendto(MESSAGE.encode("ASCII"),Clientaddress)

    def KONVERTO(s):
        
        c=s[1]
        a=float(s[2])
        temperatura=0
        if c=="C-to-K":                  
            temperatura= float (float(a)+273)
            
        elif c=="C-to-F":
            temperatura= 1.8 * float(float(a)+32)
            
        elif c=="K-to-F":
            temperatura=1.8 * float((float(a)-273)+32)
            
        elif c=="K-to-C":
            temperatura=float(float(a)-273)
            
        elif c=="F-to-C":
            temperatura=5/9*float(float(a)-32)
            
        elif c=="F-to-K":
            temperatura=5/9*float((float(a)-32)+273)
            
        elif c=="pound-to-kg":
            temperatura=float(float(a)/2.20462262)
            
        elif c=="kg-to-pound":
            temperatura=float(float(a)*2.20462262)
            
        MESSAGE=str(round(temperatura,2))
        serverSocket.sendto(MESSAGE.encode("ASCII"), Clientaddress)
        

    def INCH(b):
        x=b[1]
        numri1=float(b[2])
        numri=0
        a=2.54
        if x=="INCH-TO-CM":
            numri=float(float(numri1)*2.54)
        

        elif x=="CM-TO-INCH":
            numri=float(float(numri1)/a)
       
        MESSAGE=str(round(numri,2))
        serverSocket.sendto(MESSAGE.encode("ASCII"), Clientaddress)

    def BMI(a):
        gjatesia=float(a[1])
        pesha=float(a[2])
        bmi1=float(pesha/(gjatesia*gjatesia))
        if bmi1<=18.5:
            bmi1=str(bmi1)
            c='Pesha juaj ne BMI , ju keni peshe me te vogel se pesha normale:'+bmi1

        if bmi1>=18.5 and bmi1<25:
            bmi1=str(bmi1)
            c='Pesha juaj ne BMI , ju keni peshe normale:'+bmi1
        elif bmi1 >25 and bmi1 <30:
            bmi1=str(bmi1)
            c='Pesha juaj ne BMI, ju keni peshe me te larte se pesha normale:'+bmi1
        else:
            c='Keni peshe shume te ulet ose shume te larte!!!'
     
        MESSAGE=str(c)
        serverSocket.sendto(str.encode(str(MESSAGE)),Clientaddress)

    if next.decode("ASCII")=="1":
        IP()

    elif next.decode("ASCII")=="2":
        PORT()

    elif re.match('3 .*', next.decode("ASCII"),):
        value=str(next)
        ZANORE(value)

    elif re.match('4 .*',next.decode(),):
            _string = str(next)
            value = _string.split(" ")
            PRINTO(value)

    elif next.decode("ASCII")=="5":
        HOST()

   
    elif next.decode("ASCII")=="6":
        KOHA()

    elif next.decode("ASCII")=="7":
        LOJA()

    elif re.match('8 .*', next.decode("ASCII"),):
        request = next.decode("ASCII").split(" ")
        if request[1].isdigit():
            FIBONACCI(int(request[1]))


    elif re.match('9 .*[A-Za-z] .*[0-9.]',next.decode("ASCII"),):
        s = next.decode("ASCII").split(" ")
        KONVERTO(s)

    elif re.match('10 .*[A-Za-z] .*[0-9.]',next.decode("ASCII"),):
        b = next.decode("ASCII").split(" ")
        INCH(b)
 
   
    elif re.match('11 .*[0-9.] .*[0-9.]',next.decode("ASCII"),):
        a = next.decode("ASCII").split(" ")
        BMI(a)

    

 
while True:
    next, Clientaddress=serverSocket.recvfrom(128)
    print("Kerkesa:"+next.decode("ASCII"))
    _thread.start_new_thread(clientThread,(serverSocket,Clientaddress,next))

    


