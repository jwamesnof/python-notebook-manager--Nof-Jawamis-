#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Personal Notebook Manager:
#By Nof Jawamis

# first step - Creation of json file that contains the notes:

import json
import os
from datetime import datetime

# Define colors and styles for better UI readability - Insert Improvements section
class Style:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


MyNotes_file = "My_Notes.json"


#Second Step - design the Features:

#(1) Creates a new note and adds it to the list of notes:

def add_note(My_Notes):
    
    print(f"\n{Style.HEADER}{Style.BOLD}----- Add New Note -----{Style.RESET}")
    
    note_title = input("Enter note title: ").strip()
    if not note_title:
        print(f"{Style.RED}Title cannot be empty!{Style.RESET}")
        note_title = input("Enter note title: ").strip()
    
    note_content = input("Enter the content of the note: ").strip() 
    
    tags_input = input("Enter Tags (Please separate them by a commas): ")
    
    # Handling tags by storing them in an empty list, splitting them by a comma to get the raw pieces, and
    # stripping whitespace
    
    tags = [] 
    raw_tags = tags_input.split(",")
    for tag in raw_tags:
        clean_tag = tag.strip()
        if clean_tag:                   # Check if the tag is not empty (ignores empty strings)
            tags.append(clean_tag)
            
            
    # Using datetime to automatically set the date as per 'Insert Improvements' section
    note_date = datetime.now()
    date_format = note_date.strftime("%Y-%m-%d %H:%M:%S")
    
    new_note = {
        "title": note_title,
        "content": note_content,
        "tags": tags,
        "date": date_format
    }
    
    My_Notes.append(new_note)
    print(f"{Style.GREEN}The New Note has been added successfully!{Style.RESET}")

    
#(2) Displays all stored notes in a list, with a readable format:

def list_notes(My_Notes):
    
    print(f"\n{Style.HEADER}{Style.BOLD}------ My List of Notes ------{Style.RESET}")
    
    for index in range(len(My_Notes)):
        note = My_Notes[index]
        print(f"{Style.BLUE}{'='*40}{Style.RESET}")
        print(f"{Style.BOLD}{Style.CYAN}Note Number {index + 1}{Style.RESET}")
        print(f"{Style.BOLD}Title:   {Style.RESET}{note['title']}")
        print(f"{Style.BOLD}Content: {Style.RESET}{note['content']}")
        print(f"{Style.BOLD}Tags:    {Style.RESET}{Style.YELLOW}{', '.join(note['tags'])}{Style.RESET}")
        print(f"{Style.BOLD}Date:    {Style.RESET}{note['date']}")
    print(f"{Style.BLUE}{'='*40}{Style.RESET}")
        
    if not My_Notes:                         # we can use also: if len(My_Notes) == 0
        print(f"{Style.YELLOW}\n No notes were found!{Style.RESET}")
        


#(3) Searches notes by keyword in title or content:

def search_notes(My_Notes):
    
    keyword = input(f"\n{Style.BOLD}Enter keyword to search: {Style.RESET}").lower()
    note_found = []
    
    print(f"\n{Style.HEADER}---- Search Results for '{keyword}' ----{Style.RESET}")

    for number in range(len(My_Notes)):
        result = My_Notes[number]
        if keyword in result["title"].lower() or keyword in result["content"].lower():
            print(f"\n{Style.CYAN}Note Number {number + 1}{Style.RESET}")
            print("Title:", result["title"])
            print("Content:", result["content"])
            print("Tags:", ", ".join(result["tags"]))
            print("Date:", result["date"])
            note_found = [result]


    if not note_found:
        print(f"{Style.RED}Unfortunately no matching notes were found.{Style.RESET}")
        
            

#(4) Filtering notes by a specific tag:

def filter_by_tag(My_Notes):
    
    tag_filter = input(f"\n{Style.BOLD}Enter tag to filter by: {Style.RESET}").strip().lower()
    match_found = False
    
    print(f"\n{Style.HEADER}---- Notes tagged with '{tag_filter}' ----{Style.RESET}")
    
    for my_note in My_Notes:
        current_note_tags = my_note["tags"] #List of tags for the current note we are looking at
        for tag_note in current_note_tags:
            if tag_note.lower() == tag_filter:   # We can use the operator "in" to filter by the partial name of the tag
                match_found = True
                print(f"{Style.CYAN}* {my_note['title']}{Style.RESET} (Date: {my_note['date']})") 
                break  # We found a match! So, no need to check the rest of the tags for this note.
                   
    if not match_found:
        print(f"{Style.RED}Unfortunately no notes found with tag '{tag_filter}'{Style.RESET}")   
        

#(5) Editing an existing note from the notes list:

