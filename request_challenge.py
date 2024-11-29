from bs4 import BeautifulSoup
import requests

response = requests.get('https://en.wikipedia.org/wiki/Picea_abies')
soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.text)

# Challenge queries for the Wikipedia page:
# 1. Get the text of the top level heading (h1).
# 2. Find how many second level heading (h2) tags there are.
# 3. Extract the href of the first link on the page.

print("Top Level Heading: ")
print(soup.h1.text, '\n')

print("Second Level Headings: ")
h2_list = soup.find_all('h2')
for h2 in h2_list:
    print(h2.text)

print("h2 Tags: ", len(h2_list), "\n")

print("First href: ")
print(soup.a['href'])