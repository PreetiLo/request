import json

a={"name":"kailash","age":60,"subject":"navgurukul"}
with open("text.json","w") as file:
    json.dump(a,file)