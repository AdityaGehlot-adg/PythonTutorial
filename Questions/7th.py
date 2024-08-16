# Count vovel in a given string

string="hello my name is aditya gehlot"
vovel_list=[]

for i in range(len(string)):
    if string[i] in ['a','e','i','o','u']:
        vovel_list.append(string[i])

print(len(vovel_list))        