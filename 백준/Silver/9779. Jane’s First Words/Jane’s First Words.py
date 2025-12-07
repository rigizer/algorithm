import sys
import re

pattern = re.compile(r'^da+dd?(i|y)$')
results = []
for line in sys.stdin:
    word = line.rstrip()
    if pattern.match(word):
        results.append('She called me!!!')
    else:
        results.append('Cooing')

print('\n'.join(results))