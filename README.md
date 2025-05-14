# IDORLesson
This is a project that investigates the IDOR vulnerability and how to resolve it. IDOR stands for Insecure Direct Object Reference.
# Donwload and Install Python3 if needed
To download Python3 you can use, https://www.python.org/downloads/. It is the offical webpage for the language, and ensures you are downlaoding an authentic version of the language.

This webpage provides some guidance on how to install the downloaded software. If you need more information you can refer to, https://python.land/installing-python.

There are several online resources on this, if you want to do it a different way you are more than welcome to.
# Run IDORissue First
There are two project folders called IDORissue and IDORFix. The IDORissue folder has everything you need for the project version with the IDOR vulnerability. 

The IDORFix version removes IDOR found in IDORissue. You will not need to use this if instructions are followed as you will learn how to remove the issue.

It is there in case you run into issues and do not want to spend any more time figuring out how to remove the IDOR vulnerability. 

1. Download both IDORissue and IDORFix just in case. If you are feeling confident then you can donwload just IDORissue.
2. Save the file in a location you can easily access and remember.
3. Open Terminal or Windows Terminal depending on what system you have.
4. Move to that directory by either using the cd command as needed or the chdir command.
5. Finally run python3 app.py or py -3 app.py depending on what system and shell you are using.
6. Open up Google Chrome (preferred) or another browser.
7. Type http://localhost:5000/
8. From there it will be obvious what you need to do next.

NOTE: While I am sure you can run python 2 instead of 3, I am running the newest version of Flask. You may run into issues because of this. 
Also using a different web browser than Chrome may cause issues as Chrome is the browser I tested this application most exstensively on.
# Run IDORFix If Needed
IDORFix follows the same steps to run. It is important to not run both IDORFix and IDORissue at the same time. 
