
# Drone Delivery Analytics and Predictive Modeling

A data science research project investigating how operational and environmental factors influence drone delivery performance using statistical analysis and machine learning.

This project was completed as part of the NC State University Drone Delivery Research Program.

---

## Project Overview

Drone delivery is rapidly becoming an important solution for last-mile logistics. Companies such as Amazon and Walmart are investing in autonomous aerial delivery systems to improve efficiency and reduce delivery times.

This project explores how operational conditions—including package weight, route complexity, traffic level, weather conditions, battery level, distance, and delivery time—affect drone delivery performance. Using Python and regression analysis, we developed predictive models to better understand which variables have the greatest influence on delivery speed.

---

## Research Question

**Which operational and environmental variables have the greatest impact on drone delivery speed, and how accurately can machine learning models predict delivery performance?**

---

## Objectives

- Analyze factors affecting drone delivery speed.
- Identify variables with the strongest relationship to performance.
- Develop regression models for predicting delivery speed.
- Compare model performance using different feature combinations.
- Evaluate practical implications for autonomous retail delivery.

---

# Dataset

The dataset contained **150 successful drone deliveries**.

Variables analyzed included:

- Package Weight
- Route Complexity
- Weather Condition
- Traffic Level
- Battery Level
- Distance
- Delivery Time
- Temperature
- Drone Speed

Prior to analysis:

- unsuccessful deliveries were removed
- robot-delivery records were filtered
- data was cleaned for modeling

---

# Methodology

## Data Preparation

- Cleaned and filtered the dataset
- Removed incomplete records
- Selected relevant variables
- Prepared features for regression analysis

## Exploratory Data Analysis

Using Python and Excel, the dataset was explored through:

- Scatter plots
- Correlation analysis
- Heatmaps
- Comparative charts
- Linear regression trend lines

## Machine Learning

Several Linear Regression models were developed using Scikit-Learn.

The models evaluated relationships between:

- Package Weight → Speed
- Route Complexity → Speed
- Battery Level → Speed
- Distance + Route Complexity + Delivery Time → Speed

---

# Technologies

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Google Colab
- Microsoft Excel

---

# Results

## Package Weight

Very weak relationship with delivery speed.

**R² = 0.0041**

Package weight alone had little predictive value for delivery speed. Drone Delivery Data Analysis.pdf

---

## Route Complexity

Increasing route complexity generally reduced delivery speed.

**R² = 0.1084**

Although statistically weak, the relationship consistently showed decreasing speed with increased complexity. Drone Delivery Data Analysis.pdf

---

## Traffic

Average delivery speeds:

|Traffic|Average Speed|
|-------|-------------|
|Low|12.43 km/h|
|Medium|10.47 km/h|
|High|8.71 km/h|

Traffic level showed a meaningful impact on operational performance. Drone Delivery Data Analysis.pdf

---

## Weather

Average speeds:

|Weather|Average Speed|
|--------|-------------|
|Sunny|11.96 km/h|
|Windy|10.36 km/h|
|Rainy|9.72 km/h|
|Snowy|7.67 km/h|

Snow had the largest negative impact on delivery speed. Drone Delivery Data Analysis.pdf

---

## Temperature vs Battery

Battery performance decreased as temperature increased.

**R² = 0.7205**

This was one of the strongest relationships identified during the project. Drone Delivery Data Analysis.pdf

---

## Predictive Modeling

Several regression models were evaluated.

The strongest model used:

- Distance
- Route Complexity
- Delivery Time

Performance:

- R² = 0.7954

Using a 90/10 train-test split improved performance to:

**R² = 0.8384** Drone Delivery Data Analysis.pdf

---

# Key Findings

- Package weight had minimal influence on delivery speed.
- Route complexity modestly reduced speed.
- Snow produced the slowest deliveries.
- Sunny weather produced the fastest deliveries.
- High temperatures accelerated battery depletion.
- Combining operational variables produced much stronger predictive models than analyzing single variables independently. Drone Delivery Data Analysis.pdf

---

# My Contributions

My work included:

- Data cleaning and preparation
- Exploratory data analysis
- Building regression models in Python
- Creating visualizations
- Interpreting model performance
- Presenting findings and recommendations

---

# Limitations

- Dataset contained only 150 successful deliveries.
- Data represented a limited time period.
- Unsuccessful deliveries were excluded.
- Additional weather conditions and seasonal data would improve generalizability.
- More advanced machine-learning models could further improve prediction accuracy. Drone Delivery Data Analysis.pdf

---

# Future Work

Potential future improvements include:

- Random Forest regression
- Gradient Boosting
- Neural Networks
- Time-series delivery prediction
- Geographic route optimization
- Battery degradation modeling
- Larger multi-season datasets

---

# Repository Structure

```
Drone-Delivery-Analytics/
│
├── README.md
├── notebooks/
├── data/
├── images/
├── models/
└── presentation/
```

---

# Acknowledgements

Completed as part of the NC State University Drone Delivery Research Program.
