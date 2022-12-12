import time


now = time.time()
curDateTime = time.ctime(now)



with open('today.txt', 'w') as f:
    f.write(curDateTime)


with open('today.txt', 'r') as fIn:
    today_string = fIn.read()
    
print(today_string)
