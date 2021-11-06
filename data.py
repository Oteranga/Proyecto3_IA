import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns
from sklearn.preprocessing import StandardScaler


def parse_data(filename1 = 'dataset_tissue.txt', filename2 = 'classes.txt'):
    df = pd.read_csv(filename1, delimiter = ",")
    df.rename(columns={'Unnamed: 0':'ROW_NAME'}, inplace=True)
    col_num = df.columns.size
    df = df.T
    
    y_values = pd.read_csv(filename2, delimiter = ",")
    y_values.rename(columns={'x':'tissue'}, inplace=True)
    y_list = y_values.iloc[:,-1].values.tolist()
    
    x_features = df.iloc[1:col_num,:]
    full_data = x_features.copy()
    full_data['tissue'] = y_list
    return full_data, x_features

def reduce_dim(df,num_components):
    #FIRST WAY
    y = df.iloc[:,-1].values.tolist()
    
    #SECOND WAY
    """ pca = PCA(n_components=num_components)
    pc = pca.fit_transform(df.iloc[:,:-1])
    columns_list = []
    for i in range(num_components):
        name = "Principal component"+str(i)
        columns_list.append(name)
    pc_df = pd.DataFrame(data = pc, columns = columns_list)
    pc_df['y'] = df.iloc[:,-1].values.tolist()
    print(pc_df.head())
    print('Variation per principal component: {}'.format(pca.explained_variance_ratio_)) """
    
    """ plt.figure(figsize=(16,7))
    sns.scatterplot(
        x="Principal component 1", y="Principal component 2",
        hue="y",
        palette=sns.color_palette("hls", 7),
        data=pc_df,
        legend="full",
        alpha=0.3
    ) """