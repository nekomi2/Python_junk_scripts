import os
import sys
'''renames files, files in format number_pnumber'''
idx = 0
src = os.getcwd()
def rename(s):
    if(s[-6:-4] == 'p0'):
       global idx
       idx = idx + 1

    return str(idx) + s[s.find('_'):]


print('renaming')
script_name = sys.argv[0]
filenames = os.listdir()
filenames.remove(script_name)
filenames.sort()


new_names = list(map(rename,filenames))
for i in range(len(filenames)):
    os.rename(filenames[i],new_names[i])
