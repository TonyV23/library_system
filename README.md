#  Conventions

- database settings :

        DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'library_db',
                    'USER':'root',
                    'PASSWORD':'',
                    'HOST':'localhost',
                    'PORT':'3306
                }
        }

- Before modify anything in the code of specific branch, synchronize your local code with the remote base by running:
  `git pull --all`
- After 

# How to name things
- variable: use snake case(ex: this_is_a_variable)
- constant: use snake case(ex: THIS_IS_A_CONSTANT)
- function: use camel case(ex: thisIsAFunction)
- class:  use pascal case(ex: ThisIsAClass)
- form : use pascal case (ex: ThisIsAForm)


# Git rules
- Do not modify the code being in develop or master branch.
- Use git flow as workflow.
- Before modify anything in the code, synchronize the code with the remote base by running:
  `git pull --all`


# Project structure

#### folder and files to work on 
- app/
    * forms/
        define forms for app he 
    * models/
        define here models app
    * views/
        define here views for app
    * templating/
        * app/
            define here template for app
    * static/
        * app/
            define here static files for app

- urls.py : used to define urls for app

- library_management_system/
    * settings.py : used to setting up the project