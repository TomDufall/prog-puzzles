from itertools import *
import sys
a=str.isalpha
print(*[v if a(v:="".join(g)) else eval(v+sys.argv[2].replace("^","**").replace("/","//")) for _,g in groupby(sys.argv[1],a)],sep="")