# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# %%
sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")

df = pd.read_csv("heart.csv")
print(df.head())

pd.set_option("display.float", "{:.2f}".format)
# df.describe()

# %%
df.target.value_counts().plot(kind="bar", color=["salmon", "lightblue"])

# %%
df.isna().sum()

# %%
categorical_val = []
continuous_val = []

for column in df.columns:
    print("=====================")
    print(f"{column} : {df[column].unique()}")
    if len(df[column].unique()) <= 10:
        categorical_val.append(column)
    else:
        continuous_val.append(column)



# %%
plt.figure(figsize=(15, 15))

for i, column in enumerate(categorical_val, 1):
    plt.subplot(3,3,i)
    df[df['target'] == 0][column].hist(bins=35, color='blue', label='Have Heart Disease = No', alpha=0.6)
    df[df['target'] == 1][column].hist(bins=35, color='red', label='Have Heart Disease = YES', alpha = 0.6)
    plt.legend()
    plt.xlabel(column)

# %%
plt.figure(figsize=(15,15))

for i, column in enumerate(continuous_val, 1):
    plt.subplot(3,2,i)
    df[df["target"] == 0][column].hist(bins=35, color='blue', label='Have Heart Disease = NO', alpha=0.6)
    df[df['target'] == 1][column].hist(bins=35, color='red', label='Have Heart Disease = YES', alpha=0.6)
    plt.legend()
    plt.xlabel(column)

# %%
plt.figure(figsize=(10,8))

# Scatter with postive examples
plt.scatter(df.age[df.target==1], df.thalach[df.target == 1], c='salmon')

# Scatter with negative example
plt.scatter(df.age[df.target == 0], df.thalach[df.target == 0], c='lightblue')

# Add some helpful info
plt.title("Heart Disease in function of Age and Max Heart Rate")
plt.xlabel('Age')
plt.ylabel("Max Heart Rate")
plt.legend(["Disease", "No Disease"])

# %%
corr_matrix = df.corr()
fig, ax = plt.subplots(figsize=(15,15))
ax = sns.heatmap(corr_matrix, annot=True, linewidths=0.5, fmt=".2f", cmap="YlGnBu")
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)


# %%
df.drop('target', axis=1).corrwith(df.target).plot(kind='bar', grid=True, figsize=(12, 8), title="Correlation with target")

# %%
# print(categorical_val)
categorical_val.remove('target')
print(df.head())
dataset = pd.get_dummies(df, columns=categorical_val)
print(dataset)
from sklearn.preprocessing import StandardScaler

s_sc = StandardScaler()
col_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
dataset[col_to_scale] = s_sc.fit_transform(dataset[col_to_scale])

# %%
from sklearn.model_selection import train_test_split

X = dataset.drop('target', axis=1)
print(X.head())
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# %%
from sklearn.linear_model import LogisticRegression
from helper import print_score

lr_clf = LogisticRegression(solver='liblinear')
lr_clf.fit(X_train, y_train)

print_score(lr_clf, X_train, y_train, X_test, y_test, train=True)
print_score(lr_clf, X_train, y_train, X_test, y_test, train=False)



# %%
from sklearn.metrics import accuracy_score

test_score = accuracy_score(y_test, lr_clf.predict(X_test)) * 100
train_score = accuracy_score(y_train, lr_clf.predict(X_train)) * 100

results_df = pd.DataFrame(data=[["Logistic Regression", train_score, test_score]], columns=["Models", 'Training Accuracy %', 'Testing Accuracy %'])
print(X_test)
print("Predict Result", lr_clf.predict(X_test))

# %%
def predict(data):
    # print(data)
    real_data = pd.DataFrame(data=[[58,1,1,125,220,0,1,144,0,0.4,1,4,3]], 
                            columns=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"])

    real_data = pd.DataFrame([data])
    print(real_data)
    # Step 1: One-hot encode the real test data
    # categorical_val = ['cp', 'restecg', 'slope', 'thal']  # Example categorical columns
    # print(categorical_val)
    real_data_encoded = pd.get_dummies(real_data, columns=categorical_val)

    # Step 2: Reindex to match the training data
    real_data_encoded = real_data_encoded.reindex(columns=X_train.columns, fill_value=0)

    # Step 3: Standardize the features
    # print(col_to_scale)
    real_data_encoded[col_to_scale] = s_sc.transform(real_data_encoded[col_to_scale])
    # print(real_data_encoded)

    # Step 4: Make predictions
    predictions = lr_clf.predict(real_data_encoded)

    # prediction = lr_clf.predict(real_data_encoded)
    # predicted_probability = lr_clf.predict_proba(real_data)

    return "Predicted Classes:",  "Heart Disease YES" if predictions == 1 else "NO"
# print("Predicted Probability", predicted_probability)
# lr_clf.predict(real_data)


