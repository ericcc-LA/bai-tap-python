

def common_keys(d1, d2):

    result = []

    for key in d1: 

        if key in d2: 

            result.append(key)  

    return result

def unique_keys(d1, d2):

    result = []

    for key in d1:

        if key not in d2:

            result.append(key)  

    return result

if __name__  ==  "__main__":

    print(unique_keys({"a": 1, "b": 2}, {"b": 3, "c": 4}))

    print(common_keys({"a": 1, "b": 2}, {"b": 3, "c": 4}))