def solution(bandage, health, attacks):
    t, x, y = bandage  # 시전 시간, 초당 회복량, 추가 회복량
    max_health = health  # 최대 체력
    current_health = health  # 현재 체력
    continuous_time = 0  # 연속 성공 시간
    attack_index = 0  # 공격 처리 인덱스

    # 시뮬레이션 진행
    for current_time in range(1, attacks[-1][0] + 1):  # 마지막 공격 시간까지 진행
        # 몬스터 공격 처리
        if attack_index < len(attacks) and attacks[attack_index][0] == current_time:
            damage = attacks[attack_index][1]
            current_health -= damage  # 체력 감소
            attack_index += 1  # 다음 공격으로 이동
            continuous_time = 0  # 연속 성공 초기화

            # 체력이 0 이하라면 즉시 종료
            if current_health <= 0:
                return -1
            continue  # 공격받으면 체력 회복 불가

        # 붕대 감기 처리
        if continuous_time < t:  # 연속 성공 시간 < 시전 시간
            continuous_time += 1
            current_health = min(max_health, current_health + x)  # 초당 회복량 적용

        # 연속 성공 후 추가 회복 처리
        if continuous_time == t:
            current_health = min(max_health, current_health + y)  # 추가 회복
            continuous_time = 0  # 연속 성공 초기화

    return current_health