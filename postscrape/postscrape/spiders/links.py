import string

website_link= "https://www.nfl.com/players/"


def getPlayerLinks():
    for letter in string.ascii_lowercase:
        yield website_link + letter