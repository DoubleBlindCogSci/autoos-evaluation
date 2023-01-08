def get_factors_from_code_as_list(code: str) -> list:
    """
    Args:
        code:
    Returns:
    """
    lines = code.splitlines(False)
    objects = []
    for line in lines:
        words = line.split(' ')
        if len(words) >= 3 and words[2].startswith('Factor'):
            variable_name = words[0]
            factor_name = ''
            read = False
            for char in words[2]:
                if read and not (char == '"' or char == "'"):
                    factor_name += char
                if read and (char == '"' or char == "'"):
                    break
                if char == '"' or char == "'":
                    read = True
            objects.append((variable_name, factor_name))
    return objects

def get_factors_from_code_as_list_of_lines(code: str) -> list:
    """
        Args:
            code:
        Returns:
        """
    lines = code.splitlines(False)
    objects = []
    for line in lines:
        words = line.split(' ')
        if len(words) >= 3 and words[2].startswith('Factor'):
            objects.append(line)
    return objects

if __name__ == "__main__":
    example = 'asd = Factor("asd"), ["fdas", "dasf"])\n' \
              'bsd = Factor("bsd"), ["fdas", "dasf"])'
    print(get_factors_from_code_as_list(example))