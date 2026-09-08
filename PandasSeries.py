import pandas as pd

def main():
    sobj = pd.Series([11,21.2,"51.6",True],index = [5,6,7,8])

    print(sobj)
    print(sobj[7])


if __name__ == "__main__":
    main()