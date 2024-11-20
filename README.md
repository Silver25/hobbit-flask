![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Silvio Martinec,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

------

## Release History / Commits

Start with installing the Flask first [ pip3 install Flask ] in IDE  
Creating main file with code for App with command "Touch" [ touch run.py ]  
Generate requirements.txt file with all the packages project depends on [ pip freeze > requirements.txt ]  
In the new file the first thing to do is to import the Flask class  
Creating an instance of this class, variable called 'app'  
Creating the route decorator to tell Flask what URL should trigger the function that follows  
"import os" from the standard Python library to get application running  
"python3 run.py" to run app and "Ctrl+C" to stop the app  
Up arrow &uarr; on keyboard to display last entry (restart)  
Import the render_template() function from Flask, for the app to be able to open HTML file  
Created directory called "templates" where needed HTML file "index.html" is based  
Add basic code to index.html to run in browser as a home page  
Duplicate index.html to create about.html  
Rendering HTML and Routing [ Hello Flash walk through ] links  
Create new Contact page.  
Create Base.html to avoid duplicate of html code through pages - Template Inheritance  
Create new Careers page with block elements to test update of content to all pages  
Styling with the help of Bootstrap themes [ https://startbootstrap.com/ ]  
Create Static folder for files that don't change [ JavaScript, image files, CSS files ]  
Through VS Code Terminal change directory path to static  
Terminal 'wget' command to download and unpack bootstrap zip file  
Unzip bootstrap file - get clean-blog template  
Extract CSS, IMG, JS, Mail, SCSS and Vendor folders, delete other + zip  
Use body code from bootstrap template and import in base.html, adjust with url_for function  
Updating code with custom details/elements  


## Gitpod Reminders

### Comments

HTML &lt;!-- -->  
CSS  /*  */  
Python  #  or  ''' multiline    

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type: `python3 -m http.server`


To run a backend Python file, type `python3 run.py` if main Python file is named `run.py`, of course.

Refresh browser: CTRL + Shift + R [ clear cache ]


By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_