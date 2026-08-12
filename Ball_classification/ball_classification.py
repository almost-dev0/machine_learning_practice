from sklearn import tree

def main():
    print("Ball Classification Case Study")

    # Commit  5
    
    Independent = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]
    Dependent = [1,1,2,1,2,1,2,1,1,1,2,1,2]
    # Testing Label = [1, 2]

    # model is object of class DecisionTreeClassifier
    model = tree.DecisionTreeClassifier()

    # we send independent and dependent variables as parameters to model.fit()
    # this is essentially training the model
    model = model.fit(Independent,Dependent)

    # this is testing the model
    Result = model.predict([[35,1],[95,0]])

    print("Predicted result of model is : ",Result)

if __name__ == "__main__":
    main()