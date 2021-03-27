
def wordCount():
    
    file = open("/Users/JasirDonte/Documents/infile.txt","r")  
    file_single_line = file.readlines()
    word_count = 0
    for x in file_single_line:
        line_array = x.split(" ")
        word_count = len(line_array) + word_count
    return word_count
    
print("this file contains:", wordCount(), "words")

