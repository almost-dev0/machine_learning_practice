import pandas as pd

def main():
    data = [11,21.2,"51.6",True]

    sobj = pd.Series(data)
    print(sobj)


if __name__ == "__main__":
    main()