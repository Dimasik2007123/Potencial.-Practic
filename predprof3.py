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

def finding(name):
    '''
    Ищет корабль по его имени
    :param name: str, ship's name
    :return: str, info about ship
    '''
    print(name)
    for i in range(1,101):
        print(spaceships[i][0])
        if spaceships[i][0]==name:
            return 'Корабль '+spaceships[i][0]+' был отправлен с планеты: '+spaceships[i][1]+' и его направление движения было на '+spaceships[i][3]
    else:
        return 'error.. er.. ror.. '
spaceships=readfile('space.txt')


name=input()
while name!='stop':
    print(finding(name))
    name=input()
