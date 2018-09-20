

with open('referat.txt', 'r', encoding='utf-8') as f:
    for line in f:
        #line = line.upper()
        line=line.replace('.','!')
        print(line)
    t=len(str(f))
    print(t)
    	# попробую t=+len(str(line))

with open('referat2.txt', 'w', encoding='utf-8') as fife:
    	fife.write(line)