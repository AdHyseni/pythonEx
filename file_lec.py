"""
open prannon disa parametra pervec emris se dokumentit nje nder to eshte dhe 'r' i cile eshte perdorur ne linjen 21
kto karaktere tregojn se cfar do te behet me file ne momentin qe hapet, ku:
    'r' = read, pra vetem lexon dokumentin,nese dokumenti nuk ekziston shfaqet error
    'a' = append, modifikon dokumentin me te dhena te reja,nese nuk ekziston ateher krijon nje file me kete emer
    'w' = write, shkruaj nje dokument, ,nese nuk ekziston ateher krijon nje file me kete emer
    'x' = creat, krijo dokunent, nese dokumenti ekziston ateher kthen nje error 
    't' = specifikon tekst
    'b' = specifikon binary
    '+' = read dhe write, lexo dhe shkruaj 
    gjithashtu parameter te tjere jane dhe encoding si utf-8 nje nder me te perdorurat

sintaksa e file duhet te jete 
open(file name , mode) 
operimet qe duam te bejme
filename.close()
komandat open dhe close duhet te perdoren ne menyre qe te hapim dhe te mbyllim file

"""

f = open('./file/text.txt','r')
print(f)


#lexojm sa linja ka file yne
count = 0
for line in f:
    count = count + 1
print('Line Count:', count)
f.close() # gjithmon duhet te mbyllim file



"""
Per te anashkaluar komanden close rekomandohet te perdoret 
komanda with e cila siguron qe ne fund te operimeve te mbyll file 
"""

with open('./file/text.txt', 'r') as f:
     lorem = []
     for ln in f:
        if ln.startswith('Lorem'):
            lorem.append(ln)
print(lorem)


#Hap nje file duke shkruar emrin e file
emri = input('Shkruaj emrin e file: ')

with open(f'./file/{emri}','r') as file1:
    for i in file1:
        print(i)



#try dhe except
try:
    input_name = input('Vendos emrin e file: ')
    fhand = open(f'./file/{input_name}.txt')
except:
    print('Nuk ekziston nje file me kete emer')
finally:
    fhand.close()





try:
    emri_i_doc = input("Vendos emrin e dokumentit: ")
    doc_ri = open(f'./{emri_i_doc}', 'w')
    doc_ri.writelines('Ky eshte nje dokument i shkruar nga python')
finally:
    doc_ri.close()






#shkruaj nje file duke perdorur listat 
lista = ['ky ', 'eshte ', 'nje ', 'file ',' me ', 'kontent','nga ', 'nje ', 'list']
try:
    written_file_list = open('./list_file.txt', 'w')
    for i in lista:
        written_file_list.writelines(i)
finally:
    written_file_list.close()




"""
close()	Closes an opened file. It has no effect if the file is already closed.
detach()	Separates the underlying binary buffer from the TextIOBase and returns it.
fileno()	Returns an integer number (file descriptor) of the file.
flush()	Flushes the write buffer of the file stream.
isatty()	Returns True if the file stream is interactive.
read(n)	Reads at most n characters from the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Reads and returns one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Changes the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()	Returns an integer that represents the current position of the file's object.
truncate(size=None)	Resizes the file stream to size bytes. If size is not specified, resizes to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Writes the string s to the file and returns the number of characters written.
writelines(lines)	Writes a list of lines to the file.

"""