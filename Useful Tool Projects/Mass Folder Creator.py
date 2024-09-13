####################
# Mass Folder Generator
# Alex Bevan - UP2198095
# Disc: A mass folder generator for when I need to mass produce numerically organised folders in weeks for example
####################

# Imports
import os


base_Name = "week "

for i in range(1, 23):
    folder_name = f"{base_Name}{i}"
    folder_path = os.path.join('C:/Users/alexm/Downloads/Year 1 Materials - UOP CYBER/Cyber Security And Forensic Essentials', folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_name}")
    else:
        print(f"Folder '{folder_name}' already exists.")


# Set a base name for the folder to be called - excluding the number remembering spaces or dashes for number
# Set the range according to how many folders are required, eg. 9-13 gives 9,10,11,12 and stops before making 13
# Checks if the folder path exists, if it does then the file exists and is not made, if not then the file is made
