import os


folders = os.listdir("database_single_number/")

print(folders)


for i in range(len(folders)):
    os.rename("database_single_number/Num_"+str(i), "database_single_number/num_"+str(i))