#take 2 comma separated inputs from user
#1.) user's name
#2.) a single character

#output - 2 print lines
#1.)user's name length
#2.)count the charecter that user inputed (bonous :- case insensitive count )

name,char=input("enter comma separated name and character :-").split(",")
print(f"lenth of your name is :{len(name)}")
print(f"character count :{name.count(char)}")