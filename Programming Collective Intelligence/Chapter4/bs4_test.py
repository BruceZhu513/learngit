from bs4 import BeautifulSoup

html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=BeautifulSoup(html)
##print soup.prettify()
##print soup.title
##print soup.p
##print soup('p')
####print soup.body
##print soup.a
##print soup.head
##print type(soup.a)
##print type(soup('a'))


##print soup.name
##print soup.head.name
##print soup.a.name
##print soup.title.attrs
##print soup.p.attrs
##print dict(soup.p.attrs)
##if 'name' in soup.p.attrs:
##    print 'a'
    
##print soup.p['name']

##print soup.a
##print soup.a.string
##print type(soup.a.string)

##tag 的 .content 属性可以将tag的子节点以列表的方式输出
##print soup.head.contents
##print soup.body.contents

##list的迭代器
##print soup.head.children
##for child in soup.body.children:
##    print child

print soup.descendants
for child in soup.descendants:
    print child



