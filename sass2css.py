import re
from tempfile import mkstemp
from shutil import move, copy
from os import remove, close
import sys

title = '''
This is sass2css. A lightweight SASS to static CSS converter utility.

Usage:
    python sass2css.py <variable_file> <replaceable_file>

<variable_file>
    An scss file that contains the replaceable SASS variables.

<replaceable_file>
    A scss file you want to convert to static css file by replacing the sass
    variables in it. The original file will be reserved.


Tibor Simon 2015 All right reserved
MIT License

'''

print(title)

if len(sys.argv) != 3:
    print('Error: you have to specify the variable file and the replaceable file!')
    exit()


def replace(file_path, pattern, subst):
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    remove(file_path)
    move(abs_path, file_path)


variables = []
values = []
pattern = re.compile('(\$[\w-]+)\s+:\s+([\$\w#-\.\s]+);')
with open(sys.argv[1]) as f:
    for line in f.readlines():
        match = pattern.match(line)
        if match:
            variables.append(match.group(1))
            value = match.group(2)
            if value in variables:
                index = variables.index(value)
                value = values[index]
            values.append(value)

converted_file = 'converted_' + sys.argv[2]
copy(sys.argv[2], converted_file)

for i in range(len(variables)):
    replace(converted_file, variables[i], values[i])

print('===============================================================')
print('Variable replacement was successful!')
print()
print('Replaced variables:')

for i in range(len(variables)):
    print('  {0:<24} -> {1}'.format(variables[i], values[i]))

print()
print('sass2css finished..')




