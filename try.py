def enter():
    persons = {}
    name = input("Enter your name:")
    school = input(" Enter the name of your school:")
    persons = {"name":name, "school":school}
    return persons

persons = enter()
for person in persons:
    print(f'name: {persons["name"]}, school: {persons["school"]}')

