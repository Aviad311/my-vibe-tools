import streamlit as st
import pandas as pd

st.title("📈 מחשבון ריבית דריבית")

# קלט מהמשתמש עם סליידרים
col1, col2 = st.columns(2)
with col1:
    principal = st.slider("סכום התחלתי (₪)", min_value=0, max_value=1000000, value=10000, step=5000)
    monthly_deposit = st.slider("הפקדה חודשית (₪)", min_value=0, max_value=20000, value=1000, step=500)

with col2:
    years = st.slider("תקופת השקעה (בשנים)", min_value=1, max_value=50, value=10, step=1)
    interest_rate = st.slider("תשואה שנתית צפויה (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.5)

# חישובים
months = years * 12
monthly_rate = interest_rate / 100 / 12

data = []
current_balance = principal
total_deposits = principal

for month in range(1, months + 1):
    current_balance = current_balance * (1 + monthly_rate) + monthly_deposit
    total_deposits += monthly_deposit
    
    # שומרים נתונים כל שנה עבור הגרף
    if month % 12 == 0:
        data.append({
            "שנה": month // 12,
            "סך הפקדות": total_deposits,
            "שווי התיק": current_balance
        })

df = pd.DataFrame(data).set_index("שנה")

# הצגת תוצאות
st.divider()
st.subheader("תוצאות")

m1, m2, m3 = st.columns(3)
m1.metric("שווי סופי", f"₪{current_balance:,.0f}")
m2.metric("סך ההפקדות שלך", f"₪{total_deposits:,.0f}")
profit = current_balance - total_deposits
m3.metric("רווח נקי", f"₪{profit:,.0f}")

st.line_chart(df)
