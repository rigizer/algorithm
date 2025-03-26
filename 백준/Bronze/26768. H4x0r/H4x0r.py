replace_dict = { 'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5' }
print(''.join([replace_dict[word] if word in replace_dict else word for word in list(input())]))