from itertools import *
import sys
print("".join(v if ((v:="".join(g)).isalpha()) else str(eval(v+sys.argv[2].replace("^","**").replace("/","//"))) for _,g in groupby(sys.argv[1],str.isalpha)))