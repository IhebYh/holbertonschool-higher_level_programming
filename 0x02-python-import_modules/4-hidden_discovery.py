#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    length = dir(hidden_4)
    for i in range(len(length)):
        if(length[i][0] != '_'):
            print("{}".format(length[i]))
