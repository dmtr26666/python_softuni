pencil_packs_needed = int(input())
markers_packs_needed = int(input())
liters_of_cleaner = int(input())
discount = int(input())

price_for_pack_of_pencils = 5.80
price_for_pack_of_markers = 7.20
price_for_liter_cleaner = 1.20

pencil_price = pencil_packs_needed * price_for_pack_of_pencils
markers_price = markers_packs_needed * price_for_pack_of_markers
cleaner_price = liters_of_cleaner * price_for_liter_cleaner

price_after_discount = (pencil_price + markers_price + cleaner_price) * (discount / 100)
print((pencil_price + markers_price + cleaner_price) - price_after_discount)

