from ecommercesite import db
from ecommercesite.database import Category

db.create_all()

catlist = ['New Arrival', 'Most Popular', 'Limited Time', 'Chair', 'Table', 'Cabinet', 'Door', 'Bed', 'Decoration', 'Others']
for cat in catlist:
    cate = Category(name=cat)
    db.session.add(cate)
    print(f'{cate} category has been added')

db.session.commit()


