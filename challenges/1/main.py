def capToFront(input):
    """Write your function here, which will return a string with all the capital letters at the front.

    Args:
        input (str): The input string.

    Returns:
        str: The result.
    """
    my_list_upper = []
    my_list_lower = []
    for i in input:
        if i.isupper() == True:
            my_list_upper.append(i)
        if i.isupper() != True:
            my_list_lower.append(i)

    my_new_list = my_list_upper + my_list_lower       
    return "" .join(my_new_list)
    # for i in input:
    #     if i.isupper() != True:
    #         my_list.append(i)


    #return "".join(my_list)

result = capToFront("HeLlO")


