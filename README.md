# Django Blog project

link to live app: https://blog-sage.herokuapp.com/

This is a solution to the CRUD Django task given on Zuri. Below is the task prompt:
```
From your knowledge of Python and Django. Extend the blog we built with the following functionalities:

-    A register page (a new user can register, their details stored in a database file). 
-    login (checks in the file and logs them in if they are already registered)
-    reset password
-    logout
-    A comment section, you must be logged in to comment
-    Host the project on heroku

```



## Architecture
**Templates**

Templates were created for:\
The register, and login views and inline styling was used in those templates.they were stored in the account folder under templates folder.\
Also for the password reset feature, 4 templates were created corresponding to the 4 password reset views. they were stored in the password folder under templates.\
The templates for the CRUD pages were placed in the root templates folder. external styling where used hence the need for static folder. Theme was gotten from UIDECK.

**Models**

In addition to the post model which handled the Posts, a new model was created to handle the comments. it was assigned a foreign key of post. Default User model was used for the users.


**views**

class based views were used for the CRUD section, while function based views where used to implement register, login and password reset functionalities. ModelForm class was used in implementing form for accepting user details and comments.
django auth_views was also used in implementing the password reset feature. while @login_required decorator was used to ensure user logged in before they can comment.