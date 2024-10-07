#!/usr/bin/env python
# coding: utf-8

# Part 1

# In[35]:


import pandas as pd


# In[36]:


datasets = []


# In[37]:


#items for dataset 1: Dick's Sporting Goods dataset
db1Items = set(['Basketball', 'Basketball Shoes', 'Gatorade Bottle', 'Swim Cap', 'Swim Goggles', 'Running Shoes', 'Golf Balls', 'Golf Shoes', 'Protein Powder', 'Electrolyte Gels'])
transactions = [
    ['Basketball', 'Basketball Shoes', 'Gatorade Bottle'],
    ['Swim Cap', 'Swim Goggles'],
    ['Running Shoes', 'Electrolyte Gels', 'Gatorade Bottle'],
    ['Golf Balls', 'Golf Shoes'],
    ['Protein Powder', 'Electrolyte Gels'],
    ['Basketball', 'Gatorade Bottle'],
    ['Running Shoes', 'Gatorade Bottle'],
    ['Swim Cap', 'Swim Goggles'],
    ['Swim Cap', 'Gatorade Bottle'],
    ['Swim Goggles', 'Gatorade Bottle'],
    ['Basketball Shoes', 'Gatorade Bottle'],
    ['Golf Shoes', 'Golf Balls'],
    ['Running Shoes', 'Protein Powder', 'Electrolyte Gels'],
    ['Basketball', 'Basketball Shoes'],
    ['Running Shoes', 'Electrolyte Gels'],
    ['Swim Cap', 'Swim Goggles', 'Gatorade Bottle'],
    ['Golf Shoes', 'Golf Balls'],
    ['Protein Powder', 'Gatorade Bottle'],
    ['Basketball', 'Protein Powder'],
    ['Running Shoes', 'Electrolyte Gels'],
    ['Basketball', 'Basketball Shoes', 'Gatorade Bottle'],
    ['Running Shoes', 'Electrolyte Gels'],
    ['Swim Cap', 'Swim Goggles'],
    ['Golf Balls', 'Golf Shoes'],
    ['Basketball Shoes', 'Gatorade Bottle'],
    ['Running Shoes', 'Gatorade Bottle', 'Protein Powder'],
    ['Protein Powder', 'Electrolyte Gels'],
    ['Swim Goggles', 'Gatorade Bottle'],
    ['Basketball', 'Basketball Shoes'],
    ['Running Shoes', 'Electrolyte Gels', 'Gatorade Bottle'],
    ['Swim Cap', 'Gatorade Bottle'],
    ['Basketball', 'Gatorade Bottle'],
    ['Golf Shoes', 'Golf Balls'],
    ['Running Shoes', 'Protein Powder'],
    ['Basketball', 'Protein Powder', 'Gatorade Bottle'],
    ['Swim Cap', 'Swim Goggles', 'Gatorade Bottle'],
    ['Running Shoes', 'Electrolyte Gels', 'Gatorade Bottle'],
    ['Basketball Shoes', 'Gatorade Bottle'],
    ['Golf Balls', 'Golf Shoes'],
    ['Running Shoes', 'Electrolyte Gels'],
    ['Protein Powder', 'Gatorade Bottle'],
    ['Swim Goggles', 'Gatorade Bottle'],
    ['Basketball', 'Basketball Shoes'],
    ['Running Shoes', 'Electrolyte Gels', 'Protein Powder'],
    ['Golf Shoes', 'Golf Balls'],
    ['Basketball', 'Gatorade Bottle'],
    ['Swim Cap', 'Swim Goggles'],
    ['Protein Powder', 'Electrolyte Gels'],
    ['Running Shoes', 'Gatorade Bottle'],
    ['Golf Balls', 'Golf Shoes'],
    ['Basketball Shoes', 'Gatorade Bottle'],
    ['Swim Goggles', 'Gatorade Bottle'],
    ['Basketball', 'Basketball Shoes', 'Gatorade Bottle'],
    ['Running Shoes', 'Protein Powder'],
    ['Swim Cap', 'Gatorade Bottle'],
    ['Golf Shoes', 'Golf Balls'],
    ['Running Shoes', 'Electrolyte Gels'],
    ['Basketball', 'Protein Powder', 'Gatorade Bottle'],
    ['Swim Goggles', 'Gatorade Bottle'],
    ['Basketball Shoes', 'Gatorade Bottle'],
    ['Golf Balls', 'Golf Shoes'],
    ['Running Shoes', 'Electrolyte Gels', 'Gatorade Bottle'],
    ['Basketball', 'Gatorade Bottle'],
    ['Swim Cap', 'Swim Goggles'],
    ['Protein Powder', 'Electrolyte Gels'],
    ['Golf Shoes', 'Golf Balls'],
    ['Running Shoes', 'Gatorade Bottle'],
    ['Basketball Shoes', 'Gatorade Bottle']
]
db1 = pd.DataFrame({'Transaction Number':range(1,len(transactions)+1) , 'Items Bought':transactions})
db1.to_csv('DicksSportingGoods.csv', index=False)
datasets.append('DicksSportingGoods.csv')


