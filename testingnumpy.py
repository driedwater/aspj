import numpy as np
import pandas as pd
from datetime import datetime 

'''
total_quantity_by_month = 0
list = []
all product bought = product_bought.query.all()
for product in all product bought
    if month and year of the product is equal to oldest product bought month and year
        total_quantity_by_month = total_quantity_by_month + product.quantity
    else
    list.append(a)
    total_quantiy_by_month = 0

total_quantity_by_month = 0
list = []
all_product_bought = product_bought.query.all()
for product in all_product_bought:
    pdb = product.date_bought.strftime('%Y-%m')
    if pdb == oldest_my:
        total_quantity_by_month += product.quantity
    else:
        list.append(total_quantity_by_month)
        total_quantity_by_month = 0

'''

def trunc_datetime(someDate):
    return someDate.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

print(trunc_datetime(datetime.utcnow()))