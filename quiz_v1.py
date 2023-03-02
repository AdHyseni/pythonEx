import random as r
score = 0
quiz = {
    'Sa kontinente ka toka ?':7,
    'Cili eshte shteti me popullsine me te madhe ?':'Kina',
    'Cili eshte qyteti europian me popullsine me te madhe ?':'Stambolli',
    'A eshte Rusia nje kontinent me vete?':'Jo',
    'A ndodhe Shqiperia ne kontinentin e Amerikes se veriut?':'Jo',
}

alternativat = ['Roma', 'Italia', 'Paris','4','3','2','1','Berlin','France','Tirana']

## Kontrollo tipin
def tipi(value):
    try:
        # Kontrollo nese tipi i knovertuar eshte int
        if type(int(value)) == type(0):
            return True
    except Exception as e:
        pass
    else:
        return False
def print_alternativat(list_alt):
    perv = 0
    for i in range(0,3):
        rand_int = r.randint(0,len(list_alt))
        if perv == rand_int:
            continue
        else:
            perv = rand_int
            print(list_alt[rand_int-1])
def scores(v):
    user_input = input('Pergjigja juaj: ')
    global score
    if user_input.lower() == str(v).lower():
        score += 1
    else:
        score = score
def quiz_game(dictionary,alternativat):
    alt = list()
    for k,v in dictionary.items():
        print("Pyetja : ",k)
        if tipi(v):
            for i in alternativat:
                if tipi(i):
                    alt.append(i)
            print_alternativat(alt)
            print(v)
            scores(v)
        elif v.lower() == 'jo' or  v.lower() == 'po':
            if v.lower() == 'jo':
                print('Po')
            elif v.lower() == 'po':
                print('Jo')
            print(v)
            scores(v)

        else:
            for i in alternativat:
                try:
                    if type(int(i)) == type(0):
                        continue
                except Exception as e:
                    alt.append(i) 
            print_alternativat(alt)
            print(v)
            scores(v)
        alt.clear()  
    print(score)          
quiz_game(quiz,alternativat)




# for key, value in quiz.items():
#     print('Pyetja: ',key)
#     if type(value) == type(0):
#         # krijo nje list me alternativat
#         alt = []
#         for i in alternativat:
#             try:
#                 if type(int(i))== type(0):
#                     alt.append(i)
#             except Exception as e:
#                 continue
#         perv = 0
#         for i in range(0,3):
#             rand_int = r.randint(0,len(alt))
#             if perv == rand_int:
                
#                 continue
#             else:
#                 perv = rand_int
#                 print(alt[rand_int-1])
#         print(value)
#     elif value.lower() == 'jo' or  value.lower() == 'po':
#         if value.lower() == 'jo':
#             print('Po')
#         elif value.lower() == 'po':
#             print('Jo')
#         print(value)    
#     elif type(value) is not type(0):
#         # krijo nje list me alternativat
#         alt = []
#         for i in alternativat:
#             try:
#                 if type(int(i)) == type(0):
#                     continue
#             except Exception as e:
#                 alt.append(i)          
#         perv = 0
#         for i in range(0,3):
#             rand_int = r.randint(0,len(alt))
#             if perv == rand_int:
#                 continue
#             else:
#                 perv = rand_int
#                 print(alt[rand_int-1])
#         print(value)
    