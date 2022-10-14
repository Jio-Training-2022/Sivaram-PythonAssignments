from bs4 import BeautifulSoup
import requests
URL = 'https://www.geeksforgeeks.org/python-programming-language/'
page = requests.get(URL)

text = page.content
soup = BeautifulSoup(text, "html.parser")
soup1 = soup.get_text()
words = soup1.split()
print('Number of words in text file :', len(words))
