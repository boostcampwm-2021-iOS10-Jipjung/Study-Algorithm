from collections import defaultdict
from bisect import bisect_left
# "java backend junior pizza 150" -> jbjp150
def parsing_info(info):
    keyword_list = info.split()
    result = ""
    for keyword in keyword_list[0:-1]:
        result += keyword[0]
    return result + keyword_list[-1]

def save_info_count(info, info_dict):
    keyword = info[:4]
    score = int(info[4:])
    def dfs(i, j):
        if i == 4:
            info_dict[j].append(score)
            return
        if keyword[i] != "-":
            dfs(i + 1, j + keyword[i])
        dfs(i + 1, j + "-")
    dfs(0, "")

# "java and backend and junior and pizza 100" -> jbjp100
def parsing_query(query):
    query_list = query.split()
    score = query_list.pop()
    result = ""
    for i in range(1 + len(query_list) // 2):
        result += query_list[i * 2][0]
    return result + score

def get_count_from_query(query, info_dict):
    keyword = query[:4]
    score = int(query[4:])
    keyword_result = info_dict[keyword]
    return len(keyword_result) - bisect_left(keyword_result, score)
    
def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        parsed_info = parsing_info(info)
        save_info_count(parsed_info, info_dict)
    
    for key in info_dict.keys():
        info_dict[key].sort()
        
    for query in queries:
        parsed_query = parsing_query(query)
        answer.append(get_count_from_query(parsed_query, info_dict))
    return answer