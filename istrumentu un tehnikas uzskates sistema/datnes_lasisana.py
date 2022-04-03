'''
import fileinput
with fileinput.FileInput(files=('prieksmeti.txt', 'nomnieki.txt', 'noma.txt'), mode='r') as datne:

    for idx, line in enumerate(datne):
        if datne.isfirstline() == True:
            
            print(f'Lasa datni {datne.filename()}...')

            print(idx, line)

'''

file1 = open('prieksmeti.txt')
print(file1.read())

file1 = open('prieksmeti.txt','w')

file1.write('perforators\n')
file1.write('slipmasina\n')
file1.write('urbjmasinan\n')

file1 = open('prieksmeti.txt')
print(file1.read())

file1.close()
                        
file2 = open('nomnieki.txt')
print(file2.read())

file2 = open('nomnieki.txt','w')

file2.write('Anna\n')
file2.write('Valdis\n')
file2.write('Olgerts\n')

file2 = open('nomnieki.txt')
print(file2.read())

file2.close()
                  
