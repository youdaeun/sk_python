helloFile = open('example.txt', 'w', encoding='utf-8')
helloFile.write('Line 1: Welcome to Python file handling.\n')
helloFile.write('Line 2: This is the second line.\n')
helloFile.write('Line 3: Here is the third line.\n')
helloFile.write('Line 4: The file ends here.\n')
helloFile.close()

helloFile = open('example.txt','r',encoding='utf-8')
lines = helloFile.readlines()
for line in lines:
    print(lines)    
helloFile.close()

