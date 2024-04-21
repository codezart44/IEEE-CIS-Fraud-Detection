# #%%
# # imports
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# print(f'pd=={pd.__version__}')
# print(f'np=={np.__version__}')
# print(f'sns=={sns.__version__}')


# #%%
# # read in train and test datasets
# train_transaction = pd.read_csv('/Users/oskarwallberg/desktop/kaggle-datasets/ieee-fraud-detection/train_transaction.csv', index_col='TransactionID')
# test_transaction = pd.read_csv('/Users/oskarwallberg/desktop/kaggle-datasets/ieee-fraud-detection/test_transaction.csv', index_col='TransactionID')

# test_transaction.columns = train_transaction.columns.drop(labels='isFraud') # ensure congruent columns

# train_transaction.shape, test_transaction.shape

# #%%


