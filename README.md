# Python intro
## Why Python
### Python use cases
#### Python set up with Pycharm
##### Python variables
- Env Testing`print(""hello world)`
```python
first_name=input("Enter your first_name")
last_name=input("Enter your last_name")
dob=input("Please , enter your DOB:")
course_name=input("Please, Enter your course name :")
uk_resident =input ("Are you a resident of UK ?")
print(first_name + last_name )
print(dob)
print(course_name)
print(uk_resident)
```
# Python Variable?
- To store user data-hard code the data- any other data
```python
first_name="Meghana"# - this is String
last_name = "Aenugu"
DOB =99 #-Int
travel=14.4 #-float
salary = 40000 #-int
gross_salary = "salary+ travel"

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
 

# 

```

# How to setup git+github using SSH key pair
- Install Git in your local machine
- Create a github account 
- We can connect local host to the github by twoways
    - SSH (Secure Shell)
    - HTTPS
- Step 1 :Generate ssh keys on localhost
- Step 2 :Keep the private key on local host inside the .ssh folder
- Step 3 :Copy the public key into your repository on github
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
