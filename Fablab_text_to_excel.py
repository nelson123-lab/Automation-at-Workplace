import pandas as pd
import os
import datetime

# specify the folder path
folder_path = "C:/Users/NELSON JOSEPH/Desktop/New Folder"

# create an empty list to store file names
file_names = []

# loop through all the files in the folder
for filename in os.listdir(folder_path):
    # add the file name to the list
    file_names.append(filename)

# print the list of file names
print(file_names)

with open("C:/Users/NELSON JOSEPH/Desktop/info.txt", "r") as file:
    contents = file.readlines()
data = {}
for i in contents:
    if i.startswith("Name:"):
        Name = i.split(":")[1].strip()
        os.mkdir("C:/Users/NELSON JOSEPH/Desktop/" + Name)
        data["First Name"], data["Last Name"] = Name.split(" ", 1)[0].strip(), Name.split(" ", 1)[1].strip()
    elif i.startswith("Mavs email:"):
        data["Mavs email"] = i.split(":")[1].strip().lower()
    elif i.startswith("Mavs ID:"):
        data["Mavs ID"] = i.split(":")[1].strip()
    elif i.startswith("Ticket No:"):
        data["Job Ticket#"] = i.split(":")[1].strip()
        pass
now = datetime.datetime.now()
date, time = now.strftime("%m/%d/%Y %H:%M").split(" ")
data["Consult Date"], data["Consult Time"] = date, time
data["File_name"] = file_names[0]

index = [0]
df = pd.DataFrame(data, index= index)

# # Write the DataFrame to an Excel file
df.to_excel('C:/Users/NELSON JOSEPH/Desktop/example.xlsx', index=False)

with open("C:/Users/NELSON JOSEPH/Desktop/info.txt", "w") as file:
    file.truncate()

lines = ["Name:", "Mavs email:", "Mavs ID:", "Ticket No:"]

with open("C:/Users/NELSON JOSEPH/Desktop/info.txt", "a") as file:
    for line in lines:
        file.write(line + "\n")



import shutil

# specify the source file path
source_path = "C:/Users/NELSON JOSEPH/Desktop/New Folder/"+ file_names[0]



# move the file from source path to destination folder path


A = input("Have you already 3d printed in Fablab before?")
if A == "Y" or A == "y":
    date = date.replace('/','-')
    
    #Check for the folder already exist
    #If exists, append the 'Name' with datetime.datetime.now(datetime.timezone.utc) which appends current date time.
    os.mkdir("C:/Users/NELSON JOSEPH/Desktop/" + Name + "/" + date)
    
   
    # specify the destination folder path
    #Same naming can be used as above 
    destination_folder_path = "C:/Users/NELSON JOSEPH/Desktop/" + Name + "/" + date
    shutil.move(source_path, destination_folder_path)
else:
    # The 'Name'string can be appended with datetime.datetime.now(datetime.timezone.utc) which appends current date time.
    destination_folder_path = "C:/Users/NELSON JOSEPH/Desktop/" + Name
    shutil.move(source_path, destination_folder_path)

