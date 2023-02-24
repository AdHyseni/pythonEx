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

produktet = {
    'iphone': 1200,
    'samsung':800, 
    'pixel':700, 
    'xiaomi':400, 
    'oppo':300,
    'vivo':200, 
    'oneplus':900,
    'sony':1500
}
shporta = []
cmimet = []

def afisho(produktet):
    for element in produktet.key():
        print(element)

def bli(produkti):
    if produkti.lower() in produktet.keys():
        shporta.append(produkti)
        sasia =int(input('Vendos sasine: '))
        cmimet.append(produktet[produkti]*sasia)
    else:
        print('Produkti nuk ekziston')

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
        
        
    

