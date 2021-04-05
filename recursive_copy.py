import shutil
from pathlib import Path
'''
Finds all jpg files recursively, copy them to root and renamed
'''
p = Path().rglob("*.jpg")
x = 1
for path in p:
	name = str(x) if x >= 10 else ('0' + str(x))
	target = Path(name + '.jpg')
	shutil.copy(path,target)
	x+=1
print(x)