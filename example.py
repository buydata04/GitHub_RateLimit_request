import requests
import time

token = "access_token"

item="https://api.github.com/user/repos"
headers={"Authorization":"token "+token} #注意token要有空格
r = requests.get(item,headers=headers)

timestamp = int(r.headers['X-RateLimit-Reset'])
time_local = time.localtime(timestamp)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)


print("X-RateLimit-Limit : " + r.headers['X-RateLimit-Limit'])
print("X-RateLimit-Remaining : " + r.headers['X-RateLimit-Remaining'])
print("X-RateLimit-Reset : " + dt)
