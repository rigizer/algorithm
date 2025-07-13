def count_bluray(lectures, size):
    count = 1
    current_sum = 0
    for time in lectures:
        if current_sum + time > size:
            count += 1
            current_sum = time
        else:
            current_sum += time
    return count

def find_min_bluray_size(n, m, lectures):
    left = max(lectures)
    right = sum(lectures)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        required = count_bluray(lectures, mid)
        
        if required <= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

print(find_min_bluray_size(n, m, lectures))