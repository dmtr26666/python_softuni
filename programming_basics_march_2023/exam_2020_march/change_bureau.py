bitcoins = int(input())
yuans= float(input())
commision = float(input()) / 100

bitcoins_in_bgn = bitcoins * 1168
yuans_to_bgn = (yuans * 0.15) * 1.76


bitcoins_in_eur = bitcoins_in_bgn / 1.95
yuans_in_eur = yuans_to_bgn / 1.95

final_sum_in_eur = bitcoins_in_eur + yuans_in_eur
final_price = final_sum_in_eur - (final_sum_in_eur * commision)

print(f'{final_price:.2f}')
