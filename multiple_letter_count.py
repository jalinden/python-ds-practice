def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    frequencyDict = {}
    for letter in phrase:
        key = frequencyDict.keys()
        if letter in key:
            frequencyDict[letter] += 1
        else:
            frequencyDict[letter] = 1
    return frequencyDict