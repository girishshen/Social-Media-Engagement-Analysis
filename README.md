# Social Media Engagement Analysis

**Objective:**  
This project aims to conduct **interactive filtering, exploration**, and **predictive analysis** of social media post engagement data to uncover trends, segment high-performing content, and forecast future performance.

---

## 🛠 **Tools Used**
- **Python**  
  - Flask  
  - pandas  
  - Matplotlib  
  - Seaborn  
  - Plotly  
  - pickle
  - scikit-learn
- **JavaScript (vanilla)**
- **HTML/CSS**

---

## 📊 **Dataset Attribution**

The dataset is sourced from Kaggle:  
[Viral Social Media Trends and Engagement Analysis](https://www.kaggle.com/datasets/atharvasoundankar/viral-social-media-trends-and-engagement-analysis)

- **Raw data** is located in `data/raw/`
- **Cleaned data** is in `data/cleaned/`

---

## 🔍 **Key Features and Analysis Steps**

1. **Filtering**  
   - Select posts by platform (e.g., Twitter, Instagram, Facebook)
   - Filter posts by content type (Image, Video, Text)
   
2. **Sorting Metrics**  
   - Rank posts by: 
     - Views
     - Likes
     - Shares
     - Comments
     - Total Engagement
     - Engagement Rate
     - Virality Score

3. **Exploratory Analysis**  
   - Generate visualizations for engagement trends over time
   - Calculate distribution metrics
   - Detailed analysis available in `Analysis.ipynb`

4. **Predictive Modeling**  
   - Load pre-trained models:
     - **Engagement Model** (`models/engagement_model.pkl`) to forecast future post engagement metrics
     - **Virality Model** (`models/virality_model.pkl`) to classify posts as likely or unlikely to go viral
   - **Engagement Scaler** (`models/engagement_scaler.pkl`) and **Virality Scaler** (`models/virality_scaler.pkl`) are used to scale features to match the model's expectations.

5. **Export**  
   - Download filtered and predicted datasets as CSV
   - Export progress feedback included for transparency

---

## 🧠 **Predictive Models**

- **Engagement Model** (`models/engagement_model.pkl`):  
  Predicts post engagement level (low, medium, or high) based on likes, shares, comments, and views.

- **Virality Model** (`models/virality_model.pkl`):  
  Classifies whether a post is likely to go viral or not.

- **Engagement Scaler** (`models/engagement_scaler.pkl`):  
  Scales input data (likes, shares, comments, views) for the engagement model.

- **Virality Scaler** (`models/virality_scaler.pkl`):  
  Scales input data (likes, shares, comments, views) for the virality model.

---

For detailed EDA, methodology, and modeling, see `Analysis.ipynb`.

## Footer

© 2025 Girish Shenoy.
