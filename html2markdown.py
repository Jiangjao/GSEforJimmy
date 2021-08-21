# !/usr/bin/python3
# -- encoding=utf-8 ---


import html2text

from html2text import HTML2Text
# html2text.HTML2Text(baseurl=...)

print(HTML2Text(baseurl="./GSE14762-g-1-.html"))


print(html2text.html2text("<p>Hello, world.</p>")) 

test = html2text.HTML2Text(baseurl="./GSE14762-g-1-.html")
print(test)


# print(html2text.html2text(baseurl="./GSE14762-g-1-.html")) 
