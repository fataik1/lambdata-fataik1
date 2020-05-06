y_actual = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
y_predicted = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]

import numpy as np
import pandas as pd

class c_matrix():
    # define initialize function for class
    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred
    # define function of function that creates the main array we will use for the rest of our class.methods()
    def confusion_matrix(self, y_true, y_pred):
        '''
        This docstring's creator and owner: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix
        Compute confusion matrix to evaluate the accuracy of a classification.
        By definition a confusion matrix **C** is such that **C_{ij}** is equal to the number of observations known to be 
        in group *i* and predicted to be in group *j*.
        Thus in binary classification, the count of true negatives is **C_{0,0}**, 
        false negatives is **C_{1,0}**, true positives is **C_{1,1}** and false positives is **C_{0,1}**.
        Parameters:
            y_true: array-like of shape (n_samples,)
            Ground truth (correct) target values.
            y_pred: array-like of shape (n_samples,)
            Estimated targets as returned by a classifier.
            labels: array-like of shape (n_classes), default=None
            List of labels to index the matrix. This may be used to reorder or select a subset of labels. If None is given, those 
            that appear at least once in y_true or y_pred are used in sorted order.
            sample_weight: array-like of shape (n_samples,), default=None
            Sample weights.
            normalize{'true', 'pred', 'all'}, default=None
            Normalizes confusion matrix over the true (rows), predicted (columns) conditions or all the population. If None, confusion matrix will not be normalized.
        Returns:
        C: ndarray of shape (n_classes, n_classes)
        Confusion matrix.
        '''
        # defines X, the shape of true_label_array
        X = len(np.unique(y_true)) # Number of classes 
        # creates zeroes array with shape length X above
        result = np.zeros((X, X))
        # creates labels list with unique values of true_label_array
        labels = np.unique(y_true)
        # using list comprehension to create a columns_list from labels
        columns = [f'Predicted {label}' for label in labels]
        # using list comp. to create an index_list from labels
        index = [f'Actual {label}' for label in labels]
        # create the confusion matrix array by indexing into the arrays
        for i in range(len(y_true)):
            result[y_true[i]][y_pred[i]] += 1
        # change type of result to a DF
        result = pd.DataFrame((result), index=index, columns=columns)
        return result
if __name__ == '__main__':
    y_actual = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
    y_predicted = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]
    cm = c_matrix(y_true=y_actual, y_pred=y_predicted).confusion_matrix(y_actual, y_predicted)
    print(cm)

    #hopefully this adds to github now