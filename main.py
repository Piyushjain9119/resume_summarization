#importing pypdf for coverting pdf to text and re for usinf regular expressions
from PyPDF2 import PdfReader
import re


#reading the pdf 
reader = PdfReader("seema.pdf")  
number_of_pages = len(reader.pages)
page = reader.pages[0]
#converting pdf to text file 
text = page.extract_text()

# searching the name of the user from the pdf 
name_pattern = re.compile(r'\b[A-Za-z]*\b')
names = name_pattern.findall(text)
user_name = names[0]+" "+names[2]


# searching the phone number from the pdf 
phone_number_pattern = re.compile(r'\b(?:\+\d{1,2}\s?)?(?:(?:\(\d{1,4}\))|\d{1,4})[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b')
phone_numbers = phone_number_pattern.findall(text)
phonenumber=phone_numbers[0]

# function to extract the email address of the user
def getemailaddress(string):
    r=re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
email = getemailaddress(text)[0]



#using keyword matching for identifying the skills 
def extract_skills_with_keywords(text, keywords):
    matched_skills = [keyword for keyword in keywords if keyword.lower() in text.lower()]
    return matched_skills
#we can also change the list to the required skills we want
skills_keywords = ["Python", "Java","c++","data visualization","data modeling","communication skills","data analysis","etl","power query","core java","c#","reactjs","nodejs","angularjs","mernstack developer","android development" ,"web development", "software engineering",'numpy','pandas','Power BI','Matplotlib','Data Cleaning']

matched_skills = extract_skills_with_keywords(text, skills_keywords)
user_skills = matched_skills

# creating a string formate to breifly explain the name , skills ,email and number 
summary=(f"Name:{user_name}\nHave the skills like {user_skills}, \nand have optimal/required knowledge about all the skills listed above .\nU can contact {user_name} on -\nemail :-{email} \nnumber :-{phonenumber}")

# Specify the file path
file_path = f"{user_name}.txt"

# Open the file in write mode ('w')
with open(file_path, 'w',encoding='utf-8') as file:
    # Write the summary content to the file
    file.write(summary)
# saving the text file as user name .text
print(f"Summary has been successfully written to {file_path}")

