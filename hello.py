# 1. Load dataset
from preswald import connect, get_df
connect()
df = get_df("Top_Influencers_Modified")  # Dataset registered in preswald.toml

# 2. Query/filter dataset (ensure numeric filtering works)
from preswald import query
sql = 'SELECT * FROM Top_Influencers_Modified WHERE CAST("Influence Score" AS INTEGER) > 50'
filtered_df = query(sql, "Top_Influencers_Modified")

# 3. Display title and filtered data
from preswald import table, text
text("# 📊 My Influencer Insights Dashboard")
table(filtered_df, title="Top Influencers with Influence Score > 50")

# 4. Create and show scatter plot with cleaned data
from preswald import plotly
import plotly.express as px
import pandas as pd  # Needed for type conversion

# Ensure numeric types for plotting
# Ensure numeric types
filtered_df["Influence Score"] = pd.to_numeric(filtered_df["Influence Score"], errors="coerce")
filtered_df["Posts"] = pd.to_numeric(filtered_df["Posts"], errors="coerce")
filtered_df["Followers"] = pd.to_numeric(filtered_df["Followers"], errors="coerce")

# Check size
text(f"Plotting {len(filtered_df)} influencers")

# Plot directly without dropping rows
fig = px.scatter(
    filtered_df,
    x="Influence Score",
    y="Posts",
    size="Followers",
    size_max=60,
    hover_name="Channel Info",
    color="Country Or Region",
    title="Influence Score vs Posts (Colored by Country)",
    opacity=0.8
)

fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
plotly(fig)

