#Used to split dataset into train and validation sets
import os
import sys
import shutil
import numpy as np

def split(source1, dest1):
    files = os.listdir(source1)
    for f in files:
        if np.random.rand(1) < 0.2:
            shutil.move(source1 + '/'+ f, dest1 + '/'+ f)


if(__name__=="__main__"):
    args = sys.argv
    source = args[1]
    dest = args[2]
    split(source,dest)
