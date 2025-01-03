x="wwwwooorrrlllddd"
def clenword(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return clenword(word[1:])
    return word[0] + clenword(word[1:])
print(clenword(x))            
test="add"
