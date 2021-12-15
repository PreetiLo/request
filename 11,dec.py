from bs4 import beautifulsoup
import requests

with open('text.html') as f:
    soup=beautifulsoup(f,'goli')

m=soup.find('div')
print(m)