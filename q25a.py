def helper_combinations(input_dict):
    '''
    return a list for gen_one_length_combinations
    from a dict
    '''
    ret_list = []
    for item in input_dict:
        ret_list.append(set([item]))
    return ret_list


def gen_one_length_combinations(minor_comb, number):
    '''
    takes the sets in minor_comb and
    generate all possible combinations 
    of size sets-in-minor-comb + 1
    '''
    ret_list = []
    for each_set in minor_comb:
        for num in range(max(each_set) + 1, number):
            new_set = each_set.union(set([num]))
            ret_list.append(new_set)
    return ret_list


def gen_all_edges(input_dict):
    '''
    return a list of sets
    representing all the edges
    in the input_dict-graph
    '''
    ret_list = []
    for item in input_dict:
        if len(input_dict[item]) != 0:
            for set_item in input_dict[item]:
                if set([item, set_item]) not in ret_list:
                    ret_list.append(set([item, set_item]))
    return ret_list

def mystery(input_dict):
    '''
    main function for mystery algorithm
    '''
    input_list =  helper_combinations(input_dict)   
    all_edges = gen_all_edges(input_dict)
    dict_length = len(input_dict)
    for num in range(dict_length):
        for each_set in input_list:
            flag = True
            for each_edge in all_edges:
                 is_empty = each_edge.intersection(each_set)
                 if len(is_empty) == 0:
                     flag = False
                     break
            if flag == True:
                return each_set
        input_list = gen_one_length_combinations(input_list, dict_length)
