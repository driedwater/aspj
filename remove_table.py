from ecommercesite import db
from ecommercesite.database import Product_Bought

Product_Bought.__table__.drop(db.engine)
db.session.commit()
print('table is deleted')