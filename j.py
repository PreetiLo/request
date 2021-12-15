import requests
import json


url=requests.get("http://saral.navgurukul.org/api/courses")
a=url.json()
with open("folder.json","w")as file_data:
    json.dump(a,file_data,indent=6)
s=1
for i in a:
    print(s,".",i["name"],i["id"])
    s+=1
c=int(input("enter your number which do you want:"))
print(a[c-1]["name"])
print(a[c-1]["id"])
n=input("enter serial number which you previous or next (n/p)")
if n=="p":
    url=requests.get("http://saral.navgurukul.org/api/courses")
    a=url.json()
    with open("folder.json","w")as file_data:
        json.dump(a,file_data,indent=4)
    s=1
    for i in a:
        print(s,".",i["name"],i["id"])
        s+=1
    course_no=int(input("enter your number which do you want:"))
    print(a[course_no-1]["name"])
    id=a[course_no-1]["id"]
n=input("enter serial number which you previous or next (n/p)")
if n=="p":
    url=requests.get("http://saral.navgurukul.org/api/courses/"+str(id)+"/exercises")
    b=url.json()
    with open("topic.json","w")as k:
        json.dump(b,k,indent=4)
        s2=1
        list1=[]
        list2=[]

    for j in b["child"]["exercises"]:
        if k["child_exercises_id"]:
            print(s2,j["name"])
        s2+=1
        new_no=1
        list1.append(j)
        list2.append(j)
        continue
    if j["parent_exersices_id"]==k["id"]:
        print(s2,k["name"])
        s2+=1
        new_no+=1
        list1.append(j)
    for l in b["child"]["exercise"]:
        if k["parent_exercise_id"]!=j["id"]:
            print("  ",new_no,k["name"])
            new_no+=1
            list2.append(j)
            break
    with open("topic1.json","w")as f:
        json.dump(list1,f,indent=4)
point=int(input("enter the number point:"))
n1=input("enter weather do u want previous of next(n/p)")
if n1=="p":
    url=requests.get("http://saral.navgurukul.org/api/courses/"+str(id)+"/exercises")
    t=url.json()
    with open("topic.json","w")as k:
        json.dump(t,k,indent=4)
        serial_number2=1
        list1=[]
        list2=[]
    for j in t["child"]["exercise"]:
        if j["parent_exercise_id"]==None:
            print(serial_number2,j["name"])
            serial_number2+=1
            new_no=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exersice_id"]==j["id"]:
            print(serial_number2,j["name"])
            serial_number2+=1
            new_no=1
            list1.append(j)
        for l in t["course"]["exercise"]:
            if j["parent_exercise_id"]!=j["id"]:
                print("  ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                break
        with open("topic1.json","w")as f:
            json.dump(list1,f,indent=4)
    point=int(input("enter the number point"))


    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[point-1]["name"])
            num=(list1[0]["id"])
            print("num")

            var=[]
            var3=[]
            new_no1=1
            for n in list2:
                if n["parent_exercise_id"]==num:
                    print("  ",new_no1,n["name"])
                    var.append(n["name"])
                var3.append(n["content"])
            new_no1+=1


question=int(input("choose the specific questions no:"))
question1=question-1
print(var3[question1])
while question>0:
    question2=input("do you next question or previous question n/p:-")
    if question==len(var3):
        print("next page")
        if question2=="p":
            if question==1:
                print("no more question")
            break
        else:
            question_no=question_no-1
            print(var3[question_no])
    elif question2=="n":
        if question<len(var3):
            index=question+1
            print(var3[index-1])
            question=question+1
            if question1==(len(var3)-1):
                print("next page")
                break
