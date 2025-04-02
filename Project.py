batch = {
    "number": 761,
    "version": "6a2zx6",
    "class" : 6
}
# print(batch)
new_list = [1,"apple",25.97,"car"]
# print(new_list)
set_1 = {1,2,3,4,5,6,7}
set_2 = {3,5,7,8}
union_set = set_1.union(set_2)
# print(union_set)
intersection_set = set_1.intersection(set_2)
# print(intersection_set)
new_tuple = (1,3,2,6,7)
# print(new_tuple)
new_directories = {
    "Mcabe-files": "Confidential",
    "James-Falcon": "Denied"
}
Falonies = {
    "documented" : "Yes",
    "Version_control" : "7.4.2",
    "Crime" : "Zero"
}
Revelation = {
    "Project_Guaranteed": "Yes",
    "Consumption" : "No",
    "Vibe-Coding" : "Yes"
}
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    # print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
#using for loop to print 1 to 5
for i in range(1,6):
  print(i)
# Using While loop to print 1 to 5
a = 1
while(a<6):
  print(a)
  a += 1
# Using for loop with else to print all items in a list
for i in range(4):
  print(new_list[i])
  i += 1
else:
  print("All Items have been displayed")
