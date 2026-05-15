# Complete Updated `app.py`
import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import random

# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Budget Travel Intelligence System",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────
# MINIMAL PREMIUM CSS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
.stApp {
    background: #f8fafc;
    color: #111827;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 18px 16px 34px;
    margin: 0 auto 20px;
    text-align: center;
}

.hero h1 {
    color: #1f2937;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 700;
    line-height: 1.15;
    margin: 0 0 14px;
    text-align: center;
}

.hero p {
    color: #6b7280;
    font-size: 1rem;
    line-height: 1.5;
    margin: 0 auto;
    max-width: 680px;
    text-align: center;
}

.metric-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    min-height: 150px;
    padding: 22px 18px;
    text-align: center;
}

.metric-title {
    color: #9ca3af;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    margin-bottom: 10px;
    text-transform: uppercase;
}

.metric-value {
    color: #111827;
    font-size: 1.55rem;
    font-weight: 700;
    line-height: 1.25;
    overflow-wrap: anywhere;
}

.metric-sub {
    color: #6b7280;
    font-size: 0.9rem;
    margin-top: 8px;
    overflow-wrap: anywhere;
}

.section-title {
    color: #111827;
    font-size: 1.5rem;
    font-weight: 700;
    margin: 34px 0 18px;
}

.dest-card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    min-height: 210px;
    padding: 20px;
    margin-bottom: 16px;
}

.dest-card h3 {
    color: #111827;
    font-size: 1.1rem;
    line-height: 1.3;
    margin: 0 0 6px;
    overflow-wrap: anywhere;
}

.badge {
    display: inline-block;
    background: #f3f4f6;
    color: #374151;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 600;
    margin: 6px 6px 0 0;
    padding: 5px 10px;
    white-space: nowrap;
}

.recommend-box {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    margin-top: 16px;
    padding: 12px;
}

.recommend-label {
    font-size: 0.72rem;
    color: #9ca3af;
    font-weight: 600;
    margin-bottom: 4px;
}

.recommend-text {
    color: #374151;
    font-size: 0.88rem;
    line-height: 1.5;
}

.stSidebar {
    background: #ffffff;
}

@media (max-width: 700px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        padding-top: 8px;
    }
}

