"""
 Converts .txt dataset to .csv file with "text_id", "xloc", "yloc", "name", "entity", "name_id",
                               "title_source_text","source_text" columns, extracted from .txt file
"""

# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import re
from io import StringIO

# Function for parser
"""
    Converts .txt dataset to .csv file with "text_id", "xloc", "yloc", "name", "entity", "name_id",
                               "title_source_text","source_text" columns, extracted from .txt file
    Arguments:
        path: path to .txt file with dataset
    Returns:
        DataFrame with columns "text_id", "xloc", "yloc", "name", "entity", "name_id",
                               "title_source_text","source_text"
"""
def dataset_parser(path):
  df = pd.DataFrame(columns = ["text_id", "xloc", "yloc", "name", "entity", "name_id",
                               "title_source_text","source_text"])
  def parse_text_sep(path):
    with open(path) as f:
      contents = f.read()
      blank_line_regex = r"(?:\r?\n){2,}"
      return re.split(blank_line_regex, contents.strip())
  texts = parse_text_sep(path)

  for text in texts:
    t1,t2,t3 = text.split('\n', 2)
    text_df = pd.read_csv(StringIO(t3), sep='\t', names = ["text_id", "xloc", "yloc", "name", "entity", "name_id"])
    text_df["title_source_text"] = t1.split("|")[2]
    text_df["source_text"] = t2.split("|")[2]
    df = pd.concat([df, text_df.head(df.shape[0] -1)])
  df = df.reset_index(drop=True)
  return df

# Parse text file, transform to dataset and save new .csv files

train_df = dataset_parser('CDR_TrainingSet.PubTator.txt')
test_df = dataset_parser('CDR_TestSet.PubTator.txt')
dev_df = dataset_parser('CDR_DevelopmentSet.PubTator.txt')

print(train_df.shape, test_df.shape, dev_df.shape)

train_df.to_csv('cdr_dner_train_df.csv', index=False)
test_df.to_csv('cdr_dner_test_df.csv', index=False)
dev_df.to_csv('cdr_dner_dev_df.csv', index=False)