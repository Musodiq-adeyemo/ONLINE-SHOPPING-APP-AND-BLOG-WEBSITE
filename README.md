# ONLINE SHOPPING STORE AND BLOG WEBSITE
## CONTENT
### Title
### Introduction 
### Project Environment
### Installation
### Folder Creation
### File Creation
### Authentication and Authorization
### Jinja2 Template
### What i learned
### Challenges
### Conclusion

# TITLE:
# ONLINE SHOPPING STORE AND BLOG WEBSITE.

# INTRODUCTION :
This project is an online shopping store and also a Blog website.
The store side contains items that are available for sale and the blog side is used to advertise the items in form of a post or article which as well can be published.
This website is fully authenticated and also a token  is required for users' full authorization to the website. 
This website is built using fast API framework and jinja2 template is used for the frontend side of this website.

This project " ONLINE SHOPPING STORE AND BLOG WEBSITE" allows anyone visiting the site to be able to view all blog posts but only restricted to some web pages when not signed in and will be able to view all web pages when logged in .
The homepage which is the landing page of the website contains all the lists of articles written by different authors. The website contains many web pages, user authentication, and authorization with a well-structured database that is used in storing all users' information, items inormation, and posts.

# BUILT WITH:
<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/></a>
<a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <br> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg"  alt="flask" width="40" height="40"/></a> </p>

# PROJECT ENVIRONMENT: 
This project requires a virtual environment for the proper functioning of the project. This section gives a short demonstration of how to create a virtual environment(windows users) which is as follows:
## Step 1:
Open your system command prompt from your window search bar "search command prompt".

## Step 2 :
Make a directory to your desktop or any preferable location.
### Command: cd Desktop
## Step 3:
Install virtual environment if not installed before.
### Command: pip install virtual environment
## Step 4:
Create your flask environment with any name you want. (i will be using flaskenv for demonstration)
### Command: virtualenv flaskenv
## Step 5:
Make a directory to your environment
### Command: cd flaskenv
## Step 6:
Make a directory to scripts
### Command: cd scripts
## Step 7:
Activate your environment
### Command: activate
Yes, your environment is ready for use.
### Note: The above illustrations are for windows users only.

# INSTALLATION:
This section contains all the packages to be installed for this project.
Before installation make sure your environment is activated and packages are installed in the terminal( e.g command prompt, PowerShell, Git Bash, etc) using  "pip install package".
## Packages to be installed:
### FastAPI
### uvicorn[standard]
### flask-sqlalchemy
### python-jose
### Passlib
### Bcrypt
### Python-multipart
### Jinja2



### The command for installation:
pip install " package name"

# FOLDER CREATION:
This section contains all the folders required for the creation of this project.This folders include:
### BlogPosts Folder
### Routers Folder
### Repository Folder
### Security Folder
### Templates Folder
### Static Folder
### userimages Folder
### postimages Folder
### itemimages Folder

## BlogPosts Folder:
This folder contains all the files and folders in this project except the main.py file, virtual environment folder, and the requirements.txt file.
## Routers Folder:
The routers folder contains the route for all the endpoints for user, blog, authentication, store, and item files.This folder contains some files which include:
user.py file 
blog.py file
authentication.py file
store.py file 
items.py file
password_reset.py file

## Repository Folder:
This folder contains the functions for all the endpoints for blog, user, store, and items files. These files include:
User.py file
Blog.py file
Item.py file
Store.py file
 
## Security Folder
This folder contains some file which is the backbone for the proper authentication and authorization of this website.
These files include:
Hashing.py file
Oauth2.py file
Token.py file

Note: Others folders will be explained under Jinja 2 template.


# FILE CREATION
This section contains all the files needed for the creation of this project which is:

## main.py
This file is the engine of the project which is used for running the project. It is created outside the BlogPosts folder.
It is used to run all API endpoints using FastAPI.
This file contains a declared app that is used to connect all routers to the API Endpoint. This also contained the display endpoints which are used to connect the API Endpoint with jinja2 template that is used to display some information.


## Database.py
This file contains engine, SessionLocal, and Base which are used by base metadata to create a database table. These can all be found in the sqlalchemy module.
This file also contains the get_db function where DB can be called to store data in the database table. 

