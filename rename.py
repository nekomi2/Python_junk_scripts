import os
import sys
'''renames all file. This vs recursive copy? Files have form "number_number.jpg"'''
prefix = '00'
src = os.getcwd()
def rename(s):
    return prefix + s[s.find('_'):]


print('renaming')
script_name = sys.argv[0]
filenames = os.listdir()
filenames.remove(script_name)
filenames.sort()
filenames.reverse()

new_names = list(map(rename,filenames))
for i in range(len(filenames)):
    os.rename(filenames[i],new_names[i])
