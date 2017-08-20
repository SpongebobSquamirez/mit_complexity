# Logistic Regression
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


#set up data structure
dataset = dict()
dataset["feature_names"] = ["a", "b", "c", "d", 
        "e", "f", "g", "h", "i"]
all_categories = ['j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 
                's', 't', 'u', 'v', 'w']
max_records = 210795 #for limiting the query_with_fetchmany

for cat in all_categories:
    dataset["data"] = []
    dataset["labels"] = []
    category = cat
    print(category)
    for project in query_with_fetchmany(category, max_records):
        #in the database retriever, category is the second to last variable
        #so we want to exclude it (since we iterate through them all here)
        dataset["data"].append(project[:-2])
        
        #the database retriever puts the label/outcome as the last variable
        dataset["labels"].append(project[-1])

    #find the baseline/average 'Yes/True/Success' rate to beat
    print("baseline rate:")
    print(str(sum(dataset["labels"])/len(dataset["labels"])*100))
    
    # fit a logistic regression model to the data
    model = LogisticRegression()

    #first argument is the features, second is the labels
    model.fit(dataset["data"], dataset["labels"])
    print(model)
    
    # make predictions
    expected = dataset["labels"] #this is the true Y
    predicted = model.predict(dataset["data"])
    # summarize the fit of the model
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
