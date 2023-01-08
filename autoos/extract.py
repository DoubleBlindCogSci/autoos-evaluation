def extract(in_text: str,
            start: str,
            stop: str = '###') -> str:
    """
    Arg:
        in_text:
        start:
        stop:

    Returns:
    """
    lines = in_text.splitlines(False)
    result = ''
    read = False
    for line in lines:
        if read and not line.startswith(stop):
            result += line + '\n'
        else:
            read = False
        if line.startswith(start):
            read = True
    return result


def extract_all(in_text: str,
                dividers: str = '##') -> str:
    lines = in_text.splitlines(False)
    if len(lines)<2:
        return [lines[0]]
    result = []
    current = ''
    read = False
    for line in lines:
        if line.startswith(dividers):
            read = True
        if not line.startswith(dividers) and not read:
            continue
        if line.startswith(dividers):
            if current != '':
                result.append(current)
            current = ''
        else:
            current += line + '\n'
    if current != '':
        result.append(current)
    return result


if __name__ == '__main__':
    test = '## hi\nhafsio\ndas\n###\ndaskldf\n'
    print(extract_all(test))