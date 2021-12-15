import requests
import json
l=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")
m=l.json()
with open("f.json","w")as file_data:
    json.dump(m,file_data,indent=4)
s=1
for i in m:
    print(s,".",i["name"],i["id"])
    s+=1
course=int(input("enter your number which do you want:"))
print(m[course-1]["name"])
id=(m[course-1]["id"])
n=input("enter serial number which you previous or next (n/p)")
if n=="p":
    l=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")
    m=l.json()
    with open("f.json","w")as file_data:
        json.dump(m,file_data,indent=4)
    s=1
    for i in m:
        # print(type(i),i)
        # print(serial_number[course_no-1]["name"])
        print(s,".",i["name"],i["id"])
        s+=1
    course=int(input("enter your number which do you want:"))
    print(m[course-1]["name"])
    id=m[course-1]["id"]


# url=requests.get("https://api.merakilearn.org/courses")
n=input("enter serial number which you previous or next (n/p)")
if n=="p":
    l=requests.get("http://saral.navgurukul.org/api/courses/74/exercises/"+str(id)+"/exercises")
    v=l.json()
    with open("topic.json","w")as k:
        json.dump(v,k,indent=4)
        s2=1
        list1=[]
        list2=[]

    for j in v["course"]["exercises"]:
        if k["parent_exercises_id"]:
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
    for l in v["course"]["exercise"]:
        if k["parent_exercise_id"]!=j["id"]:
            print("  ",new_no,k["name"])
            new_no+=1
            list2.append(j)
            break
    with open("topic1.json","w")as f:
        json.dump(list1,f,indent=4)
p=int(input("enter the number point:"))
na=input("enter weather do u want previous of next(n/p)")
if na=="p":
    l=requests.get("http://saral.navgurukul.org/api/courses/74/exercises/"+str(id)+"/exercises")
    v=l.json()
    with open("topic.json","w")as k:
        json.dump(v,k,indent=4)
        s2=1
        list1=[]
        list2=[]
    for j in v["child"]["exercise"]:
        if j["child_exercise_id"]==None:
            print(s2,j["name"])
            s2+=1
            new_no=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exersice_id"]==j["id"]:
            print(s2,j["name"])
            s2+=1
            new_no=1
            list1.append(j)
        for l in v["child"]["exercise"]:
            if j["child_exercise_id"]!=j["id"]:
                print("  ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                break
        with open("t.json","w")as f:
            json.dump(list1,f,indent=4)
    point=int(input("enter the number point"))
for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[point-1]["name"])
            num=(list1[0]["id"])
            print("num")

            v1=[]
            v2=[]
            n1=1
            for n in list2:
                if n["parent_exercise_id"]==num:
                    print("  ",n1,n["name"])
                    v1.append(n["name"])
                v2.append(n["content"])
            n1+=1


question=int(input("choose the specific questions no:"))
question1=question
print(v2[question])
while question>0:
    question2=input("do you next question or previous question n/p:-")
    if question==len(v2):
        print("next page")
        if question2=="p":
            if question==1:
                print("no more question")
            break
        else:
            question=question-1
            print(v2[question])
    elif question2=="n":
        if question_no<len(v2):
            index=question_no+1
            print(v2[index-1])
            question_no=question_no+1
            if question==(len(v2)-1):
                print("next page")
                break