import myfib
import w2015
import time

t1 = time.time()
myfib.g()
t2 = time.time()
print(t2 - t1)
w2015.q6()
print(time.time() - t2)