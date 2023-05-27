actor_name = str(input())
points_from_academy = float(input())
number_of_judges = int(input())


for i in range(number_of_judges):
    judge_name = str(input())
    point_given = float(input())
    points_from_academy += (len(judge_name) * point_given) / 2
    if points_from_academy > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!")
        break
    else:
        continue

diff = abs(1250.5 - points_from_academy)
if points_from_academy < 1250.5:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")

