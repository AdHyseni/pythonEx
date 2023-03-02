# Sintaksa e fjalorit
fjalori = {}
fjalori = dict()


fjalori['shqip'] = ['Ckemi', 'Si je ','Pershendetje']
fjalori['anglisht'] = ['Hey', 'Hi','Hello']

print(fjalori)

# celsat e fjalorit

key = fjalori.keys()

key = [k for k,v in fjalori.items()]

# values

value = fjalori.values()

value = [v for k,v in fjalori.items()]

# Afishimi
for key, value in fjalori.items():
    print(f'Celsat {key} dhe vlerat {value}')

# Shtimi i nje vlere te re 
# Emri_i_fjalorit['Vlera_e_celsit'] = vlera_per_celsin
fjalori['italisht'] = ['']

