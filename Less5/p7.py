import json
with open('file_p7.txt', 'r') as f:
    ob_pr = 0
    my_dict = {}
    while True:
        firm_list = f.readline().split()
        if not firm_list:
            break
        result = int(firm_list[2]) - int(firm_list[3])
        if result > 0:
            ob_pr = result + ob_pr
            my_dict[firm_list[0]] = result
        # print(firm_list, result)
    data = ([my_dict, {'average_profit': round(ob_pr / len(my_dict), 2)}])
print(data)
with open('json_p7.json', 'w') as j:
    json.dump(data, j)

