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

def has():
    '''
    Функция, которая создаёт массив данных со значениями кода и номера кораблей по ключу названия планеты
    :return: array, array of hashed data
    '''
    a=[]
    for i in range(1,101):
        a.append([spaceships[i][1],spaceships[i][0]])
            #print('{',spaceships[i][1],'}',':','{', spaceships[i][0],'}', sep='')

    return a

def search_planet(planet):
    '''
    Функция вывода данных о корабле по его планете
    :param planet: str, planet's name
    '''
    a=has()
    for i in range(len(a)):
        if a[i][0]==planet:
            print('{' + a[i][0] + '}:' + '{' + a[i][1] + '}')


spaceships=readfile('space.txt')
has()
a=has()
for i in range(10):
    print('{' + a[i][0] + '}:' + '{' + a[i][1] + '}')

