import numpy as np
from ipdb import set_trace

def pearson(v1,v2):
    #set_trace()
    x=np.array(v1)
    y=np.array(v2)

    t1=sum((x-x.mean())*(y-y.mean()))
    t2=pow(sum(pow(x-x.mean(),2)),0.5)*pow(sum(pow(y-y.mean(),2)),0.5)
    t=t1/t2  
    #set_trace()
    print "t1:%f,t2:%f,t:%f" % (t1,t2,t)

    return t