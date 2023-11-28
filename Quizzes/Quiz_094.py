from matplotlib import pyplot as plt
import numpy as np

def dict_sorter(dict_in:dict):
    str_keys = []
    str_values = []
    int_keys = []
    int_values = []
    dict_out = {}
    for k,v in dict_in.items():
        if type(v) is int:
            str_keys.append(k)
            str_values.append(v)

        else:
            int_keys.append(k)
            int_values.append(v)

    for i in range(len(str_keys)):
        for j in range(i+1,len(str_keys)):
            if str_values[i] > str_values[j]:
                str_keys[i],str_keys[j] = str_keys[j],str_keys[i]
                str_values[i],str_values[j] = str_values[j],str_values[i]

    for i in range(len(int_keys)):
        for j in range(i+1,len(int_keys)):
            if len(int_values[i]) > len(int_values[j]):
                int_keys[i],int_keys[j] = int_keys[j],int_keys[i]
                int_values[i],int_values[j] = int_values[j],int_values[i]

    for i in range(len(str_keys)):
        dict_out[str_keys[i]] = str_values[i]

    for i in range(len(int_keys)):
        dict_out[int_keys[i]] = int_values[i]

    return dict_out

test_case1 = {'apple':5, 'banana': 2, 'orange': 8, 'grape': 1}
test_case2 = {'python': 3, 'java': 8, 'c++': 5, 'javascript': 2}
test_case3 = {'apple': 'red', 'banana': 2, 'orange': 'orange', 'grape': 1, 'kiwi': 'brown', 'pear': 8}

# print("Test Case 1 Result:", dict_sorter(test_case1))
# print("Test Case 3 Result:",dict_sorter(test_case3))
# print("Test Case 2 Result:",dict_sorter(test_case2))

def plot():
    # Generate x values
    x_values = np.linspace(0, 1, 1000)  # 1000 points between 0 and 1

    # Calculate y values
    y_values = np.sin(2 * np.pi * x_values)

    # Plot the function
    plt.plot(x_values, y_values, label=r'$y = \sin(2\pi x)$')
    plt.title('Plot of $y = \sin(2\pi x)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

plot()
