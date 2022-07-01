# Token Classification and Relation Detection
Chemicals, diseases, and their relations play central roles in many areas of biomedical research and healthcare such as drug discovery and safety surveillance. Although the ultimate goal in drug discovery is to develop chemicals for therapeutics, recognition of adverse drug reactions between chemicals and diseases is important for improving chemical safety and toxicity studies and facilitating new screening assays for pharmaceutical compound survival. In addition, identification of chemicals as biomarkers can be helpful in informing potential relationships between chemicals and pathologies. 

## To Do
Token Classification and Relation Detection for Bio Articles. Work with Tokens Classification on biological articles and use the resulting model in another task - Relations Extraction between named entities. Entities are `Chemical` and `Disease`.

## Data Preparation
The first step was data pre-processing and extracting features needed to work with. Python scripts: [`parser.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/parser.py), [`to_iob_converter.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/to_iob_converter.py), [`cid_data_extractor.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/cid_data_extractor.py) were written for that purpose. The data could be found in [folder](https://github.com/Teasotea/BioNER-and-RD/tree/main/data)

## Token Classification
![`Extracting Entities Example`](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/ent2.jpg)

Results of finetuning BERT, SciBERT, and BioBERT:
precision, recall and f1 score shown in the table below are macro avg (arithmetic mean) of those metrics for 5 classes: **B-Chemical**, **I-Chemical**, **B-Disease**, **I-Disease**, and **O**. For the finetuning task scikit-learn [wrapper](https://github.com/charles9n/bert-sklearn) was used. Code for this part could be found in [`ModelsForNERComparison.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/ModelsForNERComparison.ipynb) notebook. 

| Model  | Precision | Recall | F1 Score | Accuracy | Model Description | 
| ------------- |  ------------- | ------------- | ------------- | ------------- | ------------- | 
| BERT `bert-base-cased` | 0.83 | 0.70 | 0.76 | 0.95 | [HuggigFace](https://huggingface.co/bert-base-cased), [GitHub](https://github.com/google-research/bert), [Paper](https://arxiv.org/abs/1810.04805) | 
| SciBERT `scibert-scivocab-cased`| 0.86 | 0.77 | 0.81 | 0.96 |  [HuggingFace](https://huggingface.co/allenai/scibert_scivocab_uncased), [GitHub](https://github.com/allenai/scibert), [Paper](https://arxiv.org/pdf/1903.10676.pdf) | 
| BioBERT `biobert-v1.1-pubmed-base-cased model`| 0.86 | 0.72 | 0.78 | 0.95 | [GitHub](https://github.com/dmis-lab/biobert), [Paper](https://arxiv.org/pdf/1901.08746.pdf) | 

SciBERT has shown the best performance on given data, so it was chosen for further improvements and visualization of results, which could be found in [`Scibert_TokenClassification.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/Scibert_TokenClassification.ipynb) notebook. The SciBERT model was also finetuned with SpaCy pipelines in [`Finetuning_SciBERT_with_SpaCy_Pipeline.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/Finetuning%20SciBERT%20with%20SpaCy%20Pipeline.ipynb) notebook for more comfortable further usage.


## Knowledge Graphs

The final approach with Knowledge Graphs could be found in [`RD_KG_solution.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/RD_KG_solution.ipynb) notebook. Experiments with KG on the given dataset could be found in [`KnowledgeGraphs.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/KnowledgeGraphs.ipynb) notebook. The core idea was to analyze dependencies between words in sentences, extract objects, subjects, and relations, and then use the trained NER model to filter Diseases and Chemicals from them. The resulting .tsv file, that contains relations can be found by [link](https://github.com/Teasotea/BioNER-and-RD/blob/main/data/relations1.tsv). All in all, such approach has some issues, like small numbers of entity1-relation-entity2 triples, that are left after filtering. [Here](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/final_kg.jpg) is the visualization of the resulting Knowledge Graph.

## Visualisations

### Picture 1: Label prediction for entities of three models with the right labels on Test Set
![`Comparison of label prediction for entities of three models with the right labels`](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/iob.jpg)

### Picture 2: Fine-Tuned SciBERT Metrics
![`Fine-Tuned SciBERT Perfomance`](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/res2.jpg)

### Picture 3: Knowledge graph with "is" relation for given data
![`Knowledge graph for "is" relation for given data`](https://github.com/Teasotea/BioNER-and-RD/blob/main/img/gr2.jpg)


## Files & Notebooks
* [`parser.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/parser.py) - parsing .txt files, feature engineering, converting to .csv
* [`to_iob_converter.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/to_iob_converter.py) - converter to the IOB (Inside–outside–beginning) format - common tagging format for tagging tokens
* [`cid_data_extractor.py`](https://github.com/Teasotea/BioNER-and-RD/blob/main/cid_data_extractor.py) - extracting related name-entity pairs from DNER and CID parts of the datasets
* [`ModelsForNERComparison.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/ModelsForNERComparison.ipynb) ([nbviewer](https://github.com/Teasotea/BioNER-and-RD/blob/main/ModelsForNERComparison.ipynb)) -  Finetuning `bert-base-cased`, `scibert-scivocab-cased` and `biobert-v1.1-pubmed-base-cased model` on dataset in IOB format. Comparing the results
* [`Scibert_TokenClassification.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/Scibert_TokenClassification.ipynb) ([nbviewer](https://github.com/Teasotea/BioNER-and-RD/blob/main/Scibert_TokenClassification.ipynb)) -  Further work with `scibert-scivocab-cased` as it has shown the best performance among other models. Developing functions for extracting entities from user's text and visualizing results with `displacy`
* [`Finetuning_SciBERT_with_SpaCy_Pipeline.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/Finetuning%20SciBERT%20with%20SpaCy%20Pipeline.ipynb) -  Using [spaCy 3](https://spacy.io/usage/v3) library to finetune SciBERT for NER task with SpaCy Pipeline
* [`KnowledgeGraphs.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/KnowledgeGraphs.ipynb) ([nbviewer](https://github.com/Teasotea/BioNER-and-RD/blob/main/KnowledgeGraphs.ipynb)) - Trying out Relation Extraction methods without usage of NER Entities. Developing functions for further building of Knowledge Graphs and visualizaing th results.
* [`RD_KG_solution.ipynb`](https://github.com/Teasotea/BioNER-and-RD/blob/main/RD_KG_solution.ipynb)  - Final approach with Knowledge Graphs
