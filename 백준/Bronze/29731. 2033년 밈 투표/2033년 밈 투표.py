p = [
    'Never gonna give you up'
    ,'Never gonna let you down'
    ,'Never gonna run around and desert you'
    ,'Never gonna make you cry'
    ,'Never gonna say goodbye'
    ,'Never gonna tell a lie and hurt you'
    ,'Never gonna stop'
]

result = 'No'
for s in [input() for _ in range(int(input()))]:
    if s not in p:
        result = 'Yes'

print(result)