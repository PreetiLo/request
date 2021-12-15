import requests
import json

# printing the courses
url=requests.get("http://saral.navgurukul.org/api/courses")
a=url.json()
with open("folder1.json","w")as file_data:
    json.dump(a,file_data,indent=6)
s=1
for i in a:
    print(s,".",i["name"],i["id"])
    s+=1
c=int(input("enter your number which do you want:"))
print(a[c-1]["name"])
print(a[c-1]["id"])