


e,d,k,n=0,0,0,0

alap=input("Kérem a robot parancsait: ")
for i in alap:
    if(i=='e' or i=='E'):
        e+=1
    elif(i=='d' or i=='D'):
        d-=1
    elif(i=='k' or i=='K'):
        k+=1
    elif(i=='n' or i=='N'):
        n-=1

print("E betűk száma: ",abs(e))
print("D betűk száma: ",abs(d))
print("K betűk száma: ",abs(k))
print("N betűk száma: ",abs(n))

x_tengely=k+n
y_tengely=e+d

x,y="",""

if(x_tengely > 0):
    for irany in range(x_tengely):
        x="K"*x_tengely
elif(x_tengely < 0):
    for irany in range(abs(x_tengely)):
        x="N"*abs(x_tengely)


if(y_tengely > 0):
    for irany in range(y_tengely):
        y="E"*y_tengely
elif(y_tengely < 0):
    for irany in range(abs(y_tengely)):
        y="D"*abs(y_tengely)

print("Egy legrövidebb út parancsszava: ",x,y)


