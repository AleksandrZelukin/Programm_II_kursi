
import fileinput
with fileinput.FileInput(files=('prieksmeti.txt', 'nomnieki.txt', 'noma.txt'), mode='r') as datne:

    for idx, line in enumerate(datne):
        if datne.isfirstline() == True:
            
            print(f'Lasa datni {datne.filename()}...')

            print(idx, line)             
                        