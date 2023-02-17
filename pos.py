produktet = ['iphone 12','iphone 13','iphone 12 pro','google pixel', 'samsung s23']
cart = []
cart_price =[]

print('Pershendetje ky eshte dyqani yne virtual\n'
          +'Per te blere ju lutem shtypni b\n'
          +'Per te pare listen e produkteve shtypni a\n'
          +'Per te pare listen e produkteve te blera shtypni c'
          +'Per te printuar faturen shkruani p'
          +'Per te anulluar blerjen dhe per te dalur nga sistemi shtypni e\n')

while(True):
    user_input = input('Shtypni nje nder alternativat me siper: ')
    match user_input.lower():
        case 'a':
            for produkt in produktet:
                print(produkt)
        case 'b':
            while(True):
                produkti = input('Te lutem shkruaj emrin e produktit: ')
                if produkti in produktet:
                    if produkti.lower() == 'iphone 12':
                        cart.append(produkti)
                        sasia = int(input('Ju lutem vendosni sasine qe doni te blini: '))
                        cart_price.append(900*sasia)
                    
                    if produkti.lower() == 'iphone 13':
                        cart.append(produkti)
                        sasia = int(input('Ju lutem vendosni sasine qe doni te blini: '))
                        cart_price.append(100*sasia)
                    
                    if produkti.lower() == 'iphone 12 pro':
                        cart.append(produkti)
                        sasia = int(input('Ju lutem vendosni sasine qe doni te blini: '))
                        cart_price.append(980*sasia)
                    
                    if produkti.lower() == 'google pixel':
                        cart.append(produkti)
                        sasia = int(input('Ju lutem vendosni sasine qe doni te blini: '))
                        cart_price.append(600)
                    
                    if produkti.lower() == 'samsung s23':
                        cart.append(produkti)
                        sasia = int(input('Ju lutem vendosni sasine qe doni te blini: '))
                        cart_price.append(1200*sasia)
                else:
                    print('Produkti nuk nodhet ne dyqan')

                user_input = input('Shtypni y nese doni te blini perseri: ')
                if user_input.lower() =='y':
                    continue
                else:
                    break
        
        case 'c':
            if len(cart) != 0:
                print('Produktet qe keni blere jane')
                for produkte in cart:
                    print(produkte)
            else:
                print('Shporta juaj eshte bosh')
        case 'p':
                if len(cart) != 0:
                    no =1
                    sum=0
                    print('Fatura juaj eshte: ')
                    for produkte in cart:
                        print(f"---{no}. {produkte}--")
                        no = no + 1
                    for price in cart_price:
                        sum += price
                    print(f'------Totali------{sum}ALL----')
                else:
                    print('Shporta juaj eshte bosh')
        case 'e':
            print('Faleminderit qe blete ne dyqanin tone!')



    
                    