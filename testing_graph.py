from ecommercesite import db
from ecommercesite.database import Product_Bought
from datetime import datetime, date
#db.create_all()

item = Product_Bought(quantity=1, date_bought=date(2021,11,11) ,datetime_bought=datetime(2021, 11, 11, 5, 56, 59, 148835) ,product_id=1, user_id=1, price=10, product_name='testing', image='6775e757704c11194a4a.png')
db.session.add(item)
db.session.commit()
print('item 1 added')

item = Product_Bought(quantity=1, date_bought=date(2021,12,11) ,datetime_bought=datetime(2021, 12, 11, 5, 56, 59, 148835) , product_id=1, user_id=1, price=10, product_name='testing', image='6775e757704c11194a4a.png')
db.session.add(item)
db.session.commit()
print('item 2 added')

item = Product_Bought(quantity=1, date_bought=date(2022,1,11) ,datetime_bought=datetime(2022, 1, 11, 5, 56, 59, 148835) , product_id=1, user_id=1, price=10, product_name='testing', image='6775e757704c11194a4a.png')
db.session.add(item)
db.session.commit()
print('item 3 added')

item = Product_Bought(quantity=1, date_bought=date(2022,1,12) ,datetime_bought=datetime(2022, 1, 12, 5, 56, 59, 148835), product_id=1, user_id=1, price=10, product_name='testing', image='6775e757704c11194a4a.png')
db.session.add(item)
db.session.commit()
print('item 4 added')

item = Product_Bought(quantity=1, date_bought=date(2022,2,11) ,datetime_bought=datetime(2022, 2, 11, 5, 56, 59, 148835), product_id=1, user_id=1, price=10, product_name='testing', image='6775e757704c11194a4a.png')
db.session.add(item)
db.session.commit()
print('item 5 added')
