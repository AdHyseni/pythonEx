import random as r

opsionet = ['guri','letra','gershera']
pc =''
user=''

while(True): #infinte loop
    print("Opsionet: ",opsionet)
    user_input = input('Zgjidh nje nga opsionet: ')
    user = user_input.lower()
    rand_int = r.randint(0,2)
    pc = opsionet[rand_int]


    if user == pc:
        print("Draw")
    elif user == 'guri' and pc == 'letra':
        print('Lose')
    elif user == 'guri' and pc == 'gershera':
        print('Win')
    elif user == 'letra' and pc == 'guri':
        print('Win')
    elif user == 'letra' and pc == 'gershera':
        print("Lose")
    elif user == 'gershera' and pc == 'guri':
        print("Lose")
    elif user == 'gersher' and pc == 'letra':
        print('Win')
    else:
        print('Please choose one of the options above')
    
    user_input = input('Press r to play again or anything to exit')

    if user_input == 'y':
        continue
    else:
        break

    
    """
    Shkruani nje loje ku te gjeni numri e gjeneruar nga python 0,100
    nese numri juaj eshte 3 njesi me i madh ose me i vogel printoni jeni afer
    nese e gjeni printoni numri e gjeneruar dhe afishoni mesazhin 
    ju keni fituar

    """