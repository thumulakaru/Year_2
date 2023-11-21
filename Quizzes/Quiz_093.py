def invert(dict_in:dict):
    dict_out = {}
    for k,v in dict_in.items():
        if v not in dict_out:
            dict_out[v] = k
        else:
            if type(dict_out[v]) != list:
                dict_out[v] = [dict_out[v], k]

            else:
                dict_out[v].append(k)
    return dict_out

T1 = {"a": 1, "b": 2, "c": 3}
T2 = {"bob": 26, "alice": 30, "carl": 40}
T3 = {"q1": True, "q2": False, "q3": True, "q4": True, "q5": True}

print(invert(T1))
print(invert(T2))
print(invert(T3))
