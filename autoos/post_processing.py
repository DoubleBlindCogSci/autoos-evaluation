import re

def correct_variable_declarations(code: str):
    """
    replaces non characters in variable declarations with _
    Args
        code:
    Returns
    """
    lines = code.splitlines(False)
    res = ''
    replace_list = []
    to_replace_list = []
    for line in lines:
        words = line.split(' ')
        if len(words) > 2 and words[1] == '=':
            declaration = re.sub("[^a-zA-Z]", '_', words[0])
            replace_list.append(words[0])
            to_replace_list.append(declaration)
            line = declaration + ' ' + ' '.join(words[1:])
        res += line + '\n'
    for i in range(len(replace_list)):
        res = re.sub(f'{re.escape(replace_list[i])}(?=([^"]*"[^"]*")*[^"]*$)', to_replace_list[i], res)
    return res


