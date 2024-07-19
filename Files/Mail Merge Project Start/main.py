#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp 


PLACEHOLDER = "[name]"
# C:\Users\Dsam8\OneDrive\Documents\Python Scripts\Udemy\Practice_questions\Files
with open("/Users/Dsam8/OneDrive/Documents/Python Scripts/Udemy/Practice_questions/Files/Mail Merge Project Start/Input/Names/invited_names.txt","r") as file:
    names = file.readlines()
    
with open("/Users/Dsam8/OneDrive/Documents/Python Scripts/Udemy/Practice_questions/Files/Mail Merge Project Start/Input/Letters/starting_letter.txt","r") as letter:
    letter_content = letter.read()
    
    for name in names:
    
        striped_name = name.rstrip("\n")
        new_letter = letter_content.replace(PLACEHOLDER,striped_name)
        
        with open(f"/Users/Dsam8/OneDrive/Documents/Python Scripts/Udemy/Practice_questions/Files/Mail Merge Project Start/Output/letter_for_{striped_name}","w") as Complete_letter:
    
            Complete_letter.write(new_letter)