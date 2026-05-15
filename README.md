# 🌏 Budget Travel Intelligence System

A **Streamlit-powered** travel analytics & recommendation platform that helps you discover budget-friendly Indian destinations and hotels — all from a rich, auto-generated synthetic dataset.

---

## 🚀 Quick Start

### 1. Clone / Download the project
```bash
cd d:\Travel
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux / macOS
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

The dataset (`travel_data.csv`) is **auto-generated** on first launch — no manual downloads needed.

---

## 📁 Project Structure

```
Travel/
│
├── app.py                  # Main Streamlit application
├── generate_dataset.py     # Synthetic dataset generator
├── travel_data.csv         # Auto-generated dataset (created on first run)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## ✨ Features

| Feature | Details |
|---|---|
| 🗂️ Auto Dataset | 200+ rows of realistic Indian travel data |
| 🔍 Smart Filters | Budget, Season, Trip Type, Crowd Level, Hotel Rating |
| 🏆 Recommendations | Top destinations & hotels ranked by value |
| 📊 Analytics | Plotly charts — cost, trends, ratings, crowd |
| 💡 KPI Cards | Cheapest destination, avg cost, top hotel |
| 🧹 Error Handling | Empty results, invalid filters, missing data |

---

## 🗺️ Destinations Included

Goa, Ooty, Coorg, Meghalaya, Munnar, Pondicherry, Manali, Hampi, Gokarna, Darjeeling, Shimla, Jaipur, Rishikesh, Varanasi, Ladakh, Alleppey, Udaipur, Spiti Valley, Andaman, Mysore, Lakshadweep, Jodhpur, Nainital, Kodaikanal, Pushkar

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** — UI framework
- **Pandas** — data processing & filtering
- **Plotly** — interactive visualisations
- **NumPy** — synthetic data generation

---

## 📌 Notes

- The dataset is regenerated only if `travel_data.csv` is missing.
- All costs are in **Indian Rupees (₹)** per person per day.
- Filtering logic uses simple Pandas queries — no ML involved.
