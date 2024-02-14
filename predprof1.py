def readfile(namefile):
    '''
    Читает данные из файла в список
    :param namefile: str, file's name
    :return: array, array of spaceships
    '''
    spaceships=[]
    f=open(namefile, encoding='utf-8')
    for i in range(101):
        a=f.readline().strip().split('*')
        spaceships.append([a[0], a[1], a[2], a[3]])
    return spaceships

def repl(spaceships):
    '''
    Записывает новые данные в новый файл
    :param spaceships: массив, массив данных о космических кораблях
    :return: массив, массив данных о космических кораблях
    '''
    for i in range(1,101):
        a=spaceships[i][2].split()
        x=int(a[0])
        y=int(a[1])
        vect=spaceships[i][3].split()
        xd=int(vect[0])
        yd=int(vect[1])
        t=len(spaceships[1])
        n=int(spaceships[i][0][5])
        m=int(spaceships[i][0][6])
        if x==0 or y==0:
            if x==0:
                if n>5:
                    x=n+xd
                if n<=5:
                    x=-(n+xd)*4+t
            if y==0:
                if m>3:
                    y=m+t+yd
                if m<=3: y=-(n+yd)*m
            spaceships[i][2]=str(x)+' '+str(y)
    return spaceships

def writefile(namefile):
    '''
    Write correct data to new file
    :param namefile: str, name of new file
    '''
    f=open(namefile, 'w', encoding='utf-8')
    for i in range(101):
        s='*'.join(spaceships[i])
        f.write(s+'\n')
spaceships=readfile('space.txt')
repl(spaceships)
writefile('space_new.txt')

for i in range(1,101):
    simv=spaceships[i][0][3]
    if simv=='V':
        print(spaceships[i][0])