def edit_note(My_Notes):
    
    list_notes(My_Notes)
    
    if len(My_Notes) == 0:  #In case of empty list
        return
    
    note_number = input(f"\n{Style.BOLD}Please enter the number of the note to edit: {Style.RESET}")
    if note_number.isdigit() == False:
        print(f"{Style.RED}Invalid input. Please enter a valid number!{Style.RESET}") 
        edit_note(My_Notes)
        return
    
    else:
        note_index = int(note_number) - 1
        if note_index < 0 or note_index >= len(My_Notes):
            print(f"{Style.RED}Invalid note number. Please try again!{Style.RESET}")
            edit_note(My_Notes)
            return
        
        else:                   # 0 <= note_index < len(My_Notes):
            Note = My_Notes[note_index]
            
            print(f"{Style.BOLD}\nEditing '{Note['title']}' (leave empty to keep current title, Press Enter:){Style.BOLD}")
            new_title = input(f"New title ({Note['title']}): ")
            if new_title != "":
                Note["title"] = new_title

            
            print(f"{Style.BOLD}\nEditing '{Note['content']}' (leave empty to keep current content, Press Enter:){Style.BOLD}")
            new_content = input(f"New content: ") 
            if new_content != "":
                Note["content"] = new_content
            
            print(f"{Style.BOLD}\nEditing '{Note['tags']}' (leave empty to keep current tags, Press Enter:){Style.BOLD}")
            new_tags = input("New tags (comma separated): ")
            if new_tags != "":
                Note["tags"] = [tg.strip() for tg in new_tags.split(",")]
            
        print(f"{Style.GREEN}\nThe Note that has been chosen is updated!{Style.RESET}")
        


#(6) Deletes a selected note from the list:
    
def delete_note(My_Notes):
    
    list_notes(My_Notes)
    
    if len(My_Notes) == 0:     #In case of empty list
        return
    
    note_to_delete = input(f"\n{Style.RED}Please enter the number of the note you want to delete: {Style.RESET}")
    
    if note_to_delete.isdigit() == True:
        index_to_delete = int(note_to_delete) - 1
        
        if 0 <= index_to_delete < len(My_Notes):
            removed_note = My_Notes.pop(index_to_delete)
            print(f"{Style.YELLOW}Deleted note: {removed_note['title']} {removed_note['date']}{Style.RESET}") 
            print(f"{Style.GREEN}\nThe Note that has been chosen is deleted successfully!{Style.RESET}")
        
        else:                 #if index_to_delete < 0 or index_to_delete >= len(My_Notes):     
            print(f"{Style.RED}Invalid note number. Please select again!{Style.RESET}")
            delete_note(My_Notes)
    else:
        print(f"{Style.RED}Invalid input. Please enter a valid number!{Style.RESET}")
        delete_note(My_Notes)
        
#(7) Save the current list of notes to the JSON file:

def save_notes(My_Notes):
    
    Notes_file = open(MyNotes_file, "w")     #Write - Opens a file for writing, creates the file if it does not exist
    json.dump(My_Notes, Notes_file, indent=4)  #indent: Specifies the number of spaces for indentation to improve readability
    Notes_file.close()
    

#(8) Load notes automatically on startup from the JSON file:  

def load_notes():
    if os.path.exists(MyNotes_file):
        file = open(MyNotes_file, "r")    # "r" - Read. Opens a file for reading, error if the file does not exist
        file_read = file.read()
        file.close()
        if file_read == True:
            return json.loads(file_read)
        else:
            return []
    else:
        return []


#Third Step - Display the menu options and main loop for the application:   

# I) The main menu options:

def menu_options():
    
    print(f"\n{Style.BOLD}{Style.BLUE}****** My Personal Notebook Manager Application *****{Style.RESET}")
    print(f"\n{Style.BOLD}{Style.BLUE}*****************************************************{Style.RESET}")
    print(f" {Style.GREEN}(1){Style.RESET} Add note")
    print(f" {Style.GREEN}(2){Style.RESET} List notes")
    print(f" {Style.GREEN}(3){Style.RESET} Search notes") 
    print(f" {Style.GREEN}(4){Style.RESET} Filter by tag")
    print(f" {Style.GREEN}(5){Style.RESET} Edit note")
    print(f" {Style.GREEN}(6){Style.RESET} Delete note")
    print(f" {Style.RED}(0){Style.RESET} Save & Exit")
        

# II) The main loop:

def main():
    
    My_Notes = load_notes() 
    
    while True:
        menu_options()
        option = input(f"\n{Style.BOLD}Select your option: {Style.RESET}").strip() 

        if option == "1":
            add_note(My_Notes)
        elif option == "2":
            list_notes(My_Notes)
        elif option == "3":
            search_notes(My_Notes)
        elif option == "4":
            filter_by_tag(My_Notes)
        elif option == "5":
            edit_note(My_Notes)
        elif option == "6":
            delete_note(My_Notes)
        elif option == "0":
            save_notes(My_Notes)
            print(f"{Style.GREEN}Notes saved. \nExiting... Goodbye and see you soon!{Style.RESET}")
            break
        else:
            print(f"{Style.RED}Invalid choice. Please try again.{Style.RESET}")

if __name__ == "__main__":
    main()
    

     


# In[ ]:




