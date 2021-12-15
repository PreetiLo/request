import requests

# # # x = requests.get
# # # url='https://web.whatsapp.com/'
# # data={'p1':45,'friend':'lata koli'}

# # reponst=requests.post('https://web.whatsapp.com/',params=data)
# # print(reponst.text[201])

# # # print(reponst)

# parameter= (('page',5) , ('count',10))
r=requests.get('http://httpbin.org/')#, params=parameter)
# # print(r.text[:400])
print(r.url)

# import os  

# a=os.getcwd()
# print(a)
# os.mkdir('love')

# import time
# time.sleep(2)
# os.rename('love','love1')
# time.sleep(2)
# os.rmdir('love1')
# # help(os)