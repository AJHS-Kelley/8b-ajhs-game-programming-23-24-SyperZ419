# DNA Replication Game, Ryan Kelley, v0.4

# Import Entire Modules -- Get the whole toolbox.
import time, datetime

# Import Specific Methods -- Get the specific tool.
from random import choice

# Store the DNA Bases
dnaBases = ["G", "A", "C", "T"]

# Game Functions
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer for the number of bases to create.\n"))
    dnaSequence = ""
    
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    
    return dnaSequence


def doTranscription(dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print('Please remember, in the RNA sequence, U pairs with A from the DNA sequence.\n')
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan. 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press Enter.\n").upper()
    #if "augc" or "AUGC" not in rnaSequence:
        #print("The input sequence does not have correct RNA bases.")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can referance items with the index
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
    # Tuples CAN have duplicate values

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("The sequences are different lengths and cannot match.\n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("Error. Bases do not match.")

    return isMatch

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 3.0:
        score += 30
    elif rnaTime < 5.0:
        score += 25
    elif rnaTime < 10.0:
        score += 20
    elif rnaTime < 15.0:
        score += 15
    elif rnaTime < 20.0:
        score += 10
    else:
        score += 5
    
    scoreMulti = 0.0
    if len(rnaSequence) >= 35:
        scoreMulti = 5.0
    elif len(rnaSequence) >= 30:
        scoreMulti = 4.5
    elif len(rnaSequence) >= 25:
        scoreMulti = 4.0
    elif len(rnaSequence) >= 20:
        scoreMulti = 3.5
    elif len(rnaSequence) >= 15:
        scoreMulti = 3.0
    elif len(rnaSequence) >= 10:
        scoreMulti = 2.0
    elif len(rnaSequence) >= 5:
        scoreMulti = 1.0
    elif len(rnaSequence) >= 4:
        scoreMulti = 0.5
    elif len(rnaSequence) >= 3:
        scoreMulti = 0.25
    else:
        scoreMulti = 0.125
    score *= scoreMulti
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: float, score: int) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" + fullName + ".txt"
    saveData = open(fileName, "a")
    # File Nodes
    # "x" mode -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR
    # "w" mode -- CREATE FILE, IF FILE EXISTS, OVERWRITE IT
    # "a" mode -- CREATE FILE, IF FILE EXISTS, APPEND TO IT
    saveData.write(f"DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    saveData.write(f"Score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close()

dna = genDNA()
rna = doTranscription(dna)
if verifySequence(dna, rna[0]):
    score = (calcScore(rna[0], rna[1]))
    saveScore(dna, rna[0], rna[1], score)