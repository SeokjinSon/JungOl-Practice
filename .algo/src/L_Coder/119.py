from datetime import datetime

now = datetime.now()
a=0;
a=now.year-1900
p=a
a+=now.month-1
q=a
a+=now.day
r=a

print(p, q, r)