# In[38]:


#items for dataset 2: Best Buy
db2Items = set(['Speaker', 'Computer Mouse', 'Keyboard', 'Desktop PC', 'Smart Phone', 'TV', 'Smart Phone Charger', 'Refrigerator', 'PlayStation', 'Washing Machine'])
transactions = [
  ['Smart Phone', 'Smart Phone Charger'],
  ['Desktop PC', 'Keyboard', 'Computer Mouse'],
  ['PlayStation', 'TV'],
  ['Smart Phone', 'Speaker'],
  ['TV', 'Speaker'],
  ['Washing Machine'],
  ['Refrigerator'],
  ['Smart Phone'],
  ['PlayStation'],
  ['Desktop PC', 'TV', 'Speaker'],
  ['Smart Phone', 'TV'],
  ['PlayStation', 'Speaker'],
  ['Desktop PC', 'Keyboard'],
  ['Smart Phone Charger'],
  ['Computer Mouse'],
  ['Desktop PC'],
  ['Smart Phone', 'TV', 'Smart Phone Charger'],
  ['Washing Machine', 'Refrigerator', 'Smart Phone'],
  ['TV'],
  ['Smart Phone', 'Smart Phone Charger', 'Computer Mouse']
]
db2 = pd.DataFrame({'Transaction Number':range(1,21) , 'Items Bought':transactions})
db2.to_csv('BestBuy.csv', index=False)
datasets.append('BestBuy.csv')


# In[39]:


#items for dataset 3: Home Depot
db3Items = set(['Nails', 'Hammer', 'Wood', 'Screws', 'Seeds', 'Fertilizer', 'Shovel', 'Lawnmower', 'Oven', 'Lightbulb'])
transactions = [
  ['Nails', 'Hammer', 'Wood'],
  ['Screws', 'Hammer', 'Wood'],
  ['Seeds', 'Fertilizer', 'Shovel'],
  ['Lawnmower', 'Seeds', 'Fertilizer'],
  ['Lightbulb'],
  ['Nails', 'Screws', 'Wood'],
  ['Hammer', 'Nails'],
  ['Shovel', 'Seeds', 'Fertilizer'],
  ['Lawnmower'],
  ['Screws', 'Hammer'],
  ['Lightbulb', 'Hammer'],
  ['Seeds', 'Lawnmower'],
  ['Oven'],
  ['Wood', 'Hammer', 'Nails'],
  ['Fertilizer', 'Shovel'],
  ['Seeds'],
  ['Lightbulb'],
  ['Hammer', 'Wood'],
  ['Oven'],
  ['Lawnmower', 'Fertilizer', 'Seeds']
]
db3 = pd.DataFrame({'Transaction Number':range(1,21) , 'Items Bought':transactions})
db3.to_csv('HomeDepot.csv', index=False)
datasets.append('HomeDepot.csv')


# In[40]:


#items for dataset 4: Staples
db4Items = set(['Pencil', 'Pen', 'Notebook', 'Binder', 'Paper', 'Printer', 'Tablet', 'Eraser', 'Stapler', 'Staples'])
transactions = [
    ['Pencil', 'Notebook'],
    ['Pen', 'Notebook'],
    ['Binder', 'Paper'],
    ['Printer', 'Paper'],
    ['Tablet', 'Pen'],
    ['Eraser', 'Pencil'],
    ['Stapler', 'Staples'],
    ['Pen', 'Eraser'],
    ['Notebook', 'Binder'],
    ['Tablet', 'Notebook'],
    ['Pencil', 'Binder'],
    ['Printer', 'Notebook'],
    ['Paper', 'Printer'],
    ['Eraser', 'Notebook'],
    ['Stapler', 'Paper'],
    ['Pencil', 'Stapler'],
    ['Pen', 'Pencil'],
    ['Tablet', 'Eraser'],
    ['Printer', 'Pen'],
    ['Binder', 'Staples']
]
db4 = pd.DataFrame({'Transaction Number':range(1,21) , 'Items Bought':transactions})
db4.to_csv('Staples.csv', index=False)
datasets.append('Staples.csv')


