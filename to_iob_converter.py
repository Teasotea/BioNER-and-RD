"""
Converts dataset to the IOB (Inside–outside–beginning) format 
"""

import pandas as pd
import nltk
from nltk.tokenize import TreebankWordTokenizer as twt
nltk.download('punkt')

# Load Data

train_df = pd.read_csv('cdr_dner_train_df.csv')
test_df = pd.read_csv('cdr_dner_test_df.csv')
dev_df = pd.read_csv('cdr_dner_dev_df.csv')

# Get NER dataset

def get_ner_dataset(df):
  df = df[df['xloc'] != "CID"].reset_index(drop=True)
  df = df[df['xloc'].str.isnumeric() & df['yloc'].str.isnumeric()]
  df = df.astype({"xloc": int, "yloc": int}, errors='raise')
  df["text"] = df.apply(lambda x: x['title_source_text']+ ' '+x['source_text'], axis = 1)
  df["loc"] = df.apply(lambda x: tuple((x['xloc'],x['yloc'])), axis = 1)
  return df

DNER_train_df = get_ner_dataset(train_df)
DNER_test_df = get_ner_dataset(test_df)
DNER_dev_df = get_ner_dataset(dev_df)

# Pre-process dataset

def preprocess_df(df):
  data_text_unp = pd.DataFrame(df["text"].unique(), columns=["sent"])
  data_text_unp['tokens'] = data_text_unp.sent.apply(lambda x: list(twt().tokenize(x)))

  def get_items( source_df, item="entity"):
    items_by_text = []
    for i in source_df["text"].unique():
      items_list = source_df[source_df["text"] == i][item].tolist()
      items_by_text.append(items_list)
    return items_by_text

  def extend_df(df, source_d = DNER_train_df):
    df['entities'] = get_items(source_d,item="entity")
    df['names'] = get_items(source_d,item="name")
    df['loc'] = get_items(source_d,item="loc")
    df['name_ids'] = get_items(source_d,item="name_id")
    return df
  
  data_text_unp = extend_df(data_text_unp, source_d = df)
  data_text_unp["ent_loc"] = data_text_unp.apply(lambda x: dict(zip(x['loc'], x['entities'])), axis=1)

  return data_text_unp

train_data_text_unp = preprocess_df(DNER_train_df)
test_data_text_unp = preprocess_df(DNER_test_df)
dev_data_text_unp = preprocess_df(DNER_dev_df)

# Get IOB-tags for sentences

def get_iob(text, ent_loc):
    span_list = list(twt().span_tokenize(text))
    iob_list = []
    for start_sp, end_sp in span_list:
        iob_tag = 'O'
        for start, end in list(ent_loc.keys()):
              if int(start) == start_sp:
                iob_tag = 'B' + '-' + ent_loc[(start, end)]
                break
              elif int(start) < start_sp and end_sp <= int(end):
                iob_tag = 'I' + '-' + ent_loc[(start, end)]
                break
        iob_list.append(iob_tag)
    return iob_list

train_data_text_unp["iob_tags"] = train_data_text_unp.apply(lambda x: get_iob(x['sent'], x['ent_loc']), axis=1)
iob_train = train_data_text_unp[['tokens', 'iob_tags']]

test_data_text_unp["iob_tags"] = test_data_text_unp.apply(lambda x: get_iob(x['sent'], x['ent_loc']), axis=1)
iob_test = test_data_text_unp[['tokens', 'iob_tags']]

dev_data_text_unp["iob_tags"] = dev_data_text_unp.apply(lambda x: get_iob(x['sent'], x['ent_loc']), axis=1)
iob_dev = dev_data_text_unp[['tokens', 'iob_tags']]

# Save IOB-labeled datasets

iob_train.to_csv('iob_train.csv', index=False)
iob_test.to_csv('iob_test.csv', index=False)
iob_dev.to_csv('iob_dev.csv', index=False)