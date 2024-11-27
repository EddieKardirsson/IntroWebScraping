from bs4 import BeautifulSoup

# Learning basic BeautifulSoup functionality

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')  # html.parser removes error messages

# prettify() formats the string with a nested structure
print(soup.prettify())

print(soup.title, '\n')
print(soup.title.string, '\n')

print(soup.p.b, '\n')

print(soup.p['class'], '\n')
print(soup.a['href'], '\n')
