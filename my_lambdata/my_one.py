import pandas as pd

data = {'y_true':    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
        'y_pred': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
        }

df = pd.DataFrame(data, columns=['y_true','y_pred'])

confusion_matrix = pd.crosstab(df['y_true'], df['y_pred'], rownames=['Actual'], colnames=['Predicted'])
print (confusion_matrix)