import os 
import glob
from pathlib import Path

direcPath = Path(".") # Getting the working Directory
count = 0 
# counting the text files in the present directory
for file in direcPath.glob('*.txt'):
    count += 1

print("\n")
print(f"You are having {count} number of files in your current {direcPath.resolve()} \t")
print("\n")

inp = input("Want to Rename the files: Yes / No ")
print("\n")
print("\n")

if inp == 'y' or inp == "YES" or inp == "Y" or inp == "yes" or inp == "Yes":

    for file in direcPath.glob('*.txt'):

        print(f"This is your {file.name} file, Hit N if you don't want to cahnge the file \t")
        print("\n")

        file_name = input(("Enter the name of File for this Text or (N for Skip: )\t"))

        if file_name.strip().upper() != "N":
            if not file_name.endswith('.txt'):
                file_name += '.txt'
            
            new_path = file.parent / file_name
            
            while new_path.exists():

                file_name = input((f"{file_name} already Exists please choose another name (N for Skip: )\t"))

                if file_name.strip().upper() == 'N' or file_name.strip().lower() == 'n':
                    break

                if not file_name.endswith('.txt'):
                    file_name += '.txt'

                new_path = file.parent / file_name

            file.rename(new_path)
        else:
            print("Skipped! ")
            continue
    print("Listed or Updated files are \t")
    for file in direcPath.glob('*.txt'):
        print(f"{file.name} \t")
else:
    print("If you want to Rename your files just say Yes! BYE BYE 😁 ")