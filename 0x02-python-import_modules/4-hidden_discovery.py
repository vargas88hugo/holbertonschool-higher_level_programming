#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in range(0, len(hidden_4)):
        if hidden_4[i][:2] != "__":
            print(dir(hidden_4[i]))
