##creat list
courses=['history','math','physics','compSci']
print(courses)
##length of list
print(len(courses))
##access perticular index
print(courses[0])
#can do it with negative index which starts from end
print(courses[-1])
#access range of elements (chunk) courses[start from:till this:step]
print(courses[0:2])
##append at the end
courses.append('art')
print(courses)
##insert at perticular index   courses.insert(index at whcih insert,'what to insert')
courses.insert(0,'civics')
print(courses)

## extend (to merge element of other list, insert can also do that but it adds
##entire list i.e list inside list. so we use extend)
courses2=['humanity','security']
# courses.insert(0,courses2)
# print(courses) #[['humanity', 'seurity'], 'civics', 'history', 'math', 'physics', 'compSci', 'art']
courses.extend(courses2) # takes only one arguement at and extends at the end
print(courses)

##remove a value
courses.remove('security')
print(courses)
#pop() also removes , and we can catch it with var. by default it removes last element
popped=courses.pop(0)
print(popped)

##sort (uses tim sort by default)
num=[1,3,5,4,2]
num.sort()
print(num)
#we can sort it in reverse also (descending order)
num=[1,3,5,4,2]
num.sort(reverse=True)
print(num)
# get a sorted version of list without altering original list.
#but we need to capture it in a new list variable else it wont work.
num=[1,3,5,4,2]
sorted_num=sorted(num)
print(sorted_num)

##get min,max,sum of list
print(min(sorted_num))
print(max(sorted_num))
print(sum(sorted_num))

##find index of perticular element by name if element is not in list it gives Value error
print(courses.index("history"))
# to check if a perticulaer element is in list or not (in operator returns true or false)
print("dbms" in courses)


## to print every element in list (accessing list)
for item in courses:
	print(item,end=", ")
print()
## to print item with its index number enumerate()
for index,item in enumerate(courses,start=1):  #start argument sets starting index
	print(index, item, end=", ")
	print()

## join list to make a string and split a list to make it list.
new_string="--".join(courses)		
print(new_string)
#split string to make it a list
new_list=new_string.split("--")
print(new_list)

####################################Tuples#####
# list is mutable (changeble) but tuples are imutable
# tuples can not be changed after created.only for loop through and access.
# all the functions of list which are imutable are usable with tuples.

subjects=('history','math','physics','compSci')
#subjects[0]='chemistry'  ##TypeError: 'tuple' object does not support item assignment
print(subjects)


##sets
#unordered and no duplicates
# mainly used to cheack if a value is in set or not (membership test )and throw away duplicates
#set does it more efficiently also we can find union and intersection
subjects={'history','math','physics','compSci'}
art_courses={'history','math','design','art'}
print(subjects.intersection(art_courses)) ##gives intersection
print(subjects.union(art_courses))## union
print(subjects.difference(art_courses))## different than art
##we cant create empty set like list and tuples .
empty_list=[]
empty_tuple=()
empty_dict={}
empty_set=set()

##use dirfunction on set for what fuctions we can apply 
print(dir(set))
## how to use perticular function use help
help(empty_set.add)

#sorted is used for strings and tuples ex sorted(s1). which returns a list
#where as s1.sort() is used on dict, list for sorting 

#dictionary
# to get all the keys of dictionary a 
a={'bla':1,'gla':2,'baba':3}
a.keys() #dict_keys(['bla', 'gla', 'baba'])

#to get all pairs 
a.items()  #dict_items([('bla', 1), ('gla', 2), ('baba', 3)])

#to get all values
a.values() #dict_values([1, 2, 3])

#to get an item
a.get('key','return this if not present') 
a['key'] # is also same to that of a.get() but a[] will throw error if not present

#update
a.update(b)
#a.update(b) it updates a with the values in b. if same keys are present then 
#update will happen as per values in b if key is not present then new entry will 
#be created in a .

a.pop('key to pop')


