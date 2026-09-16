import matplotlib.pyplot as plt

def main():
    language = ["C", "C++", "Java", "Python"]
    students = [30,40,35,55]

    plt.bar(
        language,                   # X-axis
        students,                   # Y-axis
        width = 0.6,                # width of bar
        edgecolor = "black",        # border color of bar
        linewidth = 1,              # width of bar border
        alpha = 1.0,                # transparency (0.0 - 1.0)
        label = "Students"          # legend text
    )

    plt.title("Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of Students")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()