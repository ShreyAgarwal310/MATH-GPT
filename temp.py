import os

with open("requirements.txt") as i: # open file for reading, i = input file 
  with open("temp", "w") as o: # open temp file in write mode, o = output 
     for l in i: # read line by line  
         o.write("'%s',\n" % l[:-1]) # concate ' and text 
          #       ^  ^ added `'` for each line  
os.remove("requirements.txt") # delete old file. Note:this is not needed in postfix system 
os.rename("temp", "requirements.txt")  # rename file