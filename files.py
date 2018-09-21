
with open('referat.txt', 'r', encoding='utf-8') as f:
# reading a file
    referat = f.read()
    length1 = len(referat)
    print(('The text length is   {0}').format(length1),'  symbols')



with open('referat2.txt', 'w', encoding='utf-8') as fife:
    	fife.write(referat.replace('.','!'))



def many_words():
    mylist = (referat.replace('\n', ' ')).split()

    words = 0
    for word in mylist:
        words+=1
    return words
print ( many_words(),' words in my text  ')