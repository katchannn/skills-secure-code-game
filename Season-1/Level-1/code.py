'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100000
MAZ_TOTAL = 1e5

def validorder(order: Order):
    product = Decimal('0') # 買った商品の金額
    payment = Decimal('0') # 支払った金額

    for item in order.items:
        if item.type == 'product':
            if 0 < item.amount < MAX_ITEM_AMOUNT:
                product += Decimal(str(item.amount)) * Decimal(str(item.quantity))
        elif item.type == 'payment':
            if -MAX_ITEM_AMOUNT < item.amount < MAX_ITEM_AMOUNT:
                payment += Decimal(str(item.amount))
        else:
            return "Invalid item type: %s" % item.type

        if product > MAZ_TOTAL or payment > MAZ_TOTAL:
            return "Total amount payable for an order exceeded"

    # 商品の金額と支払った金額が一致している場合
    if product == payment:
        return "Order ID: %s - Full payment received!" % order.id
    else:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payment-product)