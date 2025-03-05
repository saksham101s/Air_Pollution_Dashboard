import panel as pn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add custom CSS for transitions and hover effects
custom_css = """
.transition {
  transition: all 0.5s ease;
}
.card:hover {
  transform: scale(1.02);
}
"""
pn.config.raw_css.append(custom_css)

# Enable Panel extensions with full-width responsive layout
pn.extension(sizing_mode="stretch_width")

# Load dataset (use a raw string for Windows file paths)
df = pd.read_csv(r"E:\Air Pollution Dashboard\data\cleaned_air_pollution_data.csv")

# Debug: Print dataset columns
print("Dataset Columns:", df.columns)

# Define AQI-related columns based on your dataset
valid_columns = [
    "co_aqi_value", "ozone_aqi_value", "no2_aqi_value", "pm2.5_aqi_value"
]

# Drop rows with missing values in our valid columns
df = df.dropna(subset=valid_columns)

# Compute city-wise average pollution levels
city_avg_pollution = df.groupby("city")[valid_columns].mean().sort_values(by="pm2.5_aqi_value", ascending=False)

# Function to plot AQI levels for a selected city
def plot_pollution(city):
    city_data = df[df["city"] == city]
    if city_data.empty:
        return pn.pane.Markdown("No data available for this city.")
    # Build a small DataFrame for plotting
    values = city_data.iloc[0][valid_columns]
    plot_df = pd.DataFrame({
        "Pollutant": valid_columns,
        "AQI Value": values.values
    })
    plt.figure(figsize=(8, 4))
    # Use data parameter to avoid palette warning
    sns.barplot(data=plot_df, x="Pollutant", y="AQI Value", palette="coolwarm")
    plt.xticks(rotation=45)
    plt.ylabel("AQI Value")
    plt.title(f"Air Pollution Levels in {city}")
    plt.tight_layout()
    return pn.pane.Matplotlib(plt.gcf(), tight=True)

# Create a dropdown to select a city
city_selector = pn.widgets.Select(name="Select City", options=list(df["city"].unique()))

# Add an image banner (adjust the path as needed)
# image_banner = pn.pane.PNG("assets/logo.png", width=300, height=200)

# Build the dashboard content with centered layout, transitions, and an image banner
dashboard_content = pn.Column(
    pn.layout.VSpacer(height=30),
    # Title with CSS transition applied
    pn.pane.HTML("<h1 class='transition' style='text-align:center;'>🌍 Air Pollution Dashboard</h1>"),
    pn.layout.VSpacer(height=20),
    pn.layout.VSpacer(height=20),
    pn.Row(
        pn.Card(
            pn.pane.DataFrame(city_avg_pollution, height=300),
            title="📊 Average Air Pollution Levels by City",
            width=600,
            css_classes=['card']
        ),
        align="center"
    ),
    pn.layout.VSpacer(height=20),
    pn.pane.HTML("<h2 class='transition' style='text-align:center;'>🌆 City-Specific AQI Levels</h2>"),
    pn.layout.VSpacer(height=10),
    pn.Row(city_selector, align="center"),
    pn.layout.VSpacer(height=10),
    pn.Row(pn.bind(plot_pollution, city_selector), align="center"),
    pn.layout.VSpacer(height=50)
)

# Wrap the content in an HTML div to add a background and padding with transitions
dashboard = pn.Column(
    pn.pane.HTML("<div style='background-color:whitesmoke; padding:20px; transition: all 0.5s ease;'>"),
    dashboard_content,
    pn.pane.HTML("</div>")
)

# Serve the Panel dashboard
if __name__ == "__main__":
    pn.serve(dashboard)
