import re

def solution(s):
    sets = re.findall(r'\{([^{}]+)\}', s)

    sets = [set(map(int, set_str.split(','))) for set_str in sets]

    sets.sort(key=len)
    result = []
    added = set()

    for s in sets:
        for num in s:
            if num not in added:
                result.append(num)
                added.add(num)

    return result