# Token Classification and Relation Detection
Token Classification and Relation Detection for Bio Articles

## Task
Work with tokens classification on biological articles and use the resulting model in another task - extraction of relations between named entities. Entities are `Chemical` and `Disease`. Train a model to correctly predict the class of entity and then use the given model to find chemical-disease relations on this data set.


## Token Classification Approach
Results of finetuning BERT, SciBERT, and BioBERT:
Precision, recall and f1 score shown in the table below are macro avg (arithmetic mean) of those metrics for 5 classes: **B-Chemical**, **I-Chemical**, **B-Disease**, **I-Disease**, and **O**

| Model  | Description | Precision | Recall | F1 Score | Accuracy | 
| ------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | 
| `bert-base-cased` | [HuggigFace](https://huggingface.co/bert-base-cased), [GitHub](https://github.com/google-research/bert), [Paper](https://arxiv.org/abs/1810.04805) | 0.83 | 0.70 | 0.76 | 0.95 | 
| `scibert-scivocab-cased`| [GitHub](https://github.com/allenai/scibert), [Paper](https://arxiv.org/pdf/1903.10676.pdf) | 0.86 | 0.77 | 0.81 | 0.96 | 
| `biobert-v1.1-pubmed-base-cased model`| [GitHub](https://github.com/dmis-lab/biobert), [Paper](https://arxiv.org/pdf/1901.08746.pdf) |  0.86 | 0.72 | 0.78 | 0.95 | 


## Files & Notebooks
* [`parser.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/parser.py) - parsing .txt files, feature engineering, converting to .csv
* [`to_iob_converter.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/to_iob_converter.py) - converter to the IOB (Inside–outside–beginning) format - common tagging format for tagging tokens
* [`cid_data_extractor.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/cid_data_extractor.py) - extracting related name-entity pairs from DNER and CID parts of the datasets
* [`ModelsForNERComparison.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/ModelsForNERComparison.ipynb) ([nbviewer](https://github.com/Teasotea/BioNER-and-RD/blob/main/ModelsForNERComparison.ipynb)) -  Finetuning `bert-base-cased`, `scibert-scivocab-cased` and `biobert-v1.1-pubmed-base-cased model` on dataset in IOB format. Comparing the results
* [`Scibert_TokenClassification.ipyn`](https://github.com/Teasotea/BioNER-and-RD/blob/main/Scibert_TokenClassification.ipynb) ([nbviewer](https://github.com/Teasotea/BioNER-and-RD/blob/main/Scibert_TokenClassification.ipynb)) -  Hyperparameters Tuning for `scibert-scivocab-cased` as it was shown the best performance among other models. Developing functions for extracting entities from user's text and visualizing results with `displacy`
* [`KnowledgeGraphs.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/KnowledgeGraphs.ipynb) ([nbviewer](https://github.com/Teasotea/BioNER-and-RD/blob/main/KnowledgeGraphs.ipynb)) - Trying out Relation Extraction methods without usage of NER Entities. Developing functions for further building of Knowledge Graphs and visualizaing th results.
* [`RelationExtractionBetweenEntities.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/RelationExtractionBetweenEntities.ipynb) ([nbviewer](https://github.com/Teasotea/BioNER-and-RD/blob/main/RelationExtractionBetweenEntities.ipynb)) - This work is unfinished. Futher steps will be to develop functions for extracting entity pairs in given text and the relation between them. This could be done in similar way with approch in `KnowledgeGraphs.ipynb` notebook.

## Results

### Picture 1: Comparison of label prediction for entities of three models with the right labels
![`Comparison of label prediction for entities of three models with the right labels`](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/iob.jpg)

### Picture 2: Fine-Tuned SciBERT Perfomance
![`Fine-Tuned SciBERT Perfomance`](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/res2.jpg)

### Picture 3: Extracting Entities from given text
![`Extracting Entities Example`](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/ent2.jpg)

### Picture 4: Knowledge graph with "is" relation for given data
![`Knowledge graph for "is" relation for given data`](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/gr2.jpg)

