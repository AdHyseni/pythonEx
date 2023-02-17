# sintaksa e string

string = "string 1"
string_2 = 'string 2'

# Koncepti i string 

h = "h"
e = 'e'
l = 'l'
l_1 = 'l'
o = 'o'

hello = h+e+l+l_1+o
print('Afishohet: ',hello)
# Format Print
print(f'ky eshte var_1 {string}, ky eshte var_2 {string_2}')

# Leximi i cdo karakteri ne string

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
print(text)

for karakter in text:
    print(karakter)

counter = 0
for i in text:
    if i == 'a' or i=='A':
        counter +=1

print(f'Jane {counter} -- a')

n = 0
counter = 0
while (n < len(text)):
    if text[n] == 'i' or text[n]=='I':
        counter += 1
    n += 1
print(f'Jane {counter} -- i')

# Sa zanore dhe sa bashktingellore ka text
no_z = 0
no_b = 0

for i in text:
    zanore = 'iaeouy'
    for j in zanore:  
        if i.lower() == j:
            no_z +=1
        elif i == ' ':
            continue
        elif i == ',':
            continue
        else:
            no_b +=1
print(f'Ne tekstin tone jane {no_z} zanore dhe {no_b} bashktingellore')

no_z = 0
no_b = 0
for i in text:
    zanore = 'iaeouy'
    simbole = " ,@-_/'"
    if i in zanore:  
        no_z +=1
    elif i in simbole:
        continue
    else:
        no_b +=1
print(f'Ne tekstin tone jane {no_z} zanore dhe {no_b} bashktingellore')

# Funksione te string

string.lower()
string.upper()