def parse_date(date):
    yy, mm, dd = map(int, date.split('.'))
    return (yy * 12 * 28) + (mm * 28) + dd

def solution(today, terms, privacies):
    answer = []
    
    today_val = parse_date(today)
    terms_val = dict()
    
    for term in terms:
        key, val = map(str, term.split())
        terms_val[key] = int(val) * 28
    
    for i, privacy in enumerate(privacies):
        key, val = map(str, privacy.split())
        p_val = parse_date(key) + terms_val.get(val)
        print(p_val, today_val)
        
        if p_val <= today_val:
            answer.append(i + 1)
    
    return answer