## Models.py
This file contains the class tables column information which is stored in form of a table and held all information needed for the website. This file contains:
Class User
Class BlogPost
Class UserImage
Class PostImage
Class Item
Class ItemImage
Class Store

## Class User table contains:
### Id
### Email
### Username
### Password
### Last name
### First name
### Created date
### blogs
### item_user

## Class UserImage table
### Id
### Name
### img
### Mimetype
### user_id

## Class BlogPost table contains:
### Id
### Title
### Content
### Author
### poster_id
### Posted date
### creator
### user_id

## class PostImage table
### Id
### Name
### img
### Mimetype
### blog_id

## Class Item table
### Id
### Name
### barcode
### description
### price
### prod_date
### store_id
### user_item
### store
### user

## Class ItemImage table
### Id
### Name
### img
### Mimetype
### item_id

## Class Store table
### Id
### Name
### items


## Schemas.py
This file contains the Base model from the pydantic module which is used to create a schemas class used for the CRUD operation.
This file contains:
### SchemasUser class
### UserCreator class
### SchemasBlog class
### ItemShowStore class
### UserBlog class
### ShowUser class
### UserLogin class
### ShowBlog class
### UpdateBlog class
### CreateStore class
### ShowStore class
### ItemStore class
### CreateItem class
### UpdateItem class
### ShowItem class
### Token class
### TokenData class
### PasswordReset class
### NewPassword class
### ItemImg class
### userImg class
### PostImg class

## Routers/blog.py
This file contains the APIRouter used for the endpoints, tags, and prefix.
This file contains the route for all the endpoints for the blog post which contained all the called endpoints functions from the blog.py in the repository folder.
The routes are for:
### get_all
### show_post
### cretae_post
### update_post
### delete_post
### get_title
### get_title_author
### upload

## Routers/user.py
This file contains the APIRouter used for the endpoints, tags, and prefix.
This file contains the route for all the endpoints for the users which contained all the called endpoints functions from the user.py in the repository folder.
The routes are for:
### create_user
### get_all_user
### get_user
### get_username
### upload

## Routers/item.py
This file contains the APIRouter used for the endpoints, tags, and prefix.
This file contains the route for all the endpoints for the items which contained all the called endpoints functions from the item.py in the repository folder.
The routes are for:
### get_all_item
### show_item_id
### show_item_name
### cretae_item
### update_item
### delete_item
### upload
### item_images

## Routers/store.py
This file contains the APIRouter used for the endpoints, tags, and prefix.
This file contains the route for all the endpoints for the store which contained all the called endpoints functions from the store.py in the repository folder.
The routes are for:
### show_store
### show_store_id
### show_store_name
### cretae_store
### update_store
### delete_store

## Routers/authentication.py
This is the engine for website authentication and authorization. This file is used to generate an access token for the newly registered user which will be used to get authenticated to the website.
It contains the route for user login which an access token is generated and used to log in to the website.

## Routers/password_reset.py
This file contains the APIRouter used for the endpoints, tags, and prefix.
This file contains the route for reset_request and reset functions.

## Repository/blog.py
This file contains all the functions for all the endpoints for the CRUD operations which are imported to the blog.py file in the routers folder where they are called for the CRUD operations.
These functions include:
### get_all
### show_post
### cretae_post
### update_post
### delete_post
### get_title
### get_title_author

## Repository/user.py
This file contains all the functions for all the endpoints for the CRUD operations which are imported to the user.py file in the routers folder where they are called for the CRUD operations.
These functions include:
### create_user
### get_all_user
### get_user
### get_username
### upload

## Repository/item.py
This file contains all the functions for all the endpoints for the CRUD operations which are imported to the item.py file in the routers folder where they are called for the CRUD operations.
These functions include:
### get_all_item
### show_item_id
### show_item_name
### cretae_item
### update_item
### delete_item

## Repository/store.py
This file contains all the functions for all the endpoints for the CRUD operations which are imported to the store.py file in the routers folder where they are called for the CRUD operations.
These functions include:
### show_store
### show_store_id
### show_store_name
### cretae_store
### update_store
### delete_store

## Security/hashing.py
This file contains the hash class using crypto context to hash the requested password. This file contains a class that contains a function that returned a hashed password when a password string is inserted by the user.
This is for a security guard so that the user password which is a secret key will not be exposed.

