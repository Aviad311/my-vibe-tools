import streamlit as st
import pandas as pd
from st_keyup import st_keyup

st.title("📈 מחשבון ריבית דריבית")
st.write("חשב את גדילת ההון שלך בשידור חי - כולל דמי ניהול מדויקים ומס.")

st.divider()

# קלט מהמשתמש - חלק ראשון: הפקדות וזמן
col1, col2 = st.columns(2)
with col1:
    principal = st.slider("סכום התחלתי (₪)", min_value=0, max_value=1000000, value=50000, step=5000)
    monthly_deposit = st.slider("הפקדה חודשית (₪)", min_value=0, max_value=20000, value=2000, step=500)

with col2:
    years = st.slider("תקופת השקעה (בשנים)", min_value=1, max_value=50, value=20, step=1)
    interest_rate = st.slider("תשואה שנתית צפויה (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.5)

# קלט מהמשתמש - חלק שני: עלויות (דיוק מקסימלי)
st.subheader("🛰️ עלויות ומיסוי")
c1, c2 = st.columns(2)
with c1:
    # כאן החלפנו את הסליידר בשדה הקלדה מהיר ומדויק
    fee_str = st_keyup("דמי ניהול שנתיים מהצבירה (%)", value="0.5", key="mgmt_fee")
with c2:
    tax_rate = 25  # מס רווחי הון קבוע

# לוגיקת חישוב
try:
    management_fee = float(fee_str) if fee_str else 0.0
    
    months = years * 12
    # תשואה נטו שנתית בניכוי דמי ניהול
    annual_net_rate = interest_rate - management_fee
    monthly_rate = annual_net_rate / 100 / 12

    data = []
    current_balance = principal
    total_deposits = principal

    for month in range(1, months + 1):
        current_balance = current_balance * (1 + monthly_rate) + monthly_deposit
        total_deposits += monthly_deposit
        
        if month % 12 == 0:
            data.append({
                "שנה": month // 12,
                "סך הפקדות": total_deposits,
                "שווי ברוטו": current_balance
            })

    # חישוב מס ונטו סופי
    total_profit = current_balance - total_deposits
    total_tax = max(0, total_profit * (tax_rate / 100))
    net_balance = current_balance - total_tax

    df = pd.DataFrame(data).set_index("שנה")

    # הצגת תוצאות
    st.divider()
    st.subheader("💰 סיכום תוצאות")

    m1, m2, m3 = st.columns(3)
    m1.metric("שווי ברוטו", f"₪{current_balance:,.0f}")
    m2.metric("רווח לפני מס", f"₪{total_profit:,.0f}")
    m3.metric("סך ההפקדות", f"₪{total_deposits:,.0f}")

    st.divider()
    st.subheader("🏁 השורה התחתונה (נטו)")
    n1, n2 = st.columns(2)
    n1.metric("סכום למשיכה (אחרי מס)", f"₪{net_balance:,.0f}", delta=f"-₪{total_tax:,.0f} מס", delta_color="inverse")
    n2.info(f"החישוב מתבצע לפי תשואה נטו של {annual_net_rate:.2f}% בשנה.")

    st.line_chart(df)

except ValueError:
    st.warning("נא להזין אחוז דמי ניהול תקין (למשל: 0.5)")
