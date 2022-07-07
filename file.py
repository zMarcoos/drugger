# filename -> filename is the name of the current file,
# values -> value is an array object
def write(filename, values):
    try:
        file = open(filename, 'a')

        for value in values:
            file.write(f'{str(value)}\n')
    except:
        print('Deu erro na função write_line')
    finally:
        file.close()


# function that returns an object based on a string in a file
def read(string):
    return eval(str(string))
