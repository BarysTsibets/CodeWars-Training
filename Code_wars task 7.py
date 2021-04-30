"""Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names,
 which should be separated by an ampersand.

Example:
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
     # returns 'Bart, Lisa & Maggie'
     namelist([{'name': 'Bart'}]), # returns 'Bart')
     namelist([]), # returns '', "Must work with no names"""


def namelist(names):
    new_list = []
    if len(names)<1:
        result = ""
    else:
        for item in names:
            new_list.append(item['name'])
            if len(new_list) > 2:
                result = ", ".join(new_list[0:-1]) + " & " + " ".join(new_list[-1:])
            elif len(new_list) == 2:
                result = " & ".join(new_list[:])
            elif len(new_list) == 1:
                result = item['name']
    print(result)
    return result


namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
namelist([])
