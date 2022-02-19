import string
import random

SuffixLength = 2
PrefixLength = 6

def generatePrefixForProfileID():
    return ''.join(random.choices(string.ascii_uppercase , k=SuffixLength))


def generateSuffixForProfileID():
    return ''.join(random.choices(string.digits , k=PrefixLength))

def generateUniqueProfileID():
    return generatePrefixForProfileID() + generateSuffixForProfileID()
