# sklearn contains a lot of inbuilt practice datasets, which can be imported using sklearn.datasets import load_(dataset name)
from sklearn.datasets import load_iris

def main():
    Border = "-" * 30

    print(Border)
    print("Iris Classification Case Study")
    print(Border)

    # Commit 1 
    Dataset = load_iris()

    print(Dataset)

if __name__ == "__main__":
    main()