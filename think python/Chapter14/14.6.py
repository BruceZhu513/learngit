import urllib

conn=urllib.urlopen('http://uszip.com/zip/02492')
for line in conn:
    if 'population' in line:
        print line

conn.close()

