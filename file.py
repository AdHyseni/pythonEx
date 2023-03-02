# # metoda 1 per hapur nje file

file_1 = open('test.txt','r')
print(file_1)
file_1.close()

# try:
#     file_1 = open('test2.txt','x')
#     file_1.close()
# except Exception as e:
#     print(e)

#metoda 2 
with open('test.txt','r') as f:
    for i in f:
        print(i)

# try:
#     emri_file = input('Vendos emrin e file: ')
#     with open(emri_file,'r') as f:
#         for i in f:
#             print(i)
# except Exception as e:
#     print(e)


# try:
#     f = open('test3.txt','a')
#     while True:
#         user_input = input('Shkruaj brenda ne file: ')
#         f.writelines(user_input)
#         check = input('Shkruaj y per te rishkruar ne file: ')
#         if check.lower() == 'y':
#             f.writelines('\n')
#             continue
#         else:
#             break        
# except Exception as e:
#     print(e)
# finally:
#     f.close()



"""

Krijo nje file tekst me permbajtje nga lorem ipsum.
Krijo nje program i cili te numeroj sa linja fillojn me lorem
Krijo nje program i cili:
--- Krijon nje file tekst te ri
--- Shkruaj mbi kete file
--- Apend file
--- bonus... 
----- Programi te krijoj disa file jo vetem nje te vetem

"""
count = 0
try:
    f = open('lorem.txt','r')
    for line in f:
        print(line)
        if line.startswith('Lorem') or line.startswith('lorem'):
            count = count +1
except Exception as e:
    print(e)
finally:
    f.close()

print(count)