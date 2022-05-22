import os

# Use Relative PATHS
# CHANGE TEMPLATE PATH IN script/NavHandler.py

INPUT_FOLDER="./"
OUTPUT_FOLDER="testordner/"

## IMPORTANT u have to add "/" 
## if u copy relative path you get only "testordner"

try: 
    from NavHandler import TemplateFile, FileHandler
except (ModuleNotFoundError, ImportError):
    print('\nProblem mit Modulimport bitte schau in "scripts/main.py" und den Import unter "imports" an.\n')
    raise

def read_files():
    files = os.listdir(INPUT_FOLDER)
    html_files = []
    for file in files:
        if file.endswith(".html"):
            html_files.append(file)
    return list(html_files)

def main():
    template = TemplateFile()
    html_dateien = read_files()
    print("\nDeine Template liegt unter: {}\n".format(template.template_path))
    print("Files u wanna change: \n{} ".format(html_dateien))
    
    user_input = input("\nKorrekt? (y/n): ").lower()
    if user_input != "y":
        print('Passe die Template in "script/NavHandler.py" an.')
        print('class TemplateFile() -> TEMPLATE_PATH')
        print(10*"-")
        print("Programm wird beendet")
        exit()
    else: 
        for file in html_dateien:
            print(INPUT_FOLDER+file)
            FileHandler(INPUT_FOLDER+file, OUTPUT_FOLDER+file, file)
        
if __name__ == "__main__":
    pass
    #main()
    
#IF ure ready to go and did a BACKUP then u can remove "pass" and "#" in line 46
        
    
    

