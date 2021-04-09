def lookup(phone):
    with open('belgium.txt',  encoding='utf-8') as fin:
        line = fin.readline()
        while(line != ''):
            if(line.startswith(str(phone).replace('+',''))):
                return line
            line = fin.readline()
    return None         
            
            
def increment_request_counter(line):
    #todo
    pass
 