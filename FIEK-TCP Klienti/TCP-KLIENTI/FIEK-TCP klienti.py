import socket
serverName='localhost'
serverPort=11000
print ('----------------------------------------------------------------------------------------------------------------------')
print ('                                                UNIVERSITETI I PRISHTINES                                                ')
print ('                                      Fakulteti i Inxhinieris Elektrike dhe Kompjuterike                                 ')
print ('                                                Departamenti i Kompjuterikes                                             ')
print ('                                                 Lenda:Rrjeta Kompjuterike                                               ')
print ('----------------------------------------------------------------------------------------------------------------------')
print ('\n\n\n\n\n                                             Projekti 1: DIZAJNIMI KLIENT-SERVER                                 ')
print('\n\n\n\n\nProfesori i lendes:Prof.Asoc.Dr Blerim Rexha                                 Asistenti i lendes:Prof.Asoc.Dr Haxhi Lajqi')
print('\n\n\n\n\n                                                    Studentja:Vesa Ademi                                          ')

print("Serveri u startua ne "+ str(serverName) +" ne portin :"+str(serverPort))
var5=input('\n\n\nEmri i serverit:')
var6=input('Port number:')



while 1:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverName,serverPort))
    


    print('\n\n\n\n')
    print('                                                   Zgjidhni Operacionin:                                       ')
    print('                                                 1.IP ADDRESSA E KLIENTIT                                      ')
    print('                                                 2.PORTI NUMBER I KLIENTIT                                     ')
    print('                                                 3.ZANORE                                                      ')
    print('                                                 4.PRINTO                                                      ')
    print('                                                 5.EMRI I KLIENTIT                                             ')
    print('                                                 6.KOHA                                                        ')
    print('                                                 7.LOJA                                                         ')
    print('                                                 8.FIBONACCI                                                    ')
    print('                                                 9.KONVERTO                                                     ')
    print('                                                 10.INCHCM   11.BMIWEIGHT                                      ')
    print('\n')
    a=input("Shtypni numrin per cilin operacion doni te zgjidhni : ")
                                         
    s.sendall(str.encode(a))

    
    if  a=='1' and a is not None :
        data=s.recv(128)
        print('Ip Adresa e Klientit:' , data.decode())

        print("\n")
        var=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var=='PO':
            break



    elif a=="2" and a is not None:
        data=s.recv(128)
        print('Porti i Klientit:',data.decode())

        print("\n")
        var=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var=='PO':
            break

    elif a=="3" and a is not None:
        var=input("Shkruaj nje tekst :")
        s.sendall(str.encode(var))
        data=s.recv(128)

        print('Numrim i zanoreve ne fjali:',data.decode())
        print("\n")
        var1=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var1=='PO':
            break

    elif a=="4" and a is not None:
        var=input("Shkruaj fjalin:")
        s.sendall(str.encode(var))
        data=s.recv(128)

        print('Rezultati nga serveri:',data.decode())
        print("\n")
        var1=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var1=='PO':
            break

    elif a=="5" and a is not None:
        data=s.recv(128)
        print(data.decode())
        print("\n")
        var=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var=='PO':
            break
    elif a=="6" and a is not None:
        tm=s.recv(128)
        print(tm.decode('ascii'))
        print("\n")
        var=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var=='PO':
            break

    elif a=="7" and a is not None:
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        var=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var=='PO':
            break

    elif a=="8" and a is not None:
        var=input("Jep nje numer:")
        s.sendall(str.encode(var))
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        var1=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var1=='PO':
            break

    elif a=="9" and a is not None:
        var=input("Jepni numrin :")
        var=str(var)
        s.sendall(str.encode(var))
        var1=input('Zgjidhni njeren nga konvertimet: C-to-K , C-to-F , K-to-F , K-to-C , F-to-C , F-to-K , pound-to-kg , kg-to-pound: ')
        s.sendall(str.encode(var1))
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        var2=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var2=='PO':
            break

    elif a=="10" and a is not None:
        var=input("Jepni numrin:")
        var=str(var)
        s.sendall(str.encode(var))
        var1=input("Zgjedhni njeren nga opcionet INCH-TO-CM ose CM-TO-INCH:")
        s.sendall(str.encode(var1))
        data=s.recv(128)
        print('Rezultati i kthyer nga serveri:',data.decode())
        print("\n")
        var2=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var2=='PO':
            break

    elif a=="11" and a is not None:
        var=input("Pesha juaj eshte:")
        var=str(var)
        s.sendall(str.encode(var))
        var1=input("Gjatesia juaj ne meter eshte:")
        var1=str(var1)
        s.sendall(str.encode(var1))
        data=s.recv(128)
        print('Rezultati:',data.decode())
        print("\n")
        var2=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var2=='PO':
            break
        
    else:
        print("Kerkesa nuk mund te pranohet nga serveri!!!")
        print("\n")
        var=input("                                                               Deshironi te perfundoni, shtypni PO :")
        if var=='PO':
            break

    s.close()
