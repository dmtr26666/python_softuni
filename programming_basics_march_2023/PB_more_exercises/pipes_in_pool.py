pool_volume = int(input())
pipe_debit1 = int(input())
pipe_debit2 = int(input())
hours_missing = float(input())

pipe1_usage = pipe_debit1 * hours_missing
pipe2_usage = pipe_debit2 * hours_missing
liters_in_pool = pipe1_usage + pipe2_usage

percent_fullness = (liters_in_pool / pool_volume) * 100
pipe1_percentinge = (pipe1_usage / liters_in_pool) * 100
pipe2_percentinge = (pipe2_usage / liters_in_pool) * 100

if liters_in_pool <= pool_volume:
    print(f'The pool is {percent_fullness:.2f}% full. Pipe 1: {pipe1_percentinge:.2f}%. Pipe 2: {pipe2_percentinge:.2f}%.')
elif liters_in_pool > pool_volume:
    liters_extra = abs(pool_volume - liters_in_pool)
    print(f'For {hours_missing} hours the pool overflows with {liters_extra:.2f} liters.')
