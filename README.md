# ch02-data-pipeline

**Part of the book**: *Applied AI and MLOps: From Idea to Deployment*  
**Author**: Seidu Ramadhan Hussein  
**Chapter 2 – Data Collection and Preprocessing**

---

## 🧠 What This Repo Covers

This project shows how to turn messy real-world data into machine-learning-ready pipelines.

Includes:
- ✅ ETL workflows for structured tabular data
- ✅ Data cleaning: missing values, outliers, type checks
- ✅ Feature engineering: flags, buckets, time-based features
- ✅ Profiling with `pandas_profiling`
- ✅ Airline delay forecasting case study
- ✅ Cleaned outputs for modeling (used in Chapter 3)

---

## 📂 Folder Structure

```
ch02-data-pipeline/
├── notebooks/
│   └── airline_delay_case_study/
│       └── airline_delay_eda.ipynb
├── src/
│   ├── cleaning.py
│   └── etl.py
├── tests/
│   └── test_data.py
├── config/
│   └── pipeline.yaml
├── logs/
│   └── data_validation.log
├── data/
│   ├── airline_delay.csv
│   └── airline_delay_cleaned.csv
└── README.md
```

---

## 🚀 How to Run

```bash
# Clone this repo
git clone https://github.com/YOUR_USERNAME/ch02-data-pipeline.git
cd ch02-data-pipeline

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook notebooks/airline_delay_case_study/airline_delay_eda.ipynb
```

---

## 📈 Business Case: Airline Delays

> “By engineering weekday/hour features and removing outliers, we reduced forecasting error by 22% in peak periods.”

---

## 📚 Book Reference

This repo supports:
> **Chapter 2: Data Collection and Preprocessing**  
> From the book *Applied AI and MLOps: From Idea to Deployment*
