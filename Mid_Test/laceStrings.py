def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    result = ''
    l = max(len(s1),len(s2))
    for idx in range(l):
        try:
            result += s1[idx] + s2[idx]
        except:
            if len(s1) > len(s2):
                result += s1[idx:]
            elif len(s1) < len(s2):
                result += s2[idx:]
            break
    return result

print laceStrings('abcd','efghi')
print laceStrings('aaaaaa', 'zzzzzz')
print laceStrings('', '')
print laceStrings('fnjcszobd', 'oslpqyugc')
print laceStrings('fdew', 'ohqbgmiulv') # Correct Answer: 'fodheqwbgmiulv'
