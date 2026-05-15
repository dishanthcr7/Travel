"""
generate_dataset.py
Auto-generates a realistic synthetic Indian travel dataset (travel_data.csv).
Run this script once, or let app.py call it automatically on first launch.
"""

import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

# ─────────────────────────────────────────────────────────────
# Reference data
# ─────────────────────────────────────────────────────────────

destinations_info = [
    {"Destination": "Goa",         "State": "Goa",             "Best_Season": "Winter",  "Trip_Type": "Beach",      "Crowd_Level": "High",   "Destination_Rating": 4.6, "base_transport": 4500, "base_hotel": 2800, "base_food": 900},
    {"Destination": "Ooty",        "State": "Tamil Nadu",      "Best_Season": "Summer",  "Trip_Type": "Hill Station","Crowd_Level": "Medium", "Destination_Rating": 4.3, "base_transport": 2200, "base_hotel": 1800, "base_food": 600},
    {"Destination": "Coorg",       "State": "Karnataka",       "Best_Season": "Monsoon", "Trip_Type": "Nature",     "Crowd_Level": "Low",    "Destination_Rating": 4.5, "base_transport": 2500, "base_hotel": 2200, "base_food": 700},
    {"Destination": "Meghalaya",   "State": "Meghalaya",       "Best_Season": "Monsoon", "Trip_Type": "Adventure",  "Crowd_Level": "Low",    "Destination_Rating": 4.7, "base_transport": 5500, "base_hotel": 1600, "base_food": 500},
    {"Destination": "Munnar",      "State": "Kerala",          "Best_Season": "Winter",  "Trip_Type": "Hill Station","Crowd_Level": "Medium", "Destination_Rating": 4.6, "base_transport": 3000, "base_hotel": 2000, "base_food": 650},
    {"Destination": "Pondicherry", "State": "Puducherry",      "Best_Season": "Winter",  "Trip_Type": "Cultural",   "Crowd_Level": "Medium", "Destination_Rating": 4.4, "base_transport": 2800, "base_hotel": 2100, "base_food": 750},
    {"Destination": "Manali",      "State": "Himachal Pradesh","Best_Season": "Summer",  "Trip_Type": "Adventure",  "Crowd_Level": "High",   "Destination_Rating": 4.7, "base_transport": 5000, "base_hotel": 2400, "base_food": 800},
    {"Destination": "Hampi",       "State": "Karnataka",       "Best_Season": "Winter",  "Trip_Type": "Cultural",   "Crowd_Level": "Low",    "Destination_Rating": 4.5, "base_transport": 2700, "base_hotel": 1400, "base_food": 450},
    {"Destination": "Gokarna",     "State": "Karnataka",       "Best_Season": "Winter",  "Trip_Type": "Beach",      "Crowd_Level": "Low",    "Destination_Rating": 4.4, "base_transport": 3200, "base_hotel": 1300, "base_food": 500},
    {"Destination": "Darjeeling",  "State": "West Bengal",     "Best_Season": "Summer",  "Trip_Type": "Hill Station","Crowd_Level": "Medium", "Destination_Rating": 4.5, "base_transport": 4800, "base_hotel": 1900, "base_food": 600},
    {"Destination": "Shimla",      "State": "Himachal Pradesh","Best_Season": "Summer",  "Trip_Type": "Hill Station","Crowd_Level": "High",   "Destination_Rating": 4.4, "base_transport": 4500, "base_hotel": 2300, "base_food": 750},
    {"Destination": "Jaipur",      "State": "Rajasthan",       "Best_Season": "Winter",  "Trip_Type": "Cultural",   "Crowd_Level": "High",   "Destination_Rating": 4.6, "base_transport": 3500, "base_hotel": 2500, "base_food": 800},
    {"Destination": "Rishikesh",   "State": "Uttarakhand",     "Best_Season": "Spring",  "Trip_Type": "Adventure",  "Crowd_Level": "Medium", "Destination_Rating": 4.6, "base_transport": 3800, "base_hotel": 1700, "base_food": 550},
    {"Destination": "Varanasi",    "State": "Uttar Pradesh",   "Best_Season": "Winter",  "Trip_Type": "Cultural",   "Crowd_Level": "High",   "Destination_Rating": 4.5, "base_transport": 3200, "base_hotel": 1600, "base_food": 500},
    {"Destination": "Ladakh",      "State": "Ladakh",          "Best_Season": "Summer",  "Trip_Type": "Adventure",  "Crowd_Level": "Low",    "Destination_Rating": 4.9, "base_transport": 7000, "base_hotel": 2000, "base_food": 700},
    {"Destination": "Alleppey",    "State": "Kerala",          "Best_Season": "Winter",  "Trip_Type": "Nature",     "Crowd_Level": "Medium", "Destination_Rating": 4.6, "base_transport": 3100, "base_hotel": 2200, "base_food": 700},
    {"Destination": "Udaipur",     "State": "Rajasthan",       "Best_Season": "Winter",  "Trip_Type": "Cultural",   "Crowd_Level": "Medium", "Destination_Rating": 4.7, "base_transport": 3800, "base_hotel": 2800, "base_food": 850},
    {"Destination": "Spiti Valley","State": "Himachal Pradesh","Best_Season": "Summer",  "Trip_Type": "Adventure",  "Crowd_Level": "Low",    "Destination_Rating": 4.8, "base_transport": 6500, "base_hotel": 1500, "base_food": 600},
    {"Destination": "Andaman",     "State": "Andaman & Nicobar","Best_Season": "Winter", "Trip_Type": "Beach",      "Crowd_Level": "Medium", "Destination_Rating": 4.8, "base_transport": 9000, "base_hotel": 3200, "base_food": 900},
    {"Destination": "Mysore",      "State": "Karnataka",       "Best_Season": "Autumn",  "Trip_Type": "Cultural",   "Crowd_Level": "Medium", "Destination_Rating": 4.4, "base_transport": 2400, "base_hotel": 1800, "base_food": 600},
    {"Destination": "Lakshadweep", "State": "Lakshadweep",     "Best_Season": "Winter",  "Trip_Type": "Beach",      "Crowd_Level": "Low",    "Destination_Rating": 4.9, "base_transport": 11000,"base_hotel": 3500, "base_food": 1000},
    {"Destination": "Jodhpur",     "State": "Rajasthan",       "Best_Season": "Winter",  "Trip_Type": "Cultural",   "Crowd_Level": "Medium", "Destination_Rating": 4.5, "base_transport": 3600, "base_hotel": 2200, "base_food": 700},
    {"Destination": "Nainital",    "State": "Uttarakhand",     "Best_Season": "Summer",  "Trip_Type": "Hill Station","Crowd_Level": "High",   "Destination_Rating": 4.3, "base_transport": 3900, "base_hotel": 2000, "base_food": 650},
    {"Destination": "Kodaikanal",  "State": "Tamil Nadu",      "Best_Season": "Summer",  "Trip_Type": "Hill Station","Crowd_Level": "Medium", "Destination_Rating": 4.4, "base_transport": 2600, "base_hotel": 1900, "base_food": 620},
    {"Destination": "Pushkar",     "State": "Rajasthan",       "Best_Season": "Autumn",  "Trip_Type": "Cultural",   "Crowd_Level": "Medium", "Destination_Rating": 4.3, "base_transport": 3300, "base_hotel": 1500, "base_food": 550},
]

