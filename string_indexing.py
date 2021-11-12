#indexing and slicing is very important in python
text ='basebal l'
print(len(text))
print(text[0])
print(text[1])
print(text[7])
print(len(text))
print("***************")
statement="i am a devops engineer"
print(statement[20]), #out of bounds or range, no value
#startindex : stopindex(-1) : step value
#index can be defined as index[::]
print(statement[4])
print(len(statement))
print(statement)
print(type(statement))

print(statement[1:10])

print("***********")
name="cameroon"
print(name[2:8])  #index starts at position 2 and ends at position 8. 
first_name="nketi"
print(len(first_name))
print(first_name[4])
print(first_name[2:5])
print(first_name[1:2])
print(first_name[2:5]) #eti

print("---slicing---")

#step value  means by how much you want to go to the next value 
'''step value example'''
country="Africancameroon"
print(len(country))
print(country[1:17:6])

prof="Elvis is a py trainer"
    #0123456789101112131415161718192021
print(prof)
print(len(prof))
print(prof[1:12:2])
print(prof[:15:3])  
print(prof[2:15])
print(prof[::2])
print(prof[::])

print("=============================")
name="elvis"
print(name.endswith("s")) #this would return a bolean, true or false
name='john is a good person'
print(name.find('good')) # find gives index
print(name.count('good'))
print(name.title())
print(name.join('elvis'))
print(name.upper())
print(name.islower())