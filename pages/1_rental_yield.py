import streamlit as st

st.title("🏠 מחשבון תשואה משכירות")

# קלט מהמשתמש עם סליידרים
col1, col2 = st.columns(2)

with col1:
    price = st.slider("מחיר רכישת הדירה (₪)", min_value=0, max_value=5000000, value=1500000, step=50000)
    monthly_rent = st.slider("שכירות חודשית צפויה (₪)", min_value=0, max_value=20000, value=4500, step=100)

with col2:
    expenses = st.slider("הוצאות שנתיות (תחזוקה, ביטוח וכו')", min_value=0, max_value=50000, value=5000, step=500)
    tax_rate = st.slider("אחוז מס (אם רלוונטי)", min_value=0, max_value=100, value=10, step=1)

# חישובים
annual_income = monthly_rent * 12
annual_net_income = annual_income - expenses - (annual_income * (tax_rate / 100))
yield_pct = (annual_net_income / price) * 100 if price > 0 else 0

# הצגת תוצאות
st.divider()
st.subheader("סיכום נתונים")

m1, m2, m3 = st.columns(3)
m1.metric("הכנסה שנתית נטו", f"₪{annual_net_income:,.0f}")
m2.metric("תשואה שנתית", f"{yield_pct:.2f}%")
m3.metric("החזר חודשי נטו", f"₪{annual_net_income/12:,.0f}")

if yield_pct > 4:
    st.success("זו נראית כמו עסקה מעניינת!")
elif yield_pct > 2:
    st.warning("תשואה סבירה, כדאי לבחון אלטרנטיבות.")
else:
    st.error("התשואה נמוכה יחסית.")
