from pathlib import Path 

#where am I 
cwd = Path.cwd()
print(cwd)

print('\nCurrent working directory: \n'+ str(cwd))
#combine parts to create full path and file name 
new_file = Path.joinpath(cwd, 'new_file.txt')
print('\n Full Path :\n'+ str(new_file))

print('\n Does that file exists ?'+ str(new_file.exists()) + '\n')

parent = cwd.parent 

print(parent.is_dir())

print(parent.is_file())

for child in parent.iterdir():
    if child.is_dir():
        print(child)

demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

print(demo_file.name)

print(demo_file.suffix)

print(demo_file.parent.name)

print(demo_file.stat().st_size)
