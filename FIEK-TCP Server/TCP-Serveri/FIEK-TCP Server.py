
from socket import*
import _thread
import time
from socket import gethostname;
import random
import datetime
import math


print ('----------------------------------------------------------------------------------------------------------------------')
print ('                                                UNIVERSITETI I PRISHTINES                                             ')
print ('                                      Fakulteti i Inxhinieris Elektrike dhe Kompjuterike                              ')
print ('                                                Departamenti i Kompjuterikes                                          ')
print ('                                                 Lenda:Rrjeta Kompjuterike                                            ')
print ('----------------------------------------------------------------------------------------------------------------------')
print ('\n\n\n\n\n                                             Projekti 1: DIZAJNIMI KLIENT-SERVER                                 ')
print('\n\n\n\n\nProfesori i lendes:Prof.Asoc.Dr Blerim Rexha                                 Asistenti i lendes:Prof.Asoc.Dr Haxhi Lajqi')
print('\n\n\n\n\n                                                    Studentja:Vesa Ademi                                          ')
print('\n\n\n\n')
print('                                                     Operacionet:                                            ')
print('                                                1.IP ADDRESSA E KLIENTIT                                     ')
print('                                                2.PORTI NUMBER I KLIENTIT                                    ')
print('                                                3.ZANORE                                                     ')
print('                                                4.PRINTO                                                     ')
print('                                                5.EMRI I KLIENTIT                                            ')
print('                                                6.KOHA                                                       ')
print('                                                7.LOJA                                                       ')
print('                                                8.FIBONACCI                                                  ')
print('                                                9.KONVERTO                                                   ')

serverPort=11000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))# pasi qe kemi listen() dhe accept() method, degjon per kerkesa qe dergohen qe te lidhen me adresen e vecant(particular address)
serverSocket.listen(5) # eshte ne modin e degjimit

