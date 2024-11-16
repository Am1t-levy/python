#1.
# student = {
#     "name": "amit",
#     "age": 22,
#     "grade": "A"
# }
# print(student["name"])
 
# student["school"] = "harvard"
# print(student)


#2.
# student.update({"age": "23"})
# print(student)

# student.pop("grade")
# print(student)

# if "school" in student.keys():
#     print("yes")
# else:
#     print("nahh bro")

#3. 
# capitals = { 'france': 'paris', 'spain': 'madrid', 'japan': 'tokyo' } 
# for country, capital in capitals.items():
#      print(f"the capital of {country} is {capital}")

# #4.
# print("keys:", capitals.keys())
# print("values:", capitals.values())
# print("items", capitals.items())
# capital_of_germany = capitals.get('germany', 'not found')
# print("the capital of germany is:", capital_of_germany)


#5.
# def count_chars(text):
#   d = {} 
#   for c in text:
#       if c in d:
#             d[c] += 1
#       else:
#           d[c] = 1
#  return d        

# text = "helloooooo4738653756"
# print(count_chars(text))
