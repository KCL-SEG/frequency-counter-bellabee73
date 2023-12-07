"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if type(item) != str:
            toString = str(item)
            if (toString in frequencies):
                frequencies[toString] +=1
            else:
                frequencies[toString] = 1
        else: 
            if (item in frequencies):
                frequencies[item] +=1
            else:
                frequencies[item] = 1
    return frequencies