# In[41]:


#items for dataset 5: GameStop
db5Items = set(['Guitar Hero', 'Guitar Hero Guitar', 'PlayStation Controller', 'PlayStation', 'Xbox Controller', 'Xbox', 'Uncharted 4', 'NBA 2k25', 'Halo 4', 'Smash Ultimate'])
transactions = [
    ['Guitar Hero', 'Guitar Hero Guitar'],
    ['PlayStation', 'PlayStation Controller'],
    ['Xbox', 'Xbox Controller'],
    ['Uncharted 4'],
    ['NBA 2k25'],
    ['Halo 4'],
    ['Smash Ultimate'],
    ['PlayStation'],
    ['Guitar Hero Guitar', 'Guitar Hero'],
    ['PlayStation', 'NBA 2k25'],
    ['PlayStation', 'Uncharted 4'],
    ['Xbox', 'Halo 4'],
    ['Xbox Controller', 'Halo 4'],
    ['PlayStation Controller', 'NBA 2k25'],
    ['Smash Ultimate'],
    ['Guitar Hero', 'Smash Ultimate'],
    ['PlayStation Controller', 'Uncharted 4'],
    ['Xbox', 'Xbox Controller'],
    ['PlayStation Controller'],
    ['Halo 4', 'Xbox Controller']
]
db5 = pd.DataFrame({'Transaction Number':range(1,21) , 'Items Bought':transactions})
db5.to_csv('GameStop.csv', index=False)
datasets.append('GameStop.csv')


# Part 2

# In[42]:


import itertools
import ast


# In[43]:


#Provided a some candidate itemsets as well as the transaction data and the minimum support, this function returns a set of the frequent itemsets
def findFrequentItemsets(transactions, itemsets, minSupport):
    frequentItemsets = {}
    for itemset in itemsets.keys():
            # counts the number of times that the itemset can be found in the transactions array
            for transaction in transactions:
                if isinstance(itemset, str):
                    if itemset in set(transaction):
                        itemsets[itemset] += 1
                elif set(itemset).issubset(set(transaction)):
                    itemsets[itemset] += 1
            # check to see if it is frequent or not. if it is then add the itemset to the frequent sets array
            support = itemsets[itemset]/len(transactions)
            if support >= minSupport:
                frequentItemsets[itemset] = support
    return frequentItemsets


# In[44]:


#This is a class for the association rule. It is used by me after running the brute force algorithm by generate Association rules
class AssociationRule:
    def __init__(self, a, b, confidence, support):
        self.a = a
        self.b = b
        self.confidence = confidence
        self.support = support
    def __str__(self):
        retstr = ''
        if len(self.a)==1:
            retstr+=self.a[0]
        else:
            retstr+=str(self.a)
        retstr += " implies "
        if len(self.b)==1:
            retstr+=self.b[0]
        else:
            retstr+=str(self.b)
        retstr+=f' with {self.confidence} confidence and {self.support} support'
        return retstr


# In[45]:


def generateAssociationRules(frequentItemsets, minConfidence):
    associationRules = set()
    for itemSet in frequentItemsets.keys():
        if not isinstance(itemSet, str):
            sets = []
            for i in range(1, len(itemSet)):
                sets.extend(list(itertools.combinations(itemSet, i)))
            for s in sets:
                confidence = 0
                if len(s)==1:
                    confidence = frequentItemsets[itemSet]/frequentItemsets[s[0]]
                else:
                    confidence = frequentItemsets[itemSet]/frequentItemsets[s]
                if confidence >= minConfidence:
                    associationRules.add(AssociationRule(s, tuple(set(itemSet)-set(list(s))), confidence, frequentItemsets[itemSet]))
    return associationRules


# In[46]:


