# sklearn contains a lot of inbuilt practice datasets, which can be imported using sklearn.datasets import load_(dataset name)
from sklearn.datasets import load_iris

def main():
    Border = "-" * 30

    print(Border)
    print("Iris Classification Case Study")
    print(Border)
    
    Dataset = load_iris()

    # Commit 2 : Metadata of Dataset
    print("Independent Variables are : ")
    print(Dataset.feature_names)

    print("Dependent Variables are : ")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()