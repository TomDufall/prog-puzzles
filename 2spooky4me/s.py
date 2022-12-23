from itertools import *
import sys
a=str.isalpha
_,x,y=sys.argv
print(*[v if a(v:="".join(g)) else eval(v+y.replace("^","**").replace("/","//")) for _,g in groupby(x,a)],sep="")