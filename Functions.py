def swapFileData():
    file1 = input('enter file 1 : ')
    file2 = input('enter file 2 : ')
    with open(file1) as a:
        dataA=a.read()
    with open(file2) as a:
        dataB=a.read()
    with open(file1,'w') as a:
        dataA=a.write(dataB)
    with open(file2,'w') as a:
        dataB=a.write(dataA)

swapFileData()