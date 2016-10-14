import os
import commands
import sys
def walk(dirname):
    txt=[]
    for root,dirs,files in os.walk(dirname):
        for name in files:
            splitname=os.path.join(root,name).rsplit('.')
            if splitname[-1]=='txt':
                txt.append(name)
    return txt


def find_duplicates(txts):
    md5=dict()
    duplicates=[]
    for txt in txts:
        cmd='ls -l'
        fp=os.popen(cmd)
        res=fp.read()
        md5[res].append(txt)
        fp.close()
    return md5
        
if __name__=='__main__':
    txts=walk('.')
    print txts
    print find_duplicates(txts)
    
