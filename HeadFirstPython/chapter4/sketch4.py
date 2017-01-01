from nester import print_lol
man=[]
other=[]
try:
    with open('sketch.txt') as data:
        for each_line in data:
            try:
                (role,line_spoken)=each_line.split(':',1)
                line_spoken=line_spoken.strip()
                if role=='Man':
                    man.append(line_spoken)
                elif role=='Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as err:
    print('The detafile is missing!'+str(err))    
try:
    with open('man_data.txt','w') as man_file,open('other_data.txt','w') as other_file:
        print_lol(man,fn=man_file);
        print_lol(other,fn=other_file);
except IOError as err:
    print("File error: "+str(err))

