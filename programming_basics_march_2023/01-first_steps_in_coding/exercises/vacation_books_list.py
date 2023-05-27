pagecount = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

hours_to_read_allpages = pagecount / pages_per_hour
hours_per_day_to_finish_allpages = hours_to_read_allpages / days_to_read

print(int(hours_per_day_to_finish_allpages))