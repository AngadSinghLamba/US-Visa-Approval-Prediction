import os
from pathlib import Path

project_name="us_visa"

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configration/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",cond
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
    "test.py"


]
# looping through this list
for filepath in list_of_files:
# converting everything to the "Path" so that 
#the code can execute in any os windows or mac. 
#Since we have given forward slash and in windows for creating 
#any folder we see backward slash. 
#The Path class will detect which OS you are using and convert the code for that os. 
#>>> from pathlib import Path
#>>> path="test/test.py"
#>>> Path(path)
# output- WindowsPath('test/test.py')

    filepath = Path(filepath)

#f"{project_name}/components/- This is a folder
#__init__.py"- This is a file as file having extension.py
# So we need to seprate out folder and file
# it will return two tuples on left side folder and on right file
# from pathlib import Path
# path="folder/file.py"
# Path(path)
# WindowsPath('folder/file.py')
# import os
# os.path.split(path)
# ('folder', 'file.py')
    
    filedir, filename = os.path.split(filepath)
# Inside filedir I can have all the folders name
# Inside Filename i will have all the filenames
# if file directory is not empty it will create a directory

    if filedir != "":

# (not os.path.exists(filepath)): This condition checks if the file specified by filepath doesn't exist.
# (os.path.getsize(filepath) == 0): This condition checks if the file exists but has a size of 0 bytes, indicating it's empty.
# If either of these conditions is true, the code enters the if block:
# with open(filepath, "w") as f:: This opens the file specified by filepath in write mode ("w"). If the file doesn't exist, it will be created. If it exists, its contents will be truncated (emptied). The file is opened using a with statement, ensuring it's properly closed after use.
# pass: This is a placeholder statement that does nothing. It's used here because Python requires an indented block after the with statement, even if there's no code to execute.
# If the conditions are false (i.e., the file exists and is not empty), the code prints a message indicating that the file is already present.    
        
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
# Create file if file doesn't exist and "W" will give write acess
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")

        