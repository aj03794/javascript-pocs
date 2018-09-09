def item_in_list(to_check, the_list):
    for item in the_list:
        if to_check == True:
            return True
    return False

def all_combinations(the_list):
    results = []
    for item in the_list:
        for inner_item in the_list:
            results.append((item, inner_item))
    return results
    