hotel_templates = {
    "Beach":       ["Sunset Shores Resort", "Coral Bay Inn", "SeaBreeze Boutique", "Horizon Beach Hotel", "Palm Grove Stay", "Oceanic Retreat", "Tidal Wave Resort"],
    "Hill Station":["Mountain Mist Inn", "Pine Valley Resort", "Hilltop Heritage", "Cloud9 Retreat", "Evergreen Lodge", "Summit View Hotel", "Misty Peaks Inn"],
    "Adventure":   ["Base Camp Inn", "Trekker's Den", "Summit Stay", "Explorer's Lodge", "Wilderness Retreat", "Adrenaline Hub", "Nomad's Rest"],
    "Cultural":    ["Heritage Haveli", "Old Town Inn", "Royal Retreat", "Cultural Corner", "Artisan Stay", "Palace Residency", "Craft Lodge"],
    "Nature":      ["Jungle Nest", "Canopy Lodge", "Forest Edge Resort", "Eco Haven", "Green Leaf Retreat", "Wild Orchid Inn", "Nature's Abode"],
}

travel_modes = {
    "Goa": "Flight", "Manali": "Bus", "Shimla": "Train", "Ladakh": "Flight",
    "Spiti Valley": "Bus", "Andaman": "Flight", "Lakshadweep": "Flight",
    "Jaipur": "Train", "Varanasi": "Train", "Udaipur": "Train", "Jodhpur": "Train",
    "Rishikesh": "Train", "Nainital": "Train", "Darjeeling": "Train",
    "Meghalaya": "Flight", "Alleppey": "Train", "Munnar": "Train",
    "Ooty": "Train", "Coorg": "Bus", "Gokarna": "Train", "Hampi": "Train",
    "Pondicherry": "Train", "Mysore": "Train", "Kodaikanal": "Bus",
    "Pushkar": "Train",
}

rows = []
for dest in destinations_info:
    trip_type = dest["Trip_Type"]
    hotel_names = hotel_templates.get(trip_type, hotel_templates["Cultural"])
    travel_mode = travel_modes.get(dest["Destination"], "Train")

    # Generate 8 hotel entries per destination
    for i in range(8):
        hotel_name = hotel_names[i % len(hotel_names)]
        hotel_rating = round(min(5.0, max(2.5, dest["Destination_Rating"] + random.uniform(-0.8, 0.5))), 1)

        # Tier multiplier based on rating
        tier = 1.0 + (hotel_rating - 3.0) * 0.25
        transport = int(dest["base_transport"] * random.uniform(0.85, 1.20))
        hotel    = int(dest["base_hotel"]    * tier * random.uniform(0.80, 1.25))
        food     = int(dest["base_food"]     * random.uniform(0.85, 1.20))
        total    = transport + hotel + food

        rows.append({
            "Destination":        dest["Destination"],
            "State":              dest["State"],
            "Hotel_Name":         hotel_name,
            "Hotel_Rating":       hotel_rating,
            "Transport_Cost":     transport,
            "Hotel_Cost":         hotel,
            "Food_Cost":          food,
            "Total_Cost":         total,
            "Best_Season":        dest["Best_Season"],
            "Crowd_Level":        dest["Crowd_Level"],
            "Trip_Type":          trip_type,
            "Destination_Rating": dest["Destination_Rating"],
            "Travel_Mode":        travel_mode,
        })

df = pd.DataFrame(rows)
df.to_csv("travel_data.csv", index=False)
print(f"✅  Dataset generated: {len(df)} rows saved to travel_data.csv")

if __name__ == "__main__":
    pass  # already executed at module level
