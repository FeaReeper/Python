# 2.

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(given_list):
    for dict in given_list:
        for key in dict:
            print(key + " - " + dict[key])


# iterateDictionary(students)


# 3.

def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        for key in dict:
            if key == key_name:
                print(dict[key])


# iterateDictionary2('last_name', students)


# 4. 
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key in dict:
        print(len(dict[key]), key.upper())
        i = 0
        while i < len(dict[key]):
            print(dict[key][i])
            i += 1
        print("")


printInfo(dojo)


