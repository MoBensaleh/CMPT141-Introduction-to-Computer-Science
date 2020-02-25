f = open('scrabble', 'r')
scrabbleList = list(f)
scrabbleList = [line.strip() for line in scrabbleList]
f.close()

def permutations(chars):
    """
    recursive function that creates a list of lists that contain all the permutations of a string
    :param chars: list of characters
    :return: A list of lists that contain all the permutations of a string
    """
    if len(chars) == 1:
        return [chars]
    lst = []
    for i in range(len(chars)):
        m = chars[i]
        plist = chars[:i] + chars[i+1:]
        for p in permutations(plist):
            lst.append([m] + p)
    return lst

s = ""
list_of_characters = [char for char in s]

points = {"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":5,"l":1,"m":3,"n":1,"o":1,"p":3,"q":10,"r":1,"s":1,"t":1,"u":1,"v":4,"w":4,"x":8,"y":4,"z":10}
def score(word):
    """
    A recursive function that calculates points in scrabble by taking string parameter and returning integer value associated
    with the number of points for letters in string
    :param word: string parameter
    :return: integer value associated with score from the points from each letter in string.
    """
    if len(word)<=1:
        return points.get(word[0],0)
    else:
        return points.get(word[0],0)+score(word[1:])




letters = input("Which letters do you have?: ")
list_of_letters = [char for char in letters]

permutations = permutations(list_of_letters)
permutationList = ["".join(x) for x in permutations]

valid_words = []
for combination in permutationList:
    if combination in scrabbleList:
        valid_words.append(combination)

if valid_words == []:
    print("No valid words found.")
else:
    print("Your best word(s):", valid_words)
    print("For", score(valid_words[0]), "points.")












