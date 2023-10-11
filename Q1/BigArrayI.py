import random

arr = []
while len(arr)<19:
  arr.append(random.randint(20, 90))

#Print the Array from the beginning to the end
print("1) ", arr)

#Print the Array from the beginning to the end using a for-each loop
print("\n2) ", end=" ")
for i in arr:
  print(i, end=" ")

#What number is in the middle of the Array?
print("\n\n3) ", arr[int(len(arr)/2)])

#What is the average of the first, last and middle numbers?
print("\n4)", (arr[0] + arr[int(len(arr)/2)] + arr[len(arr)-1])/3)

#Find the smallest and the largest number in the Array
max=0
min=100
for i in arr:
  if i > max:
    max=i
  if i < min:
    min = i
print("\n5) ", min, ",", max)

#Switch the largest with smallest number. Print the list
mindex = arr.index(min)
arr[arr.index(max)]=min
arr[mindex]=max
print("\n6) ", arr)

#Create a new random from 1 to 10 and insert it in the middle slot. Print the numbers.
arr[int(len(arr)/2)]=random.randint(1, 10)
print("\n7) ", arr)

#Add 10 to every number in the List. Print all.
for i in range(len(arr)):
  arr[i]+=10
print("\n8) ", arr)

#Replace the 3rd element in the array with 5 and print the number that was ousted (only use one method to complete this.)
print("\n9) ", arr[2])
arr[2]=5

#What numbers are in the 50s?
print("\n10) ", end=" ")
for i in arr:
  if i >=50 and i <60:
    print(i, end=" ")

#What numbers are multiples of 4?
print("\n\n11) ", end=" ")
for i in arr:
  if i%4==0:
    print(i, end=" ")

#Is there a 60 in the list?
sixty = False
for i in arr:
  if i == 60:
    sixty = True
print("\n\n12) ", sixty)

#Check to see if all of the elements from front to back are in the same order from back to front
palindrome = True
for i in range(len(arr)-1):
  if arr[i]!=arr[len(arr)-(i+1)]:
    palindrome = False
print("\n13) ", palindrome)

#How many numbers are greater than the average?
ave = 0
cnt = 0
for i in arr:
  ave+=1
ave/=len(arr)

for i in arr:
  if i>ave:
    cnt+=1
print("\n14) ", cnt)

#How many of the numbers are even?
cnt = 0
for i in arr:
  if i%2==0:
    cnt+=1
print("\n15) ", cnt)

#Copy all of the elements of the array into a new array but in reverse order
arr.reverse()
print("\n16) ", arr)
arr.reverse()

#Write a program to shift every element of an array circularly right. E.g.-INPUT : 1 2 3 4 5 OUTPUT : 5 1 2 3 4
ph = arr[0]
for i in range(len(arr)-1):
  arr[i]=arr[i+1]
arr[len(arr)-1]=ph
print("\n17) ", arr)

#Find the sum of all of the digits of all of the elements
cnt=0
for i in arr:
  cnt+=int(i/10)
  cnt+=int(i%10)
print("\n18) ", cnt)

"""
1)  [70, 57, 79, 41, 78, 20, 25, 81, 80, 43, 64, 88, 41, 41, 66, 36, 25, 70, 40]

2)  70 57 79 41 78 20 25 81 80 43 64 88 41 41 66 36 25 70 40 

3)  43

4) 51.0

5)  20 , 88

6)  [70, 57, 79, 41, 78, 88, 25, 81, 80, 43, 64, 20, 41, 41, 66, 36, 25, 70, 40]

7)  [70, 57, 79, 41, 78, 88, 25, 81, 80, 4, 64, 20, 41, 41, 66, 36, 25, 70, 40]

8)  [80, 67, 89, 51, 88, 98, 35, 91, 90, 14, 74, 30, 51, 51, 76, 46, 35, 80, 50]

9)  89

10)  51 51 51 50 

11)  80 88 76 80 

12)  False

13)  False

14)  19

15)  11

16)  [50, 80, 35, 46, 76, 51, 51, 30, 74, 14, 90, 91, 35, 98, 88, 51, 5, 67, 80]

17)  [67, 5, 51, 88, 98, 35, 91, 90, 14, 74, 30, 51, 51, 76, 46, 35, 80, 50, 80]

18)  167
"""