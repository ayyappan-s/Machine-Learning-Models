import pickle
sepalLength=float(input("Enter Sepal Length In Centimeter: "))
sepalWidth=float(input("Enter Sepal Width In Centimeter: "))
petalLength=float(input("Enter Petal Length In Centimeter: "))
petalWidth=float(input("Enter Petal Width In Centimeter: "))
filename="irisclassification.sav"
model=pickle.load(open(filename,'rb'))
result=model.predict([[sepalLength,sepalWidth,petalLength,petalWidth]])
if result[0]==0:
    print("Iris-setosa")
if result[0]==1:
    print("Iris-versicolor")
if result[0]==2:
    print("Iris-virginica")
