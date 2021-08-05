file = open('pythonlog.txt', 'w+')
file.write('This is something')
file.seek(0,0)

print(file.read())
file.close()