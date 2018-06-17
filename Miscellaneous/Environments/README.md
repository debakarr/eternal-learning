### Conda Environments

#### Web Scraping Environment

```bash
conda create -n WebScraping
source activate WebScraping
conda install -c conda-forge python requests beautifulsoup4 lxml selenium scrapy
pip install cfscrape -U
```
#### Machine Learning

```bash
conda create -n MachineLearning
source activate MachineLearning
conda install -c conda-forge python numpy scipy pandas matplotlib seaborn bokeh plotly scikit-learn
```

#### Deep Learning Environment

```bash
conda create -n DeepLearning
source activate DeepLearning
conda install -c conda-forge python theano tensorflow keras
```

#### Natural Language Processing

```bash
conda create -n NaturalLanguageProcessing
source activate NaturalLanguageProcessing
conda install -c conda-forge python nltk textblob spacy gensim
```

#### Data Science

```bash
conda create -n DataScience
source activate DataScience
conda install -c conda-forge python requests beautifulsoup4 lxml selenium scrapy numpy scipy pandas matplotlib seaborn bokeh plotly scikit-learn theano tensorflow tpot caffe keras nltk textblob spacy gensim nltk textblob spacy gensim statsmodels opencv pillow mahotas xgboost
```