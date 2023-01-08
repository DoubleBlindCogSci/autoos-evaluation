import random
import string


def generate_code_within(nr_levels, nr_factors):
    operators_comparision = ['==', '!=']
    operators_bool = ['and', 'or']

    lst = [_rand_name() for _ in range(random.randint(nr_levels + 3, nr_levels + 5))]
    lst_2 = [_rand_name() for _ in range(random.randint(nr_levels + 3, nr_levels + 5))]
    samples = random.sample(lst, k=3)
    samples_2 = random.sample(lst_2, k=3)
    res = ''
    if nr_factors == 1:
        factor = _rand_name()
        res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
        if nr_levels == 2:
            function_name = _rand_name()
            function_name_2 = _rand_name()
            operators = []
            params = [samples[0]]
            operators.append(random.choice(operators_comparision))
            res += f'def {function_name}({factor}):\n'
            res += f'    return {factor} {operators[0]} "{params[0]}"'
            if random.random() < .5:
                operators.append(random.choice(operators_bool))
                operators.append(random.choice(operators_comparision))
                params.append(random.choice(samples[1:]))
                res += f' {operators[1]} {factor} {operators[2]} "{params[1]}"'
            res += '\n'
            res += f'def {function_name_2}({factor}):\n'
            if random.random() < .33:
                res += f'    return {factor} {neg(operators[0])} "{params[0]}"'
                if len(params) > 1:
                    if random.random() < .5:
                        res += f' {neg(operators[1])} {factor} {neg(operators[2])} "{params[1]}"'
                    else:
                        res += f' {neg(operators[1])} not ({factor} {operators[2]} "{params[1]}")'
            elif random.random() < .5:
                res += f'    return not {function_name}({factor})'
            else:
                res += f'    return not ({factor} {operators[0]} "{params[0]}")'
                if len(params) > 1:
                    if random.random() < .5:
                        res += f' {neg(operators[1])} {factor} {neg(operators[2])} "{params[1]}"'
                    else:
                        res += f' {neg(operators[1])} not ({factor} {operators[2]} "{params[1]}")'
            res += '\n'
            if random.random() < .5:
                level_1 = _rand_name()
                level_2 = _rand_name()
                res += f'{level_1} = DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}]))\n'
                res += f'{level_2} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}]))\n'
                res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
            else:
                res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}])), DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}]))])'
        if nr_levels == 3:
            function_name = _rand_name()
            function_name_2 = _rand_name()
            function_name_3 = _rand_name()
            operators = ['==', '==']
            params = [samples[0], random.choice(samples[1:])]
            res += f'def {function_name}({factor}):\n'
            if random.random() < .5:
                res += f'     return {factor} {operators[0]} "{params[0]}"\n'
            else:
                res += f'     return "{params[0]}" {operators[0]} {factor}\n'
            res += f'def {function_name_2}({factor}):\n'
            if random.random() < .5:
                res += f'     return {factor} {operators[1]} "{params[1]}"\n'
            else:
                res += f'     return "{params[1]}" {operators[1]} {factor}\n'
            res += f'def {function_name_3}({factor}):\n'
            if random.random() < .33:
                res += f'     return (not {function_name}({factor})) and '
            elif random.random() < .5:
                res += f'     return ({factor} {neg(operators[0])} "{params[0]}") and '
            else:
                res += f'     return (not {factor} {(operators[0])} "{params[0]}") and '
            if random.random() < .33:
                res += f'(not {function_name_2}({factor}))'
            elif random.random() < .5:
                res += f'({factor} {neg(operators[1])} "{params[1]}")'
            else:
                res += f'(not {factor} {(operators[1])} "{params[1]}")'
            res += '\n'
            if random.random() < .5:
                level_1 = _rand_name()
                level_2 = _rand_name()
                level_3 = _rand_name()
                res += f'{level_1} = DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}]))\n'
                res += f'{level_2} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}]))\n'
                res += f'{level_3} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_3}, [{factor}]))\n'
                res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
            else:
                res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}])), DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}])),DerivedLevel("{_rand_name()}", WithinTrial({function_name_3}, [{factor}]))])'
    if nr_factors == 2:
        factor = _rand_name()
        factor_2 = _rand_name()
        is_different = random.random() < .5
        if is_different:
            res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
            res += f'{factor_2} = Factor("{factor_2}", ["' + '","'.join(lst_2) + '"])\n'
            if nr_levels == 2:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                operators = []
                params = [samples[0]]
                operators.append(random.choice(operators_comparision))
                res += f'def {function_name}({factor}, {factor_2}):\n'
                res += f'    return {factor} {operators[0]} "{params[0]}"'
                operators.append(random.choice(operators_bool))
                operators.append(random.choice(operators_comparision))
                params.append(random.choice(samples_2))
                res += f' {operators[1]} {factor_2} {operators[2]} "{params[1]}"'
                res += '\n'
                res += f'def {function_name_2}({factor},{factor_2}):\n'
                if random.random() < .33:
                    res += f'    return {factor} {neg(operators[0])} "{params[0]}"'
                    if random.random() < .5:
                        res += f' {neg(operators[1])} {factor_2} {neg(operators[2])} "{params[1]}"'
                    else:
                        res += f' {neg(operators[1])} not ({factor_2} {operators[2]} "{params[1]}")'
                elif random.random() < .5:
                    res += f'    return not {function_name}({factor}, {factor_2})'
                else:
                    res += f'    return not ({factor} {operators[0]} "{params[0]}")'
                    if random.random() < .5:
                        res += f' {neg(operators[1])} {factor_2} {neg(operators[2])} "{params[1]}"'
                    else:
                        res += f' {neg(operators[1])} not ({factor_2} {operators[2]} "{params[1]}")'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}, {factor_2}]))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}, {factor_2}]))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}, {factor_2}])), DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}, {factor_2}]))])'
            if nr_levels == 3:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                function_name_3 = _rand_name()
                operators = ['==', '==']
                params = [samples[0], samples_2[0]]
                res += f'def {function_name}({factor}, {factor_2}):\n'
                if random.random() < .5:
                    res += f'     return {factor} {operators[0]} "{params[0]}"\n'
                else:
                    res += f'     return "{params[0]}" {operators[0]} {factor}\n'
                res += f'def {function_name_2}({factor}, {factor_2}):\n'
                if random.random() < .5:
                    res += f'     return {factor} {neg(operators[0])} "{params[0]}" and '
                else:
                    res += f'     return "{params[0]}" {neg(operators[0])} {factor} and '
                res += f' {factor_2} {operators[1]} "{params[1]}"\n'
                res += f'def {function_name_3}({factor}, {factor_2}):\n'
                if random.random() < .33:
                    res += f'     return (not {function_name}({factor}, {factor_2})) and '
                elif random.random() < .5:
                    res += f'     return ({factor} {neg(operators[0])} "{params[0]}") and '
                else:
                    res += f'     return (not {factor} {(operators[0])} "{params[0]}") and '
                if random.random() < .33:
                    res += f'(not {function_name_2}({factor}, {factor_2}))'
                elif random.random() < .5:
                    res += f'({factor_2} {neg(operators[1])} "{params[1]}")'
                else:
                    res += f'(not {factor_2} {(operators[1])} "{params[1]}")'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    level_3 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}, {factor_2}]))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}, {factor_2}]))\n'
                    res += f'{level_3} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_3}, [{factor}, {factor_2}]))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}, {factor_2}])), DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}, {factor_2}])),DerivedLevel("{_rand_name()}", WithinTrial({function_name_3}, [{factor}, {factor_2}]))])'
        else:
            factor = _rand_name()
            res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
            factor_2 = _rand_name()
            res += f'{factor_2} = Factor("{factor_2}", ["' + '","'.join(lst) + '"])\n'
            factor_3 = _rand_name()
            res += f'{factor_3} = Factor("{factor_3}", ["' + '","'.join(lst) + '"])\n'
            if nr_levels == 2:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                operators = []
                arguments = [factor_2, factor_3]
                samples = random.sample(arguments, 2)
                params = [samples[0]]
                operators.append(random.choice(operators_comparision))
                res += f'def {function_name}({factor}, {samples[0]}, {samples[1]}):\n'
                res += f'    return {factor} {operators[0]} {params[0]}'
                if random.random() < .5:
                    operators.append(random.choice(operators_bool))
                    operators.append(random.choice(operators_comparision))
                    params.append(random.choice(samples[1:]))
                    res += f' {operators[1]} {factor} {operators[2]} {params[1]}'
                res += '\n'
                res += f'def {function_name_2}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .33:
                    res += f'    return {factor} {neg(operators[0])} {params[0]}'
                    if len(params) > 1:
                        if random.random() < .5:
                            res += f' {neg(operators[1])} {factor} {neg(operators[2])} {params[1]}'
                        else:
                            res += f' {neg(operators[1])} not ({factor} {operators[2]} {params[1]})'
                elif random.random() < .5:
                    res += f'    return not {function_name}({factor}, {samples[0]}, {samples[1]})'
                else:
                    res += f'    return not ({factor} {operators[0]} {params[0]})'
                    if len(params) > 1:
                        if random.random() < .5:
                            res += f' {neg(operators[1])} {factor} {neg(operators[2])} {params[1]}'
                        else:
                            res += f' {neg(operators[1])} not ({factor} {operators[2]} {params[1]})'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}, {factor_2}, {factor_3}])), DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}, {factor_2}, {factor_3}]))])'
            if nr_levels == 3:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                function_name_3 = _rand_name()
                operators = ['==', '==']
                arguments = [factor_2, factor_3]
                samples = random.sample(arguments, 2)
                params = [samples[0], samples[1]]
                res += f'def {function_name}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .5:
                    res += f'     return {factor} {operators[0]} {params[0]}\n'
                else:
                    res += f'     return {params[0]} {operators[0]} {factor}\n'
                res += f'def {function_name_2}({factor}, {samples[0]}, {samples[1]}):\n'
                res += f'     return {params[0]} {neg(operators[0])} {factor} and '
                if random.random() < .5:
                    res += f'{factor} {operators[1]} {params[1]}\n'
                else:
                    res += f'{params[1]} {operators[1]} {factor}\n'
                res += f'def {function_name_3}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .33:
                    res += f'     return (not {function_name}({factor}, {samples[0]}, {samples[1]})) and '
                elif random.random() < .5:
                    res += f'     return ({factor} {neg(operators[0])} {params[0]}) and '
                else:
                    res += f'     return (not {factor} {(operators[0])} {params[0]}) and '
                if random.random() < .33:
                    res += f'(not {function_name_2}({factor}, {samples[0]}, {samples[1]}))'
                elif random.random() < .5:
                    res += f'({factor} {neg(operators[1])} {params[1]})'
                else:
                    res += f'(not {factor} {(operators[1])} {params[1]})'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    level_3 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{level_3} = DerivedLevel("{_rand_name()}", WithinTrial({function_name_3}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", WithinTrial({function_name}, [{factor}, {factor_2}, {factor_3}])), DerivedLevel("{_rand_name()}", WithinTrial({function_name_2}, [{factor}, {factor_2}, {factor_3}])),DerivedLevel("{_rand_name()}", WithinTrial({function_name_3}, [{factor}, {factor_2}, {factor_3}]))])'
    return res


def generate_code_transition(nr_levels, nr_factors):
    operators_comparision = ['==', '!=']
    operators_bool = ['and', 'or']

    lst = [_rand_name() for _ in range(random.randint(nr_levels + 3, nr_levels + 5))]
    lst_2 = [_rand_name() for _ in range(random.randint(nr_levels + 3, nr_levels + 5))]
    samples = random.sample(lst, k=3)
    samples_2 = random.sample(lst_2, k=3)
    res = ''
    if nr_factors == 1:
        factor = _rand_name()
        res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
        if nr_levels == 2:
            function_name = _rand_name()
            function_name_2 = _rand_name()
            operators = []
            params = [samples[0]]
            operators.append(random.choice(operators_comparision))
            res += f'def {function_name}({factor}):\n'
            res += f'    return {factor}[0] {operators[0]} "{params[0]}"'

            operators.append(random.choice(operators_bool))
            operators.append(random.choice(operators_comparision))
            params.append(random.choice(samples[1:]))
            res += f' {operators[1]} {factor}[-1] {operators[2]} "{params[1]}"'
            res += '\n'
            res += f'def {function_name_2}({factor}):\n'
            if random.random() < .33:
                res += f'    return {factor}[0] {neg(operators[0])} "{params[0]}"'
                if random.random() < .5:
                    res += f' {neg(operators[1])} {factor}[-1] {neg(operators[2])} "{params[1]}"'
                else:
                    res += f' {neg(operators[1])} not ({factor}[-1] {operators[2]} "{params[1]}")'
            elif random.random() < .5:
                res += f'    return not {function_name}({factor})'
            else:
                res += f'    return not ({factor}[0] {operators[0]} "{params[0]}")'
                if random.random() < .5:
                    res += f' {neg(operators[1])} {factor}[-1] {neg(operators[2])} "{params[1]}"'
                else:
                    res += f' {neg(operators[1])} not ({factor}[0] {operators[2]} "{params[1]}")'
            res += '\n'
            if random.random() < .5:
                level_1 = _rand_name()
                level_2 = _rand_name()
                res += f'{level_1} = DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}]))\n'
                res += f'{level_2} = DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}]))\n'
                res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
            else:
                res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}])), DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}]))])'
        if nr_levels == 3:
            function_name = _rand_name()
            function_name_2 = _rand_name()
            function_name_3 = _rand_name()
            operators = ['==', '==']
            params = [samples[0], random.choice(samples[1:])]
            res += f'def {function_name}({factor}):\n'
            if random.random() < .5:
                res += f'     return {factor}[0] {operators[0]} "{params[0]}" and '
            else:
                res += f'     return "{params[0]}" {operators[0]} {factor}[0] and '
            if random.random() < .5:
                res += f'{factor}[-1] {neg(operators[1])} "{params[1]}"\n'
            else:
                res += f'not {factor}[-1] {operators[1]} "{params[1]}"\n'
            res += f'def {function_name_2}({factor}):\n'
            if random.random() < .5:
                res += f'     return ({factor}[0] {neg(operators[0])} "{params[0]}") and '
            else:
                res += f'     return (not "{params[0]}" {neg(operators[0])} {factor}[0]) and '
            if random.random() < .5:
                res += f' {factor}[-1] {operators[1]} "{params[1]}"\n'
            else:
                res += f' "{params[1]}" {operators[1]} {factor}[-1]\n'
            res += f'def {function_name_3}({factor}):\n'
            if random.random() < .33:
                res += f'     return (not {function_name}({factor})) and '
            elif random.random() < .5:
                res += f'     return ({factor}[0] {neg(operators[0])} "{params[0]}") and '
            else:
                res += f'     return (not {factor}[0] {(operators[0])} "{params[0]}") and '
            if random.random() < .33:
                res += f'(not {function_name_2}({factor}))'
            elif random.random() < .5:
                res += f'({factor}[-1] {neg(operators[1])} "{params[1]}")'
            else:
                res += f'(not {factor}[-1] {(operators[1])} "{params[1]}")'
            res += '\n'
            if random.random() < .5:
                level_1 = _rand_name()
                level_2 = _rand_name()
                level_3 = _rand_name()
                res += f'{level_1} = DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}]))\n'
                res += f'{level_2} = DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}]))\n'
                res += f'{level_3} = DerivedLevel("{_rand_name()}", Transition({function_name_3}, [{factor}]))\n'
                res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
            else:
                res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}])), DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}])),DerivedLevel("{_rand_name()}", Transition({function_name_3}, [{factor}]))])'
    if nr_factors == 2:
        factor = _rand_name()
        factor_2 = _rand_name()
        is_different = random.random() < .5
        if is_different:
            res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
            res += f'{factor_2} = Factor("{factor_2}", ["' + '","'.join(lst_2) + '"])\n'
            if nr_levels == 2:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                operators = []
                params = [samples[0]]
                operators.append(random.choice(operators_comparision))
                res += f'def {function_name}({factor}, {factor_2}):\n'
                res += f'    return {factor}[0] {operators[0]} "{params[0]}"'
                operators.append(random.choice(operators_bool))
                operators.append(random.choice(operators_comparision))
                params.append(random.choice(samples_2))
                res += f' {operators[1]} {factor_2}[-1] {operators[2]} "{params[1]}"'
                res += '\n'
                res += f'def {function_name_2}({factor},{factor_2}):\n'
                if random.random() < .33:
                    res += f'    return {factor}[0] {neg(operators[0])} "{params[0]}"'
                    if random.random() < .5:
                        res += f' {neg(operators[1])} {factor_2}[-1] {neg(operators[2])} "{params[1]}"'
                    else:
                        res += f' {neg(operators[1])} not ({factor_2}[-1] {operators[2]} "{params[1]}")'
                elif random.random() < .5:
                    res += f'    return not {function_name}({factor}, {factor_2})'
                else:
                    res += f'    return not ({factor}[0] {operators[0]} "{params[0]}")'
                    if random.random() < .5:
                        res += f' {neg(operators[1])} {factor_2}[-1] {neg(operators[2])} "{params[1]}"'
                    else:
                        res += f' {neg(operators[1])} not ({factor_2}[-1] {operators[2]} "{params[1]}")'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}, {factor_2}]))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}, {factor_2}]))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}, {factor_2}])), DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}, {factor_2}]))])'
            if nr_levels == 3:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                function_name_3 = _rand_name()
                operators = ['==', '==']
                params = [samples[0], samples_2[0]]
                res += f'def {function_name}({factor}, {factor_2}):\n'
                if random.random() < .5:
                    res += f'     return {factor}[-1] {operators[0]} "{params[0]}" and '
                else:
                    res += f'     return "{params[0]}" {operators[0]} {factor}[-1] and '
                if random.random() < .5:
                    res += f'{factor_2}[0] {neg(operators[1])} "{params[1]}"\n'
                else:
                    res += f'not {factor_2}[0] {operators[1]} "{params[1]}"\n'
                res += f'def {function_name_2}({factor}, {factor_2}):\n'
                if random.random() < .5:
                    res += f'     return {factor}[-1] {neg(operators[0])} "{params[0]}" and '
                else:
                    res += f'     return "{params[0]}" {neg(operators[0])} {factor}[-1] and '
                res += f'{factor_2}[0] {operators[1]} "{params[1]}"\n'
                res += f'def {function_name_3}({factor}, {factor_2}):\n'
                if random.random() < .33:
                    res += f'     return (not {function_name}({factor}, {factor_2})) and '
                elif random.random() < .5:
                    res += f'     return ({factor}[-1] {neg(operators[0])} "{params[0]}") and '
                else:
                    res += f'     return (not {factor}[-1] {(operators[0])} "{params[0]}") and '
                if random.random() < .33:
                    res += f'(not {function_name_2}({factor}, {factor_2}))'
                elif random.random() < .5:
                    res += f'({factor_2}[0] {neg(operators[1])} "{params[1]}")'
                else:
                    res += f'(not {factor_2}[0] {(operators[1])} "{params[1]}")'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    level_3 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}, {factor_2}]))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}, {factor_2}]))\n'
                    res += f'{level_3} = DerivedLevel("{_rand_name()}", Transition({function_name_3}, [{factor}, {factor_2}]))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}, {factor_2}])), DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}, {factor_2}])),DerivedLevel("{_rand_name()}", Transition({function_name_3}, [{factor}, {factor_2}]))])'
        else:
            factor = _rand_name()
            res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
            factor_2 = _rand_name()
            res += f'{factor_2} = Factor("{factor_2}", ["' + '","'.join(lst) + '"])\n'
            factor_3 = _rand_name()
            res += f'{factor_3} = Factor("{factor_3}", ["' + '","'.join(lst) + '"])\n'
            if nr_levels == 2:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                operators = []
                arguments = [factor_2, factor_3]
                samples = random.sample(arguments, 2)
                params = [samples[0]]
                operators.append(random.choice(operators_comparision))
                res += f'def {function_name}({factor}, {samples[0]}, {samples[1]}):\n'
                res += f'    return {factor}[0] {operators[0]} {params[0]}[-1]'
                if random.random() < .5:
                    operators.append(random.choice(operators_bool))
                    operators.append(random.choice(operators_comparision))
                    params.append(random.choice(samples[1:]))
                    res += f' {operators[1]} {factor}[-1] {operators[2]} {params[1]}[0]'
                res += '\n'
                res += f'def {function_name_2}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .33:
                    res += f'    return {factor}[0] {neg(operators[0])} {params[0]}[-1]'
                    if len(params) > 1:
                        if random.random() < .5:
                            res += f' {neg(operators[1])} {factor}[-1] {neg(operators[2])} {params[1]}[0]'
                        else:
                            res += f' {neg(operators[1])} not ({factor}[-1] {operators[2]} {params[1]}[0])'
                elif random.random() < .5:
                    res += f'    return not {function_name}({factor}, {samples[0]}, {samples[1]})'
                else:
                    res += f'    return not ({factor}[0] {operators[0]} {params[0]}[-1])'
                    if len(params) > 1:
                        if random.random() < .5:
                            res += f' {neg(operators[1])} {factor}[-1] {neg(operators[2])} {params[1]}[0]'
                        else:
                            res += f' {neg(operators[1])} not ({factor}[-1] {operators[2]} {params[1]}[0])'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}, {factor_2}, {factor_3}])), DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}, {factor_2}, {factor_3}]))])'
            if nr_levels == 3:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                function_name_3 = _rand_name()
                operators = ['==', '==']
                arguments = [factor_2, factor_3]
                samples = random.sample(arguments, 2)
                params = [samples[0], samples[1]]
                res += f'def {function_name}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .5:
                    res += f'     return {factor}[0] {operators[0]} {samples[0]}[-1] and '
                else:
                    res += f'     return {samples[0]}[-1] {operators[0]} {factor}[0] and '
                res += f'{factor}[-1] {neg(operators[1])} {samples[1]}[0]\n'
                res += f'def {function_name_2}({factor}, {samples[0]}, {samples[1]}):\n'
                res += f'     return {samples[0]}[-1] {neg(operators[0])} {factor}[0] and '
                if random.random() < .5:
                    res += f'{factor}[-1] {operators[1]} {samples[1]}[0]\n'
                else:
                    res += f'{samples[1]}[0] {operators[1]} {factor}[-1]\n'
                res += f'def {function_name_3}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .33:
                    res += f'     return (not {function_name}({factor}, {samples[0]}, {samples[1]})) and '
                elif random.random() < .5:
                    res += f'     return ({factor}[0] {neg(operators[0])} {samples[0]}[-1]) and '
                else:
                    res += f'     return (not {factor}[0] {(operators[0])} {samples[0]}[-1]) and '
                if random.random() < .33:
                    res += f'(not {function_name_2}({factor}, {samples[0]}, {samples[1]}))'
                elif random.random() < .5:
                    res += f'({factor}[-1] {neg(operators[1])} {samples[1]}[0])'
                else:
                    res += f'(not {factor}[-1] {(operators[1])} {samples[1]}[0])'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    level_3 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{level_3} = DerivedLevel("{_rand_name()}", Transition({function_name_3}, [{factor}, {factor_2}, {factor_3}]))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Transition({function_name}, [{factor}, {factor_2}, {factor_3}])), DerivedLevel("{_rand_name()}", Transition({function_name_2}, [{factor}, {factor_2}, {factor_3}])),DerivedLevel("{_rand_name()}", Transition({function_name_3}, [{factor}, {factor_2}, {factor_3}]))])'
    return res


