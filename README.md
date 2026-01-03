# PySpark-Polars-Pandas
A comparative between PySpark, Polars and Pandas for data analysis is presented.

## 🌎 Repository Structure
```
PySpark-Polars-Pandas/
│
├── .gitignore
├── main.py
├── env/                # Virtual enviroment
└── requirements.txt
└── Notebooks                   # Contains all Jupyter Notebooks
    └── pyspark_config.ipynb    # PySpark configuration (VSCode, Google Colab and Databricks)
    └── DA1.ipynb       # PySpark, Polars and Pandas commands for DEA
```
## ✨ Details
**pyspark_config.ipynb**: Shows how to set the enviroment to use PySpark in VSCode (locally), Google Colab and Databricks. See this notebook first of all.

**DA1.ipynb**: Data Exploratory Analysis Commands are shown by using PySpark, Polars and Pandas.


## 🚀 How to run locally
1. Clone this repository:
```
git clone https://github.com/arteaga7/PySpark-Polars-Pandas.git
```
2. Set virtual environment and install dependencies.

For Windows:
```
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
```

For Linux:
```
python -m venv env && source env/bin/activate && pip install -r requirements.txt
```
3. Run "pyspark_config.ipynb".
