hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_in_minutes = hour_of_exam * 60 + minutes_of_exam
arrival_in_minutes = hour_of_arrival * 60 + minute_of_arrival
diff = abs(exam_in_minutes - arrival_in_minutes)

hour = 0
minute = 0

if exam_in_minutes < arrival_in_minutes:
    if diff >= 60:
        hour = int(diff / 60)
        minute = diff % 60
        if minute < 10:
            print("Late")
            print(f"{hour}:0{minute} hours after the start")
        else:
            print("Late")
            print(f"{hour}:{minute} hours after the start")
    else:
        minute = diff % 60
        print("Late")
        print(f"{minute} minutes after the start")
elif exam_in_minutes >= arrival_in_minutes and (diff <= 30 or diff == 0):
    hour = int(diff / 60)
    minute = diff % 60
    if diff == 0:
        print("On time")
    else:
        print("On time")
        print(f"{minute} minutes before the start")
elif exam_in_minutes > arrival_in_minutes and diff > 30:
    if diff >= 60:
        hour = int(diff / 60)
        minute = diff % 60
        if minute < 10:
            print("Early")
            print(f"{hour}:0{minute} hours before the start")
        else:
            print("Early")
            print(f"{hour}:{minute} hours before the start")
    else:
        minute = diff % 60
        print("Early")
        print(f"{minute} minutes before the start")




