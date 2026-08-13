# sklearn contains a lot of inbuilt practice datasets, which can be imported using sklearn.datasets import load_(dataset name)
from sklearn.datasets import load_iris

def main():
    Border = "-" * 30

    print(Border)
    print("Iris Classification Case Study")
    print(Border)
    
    Dataset = load_iris()

    # Metadata of Dataset
    print("Independent Variables are : ")
    print(Dataset.feature_names)
    print("Length of Independent Variables : ",len(Dataset.feature_names))

    print("Dependent Variables are : ")
    print(Dataset.target_names)
    print("Length of Dependent Variables : ",len(Dataset.target_names))

    print(Dataset.data[0])
    print(Dataset.data[1])
    print(Dataset.data[2])
    print(Dataset.data[3])

    print(Dataset.target[0])
    print(Dataset.target[1])
    print(Dataset.target[2])
    print(Dataset.target[3])

if __name__ == "__main__":
    main()