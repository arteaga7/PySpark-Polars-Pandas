# PySpark-Polars-Pandas
A comparative between PySpark, Polars and Pandas commands for data analysis is presented.

## 🌎 Repository Structure
```
PySpark-Polars-Pandas/
│
├── .gitignore
├── env/                        # Virtual enviroment
└── requirements.txt
└── Notebooks                   # Contains all Jupyter Notebooks
    └── pyspark_config.ipynb    # PySpark configuration (VSCode, Google Colab and Databricks)
    └── DA1.ipynb               # PySpark, Polars and Pandas commands for DEA (part 1)
    └── DA2.ipynb               # PySpark, Polars and Pandas commands for DEA (part 2)
└── images                      # Contains all images used in pyspark_config.ipynb
    └── ...
└── data                        # Contains all csv files used in the notebooks
    └── ...
```
## ✨ Details
- **pyspark_config.ipynb**: Shows how to set the enviroment to use PySpark in VSCode (locally), Google Colab and Databricks. See this notebook first of all.

- **DA1.ipynb**: Data Exploratory Analysis Commands are shown by using PySpark, Polars and Pandas.


## 🚀 How to run
1. Clone this repository:
```
git clone https://github.com/arteaga7/PySpark-Polars-Pandas.git
```
2. Set virtual environment and install dependencies.

For Windows:
```
uv venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\Activate.ps1
uv pip install --link-mode=copy -r requirements.txt
```

For Linux:
```
uv venv venv
source venv/bin/activate
uv pip install -r requirements.txt
```
3. Run "Notebooks/pyspark_config.ipynb" or run any other Notebook by using Databricks (recommended).
