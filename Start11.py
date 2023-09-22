from mailtm import Email
import re
import requests
import shutil
import os
import pyperclip

def End():
     print("Crack was success!");

def listener(message):
    text = message['text'] if message['text'] else message['html']
    match = re.search(r'Activate 30-Day Trial\n(\[https://.*?\])', text)
    if match:
        link = match.group(1).strip('[]')
        response = requests.get(link)
        End()

def GetMail():
	test = Email()

	test.register()
	pyperclip.copy(str(test.address))
	print("\nIn StarDock program Enter this Email: " + str(test.address) + " (it was copy to clipboard)")

	test.start(listener)
	print("\nWaiting for emails...")

def deleteDir():
    program_data_dir = 'C:\\ProgramData\\Stardock\\'
    
    if os.path.exists(program_data_dir):
        print("\nProgram data directory found, deleting all subdirectories...")
        
        for folder_name in os.listdir(program_data_dir):
            folder_path = os.path.join(program_data_dir, folder_name)
            
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path)
                print(f"Deleted {folder_path}")
        
        print("\nAll subdirectories in the program data directory have been deleted.")
        GetMail()  
    else:
        print("\nCannot find the program data directory.")
        GetMail()  

deleteDir()