</style>
""", unsafe_allow_html=True)


def plotly_chart_stretch(fig, **kwargs):
    try:
        st.plotly_chart(fig, width="stretch", **kwargs)
    except TypeError:
        st.plotly_chart(fig, use_container_width=True, **kwargs)


def dataframe_stretch(data, **kwargs):
    try:
        st.dataframe(data, width="stretch", **kwargs)
    except TypeError:
        st.dataframe(data, use_container_width=True, **kwargs)

# ─────────────────────────────────────────────────────────────
# DATASET GENERATION
# ─────────────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def generate_dataset():
    csv_path = "travel_data.csv"
    required_columns = {
        "Destination",
        "State",
        "Hotel_Name",
        "Hotel_Type",
        "Hotel_Rating",
        "Transport_Cost",
        "Hotel_Cost",
        "Food_Cost",
        "Total_Cost",
        "Season",
        "Best_Season",
        "Crowd_Level",
        "Trip_Type",
        "Destination_Rating",
        "Travel_Mode",
    }

    if os.path.exists(csv_path):
        existing_df = pd.read_csv(csv_path)
        if required_columns.issubset(existing_df.columns):
            return existing_df

    random.seed(42)
    np.random.seed(42)

    destinations = [
        ("Goa", "Beach", "Winter", "Goa", 4.8),
        ("Ooty", "Hill Station", "Summer", "Tamil Nadu", 4.5),
        ("Coorg", "Nature", "Monsoon", "Karnataka", 4.6),
        ("Manali", "Adventure", "Summer", "Himachal Pradesh", 4.8),
        ("Munnar", "Nature", "Winter", "Kerala", 4.7),
        ("Pondicherry", "Cultural", "Winter", "Puducherry", 4.4),
        ("Gokarna", "Beach", "Winter", "Karnataka", 4.5),
        ("Jaipur", "Cultural", "Winter", "Rajasthan", 4.7),
        ("Ladakh", "Adventure", "Summer", "Ladakh", 4.9),
        ("Darjeeling", "Hill Station", "Summer", "West Bengal", 4.7),
    ]

    seasons = ["Winter", "Summer", "Monsoon", "Spring", "Autumn"]
    crowd_levels = ["Low", "Medium", "High"]
    hotel_types = ["Budget", "Mid-Range", "Luxury"]
    travel_modes = ["Bus", "Train", "Flight", "Self-drive"]

    rows = []

    for dest, trip_type, best_season, state, rating in destinations:
        for i in range(60):
            season = random.choice(seasons)
            crowd = random.choice(crowd_levels)
            hotel_type = random.choice(hotel_types)
            travel_mode = random.choice(travel_modes)

            hotel_rating = round(random.uniform(3.5, 5.0), 1)

            hotel_cost = {
                "Budget": random.randint(1200, 2500),
                "Mid-Range": random.randint(3000, 5500),
                "Luxury": random.randint(6500, 12000)
            }[hotel_type]

            transport_cost = random.randint(800, 5000)
            food_cost = random.randint(500, 2500)

            if season == best_season:
                hotel_cost = int(hotel_cost * 1.2)

            total_cost = hotel_cost + transport_cost + food_cost

            rows.append({
                "Destination": dest,
                "State": state,
                "Hotel_Name": f"{dest} {hotel_type} Stay {i+1}",
                "Hotel_Type": hotel_type,
                "Hotel_Rating": hotel_rating,
                "Transport_Cost": transport_cost,
                "Hotel_Cost": hotel_cost,
                "Food_Cost": food_cost,
                "Total_Cost": total_cost,
                "Season": season,
                "Best_Season": best_season,
                "Crowd_Level": crowd,
                "Trip_Type": trip_type,
                "Destination_Rating": rating,
                "Travel_Mode": travel_mode,
            })

    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)
    return df


df = generate_dataset()

# ─────────────────────────────────────────────────────────────
# SIDEBAR FILTERS
# ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## Travel Filters")

    budget = st.slider(
        "Max Budget",
        min_value=3000,
        max_value=20000,
        value=8000,
        step=500,
    )

    season = st.selectbox(
        "Season",
        ["All"] + sorted(df["Season"].unique().tolist())
    )

    trip_type = st.selectbox(
        "Trip Type",
        ["All"] + sorted(df["Trip_Type"].unique().tolist())
    )

    crowd = st.selectbox(
        "Crowd Level",
        ["All"] + sorted(df["Crowd_Level"].unique().tolist())
    )

    min_rating = st.slider(
        "Min Hotel Rating",
        min_value=3.0,
        max_value=5.0,
        value=4.0,
        step=0.1,
    )

# ─────────────────────────────────────────────────────────────
# SMART FILTERING
# ─────────────────────────────────────────────────────────────
fdf = df.copy()

budget_limit = int(budget * 1.25)

fdf = fdf[fdf["Total_Cost"] <= budget_limit]
fdf = fdf[fdf["Hotel_Rating"] >= min_rating]

if season != "All":
    fdf = fdf[fdf["Season"] == season]

if trip_type != "All":
    fdf = fdf[fdf["Trip_Type"] == trip_type]

if crowd != "All":
    fdf = fdf[fdf["Crowd_Level"] == crowd]

if fdf.empty:
    fdf = df.copy()
    fdf = fdf[fdf["Hotel_Rating"] >= 3.5]

fdf["Budget_Score"] = (
    1 - abs(fdf["Total_Cost"] - budget) / budget_limit
)

fdf["Budget_Score"] = fdf["Budget_Score"].clip(lower=0)

fdf["Recommendation_Score"] = (
    (fdf["Hotel_Rating"] * 0.35) +
    (fdf["Destination_Rating"] * 0.30) +
    (fdf["Budget_Score"] * 5 * 0.35)
)

# ─────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>Discover Your Next Journey</h1>
    <p>Find budget-friendly destinations and hotels tailored to your travel preferences.</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# KPI SECTION
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Overview</div>', unsafe_allow_html=True)

cheapest = fdf.loc[fdf["Total_Cost"].idxmin()]
avg_cost = int(fdf["Total_Cost"].mean())
top_hotel = fdf.loc[fdf["Hotel_Rating"].idxmax()]
dest_count = fdf["Destination"].nunique()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Cheapest Destination", cheapest["Destination"], f"Rs. {cheapest['Total_Cost']:,}")

with c2:
    st.metric("Average Trip Cost", f"Rs. {avg_cost:,}", "Budget optimized")

with c3:
    st.metric("Top Hotel Rating", top_hotel["Hotel_Rating"], top_hotel["Hotel_Name"])

with c4:
    st.metric("Destinations", dest_count, "Matching results")

# ─────────────────────────────────────────────────────────────
# RECOMMENDATIONS
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Recommended Destinations</div>', unsafe_allow_html=True)

recommendations = fdf.groupby("Destination").agg(
    Avg_Total=("Total_Cost", "mean"),
    Min_Total=("Total_Cost", "min"),
    Recommendation_Score=("Recommendation_Score", "mean"),
    Destination_Rating=("Destination_Rating", "first"),
    State=("State", "first"),
    Best_Season=("Best_Season", "first"),
    Trip_Type=("Trip_Type", "first"),
).reset_index()

recommendations = recommendations.sort_values(
    ["Recommendation_Score", "Destination_Rating"],
    ascending=[False, False]
).head(6)

cols = st.columns(3)

for idx, (_, row) in enumerate(recommendations.iterrows()):
    with cols[idx % 3]:
        with st.container(border=True):
            st.subheader(row["Destination"])
            st.caption(row["State"])
            st.write(f"Rating: {row['Destination_Rating']} | {row['Trip_Type']} | {row['Best_Season']}")
            st.metric("Starting From", f"Rs. {int(row['Min_Total']):,}")
            st.caption("Why recommended")
            st.write("Great balance of pricing, ratings, and travel experience based on your preferences.")

# ─────────────────────────────────────────────────────────────
# HOTEL SECTION
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Popular Hotels</div>', unsafe_allow_html=True)

hotel_df = fdf.sort_values(
    ["Recommendation_Score", "Hotel_Rating"],
    ascending=[False, False]
).head(6)

hc1, hc2 = st.columns(2)

for idx, (_, row) in enumerate(hotel_df.iterrows()):
    with (hc1 if idx % 2 == 0 else hc2):
        with st.container(border=True):
            st.subheader(row["Hotel_Name"])
            st.caption(f"{row['Destination']}, {row['State']}")
            st.write(f"Rating: {row['Hotel_Rating']} | {row['Hotel_Type']} | {row['Travel_Mode']}")
            hcost, tcost = st.columns(2)
            hcost.metric("Hotel Cost", f"Rs. {row['Hotel_Cost']:,}")
            tcost.metric("Trip Total", f"Rs. {row['Total_Cost']:,}")

# ─────────────────────────────────────────────────────────────
# ANALYTICS
# ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Travel Analytics</div>', unsafe_allow_html=True)

chart1, chart2 = st.columns(2)

with chart1:
    cost_chart = fdf.groupby("Destination")["Total_Cost"].mean().reset_index()

    fig = px.bar(
        cost_chart.sort_values("Total_Cost"),
        x="Destination",
        y="Total_Cost",
        color="Total_Cost",
        color_continuous_scale="Blues",
        title="Average Trip Cost",
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False,
    )

    plotly_chart_stretch(fig)

with chart2:
    crowd_chart = fdf.groupby("Crowd_Level").size().reset_index(name="Count")

    fig2 = px.pie(
        crowd_chart,
        names="Crowd_Level",
        values="Count",
        hole=0.55,
        title="Crowd Distribution",
    )

    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    plotly_chart_stretch(fig2)

# ─────────────────────────────────────────────────────────────
# RAW DATA
# ─────────────────────────────────────────────────────────────
with st.expander("View Travel Dataset"):
    dataframe_stretch(
        fdf.sort_values("Recommendation_Score", ascending=False)[[
            "Destination",
            "Hotel_Name",
            "Hotel_Rating",
            "Hotel_Cost",
            "Transport_Cost",
            "Food_Cost",
            "Total_Cost",
            "Trip_Type",
            "Season",
            "Crowd_Level"
        ]]
    )

# ─────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:60px 20px 20px;color:#9ca3af;">
    Budget Travel Intelligence System • Built with Streamlit
</div>
""", unsafe_allow_html=True)
