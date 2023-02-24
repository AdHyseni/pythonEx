a = True
while a:
    user_input = input('Shkruaj x per te krijuar nje file te ri\nShkruaj a per te modifikuar nje file')
    match user_input.lower():
        case 'x':
            try:
                user_input = input('Vendos emrin e file: ')
                with open(f'{user_input}.txt','x') as f:
                    linjat = input('Shkruaj tekstin: ')
                    f.writelines(linjat)
            except Exception as e:
                print(e)
        case 'a':
                user_input = input('Vendos emrin e file: ')
                with open(f'{user_input}.txt','a') as f:
                    linjat = input('Shkruaj tekstin: ')
                    f.writelines(f'\n{linjat}')
        
    user_input = input('Vendos doni te krijoni nje file te ri?\n Shkruaj po per te vazhduar:  ')
    if user_input.lower() == 'po':
        a = a
    else:
        a = False


