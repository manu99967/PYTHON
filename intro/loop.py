# for ,while , do_while

## -1 ,1 -> -1, 1

# while (<condition>):
to_loop=True
i=0
while to_loop:
   if i>10:
      to_loop=False
   print("i is",i)
   i=i+1 

# WEB->JS
k=0
while k<10:
   print("k is",k)
   k=k+1

#for(let i=0;i<10;i++)

# starting 2 to 10
for i in range(2,10):
   print("For loop is is",i)

#from 10 to  2
for i in range(10,2,-1):
   print("For loop is is",i)


for i in range(0,1000,5):
   print("All even numbers",i)

fruits=["Mango","Papaya","Orange"]

for fruit in fruits:
   print(fruit)

for i in range(0,3):
    # 0,1,2 // fruits[0] //fruits[1] //fruits[2]
    fruit=fruits[i]
    print(fruit)