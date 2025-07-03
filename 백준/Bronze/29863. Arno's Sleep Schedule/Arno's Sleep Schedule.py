sleep_time = int(input())
wake_time = int(input())
sleep_duration = wake_time - sleep_time if wake_time >= sleep_time else (24 - sleep_time) + wake_time
print(sleep_duration)