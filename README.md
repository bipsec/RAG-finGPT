<div align="center">
  <h1>RAG-finGPT</h1>
</div>

## Table of Contents

- [Project Structure](#project-structure)
- [Data Processing](#data-processing)



### Project Structure

```sh
RAG_finGPT/
│   ├── notebook/
│   │   ├──fintech-data.ipynb/
│   │   ├──FinGPT_Finetuning_Mistral_7B_fintech.ipynb/
│   │   ├──FinGPT_Finetuning_Mistral_7B_sentiment_data.ipynb/
│   ├── script/
│   │   ├── chroma
│   │   ├── embedding.py
│   │   └── load_data.py
│   │   └── rag.py
│   ├── stock_price/
│   │   ├── data
│   │   │   ├── csv
│   │   │   └── Fintech Stock Price Data
├── .gitignore
├── README.md
└── requirements.txt
```

### Data Processing
I have prepared a dataset by following the FinGPT Hugging face Hub. The dataset contains: 1. input, 2. Output and 3. instruction.
It can be utilized as a prompt. The origin of the dataset is taken from Kaggle: 
Dataset Link: 
```sh
https://www.kaggle.com/datasets/akouaorsot/fintech-stock-price-data
```
Notebook Link: 
```sh
https://www.kaggle.com/code/biplabkumarsarkar/fintec-data?scriptVersionId=179957930
```


