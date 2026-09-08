import pandas as pd

def main():
    sobj = pd.Series([11,21.2,"51.6",True],index = ["C","C++","Java","Python"])

    print(sobj)
    print(sobj["Java"])


if __name__ == "__main__":
    main()