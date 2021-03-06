import os
import sys
from natsort import os_sorted
idx = 0
src = os.getcwd()
def rename(s):
    if(s[-6:-4] == 'p0'):
       global idx
       idx = idx + 1
    prefix = '' if idx >= 10 else '0'
    return prefix + str(idx) + s[s.find('_'):]


print('renaming')
script_name = sys.argv[0]
filenames = os.listdir()
filenames.remove(script_name)
filenames = os_sorted(filenames) #natural sort
filenames.sort(key=lambda x:int(x[:x.find('_')]),reverse=True) #Guaranteed to be stable
new_names = list(map(rename,filenames))
for i in range(len(filenames)):
    os.rename(filenames[i],new_names[i])
