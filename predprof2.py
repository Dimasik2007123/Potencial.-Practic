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

def quicksort(spaceships):
    '''
    Быстрая сортировка массива данных
    :param: массив, массив данных о кораблях
    :return: массив, массив данных о кораблях, отсортированный
    '''
    L=0
    R=len(spaceships)
