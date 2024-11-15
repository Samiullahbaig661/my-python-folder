# f= open("my_file2.txt", "r")
# while True:
#     line = f.read()
#     if not line :
#         print("finish")
#         break
#     print (line)



# f = open("my_file2.txt", "r")

# while True:
#     line = f.readline()
 
  
    
#     if not line :
#         print("finish")
#         break
#     names = line.split(",")

#     for i in range(len(names)):
#         m2 = line.split(",")
        
#         print(f"this is your marks {names[i]} maths : {m2[0]} physics : {m2[1]} chemistry : {m2[2]}") 
    


# # Open the file for reading
# f = open("my_file2.txt", "r")

# # Read the first line to get the names
# names = f.readline().strip().split(",")

# # Loop over the remaining lines for marks
# for idx, line in enumerate(f):
#     marks = int(line.strip().split(","))  # Split the marks for the current line

#     # Print the marks for the corresponding name
#     print(f"this is your marks {names[idx]} maths : {marks[0]} physics : {marks[1]} chemistry : {marks[2]}")

# f.close()  # Close the file after processing




# file = open("my_file2.txt", "r")
# i = 0
# while True:
#     i = i +1 
#     line = file.readline()
#     if not line :
#         print("Finish")
#         break 
#     m1 = line.split(",")[0]    
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]  
#     print(f"The marks of student {i} is math : {m1}  pst : {m2}  physics : {m3}")
#     print(line)





f = open("sami.txt" , "rb")
line = ['sami','ustad','anwar']

sami = f.readline()
for lin in line:
 print(f"hi {lin}")
f.close()
