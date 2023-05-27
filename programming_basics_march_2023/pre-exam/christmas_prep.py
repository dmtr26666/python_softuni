wraping_paper = int(input()) * 5.80
cloth = int(input()) * 7.20
glue_liters = float(input()) * 1.20
percent_discount = int(input())


price = wraping_paper + cloth + glue_liters
print(f"{price * (1 - (percent_discount / 100)):.3f}")