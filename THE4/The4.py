def construct_forest(tree_list):
    new_tree_list = blankspace_remover(tree_list)
    basic_tree_list = tree_maker(new_tree_list)
    index_will_deleted = []
    func_name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for func_index in range(len(basic_tree_list)):
        if basic_tree_list[func_index][2][0] in func_name_list:
            for search_index in range(len(basic_tree_list)):
                if basic_tree_list[func_index][2][0] == basic_tree_list[search_index][0]:
                    index_will_deleted.append(search_index)
                    basic_tree_list[func_index][2] = basic_tree_list[search_index]
        if basic_tree_list[func_index][3][0] in func_name_list:
            for search_index in range(len(basic_tree_list)):
                if basic_tree_list[func_index][3][0] == basic_tree_list[search_index][0]:
                    index_will_deleted.append(search_index)
                    basic_tree_list[func_index][3] = basic_tree_list[search_index]
    remove_list = []
    for i in index_will_deleted:
        remove_list.append(basic_tree_list[i])
    for j in remove_list:
        basic_tree_list.remove(j)
    
    return basic_tree_list


def tree_maker(tree_list):    
    operator_list = ["+","-","*","^"] 
    func_name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    FuncTree = []
    for func_def in tree_list:
        func_name = func_def[0]
        for index in range(5,len(func_def)):
            if func_def[index] in operator_list:
                operator = func_def[index]
                op_index = index
        left_child = func_def[5: op_index]
        right_child = func_def[op_index+1:]
        if left_child[0] in func_name_list:
            left_child = left_child[0]
        if right_child[0] in func_name_list:    
            right_child = right_child[0]
        FuncTree.append([func_name, operator, [left_child], [right_child]])
    return FuncTree             


def blankspace_remover(tree_list):
    new_tree_list = []
    for item in tree_list:
        new_item = "".join(item.split(" "))
        new_tree_list.append(new_item)
    return new_tree_list

