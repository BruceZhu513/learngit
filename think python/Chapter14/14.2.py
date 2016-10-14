def sed(old,new,filename1,filename2):
    try:
        fin=open(filename1)
        fout=open(filename2,'w')
        for line in fin:
            print line
            if old in line:
                fout.write(line.replace(old,new))
        fin.close()
        fout.close()
    except:
        print 'wrong'

if __name__=='__main__':
    filename1='love.txt'
    filename2='lover.txt'
    old='mrs.wan'
    new='my wife'
    sed(old,new,filename1,filename2)
    
