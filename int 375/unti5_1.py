# import numpy as np
# from scipy.stats import chi2_contingency
# ###Obsered frequency table from your image
# #Rows:[cs,Non-CS]
# #Columns:[Python,Java,C++]
# observed =np.array([
#     [30,10,10], #CS
#     [10,20,20]  #Non -CS
# ])
# ##Perfom the chi-square test
# chi2_stat,p_value,dof,expected =chi2_contingency(observed)

# #Display the results
# print("Chi-Square Test of Independence")
# print("--------------------------------------------")
# print(f"Chi-Square Statistic ={chi2_stat:.4f}") 
# print(f"Degrees of Freedom ={dof}")
# print(f"P-value       ={p_value:.4f}")
# print("\nExpected Frequencies: ")
# print(expected)
# ##Interpretation at 0.05 significant level
# alpha=0.05
# if p_value<alpha:
#     print("\nReject the null hypothesis:There is a significant")
# else:
#     print("\n Fail to reject thr null hypothesis: No significant ")



# '''Q2
# A/B     B1   B2     B3
# A1      35   52.5   12.5
# A2      28.1 42.1   9.8
# A3      6.9 10.4    2.7
# '''

# import numpy as np
# from scipy.stats import chi2_contingency

# observed =np.array([[35,52.5 ,12.5],
#                     [28.1,42.1,9.8],
#                     [6.9,10.4,2.7]])
# ##Perfom the chi-square test
# chi2_stat,p_value,dof,expected =chi2_contingency(observed)

# #Display the results
# print("Chi-Square Test of Independence")
# print("--------------------------------------------")
# print(f"Chi-Square Statistic ={chi2_stat:.4f}") 
# print(f"Degrees of Freedom ={dof}")
# print(f"P-value       ={p_value:.4f}")
# print("\nExpected Frequencies: ")
# print(expected)
# ##Interpretation at 0.05 significant level
# alpha=0.05
# if p_value<alpha:
#     print("\nReject the null hypothesis:There is a significant difference betwwent he two groups")
# else:
#     print("\n Fail to reject thr null hypothesis: No significant "

# from scipy import  stats
# group_a=[23,43,59,69]
# group_b=[12,42,96,103]
# t,p=stats.ttest_ind(group_a,group_b, equal_var=True)


# print(f"t-statistics: {t:.4f}")
# print(f"p-value: {p:.4f}")


# alpha=0.05
# if p<alpha:
#     print("\nReject the null hypothesis:There is a significant difference betwwent he two groups")
# else:
#     print("\n Fail to reject thr null hypothesis: No significant ")


###########-----------------------------------------------------------------------

from statsmodels.stats.proportion import proportions_ztest
from scipy import stats

# Group 1 : 50 conversions out of 200 visits
#Gruoup 2L 65 conversions out  of 220  visits

conv_rate=[50,65]
samples=[200,200]
z_stat,p_value=proportions_ztest(conv_rate,samples)
print("Z-statistic:",z_stat)
print("P-value:",p_value)
alpha=0.05
if p_value<alpha:
    print("Reject thr null hypothesis -sigificant difference between proportions")
else:
    print("Fail to reject the  null hypothesis -no significant difference between the proportions")

########################## t test#######################

#Sample data: revenue per user
g1 = [23, 21, 19, 24, 25]
g2 = [27, 29, 26, 30, 28]
t_stat_two, p_value_two = stats.ttest_ind(g1, g2, equal_var=True)
print("Two-sample t-test (Independent samples, equal variance):")
print(f"T-statistic = {t_stat_two:.4f}")
print(f"P-value = {p_value_two:.4f}")

if p_value_two < alpha:
    print("Conclusion: Reject the null hypothesis. There is a significant differ")
else:
    print("Conclusion: Fail to reject the null hypothesis. No significant differ")


###############################Shapiro-Wilh Test Statistics###################################

import numpy as np
data=[12.1,13.4,13.8,14.0,13.9,13.3,12.9,13.7,13.5,14.1]
statistic,p_value=stats.shapiro(data)
print("Shapiro-Wikh Test  Statistics",statistic)
print("P-value: ",p_value)
alpha=0.05





