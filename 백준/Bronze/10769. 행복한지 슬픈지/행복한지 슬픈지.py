message = input()
if message.count(':-)') == 0 and message.count(':-(') == 0:
    print('none')
elif message.count(':-)') == message.count(':-('):
    print('unsure')
elif message.count(':-)') > message.count(':-('):
    print('happy')
else:
    print('sad')