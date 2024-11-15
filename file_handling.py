# reading a file 
# f= open("myfile.txt","w")
# sami = f.write("match_case.py")
# print(sami)``
# f.close()

# Writing a file 
# f= open("my_file2.txt","rb")
# sami = f.read()
# print(sami)
# f.close()


# f= open("my_file2.txt","a")
# sami = f.write("\nAlhamdullilah ap btain asad bhai bhi bikul thek thak hain ")
# f.close()


with open ("my_file2.txt","a") as f:
    f.write("sami bhai python course acha ja raha hai")
    f.write("\nap btao kab khatam hu raha hai yeh course")
    f.write("\nbas yr jaldi hi khatam hu jae ga yeh")
# First write operation with try-except




# try:
#     f = open("my_file2.txt", "a")  # Open file in append mode
#     sami = f.write("\nAlhamdullilah ap btain asad bhai bhi bikul thek thak hain")
#     f.close()
# except Exception as e:
#     print(f"An error occurred: {e}")

# # Second write operation using 'with' and proper handling of 'try-except'
# try:
#     with open("my_file2.txt", "a") as f:  # Open file using 'with' in append mode
#         f.write("\nAlhamdullilah ap btain asad bhai bhi bikul thek thak hain")
# except Exception as e:
#     print(f"An error occurred: {e}")




