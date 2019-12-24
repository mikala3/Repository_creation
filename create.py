from click._compat import raw_input
from webbot import Browser
import getpass
import sys
import os

test = "test"
print("this is \"%s\"" % (test))
#move to directory where projects is stored
PATH = "C:\\Users\\Mikael\\PycharmProjects\\"
os.chdir(PATH)

#create dir for new project, if
if not os.path.exists(PATH+str(sys.argv[1])):
    os.makedirs(PATH+str(sys.argv[1]))
    os.chdir(PATH+str(sys.argv[1]))
    os.system('git init')
    try:
        if(sys.argv[1]):
            web = Browser()
            url = "https://github.com/login"
            username = raw_input("Type in your username for github : ")
            password = getpass.getpass("Type in your password for github : ")
            web.go_to(url)
            web.type(username, into='login', id='login_field')
            web.type(password, into='password', id='password')
            web.click('Sign in')
            web.go_to("https://github.com/new")
            web.type(str(sys.argv[1]), into='respository[name]', id='repository_name')
            web.click('private')
            web.click('Create repository')
            web.quit()
            web.stop_client()
            os.system("git remote add origin https://github.com/"+str(username)+"/"+str(sys.argv[1])+".git")
            os.system("type nul > "+"README.md")
            os.system("git add .")
            message = "initial commit"
            os.system("git commit -m \"%s\"" % (message))
            os.system("git push -u origin master")
    except IndexError:
        print("Need an argument, type the name of the repository")
else:
    print("The projectname already exists")