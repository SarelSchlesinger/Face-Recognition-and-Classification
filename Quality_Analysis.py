def Quality_Analysis(dictionary):
    lst = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    if lst[0][1] >= 50:
        if lst[0][0] == 'good':
            return 'Your picture is good!'
        else:
            return f'Improve your picture. The problem is {lst[0][0]}.'
    elif lst[0][1] <= 35:
        return f'We are not sure if your picture is good or not. Please upload new picture.'
    else:
        if lst[0][1] - lst[1][1] >= 20:
            if lst[0][0] == 'good':
                return 'Your picture is good!'
            else:
                return f'Improve your picture. The problem is {lst[0][0]}.'
        else:
            return f'We are not sure if your picture is good or not. Please upload new picture.'