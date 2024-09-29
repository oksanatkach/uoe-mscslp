Q = [0, 1, 2, 3, 4]
E = ['b', 'a', '!']
start_state = Q[0]
F = {Q[4]}
transition_table = [
    # ['b',  'a',  '!']
      [1,    None, None],
      [None, 2,    None],
      [None, 3,    None],
      [None, 3,    4],
      [None, None, None]
]


def check_if_valid(string):
    current_state = start_state

    for char in string:
        transitioned = False
        state_row = transition_table[current_state]
        for input_ind in range(len(E)):
            if char == E[input_ind]:
                if state_row[input_ind]:
                    current_state = state_row[input_ind]
                    transitioned = True
                    break
        if current_state in F:
            return True
        if not transitioned:
            return False
    return False


print(check_if_valid('hregftfgsfzd'))
print(check_if_valid('b'))
print(check_if_valid('a'))
print(check_if_valid('!'))
print(check_if_valid('ba'))
print(check_if_valid('baaaaa'))
print(check_if_valid('ba!'))
print(check_if_valid('baa!'))
print(check_if_valid('baaa!'))
print(check_if_valid('baaaa!'))
print(check_if_valid('baaaaa!'))
