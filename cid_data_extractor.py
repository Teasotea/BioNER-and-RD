"""
Extracts features from DNER and CID parts of dataset, returns .csv files with name-entity pairs of related terms
"""
# Import Libraries

import pandas as pd
import nltk

# Load Data

train_df = pd.read_csv('cdr_dner_train_df.csv')
test_df = pd.read_csv('cdr_dner_test_df.csv')
dev_df = pd.read_csv('cdr_dner_dev_df.csv')

DNER_train_df = train_df[train_df['xloc'] != "CID"].reset_index(drop=True)
DNER_test_df = test_df[test_df['xloc'] != "CID"].reset_index(drop=True)
DNER_dev_df = dev_df[dev_df['xloc'] != "CID"].reset_index(drop=True)

# Get CID features from datasets

def get_cid_dataset(df):
  cid_df = df[df['xloc'] == "CID"].reset_index(drop=True)
  cid_df["text"] = cid_df.apply(lambda x: x['title_source_text']+ ' '+x['source_text'], axis = 1)
  cid_df = cid_df.drop(columns = ['entity', 'name_id', 'title_source_text', 'source_text', 'xloc'])
  cid_df = cid_df[cid_df['name'].str.startswith('D') & cid_df['yloc'].str.startswith('D')].rename(columns = {'yloc':'w1', 'name':'w2'})
  return cid_df

CID_train_df = get_cid_dataset(train_df)
CID_test_df = get_cid_dataset(test_df)
CID_dev_df = get_cid_dataset(dev_df)

# Pre-process datasets

def prepr_df(df, df2):
  nameid_df = df[['name','entity', 'name_id']]
  nameid_df = nameid_df[nameid_df['name_id'].str.contains('D', na=False)]
  nameid_df["name_entity"] = nameid_df.apply(lambda x: {x["name"]: x["entity"]},axis=1)
  nameid_df = nameid_df.drop(columns=['name', 'entity'])
  nameid_df.set_index('name_id', inplace=True)
  final_df = df2.replace({"w1": nameid_df.squeeze().to_dict(), "w2": nameid_df.squeeze().to_dict()})
  return final_df

train_cid= prepr_df(DNER_train_df, CID_train_df)
test_cid = prepr_df(DNER_test_df, CID_test_df)
dev_cid = prepr_df(DNER_dev_df, CID_dev_df)

# Save datasets with CID relations data

train_cid.to_csv('train_cid.csv', index=False)
test_cid.to_csv('test_cid.csv', index=False)
dev_cid.to_csv('dev_cid.csv', index = False)
