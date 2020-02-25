# Mohamed Bensaleh
# mob127
# 11254030
# CMPT 141-02




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

s = 'cat'
list_of_characters = [char for char in s]
print(permutations(list_of_characters))
