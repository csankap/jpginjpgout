lista = []
with open('example.jpg', 'rb') as f:  #bájtok beolvasása a képből
    byte = f.read(1)
    lista.append(byte)
    while byte:
        byte = f.read(1)
        lista.append(byte)




szamsor = [ord(i) for i in lista[:-1]]  #integerré alakítás

hexsor = [hex(i).replace('0x',' ') for i in szamsor] #hexadecimálisba konvertálás
with open('new.valami','w', encoding = 'utf-8') as f:      #hexadecimális karakterek beírása az új fileba
    for i in hexsor:
        f.write(i)



with open('new.valami','r',encoding='utf-8') as f:                             # hexadecimális karakterek beolvasása byte stringgé alakítás
    hexek = f.read()                                                        #
                                                                            #    
hexlista = hexek.split()                                                    #
bytelista = [(int('0x'+i,0)).to_bytes(1,'big') for i in hexlista]           #

with open('exampleee.jpg', 'wb') as sz: # eredeti file visszaállítva :)
    for i in bytelista:
        sz.write(i)



