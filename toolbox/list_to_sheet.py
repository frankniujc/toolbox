def list_to_csv(lsts):
    csv_strings = []
    for lst in lsts:
        csv_strings.append(','.join(str(x) for x in lst))
    return '\n'.join(csv_strings)