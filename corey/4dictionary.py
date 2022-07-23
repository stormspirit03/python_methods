##dictionary is similar to the structure in c language
student={'name':'john','age':25,'courses':['math','algorithm']}
#access perticular element, if not found thorws key error
print(student['name']) ##john 
# get method to access the dictionary 
print(student.get('phone','Not found !!'))  # second arguement is default for not found.
#add new entry to the dictionary
student['phone']='5555-555555'
print(student)
##to update multiple values at a time 
student.update({'name':'Jane','age':24})
print(student)
##delete - del
del student['age']
print(student)

student['age']=24
print(student)
#pop 
age=student.pop('age')
print(age)
print(student)

#length of dict
print(len(student))
#get all the keys (name,age etc)
print(student.keys())
#to get repsective values
print(student.values())
#######loop through  only keys
for key in student:
	print(key)

####for both key and value
for key,value in student.items():
	print(key,value)	