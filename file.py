def write_line(filename, values):
     '''
     filename -> filename is the name of the current file,
     values -> value is a array object
     '''
     
     try:
          file = open(filename, 'a')
          
          for value in values:
               file.write(str(value)+ "\n")
     except:
          print('Deu erro na função write_line')
     finally:
          file.close()

def to_object(filename, string):
     '''
     function that returns an object based on a string in a file
     '''
     
     return eval(str(string))     
