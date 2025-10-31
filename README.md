# Content-Monetization-Modeler
**Content Monetization Modeler**

**Project Overview**

As YouTube creators and media companies increasingly rely on ad revenue, predicting potential earnings is crucial. This project builds a regression model to estimate YouTube ad revenue for individual videos using performance and contextual features.

It also includes a Streamlit web application for interactive predictions and visualizations.


**Skills & Technologies**

Machine Learning & Modeling: Linear Regression, Decision Tree Regressor, Random Forest Regressor,GradientBoostingRegressor
Data Handling & Preprocessing: Pandas, NumPy, Missing Value Handling, Outlier Detection, Categorical Encoding

EDA & Data Visualization: Matplotlib, Seaborn, Feature Insights

Regression Metrics: R² Score, RMSE, MAE

Web App Development: Streamlit

**Dataset**

Name: YouTube Monetization Modeler

Format: CSV (~122,000 rows, synthetic)

Target Variable: ad_revenue_usd

**Columns:**
**Column	Description**
video_id	Unique identifier for each video
date	Upload/report date
views	Number of views
likes	Number of likes
comments	Number of comments
watch_time_minutes	Total watch time in minutes
video_length_minutes	Video length in minutes
subscribers	Subscriber count of the channel
category	Video category
device	Device type
country	Viewer country
ad_revenue_usd	Revenue generated (target)

**Problem Statement**

Predict ad revenue (ad_revenue_usd) for a video based on historical performance and contextual data.

Business Use Cases

Content Strategy Optimization: Identify high-performing content

Revenue Forecasting: Estimate expected income for future uploads

Creator Support Tools: Assist YouTubers with insights

Ad Campaign Planning: Forecast ROI for advertisers

**Approach**

Data Understanding & EDA – Explore trends, correlations, and outliers

Preprocessing – Handle missing values (~5%), remove duplicates (~2%), encode categorical variables

Feature Engineering – Example: engagement_rate = (likes + comments)/views

Model Training – Train 5 regression models and select the best

Evaluation – Metrics: R², RMSE, MAE

Streamlit App – Interactive ad revenue prediction

Insights – Identify features that drive revenue

**Model Performance**
Linear Regression : mse = 181.6875 , r2 = 0.9526 , rmse = 13.4792
Decision Tree Regressor : mse = 221.5493 , r2 = 0.9422 , rmse = 14.8845
Random Forest Regressor : mse = 208.9389 , r2 = 0.9455 , rmse = 14.4547
Gradient Boosting Regressor : mse = 257.0742 , r2 = 0.9329 , rmse = 16.0335
Best Model: Linear Regression (R² = 0.9526)

**Best Model**: Linear Regression


**Project Deliverables**

Jupyter Notebook and Python Script – Full EDA, preprocessing, modeling, evaluation, insights

Streamlit App – Interactive revenue prediction and basic visual analytics

README.md – Project overview, instructions, and metrics

**Insights**

Engagement (likes + comments) strongly correlates with revenue

Views and subscribers are top drivers for ad revenue

Video category and device type can influence monetization


**Technical Tags**

Python | Pandas | Scikit-learn | Streamlit | Linear Regression | Ridge | Lasso | Random Forest | Gradient Boosting | EDA | Feature Engineering | Data Visualization | Regression Metrics
