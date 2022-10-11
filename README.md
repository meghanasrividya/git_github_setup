# Python intro
- Python is a popular programming language.
- Python can be used on a server to create web applications.
## Why Python
![img_1.png](img_1.png)
### Python use cases
- web development
- DevOps
- data science
- data analysis
- machine learning
- finance industry
### Python variables
- Variables are containers for storing data values.
- Python has no command for declaring a variable.
- A variable is created the moment you first assign a value to it.
### Example program to take input from the user and print to console.
```python
# Get user first_name and last_name
first_name=input("Enter your first_name") # Takes the input from the user and stores in the variable first_name
last_name=input("Enter your last_name") # Takes the input from the user and stores in the variable last_name

# display the names in the line
print(first_name + last_name )
dob=input("Please , enter your DOB:") # Takes the input dob from user
print(dob)
# course name
course_name=input("Please, Enter your course name :")
print(course_name)
# UK_resident
uk_resident =input ("Are you a resident of UK ?")
print(uk_resident)
```
### Output of the console is 
![img_2.png](img_2.png)
### Python Comments
- Comments can be used to explain Python code.
- Comments can be used to make the code more readable.
### Python Data Types
- Built-in Data Types
- In programming, data type is an important concept.
- Variables can store data of different types, and different types can do different things.
- Python has the following data types built-in by default, in these categories:
  - Text Type:	str
  - Numeric Types:	int, float, complex
  - Sequence Types:	list, tuple, range
  - Mapping Type:	dict
  - Set Types:	set, frozenset
  - Boolean Type:	bool
  - Binary Types:	bytes, bytearray, memoryview
  
# How to setup git+github using SSH key pair
- Install Git in your local machine
- Create a github account 
- We can connect local host to the github by twoways
    - SSH (Secure Shell)
    - HTTPS
- Step 1 :Generate ssh keys on localhost
    - Open git bash terminal
        - Go to .ssh directory using the command cd ~/.ssh 
        - If the .ssh directory does not exist , create it using the command mkdir .ssh
        - Now go to the directory using the command cd ~/.ssh
        - To generate the key use the command ssh-keygen -t rsa -b 4096 -C "your@email.com"
        - It will ask to enter the file to save the key.Don't give any file name, just click enter and enter
        - Give command  ls to list the files in .ssh
        - We will have key-pair (2 files) id_rsa ,id_rsa.pub. 
           - One with .pub extension is public key
           - One without .pub extension is called private key
- Step 2 :Keep the private key on local host inside the .ssh folder
- Step 3 :Copy the public key into your repository on github
     - Use the command cat id_rsa.pub to open the public key file.
          - Once opened,copy the contents of the file 
          - Go to the Github account settings--> SSH and GPG Keys-->Click on New SSH Key-->Give some title and paste the key and click on "Add SSH Key".
          - It will ask the passwork to confirm 
- After doing the above three steps we can push anything to Github from our local machine and we can clone anything from Github to pur local machine.
![img.png](img.png)
## Points to be noted
- Always open Pycharm as administrator.
- Make sure you copy the public key without spaces and paste into repository
### Steps to push to github from local machine
- create README.md file in pycharm in local machine
- Add the notes 
- Use the below commands to push into the github
- git init
- git commit
- git commit -m "first commit"
- git add .
- git branch -M main
- git remote add origin git@github.com:meghanasrividya/git_github_setup.git
- git push -u origin main
### Git and GitHUb
- add changes to our Git -Hub repo - the changes we made on localhost
-  `git add filename` or `git add .`
-  `git commit -m "new markdown  guide added"`
- now let's send this new data to github
- `git push -u origin main`
- `git status`
- git add `.gitignore` then add all dependencies that you do not want to push