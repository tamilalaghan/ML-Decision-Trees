import pandas as pd
from dataclasses import dataclass
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier



@dataclass
class LoansDataFrame:
    filename : str

    def toPandasDataFrame(self):
        return pd.read_csv(self.filename)
    

inputfilename = "loan.csv"
loans = LoansDataFrame(inputfilename)
loans_df = loans.toPandasDataFrame()

print(loans_df.info())
# # print(loans_df.describe())

# #Box Plot Default and Income
# plt.figure(figsize=(5,4))
# sns.boxplot( data=loans_df, x='Default', y='Income')
# plt.title("Box Plot B/W Default and Income")

# #Box Plot Default and Loan Amount
# plt.figure(figsize=(5,4))
# sns.boxplot(data=loans_df,x='Default',y='Loan Amount')
# plt.title("Box Plot B/W Default and Loan Amount")

# #Scatter Plot Default and Loan Amount and Income
# plt.figure(figsize=(5,4))
# plt.title("Scatter Plot between LoanAmount and Income")
# sns.scatterplot(data=loans_df, x='Loan Amount', y='Income', hue='Default',style='Default',markers=["^","o"])
# plt.legend(bbox_to_anchor=(1,1),loc="upper left")
# plt.tight_layout()
# plt.show()


# Response
y = loans_df[['Default']]

# Predictors
x = loans_df[['Income', 'Loan Amount']]

# Split the Data into Training and Test Sets
x_train, x_test, y_train, y_test = train_test_split(x,y,
                                   test_size=0.2, random_state=456)

print(f"****Training Testing Split****\n x Train = {x_train.shape}\n x Test  = {x_test.shape}\n y Train = {y_train.shape}\n y Test  = {y_test.shape} ")


# Model Training
decisiontree = DecisionTreeClassifier(random_state=456)
model = decisiontree.fit(x_train,y_train)

# Model Evaluation
print("The Model Prediction Score is : ",model.score(x_test,y_test))