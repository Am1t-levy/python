#1.
my_sets = {1,2,3,4,5,}
my_sets.add(6)
print(my_sets)
my_sets.add(3)
my_sets.remove(2)
print(my_sets)

#2.
 set_1 = {1,2,3,4}
 set_2 = {3,4,5,6} 
set3 = set_1.union(set_2)
print(set3)

intersection_result = set_1.intersection(set_2)
print("intersection:", intersection_result)

difference_result = set_1.difference(set_2)
print("difference (set_1 - set_2):", difference_result)

symmetric_difference_result = set_1.symmetric_difference(set_2)
print("symmetric difference:", symmetric_difference_result)

#3.
numbers = [1,2,2,3,4,4,5]
unique_members = list(set(numbers))
print("unique numbers:", unique_members)

#4.
set_1 = {1,2,3,4}
set_2 = {3,4,5,6} 

if 3 in set_1:
    print("The number 3 is in set_1")
else:
    print("The number 3 is not in set_1")

if 6 in set_2:
    print("the number 6 is in set_1")
else: 
    print("the number 6 is not in set_1")     

#5. 
set_a = {1,2,3,4,5}
set_a.add(6)
print("after adding 6:", set_a)

set_a.remove(3)
print("afer removing 3:", set_a)

set_a.discard(2)
print("after discarding 2:", set_a)

set_a.discard(10)
print("after discarding 10 (not present):", set_a)

