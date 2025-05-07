def get_num_list(file_name):
    f = open(file_name)
    num_list = []
    for line in f:
        num_list.append(int(line))
    return num_list


def get_num_list_comma_sep(file_name):
    content = open(file_name).read()
    return [int(n) for n in content.split(",")]