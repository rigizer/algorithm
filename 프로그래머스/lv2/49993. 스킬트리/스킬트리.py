def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        checked = []
        for s in skill_tree:
            if s in skill:
                idx = skill.index(s)
                if idx == 0 or skill[idx - 1] in checked:
                    checked.append(s)
                else:
                    break
        else:
            answer += 1
    return answer