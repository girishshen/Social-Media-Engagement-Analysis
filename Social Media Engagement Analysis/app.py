from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    try:
        # Load cleaned data
        df = pd.read_csv('data/cleaned/Cleaned_Data.csv')
        print("Data loaded successfully.")  # Debugging line to check if the data is loaded

        # Load the pre-trained engagement model
        model = joblib.load('models/engagement_model.pkl')
        print("Model loaded successfully.")  # Debugging line for model loading

    except Exception as e:
        print(f"Error loading data or model: {e}")
        return "Error loading data or model, please check your file paths."

    # Generate visualizations for the dashboard
    graphs = []

    try:
        # 1. Total Engagement by Platform
        fig1 = px.bar(
            df.groupby('Platform')['Total_Engagement'].sum().reset_index(),
            x='Platform', y='Total_Engagement', title='Total Engagement by Platform'
        )

        fig1.update_layout(template='plotly_dark')  # Apply dark theme
        graphs.append(pio.to_html(fig1, full_html=False))

        # 2. Engagement Rate Distribution by Content Type
        fig2 = px.box(
            df, x='Content_Type', y='Engagement_Rate',
            title='Engagement Rate Distribution by Content Type'
        )

        fig2.update_layout(template='plotly_dark')  # Apply dark theme
        graphs.append(pio.to_html(fig2, full_html=False))

        # 3. Virality Score vs Views (Scatter plot)
        fig3 = px.scatter(
            df, x='Views', y='Virality_Score', color='Platform',
            title='Virality Score vs Views'
        )

        fig3.update_layout(template='plotly_dark')  # Apply dark theme
        graphs.append(pio.to_html(fig3, full_html=False))

        # 4. Distribution of Engagement Rate
        fig4 = px.histogram(
            df, x='Engagement_Rate', nbins=30,
            title='Distribution of Engagement Rate'
        )

        fig4.update_layout(template='plotly_dark')  # Apply dark theme
        graphs.append(pio.to_html(fig4, full_html=False))

        # 5. Engagement vs Shares (Scatter plot)
        fig5 = px.scatter(
            df, x='Shares', y='Engagement_Rate', color='Platform',
            title='Engagement vs Shares'
        )

        fig5.update_layout(template='plotly_dark')  # Apply dark theme
        graphs.append(pio.to_html(fig5, full_html=False))

        # 6. Engagement vs Comments (Scatter plot)
        fig6 = px.scatter(
            df, x='Comments', y='Engagement_Rate', color='Platform',
            title='Engagement vs Comments'
        )

        fig6.update_layout(template='plotly_dark')  # Apply dark theme
        graphs.append(pio.to_html(fig6, full_html=False))

        # 7. Total Engagement by Region
        fig7 = px.bar(
            df.groupby('Region')['Total_Engagement'].sum().reset_index(),
            x='Region', y='Total_Engagement', title='Total Engagement by Region'
        )

        fig7.update_layout(template='plotly_dark')  # Apply dark theme
        graphs.append(pio.to_html(fig7, full_html=False))

        # 8. Engagement Rate vs Likes (Scatter plot)
        fig8 = px.scatter(
            df, x='Likes', y='Engagement_Rate', color='Platform',
            title='Engagement Rate vs Likes'
        )

        fig8.update_layout(template='plotly_dark')  # Apply dark theme
        graphs.append(pio.to_html(fig8, full_html=False))

    except Exception as e:
        print(f"Error generating plots: {e}")

    # Return the dashboard page
    return render_template(
        'dashboard.html',
        graphs=graphs,
    )


if __name__ == '__main__':
    app.run(debug=True)