def generate_code_window(nr_levels, nr_factors):
    operators_comparision = ['==', '!=']
    operators_bool = ['and', 'or']

    lst = [_rand_name() for _ in range(random.randint(nr_levels + 3, nr_levels + 5))]
    lst_2 = [_rand_name() for _ in range(random.randint(nr_levels + 3, nr_levels + 5))]
    samples = random.sample(lst, k=3)
    samples_2 = random.sample(lst_2, k=3)
    res = ''
    indices = [0, -1, -2]
    indices_sample = random.sample(indices, k=2)
    window_width = (min(indices_sample) - 1) * -1
    if nr_factors == 1:
        factor = _rand_name()
        res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
        if nr_levels == 2:
            function_name = _rand_name()
            function_name_2 = _rand_name()
            operators = []
            params = [samples[0]]
            operators.append(random.choice(operators_comparision))
            res += f'def {function_name}({factor}):\n'
            res += f'    return {factor}[{indices_sample[0]}] {operators[0]} "{params[0]}"'
            operators.append(random.choice(operators_bool))
            operators.append(random.choice(operators_comparision))
            params.append(random.choice(samples[1:]))
            res += f' {operators[1]} {factor}[{indices_sample[1]}] {operators[2]} "{params[1]}"'
            res += '\n'
            res += f'def {function_name_2}({factor}):\n'
            if random.random() < .33:
                res += f'    return {factor}[{indices_sample[0]}] {neg(operators[0])} "{params[0]}"'
                if random.random() < .5:
                    res += f' {neg(operators[1])} {factor}[{indices_sample[1]}] {neg(operators[2])} "{params[1]}"'
                else:
                    res += f' {neg(operators[1])} not ({factor}[{indices_sample[1]}] {operators[2]} "{params[1]}")'
            elif random.random() < .5:
                res += f'    return not {function_name}({factor})'
            else:
                res += f'    return not ({factor}[{indices_sample[0]}] {operators[0]} "{params[0]}")'
                if random.random() < .5:
                    res += f' {neg(operators[1])} {factor}[{indices_sample[1]}] {neg(operators[2])} "{params[1]}"'
                else:
                    res += f' {neg(operators[1])} not ({factor}[{indices_sample[0]}] {operators[2]} "{params[1]}")'
            res += '\n'
            if random.random() < .5:
                level_1 = _rand_name()
                level_2 = _rand_name()
                res += f'{level_1} = DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}],{window_width},1))\n'
                res += f'{level_2} = DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}],{window_width},1))\n'
                res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
            else:
                res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}],{window_width},1)), DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}],{window_width},1))])'
        if nr_levels == 3:
            function_name = _rand_name()
            function_name_2 = _rand_name()
            function_name_3 = _rand_name()
            operators = ['==', '==']
            params = [samples[0], random.choice(samples[1:])]
            res += f'def {function_name}({factor}):\n'
            if random.random() < .5:
                res += f'     return {factor}[{indices_sample[0]}] {operators[0]} "{params[0]}" and '
            else:
                res += f'     return "{params[0]}" {operators[0]} {factor}[{indices_sample[0]}] and '
            res += f'not {factor}[{indices_sample[1]}] {operators[1]} "{params[0]}"\n'
            res += f'def {function_name_2}({factor}):\n'
            if random.random() < .5:
                res += f'     return {factor}[{indices_sample[0]}] {neg(operators[0])} "{params[0]}" and '
            else:
                res += f'     return not "{params[0]}" {operators[0]} {factor}[{indices_sample[0]}] and '
            if random.random() < .5:
                res += f' {factor}[{indices_sample[1]}] {operators[1]} "{params[1]}"\n'
            else:
                res += f' "{params[1]}" {operators[1]} {factor}[{indices_sample[1]}]\n'
            res += f'def {function_name_3}({factor}):\n'
            if random.random() < .33:
                res += f'     return (not {function_name}({factor})) and '
            elif random.random() < .5:
                res += f'     return ({factor}[{indices_sample[0]}] {neg(operators[0])} "{params[0]}") and '
            else:
                res += f'     return (not {factor}[{indices_sample[0]}] {(operators[0])} "{params[0]}") and '
            if random.random() < .33:
                res += f'(not {function_name_2}({factor}))'
            elif random.random() < .5:
                res += f'({factor}[{indices_sample[1]}] {neg(operators[1])} "{params[1]}")'
            else:
                res += f'(not {factor}[{indices_sample[1]}] {(operators[1])} "{params[1]}")'
            res += '\n'
            if random.random() < .5:
                level_1 = _rand_name()
                level_2 = _rand_name()
                level_3 = _rand_name()
                res += f'{level_1} = DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}],{window_width},1))\n'
                res += f'{level_2} = DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}],{window_width},1))\n'
                res += f'{level_3} = DerivedLevel("{_rand_name()}", Window({function_name_3}, [{factor}],{window_width},1))\n'
                res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
            else:
                res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}],{window_width},1)), DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}],{window_width},1)),DerivedLevel("{_rand_name()}", Window({function_name_3}, [{factor}],{window_width},1))])'
    if nr_factors == 2:
        factor = _rand_name()
        factor_2 = _rand_name()
        is_different = random.random() < .5
        if is_different:
            res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
            res += f'{factor_2} = Factor("{factor_2}", ["' + '","'.join(lst_2) + '"])\n'
            if nr_levels == 2:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                operators = []
                params = [samples[0]]
                operators.append(random.choice(operators_comparision))
                res += f'def {function_name}({factor}, {factor_2}):\n'
                res += f'    return {factor}[{indices_sample[0]}] {operators[0]} "{params[0]}"'
                operators.append(random.choice(operators_bool))
                operators.append(random.choice(operators_comparision))
                params.append(random.choice(samples_2))
                res += f' {operators[1]} {factor_2}[{indices_sample[1]}] {operators[2]} "{params[1]}"'
                res += '\n'
                res += f'def {function_name_2}({factor},{factor_2}):\n'
                if random.random() < .33:
                    res += f'    return {factor}[{indices_sample[0]}] {neg(operators[0])} "{params[0]}"'
                    if random.random() < .5:
                        res += f' {neg(operators[1])} {factor_2}[{indices_sample[1]}] {neg(operators[2])} "{params[1]}"'
                    else:
                        res += f' {neg(operators[1])} not ({factor_2}[{indices_sample[1]}] {operators[2]} "{params[1]}")'
                elif random.random() < .5:
                    res += f'    return not {function_name}({factor}, {factor_2})'
                else:
                    res += f'    return not ({factor}[{indices_sample[0]}] {operators[0]} "{params[0]}")'
                    if random.random() < .5:
                        res += f' {neg(operators[1])} {factor_2}[{indices_sample[1]}] {neg(operators[2])} "{params[1]}"'
                    else:
                        res += f' {neg(operators[1])} not ({factor_2}[{indices_sample[1]}] {operators[2]} "{params[1]}")'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}, {factor_2}],{window_width},1))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}, {factor_2}],{window_width},1))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}, {factor_2}],{window_width},1)), DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}, {factor_2}],{window_width},1))])'
            if nr_levels == 3:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                function_name_3 = _rand_name()
                operators = ['==', '==']
                params = [samples[0], samples_2[0]]
                res += f'def {function_name}({factor}, {factor_2}):\n'
                if random.random() < .5:
                    res += f'     return {factor}[{indices_sample[1]}] {operators[0]} "{params[0]}" and '
                else:
                    res += f'     return "{params[0]}" {operators[0]} {factor}[{indices_sample[1]}] and '
                if random.random() < .5:
                    res += f'{factor_2}[{indices_sample[0]}] {neg(operators[1])} "{params[1]}"\n'
                else:
                    res += f'not {factor_2}[{indices_sample[0]}] {operators[1]} "{params[1]}"\n'
                res += f'def {function_name_2}({factor}, {factor_2}):\n'
                if random.random() < .5:
                    res += f'     return {factor}[{indices_sample[1]}] {neg(operators[0])} "{params[0]}" and '
                else:
                    res += f'     return "{params[0]}" {neg(operators[0])} {factor}[{indices_sample[1]}] and '
                res += f' {factor_2}[{indices_sample[0]}] {operators[1]} "{params[1]}"\n'
                res += f'def {function_name_3}({factor}, {factor_2}):\n'
                if random.random() < .33:
                    res += f'     return (not {function_name}({factor}, {factor_2})) and '
                elif random.random() < .5:
                    res += f'     return ({factor}[{indices_sample[1]}] {neg(operators[0])} "{params[0]}") and '
                else:
                    res += f'     return (not {factor}[{indices_sample[1]}] {(operators[0])} "{params[0]}") and '
                if random.random() < .33:
                    res += f'(not {function_name_2}({factor}, {factor_2}))'
                elif random.random() < .5:
                    res += f'({factor_2}[{indices_sample[0]}] {neg(operators[1])} "{params[1]}")'
                else:
                    res += f'(not {factor_2}[{indices_sample[0]}] {(operators[1])} "{params[1]}")'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    level_3 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}, {factor_2}],{window_width},1))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}, {factor_2}],{window_width},1))\n'
                    res += f'{level_3} = DerivedLevel("{_rand_name()}", Window({function_name_3}, [{factor}, {factor_2}],{window_width},1))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}, {factor_2}],{window_width},1)), DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}, {factor_2}],{window_width},1)),DerivedLevel("{_rand_name()}", Window({function_name_3}, [{factor}, {factor_2}],{window_width},1))])'
        else:
            factor = _rand_name()
            res += f'{factor} = Factor("{factor}", ["' + '","'.join(lst) + '"])\n'
            factor_2 = _rand_name()
            res += f'{factor_2} = Factor("{factor_2}", ["' + '","'.join(lst) + '"])\n'
            factor_3 = _rand_name()
            res += f'{factor_3} = Factor("{factor_3}", ["' + '","'.join(lst) + '"])\n'
            if nr_levels == 2:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                operators = []
                arguments = [factor_2, factor_3]
                samples = random.sample(arguments, 2)
                params = [samples[0]]
                operators.append(random.choice(operators_comparision))
                res += f'def {function_name}({factor}, {samples[0]}, {samples[1]}):\n'
                res += f'    return {factor}[{indices_sample[0]}] {operators[0]} {params[0]}[{indices_sample[1]}]'
                if random.random() < .5:
                    operators.append(random.choice(operators_bool))
                    operators.append(random.choice(operators_comparision))
                    params.append(random.choice(samples[1:]))
                    res += f' {operators[1]} {factor}[{indices_sample[1]}] {operators[2]} {params[1]}[{indices_sample[0]}]'
                res += '\n'
                res += f'def {function_name_2}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .33:
                    res += f'    return {factor}[{indices_sample[0]}] {neg(operators[0])} {params[0]}[{indices_sample[1]}]'
                    if len(params) > 1:
                        if random.random() < .5:
                            res += f' {neg(operators[1])} {factor}[{indices_sample[1]}] {neg(operators[2])} {params[1]}[{indices_sample[0]}]'
                        else:
                            res += f' {neg(operators[1])} not ({factor}[{indices_sample[1]}] {operators[2]} {params[1]}[{indices_sample[0]}])'
                elif random.random() < .5:
                    res += f'    return not {function_name}({factor}, {samples[0]}, {samples[1]})'
                else:
                    res += f'    return not ({factor}[{indices_sample[0]}] {operators[0]} {params[0]}[{indices_sample[1]}])'
                    if len(params) > 1:
                        if random.random() < .5:
                            res += f' {neg(operators[1])} {factor}[{indices_sample[1]}] {neg(operators[2])} {params[1]}[{indices_sample[0]}]'
                        else:
                            res += f' {neg(operators[1])} not ({factor}[{indices_sample[1]}] {operators[2]} {params[1]}[{indices_sample[0]}])'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}, {factor_2}, {factor_3}],{window_width},1))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}, {factor_2}, {factor_3}],{window_width},1))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}, {factor_2}, {factor_3}],{window_width},1)), DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}, {factor_2}, {factor_3}],{window_width},1))])'
            if nr_levels == 3:
                function_name = _rand_name()
                function_name_2 = _rand_name()
                function_name_3 = _rand_name()
                operators = ['==', '==']
                arguments = [factor_2, factor_3]
                samples = random.sample(arguments, 2)
                params = [samples[0], samples[1]]
                res += f'def {function_name}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .5:
                    res += f'     return {factor}[{indices_sample[0]}] {operators[0]} {params[0]}[{indices_sample[1]}] and '
                else:
                    res += f'     return {params[0]}[{indices_sample[1]}] {operators[0]} {factor}[{indices_sample[0]}] and '
                res += f'{factor}[{indices_sample[1]}] {neg(operators[1])} {params[1]}[{indices_sample[0]}]\n'
                res += f'def {function_name_2}({factor}, {samples[0]}, {samples[1]}):\n'
                res += f'     return {params[0]}[{indices_sample[1]}] {neg(operators[0])} {factor}[{indices_sample[0]}] and '
                if random.random() < .5:
                    res += f'{factor}[{indices_sample[1]}] {operators[1]} {params[1]}[{indices_sample[0]}]\n'
                else:
                    res += f'{params[1]}[{indices_sample[0]}] {operators[1]} {factor}[{indices_sample[1]}]\n'
                res += f'def {function_name_3}({factor}, {samples[0]}, {samples[1]}):\n'
                if random.random() < .33:
                    res += f'     return (not {function_name}({factor}, {samples[0]}, {samples[1]})) and '
                elif random.random() < .5:
                    res += f'     return ({factor}[{indices_sample[0]}] {neg(operators[0])} {params[0]}[{indices_sample[1]}]) and '
                else:
                    res += f'     return (not {factor}[{indices_sample[0]}] {(operators[0])} {params[0]}[{indices_sample[1]}]) and '
                if random.random() < .33:
                    res += f'(not {function_name_2}({factor}, {samples[0]}, {samples[1]}))'
                elif random.random() < .5:
                    res += f'({factor}[{indices_sample[1]}] {neg(operators[1])} {params[1]}[{indices_sample[0]}])'
                else:
                    res += f'(not {factor}[{indices_sample[1]}] {(operators[1])} {params[1]}[{indices_sample[0]}])'
                res += '\n'
                if random.random() < .5:
                    level_1 = _rand_name()
                    level_2 = _rand_name()
                    level_3 = _rand_name()
                    res += f'{level_1} = DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}, {factor_2}, {factor_3}],{window_width},1))\n'
                    res += f'{level_2} = DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}, {factor_2}, {factor_3}],{window_width},1))\n'
                    res += f'{level_3} = DerivedLevel("{_rand_name()}", Window({function_name_3}, [{factor}, {factor_2}, {factor_3}],{window_width},1))\n'
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [{level_1}, {level_2}, {level_3}])\n'
                else:
                    res += f'{_rand_name()} = Factor("{_rand_name()}", [DerivedLevel("{_rand_name()}", Window({function_name}, [{factor}, {factor_2}, {factor_3}],{window_width},1)), DerivedLevel("{_rand_name()}", Window({function_name_2}, [{factor}, {factor_2}, {factor_3}],{window_width},1)),DerivedLevel("{_rand_name()}", Window({function_name_3}, [{factor}, {factor_2}, {factor_3}],{window_width},1))])'
    return res


def neg(operator):
    if operator == '==':
        return '!='
    if operator == '!=':
        return '=='
    if operator == 'and':
        return 'or'
    if operator == 'or':
        return 'and'


def _rand_name():
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))


if __name__ == '__main__':
    print(generate_code_window(3, 2))
