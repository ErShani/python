# File Operations

num = input("Enter Number:")
f = open('first.txt','wb')
num = str(num)
f.write(num)
f.close()

f = open('first.txt','r')

num = f.read()

num = int(num)

if num>200:
    f1 = open('second.txt','wb')
    num1 = str(num)
    f1.write("{0} is Larger".format(num1))
    f1.close()
    
else:
    f2 = open('second.txt','wb')
    num2 = str(num)
    f2.write("{0} is small".format(num2))
    f2.close()
    
f2 = open('second.txt','r')
print f2.read()
