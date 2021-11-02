"""
This program is intended as a tracer round for the flow of control as a user
of a social media account makes, deletes, and edits posts. For testing,
a user should be able to enter their user name, change which user name they
are currently using, add a post using their current user name, remove a post
made under their current user name, edit a post made under their current user 
name, print the contents of the list of posts, or quit the program.
"""

#This line of code tells the Python interpreter that it needs to reference the 
#post.py file in order to run the rest of the code in this file.
from CSE_322_post import Post

# How will you save the posts you will create? Review the for loop near the end of this code for an answer.

# What is the user name they want to use?
userName = raw_input("Hello, what would you like your username to be? ");
# Welcome user to the program 
userName=Post(userName, "");
#Store initial user input in a variable identified by user_input

#You may need to use this statement again to complete the activity.
messageList = [];
user_input = "";
def askQuestion():
    global user_input;
    user_input = raw_input("""What would you like to do?
    "add" - Add a post to the archive
    "remove" - Remove a post from the archive
    "change user" - Change the user name associated with any future posts
    "print" - Display the current up to date list of all posts
    "quit" - End the program
    """)


#Where are we posting to in this code. Review the end of this code for an answer.

#What is the user name they want to use?

#This while loop ensures that the program will continue executing statements
# at the next indentation level until the user types "quit" in response to the 
# prompt.

while user_input != "quit":                                                 #Start Loop

    #code for adding a post here
    if user_input.lower() == "add":                                         #If response is add
        print("Add");
        message = raw_input("What message would you like to store? ");
        post = Post(userName, message);
        messageList.append(post)                                            #Add Items to list with name
    elif user_input.lower() == "remove":                                    #If response is remove
        print("Remove");
        removeIndex = input("Which index would you like to remove? ")
        if type(removeIndex) == int and removeIndex <= len(messageList) -1 and removeIndex >= 0:
            del messageList[int(removeIndex)]                               #Delete index given
        else:
            print("That action cannot be performed with that input. ")      #Cannot delete with strings and floats
    elif user_input.lower() == "change user":                               #If response is change user
        print("Change");
        userName = raw_input("What would you like your new name to be? ");  #Sets name to new response
    elif user_input.lower() == "print":                                     #If response is print
        print("Print");
        print(messageList)
        #for post in messageList:
        index = 0;
        for post in messageList:
            global messageList;
            print (str(int(index)) + ":" + str(messageList[int(index)]))    #Prints each item in messageList
            index += 1;
            #get_post_id(self)
    elif user_input == "":                                                  #If response is blank
        print("You did not type anything")
    else:
        print("Not a choice")                                               #If response is not blank or correct
    askQuestion();
    
    #code for removing a post here
    #code for changing the current user here
    #code to display all posts, you can use the code in comments below
    
	# this for loop will print the index of the element in the list
	# and the element itself
    """
    for post in post_list:
        print str(index), ":" ,  post
		index += 1
    """
    #code to inform the user that their input was not valid here
    
#Code that will allow the user to make a new selection
#This code will finish the loop