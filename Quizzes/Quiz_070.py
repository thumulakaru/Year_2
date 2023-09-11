def ipV4machine():
    output = []
    for i in range(0,256):
        for j in range(0, 256):
            for k in range(0, 256):
                for l in range(0, 256):
                    output.append(f"{i}.{j}.{k}.{l}")

    return output