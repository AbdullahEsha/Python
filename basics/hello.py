import numpy as np
x = 15
y = 'hi'
z = ("apple", "banana", "cherry")
fruits = ["apple", "banana", "cherry"]
s = {"apple", "banana", "cherry"}
arrnp = np.array([1, 2, 3, 4, 5])

print("find type!!\n")
print(type(y))
print(type(x))
print(type(z))
print(type(fruits))
print(type(s))
print(type(arrnp))

print("\nwhile loop!!\n")
i = 1
while i < 6:
  print(i)
  if i == 5:
    break
  i += 1

print("\nFor loop for tuple!!\n")
for i in z:
  if i == "cherry":
    break
  print(i)

print("\nFor loop for list!!\n")
for x in fruits:
  if x == "banana":
    break
  print(x)
  
print("\nFor loop for set!!\n")
for j in s:
  if j == "cherry":
    break
  print(j)
  
print("\nthis is:",arrnp,"a numpy array!!")
