# Social Media Engagement Analysis

Objective of this project is to conduct interactive filtering, exploration, and predictive analysis of social media post engagement data to uncover trends, segment high-performing content, and forecast future performance.

**Tools Used:** Python (Flask, pandas, Matplotlib, Seaborn, Plotly, joblib, scikit-learn), JavaScript (vanilla), HTML/CSS

**Dataset Attribution:**
Dataset sourced from Kaggle: [Viral Social Media Trends and Engagement Analysis](https://www.kaggle.com/datasets/atharvasoundankar/viral-social-media-trends-and-engagement-analysis)  
CSV files located in `data/raw/` and cleaned data in `data/cleaned/`.

**Key Features and Analysis Steps:**
1. **Filtering:** Select posts by platform (e.g., Twitter, Instagram, Facebook) and content type (Image, Video, Text).
2. **Sorting Metrics:** Rank posts by Views, Likes, Shares, Comments, Total Engagement, Engagement Rate, and Virality Score.
3. **Exploratory Analysis:** Generate visualizations for engagement trends over time and calculate distribution metrics in `Analysis.ipynb`.
4. **Predictive Modeling:** Load a pre-trained model (`models/engagement_model.pkl`) to forecast future post engagement metrics.
5. **Export:** Download filtered and predicted datasets as CSV with progress feedback.

For detailed EDA, methodology, and modeling, see `Analysis.ipynb`.

## Footer

© 2025 Girish Shenoy.
