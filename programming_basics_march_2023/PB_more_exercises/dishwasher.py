washing_fluid = int(input())

count = 0

washing_fluid_ml = washing_fluid * 750

dishes = 0
pots = 0

while washing_fluid_ml >= 0:
    command = input()
    count += 1

    if command == "End":
        if washing_fluid_ml >= 0:
            print("Detergent was enough!")
            print(f"{dishes} dishes and {pots} pots were washed.")
            print(f"Leftover detergent {washing_fluid_ml} ml.")
            break

    else:
        if count % 3 == 0:
            dishes_count = int(command)
            washing_fluid_ml = washing_fluid_ml - (dishes_count * 15)
            pots += dishes_count
        else:
            dishes_count = int(command)
            washing_fluid_ml = washing_fluid_ml - (dishes_count * 5)
            dishes += dishes_count

if washing_fluid_ml < 0:
    print(f"Not enough detergent, {abs(washing_fluid_ml)} ml. more necessary!")
