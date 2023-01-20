def transform(input_list):
    if len(input_list) == 0:
        return ''
    
    if len(input_list) == 1:
        return input_list[0]
    
    return '{} and {}.'.format(
        ', '.join(input_list[:-1]),
        input_list[-1]
        )

