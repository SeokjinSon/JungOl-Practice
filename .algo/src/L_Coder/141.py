num = input()
i=1
result=1

while 1:
    if((int(num)*i)<100):
        result = int(num)*i
        i+=1
        print(str(result) + " ", end='')
        if result%10==0:
            break


# while result<100:
    
#     i+=1
#     if(result%10==0):
#         print(str(result) + " ", end='')
#         break
#     print(str(result) + " ", end='')