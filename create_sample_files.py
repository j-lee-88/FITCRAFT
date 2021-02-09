import os

#count = 0
with open('pos.txt','w') as files:
    for filename in os.listdir('pos'):
        files.write('pos/' + filename + ' ' + str(1) + ' ' + str(0) + ' ' + str(0) + ' ' + str(28) + ' ' + str(28) + '\n')