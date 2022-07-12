def pig_latin(word):
    if word[0] in 'aeiou':
        word = word + 'way'
    else:
        word = word[1:] + word[0] + 'ay'
    
    return word


print(pig_latin('computer'))