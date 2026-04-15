import streamlit as st

st.title("🔢 ממיר בסיסים")
st.write("בחר את בסיס המקור ואת בסיס היעד, והכנס את הערך שתרצה להמיר.")

st.divider()

# הגדרת הבסיסים האפשריים
bases = {
    "דצימלי (Decimal) - 10": 10,
    "הקסדצימלי (Hex) - 16": 16,
    "בינארי (Binary) - 2": 2,
    "אוקטלי (Octal) - 8": 8
}

# יצירת שתי עמודות לתצוגה סימטרית
col1, col2 = st.columns(2)

with col1:
    st.markdown("### מאיזה בסיס?")
    source_base_name = st.selectbox("בחר בסיס מקור:", list(bases.keys()), key="source")
    source_val = st.text_input("הכנס קלט להמרה:", placeholder="לדוגמה: 1A או 1011")

with col2:
    st.markdown("### לאיזה בסיס?")
    target_base_name = st.selectbox("בחר בסיס יעד:", list(bases.keys()), key="target")
    
    # לוגיקת ההמרה מופעלת רק אם הוזן קלט
    result = ""
    if source_val:
        try:
            source_base = bases[source_base_name]
            target_base = bases[target_base_name]
            
            # שלב 1: המרת הקלט למספר שלם (בסיס 10) לפי בסיס המקור
            decimal_val = int(source_val, source_base)
            
            # שלב 2: המרת המספר השלם לבסיס היעד
            if target_base == 10:
                result = str(decimal_val)
            elif target_base == 16:
                result = hex(decimal_val).replace("0x", "").upper()
            elif target_base == 2:
                result = bin(decimal_val).replace("0b", "")
            elif target_base == 8:
                result = oct(decimal_val).replace("0o", "")
                
        except ValueError:
            result = "❌ קלט לא תקין לבסיס זה"

    # הצגת התוצאה כשדה טקסט קריאה-בלבד
    st.text_input("פלט ההמרה:", value=result, disabled=True)
