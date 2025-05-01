from flask import Flask, request, render_template
import pandas as pd
import pickle
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Load models and scalers
with open("models/engagement_model.pkl", "rb") as f:
    engagement_model = pickle.load(f)

with open("models/engagement_scaler.pkl", "rb") as f:
    engagement_scaler = pickle.load(f)

with open("models/virality_model.pkl", "rb") as f:
    virality_model = pickle.load(f)

with open("models/virality_scaler.pkl", "rb") as f:
    virality_scaler = pickle.load(f)

# Load dataset for dashboard
df = pd.read_csv("data/cleaned/Cleaned_Data.csv")

# ---------- Dashboard Visualizations ----------
def create_graphs():
    graphs = []

    fig1 = px.bar(df.groupby('Platform')['Total_Engagement'].sum().reset_index(),
                  x='Platform', y='Total_Engagement', title="Total Engagement by Platform")
    graphs.append(pio.to_html(fig1, full_html=False))

    fig2 = px.box(df, x='Content_Type', y='Engagement_Rate', title="Engagement Rate by Content Type")
    graphs.append(pio.to_html(fig2, full_html=False))

    fig3 = px.scatter(df, x='Views', y='Virality_Score', color='Platform', title="Virality Score vs Views")
    graphs.append(pio.to_html(fig3, full_html=False))

    fig4 = px.histogram(df, x='Engagement_Rate', nbins=30, title="Distribution of Engagement Rate")
    graphs.append(pio.to_html(fig4, full_html=False))

    fig5 = px.pie(df, names='Content_Type', title='Content Type Distribution')
    graphs.append(pio.to_html(fig5, full_html=False))

    fig6 = px.box(df, x='Platform', y='Virality_Score', title="Virality Score by Platform")
    graphs.append(pio.to_html(fig6, full_html=False))

    fig7 = px.histogram(df, x='Likes', title="Like Count Distribution")
    graphs.append(pio.to_html(fig7, full_html=False))

    fig8 = px.scatter(df, x='Likes', y='Shares', title="Likes vs Shares")
    graphs.append(pio.to_html(fig8, full_html=False))

    return graphs

# ---------- Routes ----------
@app.route("/")
def dashboard():
    graphs = create_graphs()
    return render_template("dashboard.html", graphs=graphs)

@app.route("/predict", methods=["POST"])
def predict():
    result = None

    if request.method == "POST":
        try:
            action = request.form.get("action")

            like_count = float(request.form["like_count"])
            share_count = float(request.form["share_count"])
            comment_count = float(request.form["comment_count"])
            view_count = float(request.form["view_count"])

            if action == "predict_engagement":
                # Only 4 features for engagement
                engagement_features = {
                    "Likes": like_count,
                    "Shares": share_count,
                    "Comments": comment_count,
                    "Views": view_count
                }

                engagement_input_df = pd.DataFrame([engagement_features], columns=engagement_scaler.feature_names_in_)
                engagement_input_df = engagement_input_df.reindex(columns=engagement_scaler.feature_names_in_, fill_value=0)
                scaled_engagement = engagement_scaler.transform(engagement_input_df)

                pred = engagement_model.predict(scaled_engagement)[0]

                if pred < 0.3:
                    result = "📉 Engagement Level: Low"
                elif pred < 0.7:
                    result = "📊 Engagement Level: Medium"
                else:
                    result = "📈 Engagement Level: High"


            elif action == "predict_virality":
                # Virality model expects 5 features including Virality_Score

                # We'll use a placeholder value for Virality_Score (e.g., 0.0)

                virality_input_dict = {
                    "Virality_Score": 0.0,
                    "Likes": like_count,
                    "Shares": share_count,
                    "Comments": comment_count,
                    "Views": view_count
                }

                # Create full DataFrame with all 5 features
                virality_input_df = pd.DataFrame([virality_input_dict])

                # Extract only the columns used for scaling (excluding Virality_Score)
                scale_columns = ["Likes", "Shares", "Comments", "Views"]
                scaled_part = virality_scaler.transform(virality_input_df[scale_columns])

                # Reconstruct full scaled input with placeholder Virality_Score at front
                final_input = pd.DataFrame(
                    [[0.0] + list(scaled_part[0])],

                    columns=[
                        "Virality_Score",
                        "Likes",
                        "Shares",
                        "Comments",
                        "Views"
                    ])

                # Predict
                pred = virality_model.predict(final_input)[0]

                result = "🔥 This post is likely to go viral!" \
                    if pred == 1 else "❄️ This post is unlikely to go viral."

            else:
                result = "❗ Unknown prediction type."

        except Exception as e:
            result = f"Error: {str(e)}"

    graphs = create_graphs()
    return render_template("dashboard.html", prediction=result, graphs=graphs)

# ---------- Run Server ----------
if __name__ == "__main__":
    app.run(debug=True)