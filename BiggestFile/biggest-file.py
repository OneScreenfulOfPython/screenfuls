"""Find the biggest file in a directory structure

The files() function iterates recursively over all the files
in an entire directory structure, using a generator to avoid
building up the whole list into memory.

The builtin max() function finds the maximum entry in the
iterator returned from files, going by os.path.getsize.
NB It doesn't return the *size* but the *filepath* which is
the biggest; you have to do a further lookup to get the size.
"""
import os, sys
import glob

def files(dirpath):
    for f in glob.iglob(os.path.join(dirpath, "*")):
        if os.path.isfile(f):
            yield f
        else:
            for g in files(f):
                yield g

def biggest(dirpath):
    return max(files(dirpath), key=os.path.getsize)

if __name__ == '__main__':
    biggest_file = biggest(os.path.dirname(sys.executable))
    print(biggest_file, "=>", os.path.getsize(biggest_file))
