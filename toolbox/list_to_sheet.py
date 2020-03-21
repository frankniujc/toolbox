def lists_to_csv(lsts, sep=','):
    csv_strings = []
    for lst in lsts:
        csv_strings.append(sep.join(str(x) for x in lst))
    return '\n'.join(csv_strings)


def dicts_to_csv(*dicts, **kwargs):
    if not dicts:
        return ''

    dicts = list(dicts)
    keys = dicts[0].keys()

    if 'default_value' in kwargs:
        default_value = kwargs['default_value']

        keys = set()
        for dic in dicts:
            keys = keys.union(dic.keys())
    else:
        for dic in dicts:
            assert dic.keys() == keys, 'All dictionaries should have matching keys'

    lsts = []

    if 'sort_key' in kwargs:
        sort_key = kwargs['sort_key']
    else:
        sort_key = None

    sorted_keys = sorted(keys, key=sort_key)

    for key in sorted_keys:
        row = [key]
        for dic in dicts:
            if key in dic:
                row.append(dic[key])
            else:
                row.append(default_value)
        lsts.append(row)

    return lists_to_csv(lsts)

def lists_to_latex(lsts):
    latex_strings = []
    for lst in lsts:
        latex_strings.append(' & '.join(str(x) for x in lst) + ' \\')
    return '\n'.join(latex_strings)
