"""
1-Afisho nje mesazh mikprites # done
2-Afisho listen me komanda    # done
3-Afisho listen me produkte
4-Bli produkte
    - Nje shport me emrat e produkteve te blere
    - Nje liste me cmimet
5-Afisho faturen me emrat e produkteve dhe cmimin total

"""

print('Pershendetje ky eshte dyqani virtual \"AbiTech\" ')

komandat = ['Per te shikuar listen e produkteve shtypni \'a\''
            ,'Per te blere shtypni \'b\''
            ,'Per te pare shporten shtypni \'s\''
            ,'Per te printuar faturen shtypni \'p\''
            ,'Per te printuar komandat shtypni \'h\''
            ]

produktet = ['iphone', 'samsung', 'pixel', 'xiaomi', 'oppo','vivo', 'oneplus','sony']
shporta = []
cmimet = []

def afisho(lista):
    for element in lista:
        print(element)

def bli(produkti):
    if produkti == 'iphone':
        shporta.append(produkti)
        sasia = int(input('Vendos sasine: '))
        cmimet.append(sasia*1000)
    elif produkti == 'samsung':
        shporta.append(produkti)
        sasia = int(input('Vendos sasine: '))
        cmimet.append(sasia*1200)
    elif produkti == 'sony':
        shporta.append(produkti)
        sasia = int(input('Vendos sasine: '))
        cmimet.append(sasia*2000)
    elif produkti == 'pixel':
        shporta.append(produkti)
        sasia = int(input('Vendos sasine: '))
        cmimet.append(sasia*800)
    elif produkti == 'xiaomi':
        shporta.append(produkti)
        sasia = int(input('Vendos sasine: '))
        cmimet.append(sasia*600)
    elif produkti == 'oppo':
        shporta.append(produkti)
        sasia = int(input('Vendos sasine: '))
        cmimet.append(sasia*400)
    elif produkti == 'oneplus':
        shporta.append(produkti)
        sasia = int(input('Vendos sasine: '))
        cmimet.append(sasia*500)
    elif produkti == 'vivo':
        shporta.append(produkti)
        sasia = int(input('Vendos sasine: '))
        cmimet.append(sasia*200)
    else:
        print('Produkti nuk ndodhet ne dyqanin tone')

def fatura(shporta, cmimet):
    print('------- Fatura -------')
    no = 1
    for i in shporta:
        print(f'--- Produkti -- {no}. {i}')
        no = no+1
    totali = sum(cmimet)
    print(f'------ Totali -- {totali} Eu----')



while True:
    afisho(komandat)
    user_input = input('Shkruaj komanden: ')

    match user_input.lower():
        case 'a':
            print('Lista e produkteve eshte: ')
            afisho(produktet)
        case 's':
            print('Lista e produkteve te shpores eshte: ')
            afisho(shporta)
        case 'b':
            produkti = input("Shkruaj emrin e produktit: ")
            bli(produkti.lower())
        case 'p':
            fatura(shporta, cmimet)
        case 'h':
            afisho(komandat)
    user_input = input('Doni te blni produkt tjeter, nese po shkruani y ose cdo shkronje tjeter per te dalur: ')
    if user_input.lower() == 'y':
        continue
    else:
        break 
        
        
    
