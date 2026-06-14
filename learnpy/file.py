#open a file
myfile = open('myfile.txt','w')

print('Name', myfile.name)
print('Isclosed',myfile.closed)
print('Opening mode',myfile.mode)

myfile.write('Python is my favorite language to code')
myfile.close()

#Append to file so that one can't overwrite it
myfile = open('myfile.txt','a')
myfile.write('\nI love coding in Python')
myfile.close()

#Reading from a file to display in the terminal
myfile = open('myfile.txt', 'r+')
text = myfile.read()
print(text)
