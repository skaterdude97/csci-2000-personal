def has_no_e(string):
    return 'e' in string

reader = open('gadsby_stripped.txt', 'r')
line = reader.readline()
while line != '' :
    print (line)
    print (has_no_e(line))
    line = reader.readline()
reader.close()
