import re
def challenge1(text):
    pattern = 'ab+'
    if re.search(pattern,text):
        return ('Found a match!')
    else:
        return('Not matched!')

print(challenge1("ab"))
print(challenge1("abbb"))
print(challenge1("a"))

def challenge2(text):
    pattern = 'ab?'
    if re.search(pattern,text):
        return ('Found a match!')
    else:
        return('Not matched!')

print(challenge1("ab"))
print(challenge1("abbb"))
print(challenge1("a"))

def challenge3(text):
    pattern = 'abbb'
    if re.search(pattern,text):
        return ('Found a match!')
    else:
        return('Not matched!')

print(challenge3("ab"))
print(challenge3("abbb"))
print(challenge3("a"))

def challenge4(text):
    pattern = 'abbb?'
    if re.search(pattern,text):
        return ('Found a match!')
    else:
        return('Not matched!')

print(challenge4("ab"))
print(challenge4("abbb"))
print(challenge4("abb"))