def clientThread(serverSocket,clientAddress,numri):

    def IPKLIENTI():

        print("Ip Adresa e Klientit:",clientAddress[0])
        connectionSocket.send(str(clientAddress[0]).encode("ASCII"))

   


    def PORTIKLIENTIT():
        print("Port Number i Klientit :" ,str(clientAddress[1]))
        connectionSocket.send(str(clientAddress[1]).encode("ASCII"))

    
    def ZANORE(s):

        i=0
        counter=0
        while i<len(s):
            if s[i] in 'aeiouAEIOU':
                counter=counter+1
            i=i+1
        print(counter)
        connectionSocket.send(str.encode(str(counter)))

    def PRINTO():
        data=connectionSocket.recv(128)
        print(data)
        connectionSocket.send(data)


    def EMRIKLIENTIT():
        emri=''
        if gethostname()==None :
            emri='\Emri i klientit nuk dihet !\n'
        else:
            emri='Emri i klientit eshte:'+gethostname()

        print(emri)
        connectionSocket.send(str.encode(emri))

    def KOHA():
        currentTime=time.ctime(time.time())
        print(str(currentTime))
        connectionSocket.send(str.encode(str(currentTime)))
        
    def LOJA():
        m=[]
        for i in range (20):
            m.append(random.randint(1,100))
    
        print(m)
        connectionSocket.send(str.encode(str(m)))
  
    def FIBONACCI(n):
         first,second =0,1
         for i in range (0,n):
             first,second=second,first+second
         print(first)
         connectionSocket.send(str.encode(str(first)))

    def KONVERTO(temperatura,x):
        if x=="C-to-K": 
            temperatura=str(float (float(temperatura)+273.00))
            connectionSocket.send(str.encode(str(temperatura)))

       
        elif x=="C-to-F":
            temperatura= str(1.8 * float(float(temperatura)+32))
            connectionSocket.send(str.encode(str(temperatura)))  
        

        elif x=="K-to-F":
            temperatura=str(1.8 * float(float(temperatura)-273)+32)
            connectionSocket.send(str.encode(str(temperatura)))  
        
       
        elif x=="K-to-C":
            temperatura=str(float(float(temperatura)-273))
            connectionSocket.send(str.encode(str(temperatura)))  
       

        elif x=="F-to-C":
            temperatura=str(5/9*float(float(temperatura))-32)
            connectionSocket.send(str.encode(str(temperatura)))  
       
      
        elif x=="F-to-K":
            temperatura=str(5/9*float(float(temperatura)-32)+273)
            connectionSocket.send(str.encode(str(temperatura)))  
   

        elif x=="pound-to-kg":
            c=str(float(float(temperatura))/2.20462262)
            connectionSocket.send(str.encode(str(c)))  
       
        elif x=="kg-to-pound":
            c=str(float(float(temperatura))*2.20462262)
            print(c)
            connectionSocket.send(str.encode(str(c))) 
   
        else:
            print('Kerkesa juaj nuk mund te pranohet !')
            connectionSocket.send(str.encode('Kerkesa juaj nuk mund te pranohet'))

    def INCH(numrii,x):
        a=2.54
        if x=="INCH-TO-CM":
            numrii=str(float(float(numrii)*2.54))
            print(numrii)
            connectionSocket.send(str.encode(numrii))

        elif x=="CM-TO-INCH":
            numrii=str(float(float(numrii)/a))
            print(numrii)
            connectionSocket.send(str.encode(numrii))


    def BMIWEIGHT(pesha,gjatesia):
        bmi=float(float(pesha)/(float(gjatesia)*float(gjatesia)))
        if bmi <=18.5:
            bmi=str(bmi)
            c='Pesha juaj ne BMI , ju keni peshe me te vogel se pesha normale:'+bmi
            connectionSocket.send(str.encode(str(c)))

        elif bmi >=18.5 and bmi <25:
            bmi=str(bmi)
            c='Pesha juaj ne BMI, ju keni peshe normale:'+bmi
            connectionSocket.send(str.encode(str(c)))

        elif bmi >25 and bmi<30:
            bmi=str(bmi)
            c='Ju keni peshe , me te larte se pesha normale:'+bmi
            connectionSocket.send(str.encode(str(c)))

        else:
            c='Keni peshe shume te ulet ose shume te larte!!!'
            connectionSocket.send(str.encode(str(c)))
        print(str(c))

    if numri=='1':
         IPKLIENTI()

    elif numri=='2':
        PORTIKLIENTIT()

    elif numri=='3':
        data1=connectionSocket.recv(128)
        data1=data1.decode()
        print(data1)
        ZANORE(data1)
    

      
    elif numri=='4':
        PRINTO()

    elif numri=='5':
        EMRIKLIENTIT()

    elif numri=='6':
        KOHA()

    elif numri=='7':
        LOJA()
   
    elif numri=='8':
        data2=connectionSocket.recv(128)
        data2=data2.decode()
        print(data2)
        FIBONACCI(int(data2))
           
    

    elif numri=='9':
        data2=connectionSocket.recv(128)
        data2=data2.decode()
        print(data2)
        data3=connectionSocket.recv(128)
        data3=data3.decode()
        print(data3)
        KONVERTO(data2,data3)
      
    elif numri=='10':
        data2=connectionSocket.recv(128)
        data2=data2.decode()
        print(data2)
        data3=connectionSocket.recv(128)
        data3=data3.decode()
        print(data3)
        INCH(data2,data3)
     
    elif numri=='11':
        data2=connectionSocket.recv(128)
        data2=data2.decode()
        print(data2)
        data3=connectionSocket.recv(128)
        data3=data3.decode()
        print(data3)
        BMIWEIGHT(data2,data3)








while 1:
    connectionSocket,clientAddress=serverSocket.accept();
    numri=connectionSocket.recv(128)
    numri=numri.decode()
    print('Operacioni i zgjedhur nga klienti: '+numri)

    _thread.start_new_thread(clientThread,(serverSocket,clientAddress,numri))


   
connectionSocket.close()