import os 
import glob
from pathlib import Path

direcPath = Path(".") # Getting the working Directory
count = 0 
# counting the text files in the present directory
for file in direcPath.glob('*.txt'):
    count += 1

print(count)



