shoes = {'имя': 'Модные туфли', 'цена': 14900}


def apply_discount(product, discount):
   price = int(product['цена']  *  (1.0 - discount))
   assert 0 <= price <= product['цена']
   return price

print(apply_discount(shoes, 0.25))

print(apply_discount(shoes, 2))