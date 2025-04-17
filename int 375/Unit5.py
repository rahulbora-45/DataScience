# import numpy as np
# import pandas as pd
# import scipy.stats as stats
# import seaborn as sns ### for z -score
# import statsmodels.api as sm ##for z-test

# ##Load Iris dataset from seaborn
# df=sns.load_dataset("iris")

# # ##Z -Test
# sample=df['sepal_length'].sample(30,random_state=42) 
# pop_mean=df['sepal_length'].mean() ##Population mean
# pop_std=df['sepal_length'].std() ##Population standard deviation
# z_score=(sample.mean()-pop_mean)/(pop_std/np.sqrt(len(sample)))
# p_value=stats.norm.sf(abs(z_score))*2

# print(f"Z-test: Z-score ={z_score:.4f},p-value = {p_value:.4f}")





# import math 
# from scipy.stats import norm

# #Sample data
# sample_mean=169.5
# population_mean=168
# population_std_dev=3.9
# sample_size=36
# alpha=0.05
# tail='two'
# ##Standar error
# standard_error=population_std_dev/math.sqrt(sample_size)
# ##Z-score
# z_score=(sample_mean-population_mean)/standard_error
# ## p-value based on the type of test
# if tail=='two':
#     p_value=2*(1-norm.cdf(abs(z_score)))
#     print(norm.cdf(abs(z_score)))
# elif tail =='left':
#     p_value=norm.cdf(z_score)
# elif tail=='right':
#     p_value=1-norm.cdf(z_score)
# else:
#     raise ValueError ("tail must be 'two','left',or 'right'")
# #output
# if p_value<alpha:
#     conclusion="Reject the null hypothesis"
# print(f"Z-score: {z_score:.4f}")
# print(f"P-value: {p_value:.4f}")



# #Z-test = (sample_mean - population_mean) / (population_std_dev / math.sqrt(sample_size)) 
# #T-test = (sample_mean - population_mean) / (sample_std_dev / math.sqrt(sample_size))
# # Assuming a normal distribution, we can use the Z-test for large sample sizes




from scipy import stats
#Significance level
alpha=0.05
#One_sample t_test
sample_data=[12,15,14,10,13,14,15,16,14,13]
population_mean=13
t_stat_one,p_value_one=stats.ttest_lsam(sample_data,population_mean)
print("One-sample t-test:")
print(f"T-statistic ={t_stat_one:.4f}")
print(f"P-value= {p_value_one:.4f}")
if p_value_one<alpha:
    print("Conlusion: Reject the null hypothesis.There is a significant diffrence ")
else:
    print("Conclusion: Fail to reject the null hypothese.No significant differ")

#Two -sample independent t-test(equal variance assumed)
group1=[23,21,19,24,25]
group2=[27,29,26,30,28]
t_stat_two,p_value_two=stats.ttest_ind(group1,group2,equal_var=True)
print("Two-sample t-test (Independent samples,equl variance):")
print(f"T-statistic={t_stat_two:.4f}")
print(f"P-value = {p_value_two: .4f}")
if p_value_two<alpha:
    print("Conclusion :Reject the null hypothesis.There is significant dofference ")
else:
    print("Conclusion: Fail to reject the null hypothesis.No significant difference")




