f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()



f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()


f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()