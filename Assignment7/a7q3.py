# Mohamed Bensaleh
# mob127
# 11254030
# CMPT141-02


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
print("gif:",score("gif"))
print("zoo:",score("zoo"))