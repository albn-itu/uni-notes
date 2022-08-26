from os import path, mkdir
import argparse

def get_exercise_name(number: int):
    return f'ex{number}'

def exercise_exists(number: int):
    return path.exists(get_exercise_name(number))

def copy_make_file(number: int):
    name = get_exercise_name(number)

    with open('Make_def', 'r') as file:
        filedata = file.read()
    
    filedata = filedata.replace('PLACE_TARGET_HERE', name)

    with open(f'{name}/makefile', 'w') as file:
        file.write(filedata)

def copy_source(number: int):
    name = get_exercise_name(number)

    with open('Source_def', 'r') as file:
        filedata = file.read()
    
    with open(f'{name}/{name}.c', 'w') as file:
        file.write(filedata)

def add_to_make(number: int):
    name = get_exercise_name(number)

    with open('makefile', 'r') as file:
        lines = file.readlines()
   
    lines[0] = lines[0].replace('\n', f' {name}\n') 
    with open(f'makefile', 'w') as file:
        file.writelines(lines)


def create_exercise(number: int):
    if exercise_exists(number):
        print('Exercise already exists')
        return

    mkdir(get_exercise_name(number)) 
    copy_source(number)
    copy_make_file(number)
    add_to_make(number)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create folder structures for C exercises')
    parser.add_argument('--exercise', '-e', dest='exercise', type=int, required=True)

    args = parser.parse_args()
    create_exercise(args.exercise)
    
