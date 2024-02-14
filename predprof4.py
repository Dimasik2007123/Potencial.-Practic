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

def password(spaceship):
    '''
    Making password
    :param name: str, ship information
    :return: str, password
    '''
    pa=''
    f3=spaceship[1][:3]
    big='ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
    small='йцукенгшщзхъфывапролджэячсмитьбюё'
    f3=f3[::-1]
    f3b=''
    f1=spaceship[1][len(spaceship[1])-3:]
    f1b=''
    for i in range(len(f3)):
        if f1[i] not in small:
            f1b+=f1[i]
        else: f1b+=big[small.find(f1[i])]
        if f3[i] not in small:
            f3b+=f3[i]
        else: f3b+=big[small.find(f3[i])]

    pa+=f1b
    pa+=spaceship[0][2]+spaceship[0][1]
    pa+=f3b
    return pa

def writefile(namefile):
    '''
    Write correct data to new file
    :param namefile: str, name of new file
    '''
    f=open(namefile, 'w', encoding='utf-8')
    f.write('*'.join(spaceships[0])+'*'+'password'+'\n')
    for i in range(1,101):
        s='*'.join(spaceships[i])
        f.write(s+'*'+password(spaceships[i])+'\n')
    f.close()

spaceships=readfile('space.txt')
writefile('space_uniq_password.csv')
