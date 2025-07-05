import os
import shutil

from_dir=input('ENTER the dir of folder to protect: ')
fname=input('Enter folder name to create')
pasw=input('Enter the password')

todir='C:/Users/divya/OneDrive/Desktop'
todir=os.path.join(todir,fname)
os.mkdir(todir)

for i in pasw:
    for j in range(1,21):
        path=os.path.join(todir,str(j))
        try:
            os.mkdir(path)
        except:
            print('Done')
        for k in range(1,21):
            path2=os.path.join(path,str(k))
            try:
                os.mkdir(path2)
            except:
                print('Done2')
            
    todir=todir+'/'+i

try:
    shutil.move(from_dir,todir)
except:
    print()