## Security/token.py
This file contains the create_access_token and verify_token functions which are later called in the authentication file and is being used to authenticate the user and authorized the user access to the website.
This file also contains:
### ACCESS_TOKEN_EXPIRE_MINUTES
### SECRET_KEY
### ALGORITHM


## Security/oauth2.py
This file contains the get_current_user function which is later called in all the routers that are needed to be protected and to identify the activeness of the user.
This file also verifies the user's information before it can be processed and stored in a database.

# AUTHENTICATION AND AUTHORIZATION
This website authentication is solely based on Oauth2.
OAuth2 is a specification that defines several ways to handle authentication and authorization.
It is quite an extensive specification and covers several complex use cases.
It includes ways to authenticate using a "third party".
An OAUTH2PasswordBearer can be imported from fastapi security module.
This also has a built-in form known as the OUATH2PasswordRequestForm which is  an authorized form for user authorization.
Jwt and jwtError are imported from the python- Jose which is used to encode and decode tokens, data, secret keys, algorithms, and so on.

# JINJA2 Template
Jinja2 is a modern-day templating language for Python developers. It was made after Django’s template. It is used to create HTML, XML, or other markup formats that are returned to the user via an HTTP request.

## Using Jinja2Templates
#### Import Jinja2Templates.
#### Create a templates object that you can re-use later.
#### Declare a Request parameter in the path operation that will return a template.
#### Use the templates you created to render and return a TemplateResponse, passing the request as one of the key-value pairs in the Jinja2 "context".

The folders under jinja2 template are: 
### Static folder
### Templates folder

## Static Folder
This folder contains three folders and one file namely:
### Userimages folder
The userimages folder contains all the user's image uploaded to the website.
### Postimages folder
The postimages contain all the post images needed in a written article.
### itemimages folder
The itemsimages contain all the images uploaded for all the items created.
### Main.css
The main.css file is the file that contains all the CSS styling for the website frontend side.

## Template Folder
The templates folder contains six files which are:
### Base.html
This is the base for all others HTML file.its contain the nav bar for others file.
### Home.html
Home.html contains the HTML file for all the blog posts created.
### User.html
User.html contains all the information of the users registered on the website.
### Items.html
Items.html contains all the information for all the items created on the website.
### Store.html
This file contains all the store information and items in the store on the website.
### Content.html
This file contains individual item detailed information that cannot be found in the item.html file.

The jinja2 template is the backbone of the client side in this project and used to displayed all information on the website.


# What I learned 
### How to generate an access token.
### Effectively use of pydantic schema.
### Swagger UI configuration.
### Full API authentication and authorization.
### Uploading of files and storing of files to the database.
### Retrieving uploaded images from the database to display on the website.
### Uploading of files to the static folder and any desired path.



# THE Challenges’
### How to reset a forgotten Password
### How to get data by name, title etc
### How to get images directly from database using fastapi.



# CONCLUSION
This project's Online shopping store and blog website were designed using the blog side to create an advertising article for the uploaded items and also can be used to publish other articles on the website.
The shopping side is meant for selling and buying items present on the website.
CRUD operations can be performed on : 
### Blog
### User
### Items
### Store.
This project(both frontend and backend) is created by ADEYEMO MUSODIQ OLALEKAN an AltSchool Africa School of Engineering student.
This project is open for contribution.
You can contact me on WhatsApp  08141171294


<h1 align="left" font-weight="bold">Connect with me:</h1>
<p align="left">
<a href="https://twitter.com/sirmuso" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="sirmuso" height="30" width="40" /></a>
<a href="https://linkedin.com/in/musodiq-adeyemo" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="musodiq-adeyemo" height="30" width="40" /></a>
<a href="https://fb.com/https://www.facebook.com/adeyemo.musodiq" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="https://www.facebook.com/adeyemo.musodiq" height="30" width="40" /></a>
</p>

- 📫 How to reach me **adeyemomusodiq@gmail.com**

- ⚡ Fun fact **I'm currently studying at AltSchool Africa School of Software Engineering Class of 2022.**


You can contact me on WhatsApp at 08141171294

## GOD BLESS ALT SCHOOL  AFRICA






