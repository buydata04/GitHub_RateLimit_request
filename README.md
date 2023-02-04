簡易查詢剩餘訪問次數請求&下次重製時間

使用說明:
將yout_access_token修改為你申請的access_token

```go
access_token = "yout_access_token"

item="https://api.github.com/user/repos"
headers={"Authorization":"token "+access_token}
r = requests.get(item,headers=headers)

timestamp = int(r.headers['X-RateLimit-Reset'])
time_local = time.localtime(timestamp)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)


print("X-RateLimit-Limit : " + r.headers['X-RateLimit-Limit'])
print("X-RateLimit-Remaining : " + r.headers['X-RateLimit-Remaining'])
print("X-RateLimit-Reset : " + dt)
```
