'''n1=int(input("enter a value for n1"))
n2=int(input("enter a value for n2"))
array=[i for i in range(n1,n2+1)]
print(array)
l1=[array[i:j+1] for i in range(len(array))for j in eange(i,len(array))]
print(l1)
c=0
for i in l1:
   if sum(i)%2!=0:
    c+=1
print(c)'''
#------------------------------------------

#list comprehension
#for loop version
'''result=[]
for i in range(11):
    result.append(i)
print(result)
#list comprehension version
print([i for i in range(11)])'''
#------------------------------------------

'''result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
print([i for i in range(11) if i%2!=0])'''
#------------------------------------------

'''result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])'''
#-------------------------------------------------------

'''mat=[[1,2,3,4],[5,6,7,8,],[9,10,11,12],[13,14,15,16]]
result=[]
for i in range(len(mat)):
    for j in mat[i]:
        if j%2!=0:
           result.append(j**2)
        else:
           result.append(j**3)
print(result)
print([j**2 if j%2!=0 else j**3 for i in range(len(mat)) for j in mat[i]])'''
#---------------------------------------------------------------------------------

'''mat=[[1,2,3,4],[5,6,7,8,],[9,10,11,12],[13,14,15,16]]
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
           row_data.append(ele**2)
        else:
           row_data.append(ele**3)
print(result)
print([ele**2 if ele%2!=0 else ele**3 for row in mat for ele in row])
print([[ele**2 if ele%2!=0 else ele**3 for ele in row] for row in mat])'''
#-----------------------------------------------------------------------------------

'''mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]
for i in list_b:
    if i in mylist:
        a=(i,mylist.index(i))
    result.append(a)
print(result)
print([(i,mylist.index(i)) for i in list_b if i in mylist])'''  
#------------------------------------------------------------------------

#dictionary comprehension
'''mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result={}
for i in list_b:
    result[i]=mylist.index(i)
print(result)
print({i:mylist.index(i) for i in list_b})'''
#------------------------------------------------------------------

'''sentences=["a new world record was set",
           "in the holy city of ayodhya",
           "on the eve of diwali on tuesday",
           "with over three lakh diya or earthen lamps",
           "list up simultaneously on the banks of the salary river"]
stopwords=['for','a','of','the','and','to','in','on','with']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
       print(word)
       if word not in stopwords:
           row_data.append(word)
    result.append(row_data)
print(result)
print([word for word in sentence.split() if word not in stopwords for sentence in sentences])'''
#---------------------------------------------------------------------------------------------

'''array=list(map(int,input().split(",")))
number1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
print(number1)
l=array[array.index(5):array.index(8+1)]
number2=""
for i in l:
    number2+=str(i)
print(number2)
print(int(number2)+number1)'''
#---------------------------------------------------------------------

'''s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    num.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))'''
#------------------------------------------------------------


'''def isPrime(num):
    if num==2:
        return True
    for i in range(2,num//2+1,1):
        if num%i:
            continue
        else:
            return False
            break
    else:
        return True
def factors(num):
    res=[1]
    for i in range(2,num//2+1):
        if num%i==0:
            res.append(i)
    res.append(num)
    return res
num=int(input("Enter the number here: "))
numl=[i for i in range(num,num+9,1)]
res=[]
print(numl)
for i in numl:
    f=factors(i)
    for j in range(len(f)-1,-1,-1):
        if isPrime(f[j]):
            res.append(f[j])
            break
print(f"{res} sum= {sum(res)}")'''
#---------------------------------------------------
