# aspj
Run run.py to start the server

------------------------------
How to drop sql tables
1. type "python" in command line
2. type "from ecommercesite import db"
3. type "from ecommercesite.database import 'the table name you want to drop'"
3. type "tablename.__table__.drop(db.engine)"
5. type "db.session.commit()"
6. to exit type exit()
