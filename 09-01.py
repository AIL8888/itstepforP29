import os


spysok = [1.4, 6.7, 8.2]
file1 = open('myfile1.doc', 'wb')
for item in spysok:
    zminna = str(item) + '\n'
    bt = zminna.encode() # encode - конвертує рядок у послідовність байт
    file1.write(bt)
file1.close()
spysok2 = []
file2 = open('myfile1.doc', 'rb')
for item1 in file2:
    x = float(item1)
    spysok2 += [x]
print(spysok2)
file2.close()


file = open('m1.bin', 'rb')
d = file.read()
print('d = ', d)


path = 'C:\Windows\Web'
for path, dirnames, filenames in os.walk(path):
    print(f'path - {path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames - {filenames}')


dir_1 = 'Windows'
dir_2 = 'Web'
path = os.path.join(dir_1, dir_2)
print(path)


path = os.path.normpath('C:\\Windows\\Web')
print(os.path.isabs(path))
print(os.path.isfile(path))
print(os.path.isdir(path))
print(os.path.islink(path))


path1 = os.path.normpath('new_dir')
os.mkdir(path1)
os.rmdir(path1)


def file_collector(path):
    path = os.path.normpath(path)
    result = {'dirs':[], 'files':[]}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result['dirs'].append(dir)
        for file in filenames:
            result['files'].append(file)
    with open('nashidanni.txt', 'w') as file:
        file.write('\n{:-^50}\n'.format('Directories'))
        for dir in result['dirs']:
            file.write(f'\t{dir}\n')
        file.write('\n{:-^50}\n'.format('Files'))
        for files in result['files']:
            file.write(f'\t{files}\n')
zminna = 'C:\\Windows\\Web'
file_collector(zminna)
