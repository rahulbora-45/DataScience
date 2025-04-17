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

from scipy import  stats
group_a=[23,43,59,69]
group_b=[12,42,96,103]
t,p=stats.ttest_ind(group_a,group_b, equal_var=True)


print(f"t-statistics: {t:.4f}")
print(f"p-value: {p:.4f}")


alpha=0.05
if p<alpha:
    print("\nReject the null hypothesis:There is a significant difference betwwent he two groups")
else:
    print("\n Fail to reject thr null hypothesis: No significant ")





