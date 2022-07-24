# aspj
Run run.py to start the server

------------------------------
# How to drop sql tables
1. type "python" in command line
2. type "from ecommercesite import db"
3. type "from ecommercesite.database import 'the table name you want to drop'"
3. type "tablename.__table__.drop(db.engine)"
5. type "db.session.commit()"
6. to exit type exit()

------------------------------
# How to set up .venv
1. open pyvenv.cfg located in .venv folder in .venv and change the home= folder path to your python 3.10 folder

example: 

         my folder path to python 3.10 folder is D:\Python310

         so my home= path should be home = D:\Python310
         
2. open activate.bat located in .venv/Scripts folder and at the set VIRTUAL_ENV= change the path to your .venv folder

example: 

         the path of my .venv is C:\School_homework\Application_Security_Project\Assignment_new\.venv

         so my VIRTUAL_ENV= should be VIRTUAL_ENV=C:\School_homework\Application_Security_Project\Assignment_new\.venv
         
         make sure your path do not have any spaces!! 
         
         eg. C:\School homework\Application_Security_Project\Assignment_new\.venv will not work.
