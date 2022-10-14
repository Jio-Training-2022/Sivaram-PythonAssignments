from bs4 import BeautifulSoup
import requests
URL = 'https://github.com/Jio-Training-2022/python-training/blob/main/days/day-13-UnitedStates.md'
page = requests.get(URL)

text = page.content
soup = BeautifulSoup(text, "html.parser")
soup1 = soup.get_text()
soup1 = soup1.encode('utf-8').decode('ascii', 'ignore')
text_file = open("readme1.txt", "w")
text_file.write(soup1)
text_file.close()