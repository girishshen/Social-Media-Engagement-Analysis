# Social Media Engagement Analysis

Objective of this project is to conduct filtering, exploration, and predictive analysis of social media post engagement data to identify trends, segment high-performing content, and forecast future performance.

Tools Used: Python (Flask, pandas, Plotly, joblib, scikit-learn), JavaScript (vanilla), HTML/CSS

Dataset Attribution:
This project uses the dataset [Viral Social Media Trends](https://www.kaggle.com/datasets) sourced from Kaggle.  
The raw data is in `data/raw/Viral_Social_Media_Trends.csv`, and cleaned data in `data/cleaned/Cleaned_Data.csv`.

Key Analysis and Features:
1. Engineered engagement metrics such as Total Engagement, Engagement Rate, and Virality Score.
2. Interactive filtering by Platform (Twitter, Instagram, Facebook) and Content Type (Image, Video, Text).
3. Sorting and ranking posts by Views, Likes, Shares, Comments, and custom scores.
4. Predictive modeling using a pre-trained machine learning model (`models/engagement_model.pkl`) for future engagement forecasts.
5. Interactive visualizations using Plotly to explore trends and comparative insights.
