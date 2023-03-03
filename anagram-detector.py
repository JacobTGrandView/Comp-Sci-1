test = 'muscle'
original = 'elcsum'

def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower()) 


if is_anagram(test, original) == True:
    print('True')
else:
    print('False')