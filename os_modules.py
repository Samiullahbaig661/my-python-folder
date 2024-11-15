#############################################
# import os
# if not os.path.exists("bekar"):
#     os.mkdir("bekar")
# for i in range (1,101):
#         os.mkdir(f"bekar/chal nikal {i}")

#############################################

# import os

# for i in range (1,101):
#         os.rename(f"bekar/chal nikal {i}",f"bekar/sorry bro {i}")

#############################################

# import os
# folders = os.listdir("bekar")
# print(os.getcwd())
# os.chdir("/sami work")
# print(os.getcwd())

# for folder in folders:
#     os.rmdir()
#     print(folder)
#     if os.listdir(f"faltu folder hai yeh/bekar/{folder}") :
#      print(f"found : ja ja ke ash kr {os.listdir(f"faltu folder hai yeh/bekar/{folder}")}")    

#############################################

# import os
# folders = os.listdir("bekar")
# print(os.getcwd())
# os.chdir("/sami work")
# print(os.getcwd())

# for folder in folders:
#     os.rmdir()
#     print(folder)
#     if os.listdir(f"faltu folder hai yeh/bekar/{folder}") :
#      print(f"found : ja ja ke ash kr {os.listdir(f"faltu folder hai yeh/bekar/{folder}")}")    

#############################################

# import os 
# folders = os.listdir("bekar")
# for folder in folders:
#     print(folder)

#############################################

# import os

# def remove_tree(directory):
#     for item in os.listdir(directory):
#         item_path = os.path.join(directory, item) 

        
#         if os.path.isdir(item_path):
          
#             remove_tree(item_path)
#         os.remove(item_path)
#     os.rmdir(directory)
# parent_dir = "bekar"
# folders = os.listdir(parent_dir)
# for folder in folders:
#     folder_path = os.path.join(parent_dir, folder)  
#     if os.path.isdir(folder_path):
#         remove_tree(folder_path)
#         print(f"Removed directory: {folder_path}")

# print("All directories and their contents have been removed.")

#############################################




# import os 
# os.makedirs("sami-12/sami21")
# folder_path = "D:\python programs\sami-12\sami21"
# os.removedirs(folder_path)
# print(f"The folder '{folder_path}' has been deleted.")
# print(os.listdir())


#############################################



# import os
# os.rename("list_of_list.py" , "list.py")
# print(os.listdir())



#############################################


# import os
# from datetime import datetime
# time = (os.stat("os_modules.py").st_mtime)
# print(datetime.fromtimestamp(time))


#############################################


import os 
for dirpath , dirname , filename in os.walk('D:\python programs'):
    print("current path : ",dirpath)
    print("Diretories : " )





























