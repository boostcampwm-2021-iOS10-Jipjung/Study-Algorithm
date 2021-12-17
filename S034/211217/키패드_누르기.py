def get_distance(center_number, from_number):
    return abs((center_number - 1) % 3 - (from_number - 1) % 3) + abs((center_number - 1) // 3 - (from_number - 1) // 3)

def check_hand(number, left_position, right_position, main_hand):
    if number == 0:
        number = 11  
    if number % 3 == 1:
        return ("L", number, right_position)
    elif number % 3 == 0:
        return ("R", left_position, number)
    left_distance = get_distance(number, left_position)
    right_distance = get_distance(number, right_position)
    if left_distance < right_distance:
        return ("L", number, right_position)
    elif left_distance > right_distance:
        return ("R", left_position, number)
    if main_hand == "left":
        return ("L", number, right_position)
    else:
        return ("R", left_position, number)
    
def solution(numbers, hand):
    answer = ""
    left_position, right_position = 10, 12
    for number in numbers:
        lr, left_position, right_position = check_hand(number, left_position, right_position, hand)
        answer += lr
    return answer