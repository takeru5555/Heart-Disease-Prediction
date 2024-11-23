from sklearn.metrics import accuracy_score,  confusion_matrix, classification_report
import pandas as pd
def print_score(clf, X_train, y_train, X_test, y_test, train=True):
    if train:
        pred = clf.predict(X_train)
        clf_report = pd.DataFrame(classification_report(y_train, pred, output_dict=True))
        print("Train Result: \n =======================")
        print(f"Accuracy Score: {accuracy_score(y_train, pred) * 100: .2f}%")
        print("__________________________")
        print(f"Classification Report: \n {clf_report}")
        print("__________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_train, pred)} \n")
    
    elif train == False:
        pred = clf.predict(X_test)
        clf_report = pd.DataFrame(classification_report(y_test, pred, output_dict=True))
        print("Test Result: \n ========================")
        print(f"Accuracy Score: {accuracy_score(y_test, pred) * 100:.2f}%")
        print("_______________________")
        print(f"Classification Report: \n{clf_report}")
        print("_______________________")
        print(f"Confussion Matrix: \n {confusion_matrix(y_test, pred)} \n")

