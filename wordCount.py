 # function to count words in a file and handle exceptions.

def countWordsFile(filename):
    try: 
        with open(filename, "r")as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return ("File not found. please check the file path and try again.")
    
    except Exception as e: 
        return f"An error occurred: {e}"
    

#main program
if __name__ == "__main__":

    print(" Hey there! Welcome to Word Count by Babyface Mokoena.\n")
    filename= input("Enter the file path: ")
     
    wordCount = countWordsFile(filename)
    print (" Word count:", wordCount)