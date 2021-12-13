from itertools import combinations

def calc_combination_count(combination_count_dict, combination_list):
    for combination in combination_list:
        if combination in combination_count_dict:
            combination_count_dict[combination] += 1
        else:
            combination_count_dict[combination] = 1
            
def get_max_selected_combinations(combination_count_dict):
    result = []
    if len(combination_count_dict) == 0:
        return result
    combination_count_items = sorted(combination_count_dict.items(), key = lambda x: -x[1])
    max_value = combination_count_items[0][1]
    for item in combination_count_items:
        if item[1] == max_value and max_value >= 2:
            result.append(item[0])
        else:
            break
    return result
        
def solution(orders, course):
    answer = []
    
    for menu_count in course:
        combination_count_dict = {}        
        for order in orders:
            single_menu_combinations = list(map(''.join, combinations(sorted(order), menu_count)))
            calc_combination_count(combination_count_dict, single_menu_combinations)
        answer += get_max_selected_combinations(combination_count_dict)
    answer.sort()
    return answer