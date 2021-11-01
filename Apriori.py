import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

file_Path = r'C:\Users\Ayodeji.odebiyi.GLOBALACCELEREX\Desktop\LECTURES\DATA MINING\PRAC 4\specs\gpa_question1.csv'
file_Bank = r'C:\Users\Ayodeji.odebiyi.GLOBALACCELEREX\Desktop\LECTURES\DATA MINING\PRAC 4\specs\bank_data_question2.csv'

store_Data = pd.read_csv(file_Path)
bank_data = pd.read_csv(file_Bank)
print(store_Data)

final_data = pd.DataFrame(columns=['Transaction','Items'])
store_Data = store_Data.T
for col in store_Data.columns:
    col_data = list(store_Data[col])
    
    temp_dict = {'Transaction':[int(col)]*len(col_data),  'Items':col_data }
    temp_df = pd.DataFrame(temp_dict)
    final_data = final_data.append(temp_df,ignore_index=True)
final_data.head()

print (final_data)

final_data_dummy = pd.get_dummies(final_data['Items'])
final_data_dummy['Transaction'] = final_data['Transaction']
print(final_data_dummy)

def encode_units(x):
    if x <=  0:
        return 0
    if x >=  1:
        return 1
format_data= final_data_dummy.groupby('Transaction').sum()
print(format_data)
format_data = format_data.applymap(encode_units)
format_data.head()

print(format_data)

#Question 2 and 4
frequent_itemsets  =  apriori(format_data, min_support = 0.15, use_colnames = True).sort_values(by='support',ascending=False)
frequent_itemsets.head()
print(frequent_itemsets)

results_df = pd.DataFrame(frequent_itemsets)
results_df.to_csv('output/question1_out_apriori.csv', index=False)

pd.read_csv('output/question1_out_apriori.csv',index_col='support')


#question 5 and 6
result_association = association_rules(frequent_itemsets, metric = "confidence", min_threshold=0.6)
result_association.sort_values('confidence',ascending=False)
print(result_association)

result2_df = pd.DataFrame(result_association)
result2_df.to_csv('output/question1_out_rules06.csv', index=False)



#question 7and 8
result_association_2 = association_rules(frequent_itemsets, metric = "confidence", min_threshold=0.9)
result_association.sort_values('lift',ascending=False)
print(result_association_2)

result3_df = pd.DataFrame(result_association_2)
result3_df.to_csv('output/question1_out_rules09.csv', index=False)

#Number 2
print (pd.qcut(bank_data['age'], q=3, labels=False))
print (pd.qcut(bank_data['income'], q=3, labels=False))


    
one_hot_encoded_data = pd.get_dummies(bank_data[['sex','region','married','children','car','save_act','current_act','mortgage','pep']], columns = ['sex','region','married','children','car','save_act','current_act','mortgage','pep'])

print(one_hot_encoded_data)
#Question 2_2_3
fp_freqitems = fpgrowth(one_hot_encoded_data, min_support=0.20, use_colnames=True).sort_values(by='support',ascending=False)

fp_result = pd.DataFrame(fp_freqitems)
fp_result.to_csv('output/question2_out_fpgrowth.csv', index=False)

#Number2_4
fp_association = association_rules(fp_freqitems, metric="confidence", min_threshold=0.0).sort_values(by='confidence',ascending=False)
print(fp_association)
confidence = 1

while True:
    if len (association_rules(fp_freqitems, metric="confidence", min_threshold=confidence)) >=10:
        break
    confidence -=0.01

print (f"Question2_confidence_value:{confidence} ")


fp_df = pd.DataFrame(fp_association)
fp_df.to_csv('output/question2_out_rules.csv', index=False)
