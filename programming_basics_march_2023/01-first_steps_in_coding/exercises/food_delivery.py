ordered_chicken_menus = int(input()) * 10.35
ordered_fish_menus = int(input()) * 12.40
ordered_vegie_menus = int(input()) * 8.15

delivery_fee = 2.50

price_without_delivery = ordered_chicken_menus + ordered_vegie_menus + ordered_fish_menus

desert = price_without_delivery * 0.20

print(price_without_delivery + desert + delivery_fee)

