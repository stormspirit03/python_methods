###Strings ###


#multiple line print
message="""Hello
world """
print(message) 

##lenth of string
print(len(message))
#access range in string 
print(message[0:12])
# all lower case and upper case
print(message.lower())
print(message.upper())
#count appearance of perticular character or word
print(message.count("i"))
# to find starting index of a substring
# returns -1 if doesnt find any
print(message.find("nice"))
# replace a sub string or string with new 
#name.replace(whom to replace, with whom) u should captrure it
new_message=message.replace('world','universe')
print(new_message)
#formating string
greeting='Hello'
name='Raviraj'
message=f'{greeting}, {name.lower()}. welcome!'
print(message)
#to find all atributes and methods accessable to a perticular variable.
print(dir(message))
# help function 
help(str)
## more specific
help(str.lower)



