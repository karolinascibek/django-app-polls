def check_list_index(list, obj):
    try:
        list.index(obj)
        return True
    except ValueError:
        return False