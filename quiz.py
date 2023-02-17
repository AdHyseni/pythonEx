


def pyetsori(
             pyetja_1,
             alternativat_1,
             pergjigja_1,
             pyetja_2,
             alternativat_2,
             pergjigja_2,
             pyetja_3,
             alternativat_3,
             pergjigja_3,
             pyetja_4,
             alternativat_4,
             pergjigja_4,
             pyetja_5,
             alternativat_5,
             pergjigja_5,
             piket
             ):
    print(pyetja_1)
    print(alternativat_1)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit == pergjigja_1:
        piket +=1
    else: 
        piket = piket
    print(pyetja_2)
    print(alternativat_2)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit == pergjigja_2:
        piket +=1
    else: 
        piket = piket
    print(pyetja_3)
    print(alternativat_3)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit == pergjigja_3:
        piket +=1
    else: 
        piket = piket
    print(pyetja_4)
    print(alternativat_4)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit == pergjigja_4:
        piket +=1
    else: 
        piket = piket
    print(pyetja_5)
    print(alternativat_5)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit == pergjigja_5:
        piket +=1
    else: 
        piket = piket
    print(f'Piket e juaja jane:  {piket}')


def quiz():
    kategoria = input("Zgjidhni kategorin gjeografi, sport, showbiz, programim: ")
    piket = 0
    match kategoria:
        case 'gjeografi':
            print('Cili eshte shteti me sip me te madhe?')
            print('USA\nRusia\nAustralia\nItalia\n')
            pergjigja_e_userit = input('Shkruaj pergjigjen: ')
            if pergjigja_e_userit == 'Rusia':
                piket +=1
            else: 
                piket = piket
            print('Cili eshte shteti me popullsine me te madhe?')
            print('Kina\nIndia\nAustralia\nSHBA\n')
            pergjigja_e_userit = input('Shkruaj pergjigjen: ')
            if pergjigja_e_userit == 'Kina':
                piket +=1
            else: 
                piket = piket
            print('A eshte Australia nje kontinent me vete?')
            print('Po\nJo\n')
            pergjigja_e_userit = input('Shkruaj pergjigjen: ')
            if pergjigja_e_userit == 'Po':
                piket +=1
            else: 
                piket = piket
            print('A ndodhet Shqiperia ne kontinentin e Amerikes se Veriut')
            print('Po\nJo\n')
            pergjigja_e_userit = input('Shkruaj pergjigjen: ')
            if pergjigja_e_userit == 'Jo':
                piket +=1
            else: 
                piket = piket
            print('SHBA dhe Rusi kane te njenten siperfaqe')
            print('E vertet\nGabim\nNodshta\nSe di\n')
            pergjigja_e_userit = input('Shkruaj pergjigjen: ')
            if pergjigja_e_userit == 'Gabim':
                piket +=1
            else: 
                piket = piket
            print(f'Piket e juaja jane:  {piket}')
        case 'sport':
            pyetsori(
                'A je tifoz i Gjermanis?',
                'Po\nJo\n',
                'Jo',
                'Sa chempion league ka Real Madrid',
                '3\n14\n7\n1\n',
                '14',
                'A luan Napoli ne La Liga ',
                'Po\nJo\n',
                'Jo',
                'A luan Ibrahimovic tek Interi?',
                'Po\nJo\n',
                'Jo',
                'Ku luan Messi?',
                'PSG\nBarcelona\nMaiami\nInter\n',
                'PSG',
                0
            )
        case _:
            print('Faleminderit qe luajtet me ne')


user = True
while user == True:
    user_input = input('Shtypni S per te nisur lojen ose E per te dalur nga ajo')
    if user_input == 'S':
        quiz()
        
    else:
        print('Faleminderit!')  
        break

