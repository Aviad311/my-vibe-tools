import streamlit as st
from st_keyup import st_keyup

st.title("⏱️ ממיר תדרי שעון וזמנים")
st.write("מחשבון מהיר להמרות בין תדרי מערכת לזמני מחזור (Period) - מתעדכן בזמן אמת.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("מתדר לזמן מחזור")
    # שימוש ב-st_keyup במקום שדה מספר רגיל
    freq_str = st_keyup("הכנס תדר:", value="1.0", key="f_val")
    freq_unit = st.selectbox("יחידת מידה:", ["GHz", "MHz", "kHz", "Hz"], key="f_unit")
    
    try:
        # המרת הטקסט למספר עשרוני בבטחה
        freq_val = float(freq_str) if freq_str else 0.0
        
        if freq_val > 0:
            # המרה להרץ
            multiplier = {"GHz": 1e9, "MHz": 1e6, "kHz": 1e3, "Hz": 1}
            freq_hz = freq_val * multiplier[freq_unit]
            
            # חישוב זמן מחזור
            period_s = 1 / freq_hz
            
            st.info(f"**זמן מחזור (Period):**\n"
                    f"- {period_s * 1e9:.3f} ns (ננו-שניות)\n"
                    f"- {period_s * 1e12:.0f} ps (פיקו-שניות)")
    except ValueError:
        st.warning("נא להזין מספר תקין")

with col2:
    st.subheader("מזמן מחזור לתדר")
    # שימוש ב-st_keyup
    time_str = st_keyup("הכנס זמן מחזור:", value="1.0", key="t_val")
    time_unit = st.selectbox("יחידת מידה:", ["ns (ננו-שניות)", "ps (פיקו-שניות)", "us (מיקרו-שניות)"], key="t_unit")
    
    try:
        # המרת הטקסט למספר עשרוני בבטחה
        time_val = float(time_str) if time_str else 0.0
        
        if time_val > 0:
            # המרה לשניות
            multiplier = {"ns (ננו-שניות)": 1e-9, "ps (פיקו-שניות)": 1e-12, "us (מיקרו-שניות)": 1e-6}
            time_s = time_val * multiplier[time_unit]
            
            # חישוב תדר
            freq_hz = 1 / time_s
            
            st.success(f"**תדר מערכת (Frequency):**\n"
                     f"- {freq_hz / 1e9:.3f} GHz\n"
                     f"- {freq_hz / 1e6:.3f} MHz")
    except ValueError:
        st.warning("נא להזין מספר תקין")