# transactions should be a 2 dimensional array of all the transactions
# min support and min confidence should be as a decimal, not a percentage
# runs the brute force algorithm I was assigned to design. It also generates the association rules and returns them
def bruteForce(transactions, minSupport, minConfidence):
    frequentSets = {}
    items = set()
    for transaction in transactions:
        for item in transaction:
            items.add(item)
    k = 1
    itemsets = {item: 0 for item in items}
    while True:
        f = findFrequentItemsets(transactions, itemsets, minSupport)
        if len(f.keys()) == 0:
            break
        frequentSets.update(f)
        k+=1
        itemsets = {item: 0 for item in set(itertools.combinations(items, k))}
    return generateAssociationRules(frequentSets, minConfidence)
    # do the confidence equations for all the combinations and return the association rules


# Part 3

# In[47]:


from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
from mlxtend.preprocessing import TransactionEncoder
import timeit


# In[48]:


#gather user input in regards to the dataset, minimum support and minimum confidence
for i in range(len(datasets)):
    print(f'({i+1}) {datasets[i][:-4]}')
d=8
while d>5 or d<1:
    d = int(input('Choose a number corresponding to a dataset: '))
file_path = f'./{datasets[d-1]}'
minimumSupport = 100
while minimumSupport>1 or minimumSupport<0:
    minimumSupport = float(input('Enter a minimum support between 0 and 1: '))
minimumConfidence = 100
while minimumConfidence>1 or minimumConfidence<0:
    minimumConfidence = float(input('Enter a minimum confidence between 0 and 1: '))


# In[49]:


#reads the chosen dataset in and formats the data
df = pd.read_csv(file_path)
transactions = df['Items Bought'].apply(ast.literal_eval).tolist()
rules = None


# In[50]:


#wrapper function so that the association rules can be returned and the algorithms can be timed
def wrapperFunction(func):
    global rules
    if func==1:
        rules = bruteForce(transactions, minimumSupport, minimumConfidence)
    elif func==2:
        frequentItemsets = apriori(formattedData, min_support=minimumSupport, use_colnames=True)
        rules = association_rules(frequentItemsets, metric="confidence", min_threshold=minimumConfidence)
    elif func==3:
        frequentItemsets = fpgrowth(formattedData, min_support=minimumSupport, use_colnames=True)
        rules = association_rules(frequentItemsets, metric="confidence", min_threshold=minimumConfidence)


# In[51]:


#this runs, times and prints the output of the brute force algorithm
args = tuple([1])
executionTime = timeit.timeit(lambda: wrapperFunction(*args), number=1)
for rule in rules:
    print(rule)
print(f'\nExecution Time: {executionTime}')


# In[52]:


#formats the data for the apriori and fp tree algorithms
encoder = TransactionEncoder()
formattedData = pd.DataFrame(encoder.fit(transactions).transform(transactions), columns=encoder.columns_)


# In[53]:


#this runs, times and prints the output of the apriori algorithm
args = tuple([2])
executionTime = timeit.timeit(lambda: wrapperFunction(*args), number=1)
for t, rule in rules.iterrows():
    printstr = ''
    if len(rule['antecedents']) == 1:
        printstr += tuple(rule['antecedents'])[0]
    else:
        printstr += str(tuple(rule['antecedents']))
    
    printstr += ' implies '
    
    if len(rule['consequents']) == 1:
        printstr += tuple(rule['consequents'])[0]
    else:
        printstr += str(tuple(rule['consequents']))
    printstr += f" with {rule['confidence']} confidence and {rule['support']} support"
    print(printstr)
print(f'\nExecution Time: {executionTime}')


# In[54]:


#this runs, times and prints the output of the fp growth algorithm
args = tuple([3])
executionTime = timeit.timeit(lambda: wrapperFunction(*args), number=1)
for t, rule in rules.iterrows():
    printstr = ''
    if len(rule['antecedents']) == 1:
        printstr += tuple(rule['antecedents'])[0]
    else:
        printstr += str(tuple(rule['antecedents']))
    
    printstr += ' implies '
    
    if len(rule['consequents']) == 1:
        printstr += tuple(rule['consequents'])[0]
    else:
        printstr += str(tuple(rule['consequents']))
    printstr += f" with {rule['confidence']} confidence and {rule['support']} support"
    print(printstr)
print(f'\nExecution Time: {executionTime}')

