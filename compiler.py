f = open("code.no", "rt")
contents = f.readlines()
print(contents)

# PRE-PROCESSOR
# TO-DO

# TOKENISER
types = {
    "nummer": 0,
    "fraksjon": 0
}

def printToFile(lineno, line, place, word, type):
    print("%04d %s" % (lineno, line))
    print("%s%s" % (place*" ", len(word)*"^"))
    print("---> %s" % (type))
    print("%s" % (40*"-"))

def parseWord(lineno, no, line, words, type):
    place = 5
    noTemp = no
    while noTemp > 0:
        place += len(words[noTemp-1]) +1
        noTemp -= 1

    if type == "Newline":
        printToFile(lineno, line, place-1, " ", type)
        return

    word = words[no]
    printToFile(lineno, line, place, word, type)
    return

def parseLine(lineno, line):
    lineNoEndl = line.split('\n')[0]
    words = lineNoEndl.split(" ")
    charNo = 5

    # Definition
    if (words[0] in types.keys()):
        parseWord(lineno, 0, lineNoEndl, words, words[0])
        parseWord(lineno, 1, lineNoEndl, words, "Identifier("+words[0]+") "+ words[1])
        parseWord(lineno, 2, lineNoEndl, words, words[2])
        parseWord(lineno, 3, lineNoEndl, words, "Literal("+words[0]+") "+ words[3])
        parseWord(lineno, 4, lineNoEndl, words, 'Newline')
    
    # for no, word in enumerate(words):
    #     result = parseWord(word)
    return 0

for no, line in enumerate(contents):
    parseLine(no, line)
print("EOF")

# PARSER

# CODE GENERATOR

# LINKER


