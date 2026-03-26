import sys
input = lambda: sys.stdin.readline().rstrip()

S = int(input())

if S % 4763 != 0:
    print(0)
else:
    X = S // 4763
    result_set = set()
    
    for d1 in range(201):
        for d2 in range(201):
            m1_candidates = [108] if d1 == 0 else [508, 108]
            m2_candidates = [305] if d2 == 0 else [212, 305]
            
            for m1 in m1_candidates:
                for m2 in m2_candidates:
                    if d1 * m1 + d2 * m2 == X:
                        result_set.add((d1, d2))
    
    result = sorted(list(result_set))
    
    print(len(result))
    for d1, d2 in result:
        print(d1, d2)