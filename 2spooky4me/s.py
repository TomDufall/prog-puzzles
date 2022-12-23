from itertools import *
import sys
print("".join(str(eval(v+sys.argv[2].replace("^","**").replace("/","//"))) if ((v := "".join(g)).isdecimal()) else v for _, g in groupby(sys.argv[1], str.isalpha)))