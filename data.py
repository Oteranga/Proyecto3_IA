import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def parse_data(filename1 = 'dataset_tissue.txt', filename2 = 'classes.txt'):
    df = pd.read_csv(filename1, delimiter = ",")
    df.rename(columns={'Unnamed: 0':'ROW_NAME'}, inplace=True)
    df = df.T
    col_num = df.columns.size
    row_names = df.iloc[:,0]
    x_features = df.iloc[:,1:col_num-1]
    
    y_values = pd.read_csv(filename2, delimiter = ",")
    y_values.rename(columns={'x':'tissue'}, inplace=True)
    y_values = y_values.iloc[:,1]
    return x_features, y_values

def reduce_dim(df):
    X_std = StandardScaler().fit_transform(df)
    print(X_std)
    print(X_std.mean(axis=0))
    
    pca_data = PCA(n_components=2)
    principalComponents = pca_data.fit_transform(X_std)
    principal_Df = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
    print(principal_Df.tail())
    print('Explained variation per principal component: {}'.format(pca_data.explained_variance_ratio_))
    plt.figure()
    plt.figure(figsize=(10,10))
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=14)
    plt.xlabel('Principal Component - 1',fontsize=20)
    plt.ylabel('Principal Component - 2',fontsize=20)
    plt.title("Principal Component Analysis of Tissues",fontsize=20)
    targets = ['Component 2', 'Component 1']
    colors = ['r', 'g']
    for target, color in zip(targets,colors):
        indicesToKeep = df['label'] == target
        plt.scatter(principal_Df.loc[indicesToKeep, 'principal component 1']
                , principal_Df.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)

    plt.legend(targets,prop={'size': 15})

x_features,y_values = parse_data()
#reduce_dim(data)