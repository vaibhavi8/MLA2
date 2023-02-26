#-------------------------------------------------------------------------
# AUTHOR: Vaibhavi Jhawar
# FILENAME: decision_tree_2.py
# SPECIFICATION: Creating a decision tree to determine whether a patient should get lenses (from assignment 2)
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)


    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    for i in range(len(dbTraining)):
        temp = []
        for j in range(len(dbTraining)):
            if j == 0:
                if dbTraining[i][j] == 'Young':
                    temp.append(0)
                elif dbTraining[i][j] == 'Presbyopic':
                    temp.append(1)
                else:
                    temp.append(2)
            if j == 1:
                if dbTraining[i][j] == 'Myope':
                    temp.append(0)
                else:
                    temp.append(1)
            if j == 2:
                if dbTraining[i][j] == 'Yes':
                    temp.append(0)
                else:
                    temp.append(1)
            if j == 3:
                if dbTraining[i][j] == 'Normal':
                    temp.append(0)
                else:
                    temp.append(1)
        X.append(temp)


    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    for i in dbTraining:
        for j in range(len(i)):
            if j == (len(i)-1):
                if i[j]=="Yes":
                    Y.append(1)
                    
                elif i[j] =="No":
                    Y.append(0)
                else:
                    print("Error")
                    

    #loop your training and test tasks 10 times here
    yes = 0
    no = 0
    for i in range (10):
        prediction = []

       #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append(row)


    #    for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
            # print(dbTest)
            tempFeat = []
            for i in range(len(dbTest)):
                temp = []
                for j in range(len(dbTest[i])):
                    if j == 0:
                        if dbTest[i][j] == 'Young':
                            temp.append(0)
                        elif dbTest[i][j] == 'Presbyopic':
                            temp.append(1)
                        else:
                            temp.append(2)
                    if j == 1:
                        if dbTest[i][j] == 'Myope':
                            temp.append(0)
                        else:
                            temp.append(1)
                    if j == 2:
                        if dbTest[i][j] == 'Yes':
                            temp.append(0)
                        else:
                            temp.append(1)
                    if j == 3:
                        if dbTest[i][j] == 'Normal':
                            temp.append(0)
                        else:
                            temp.append(1)
                tempFeat.append(temp)
            tempResult = []
            for i in dbTest:
                for j in range(len(i)):
                    if j == (len(i)-1):
                        if i[j]=="Yes":
                            tempResult.append(1)
                            
                        elif i[j] =="No":
                            tempResult.append(0)
                        else:
                            print("Error")
            # print(tempFeat)
           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here
            for i in tempFeat:

                x = clf.predict([i])[0]
                prediction.append(x)

            for i in range(len(prediction)):
                if prediction[i] == tempResult[i]:
                    yes += 1
                else:
                    no += 1



            
    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    averageAcurracy = (yes/(yes+no))
    

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("Final accuracy when training on %s : %f" %(ds, averageAcurracy))