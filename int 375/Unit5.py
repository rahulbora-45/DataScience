import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns ### for z -score
import statsmodels.api as sm ##for z-test

##Load Iris dataset from seaborn
df=sns.load_dataset("iris")

# ##Z -Test
sample=df['sepal_length'].sample(30,random_state=42) 
pop_mean=df['sepal_length'].mean() ##Population mean
pop_std=df['sepal_length'].std() ##Population standard deviation
z_score=(sample.mean()-pop_mean)/(pop_std/np.sqrt(len(sample)))
p_value=stats.norm.sf(abs(z_score))*2

print(f"Z-test: Z-score ={z_score:.4f},p-value = {p_value:.4f}")


