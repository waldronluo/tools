import os
import os.path
import subprocess
import pprint
import sys


def visit(arg, dirname, names):
    for  name in names:
        subname  =  os.path.join(dirname, name)
        if os.path.isdir (subname):
            #print dirname + '' + '%s/' % name
            a = 2+2 
        else :
            #print dirname + '' + '%s' % name
            print("cat " +  dirname + '/' + name + ' | ' + ' grep ' + arg)
            os.system("cat " +  dirname + '/' + name + ' | ' + ' grep ' + arg)
       #     subprocess.call(['cat', dirname + '' + name + ' | ' + 'grep ' + arg])
#    print



if __name__ == "__main__":
    
    if ( len(sys.argv) > 1 ):
        print ("Searching for "+ sys.argv[1] )
        os.path.walk(sys.argv[1], visit, sys.argv[2])
