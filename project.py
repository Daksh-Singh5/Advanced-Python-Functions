power1=int(input("Enter any number: "))
power2=int(input("Enter any number: "))


num = [1,2,3,4,5,6,7,8,9,10]

def square(num):
    return num**power1

def cube(num):
    return num**power2

squarenum = list(map(square,num))
cubenum = list(map(cube,num))

print(squarenum)
print(cubenum)

zipset = list(zip(cubenum,squarenum))
print(zipset)

for i in zipset:
    if i < (512,64):
        print(exit)
        exit()
    print(i)