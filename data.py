import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from seaborn.palettes import color_palette
from sklearn.decomposition import PCA
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import pandas as pd
import aux as a
from mpl_toolkits import mplot3d
plt.style.use('ggplot')

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
    x = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    
    scaler = StandardScaler()
    scaler.fit(x)
    x_scaled = scaler.transform(x)
    pca = PCA(n_components=num_components)
    pca.fit(x_scaled)
    x_pca = pca.transform(x_scaled)
    
    cumsum_variance = np.around(np.cumsum(pca.explained_variance_ratio_*100),2)
    np.savetxt("files/explained_variance.txt",pca.explained_variance_ratio_*100,delimiter=",")
    np.savetxt("files/cumsum_explained_variance.txt",cumsum_variance,delimiter=",")
    
    plt.plot([*range(1,num_components+1,1)],cumsum_variance,marker='o')
    plt.title("Variance for "+str(num_components)+" components")
    plt.xlabel('# of components')
    plt.ylabel('Explained variance')
    plt.savefig("plots/var_for_"+str(num_components))
    
    """ for i in range(num_components):
        print("Variance explained by the First " + str(i+1) + " principal component(s) =",np.cumsum(pca.explained_variance_ratio_*100)[i]) """
    
    plotting(num_components,x_pca,y)


def plotting(num_components,x_pca,y):
    y_list = y.values.tolist()
    target_names = a.get_unique_values(y_list)
    labels,new_y = convert_tissue_to_num(y_list,target_names)
    
    if num_components==2:
        plt.figure(figsize=(10,7))
        sns.scatterplot(x=x_pca[:,0],y=x_pca[:,1],s=70,hue=y_list,palette=color_palette("hls",7),alpha=0.6)
        plt.xlabel("First principal component")
        plt.ylabel("Second principal component")
        plt.savefig("plots/2d_plot")
    
    if num_components==3:
        plt.figure(figsize=(12,8))
        ax = plt.axes(projection='3d')
        sc = ax.scatter(x_pca[:,0],x_pca[:,1],x_pca[:,2],c=new_y,s=50,alpha=0.6)
        ax.legend(target_names)
        plt.legend(*sc.legend_elements(), bbox_to_anchor=(1.05, 1), loc=2)
        ax.set_xlabel("First principal component")
        ax.set_ylabel("Second principal component")
        ax.set_zlabel("Third principal component")
        plt.savefig("plots/3d_plot")


def convert_tissue_to_num(y,target_names):
    dic = dict()
    new_y = []
    for i in range(len(target_names)):
        dic[target_names[i]] = i+1
    
    for i in range(len(y)):
        new_y.append(dic[y[i]])
    
    return list(dic.values()),new_y