import string

s='  asf fsad, asf. saf'
print s.strip(string.punctuation+string.whitespace)
print s.replace('af ','a')
print s.translate(None,string.punctuation+string.whitespace)
print s.split()[2].translate(None,string.punctuation+string.whitespace)
