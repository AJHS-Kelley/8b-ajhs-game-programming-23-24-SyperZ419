# DNA Replication Game, Ryan Kelley, v0.1

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

dna = genDNA()
print(dna)