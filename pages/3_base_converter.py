import streamlit as st

st.title("🔢 ממיר בסיסים וייצוג חומרה")
st.write("כלי עזר להמרות בסיסים מהירות ולחישובי משלים ל-2 (Two's Complement).")

bit_width = st.radio("בחר רוחב סיביות (Bit Width):", [8, 16, 32, 64], index=2, horizontal=True)

col1, col2 = st.columns(2)
with col1:
    input_base = st.selectbox("בסיס הקלט שלך:", ["דצימלי (Decimal)", "הקסדצימלי (Hex)", "בינארי (Binary)"])
with col2:
    input_value = st.text_input("הכנס ערך:")

if input_value:
    try:
        # המרת הקלט למספר שלם
        if input_base == "דצימלי (Decimal)":
            val = int(input_value)
        elif input_base == "הקסדצימלי (Hex)":
            val = int(input_value, 16)
        else:
            val = int(input_value, 2)
            
        # הפעלת מסכה לפי רוחב הסיביות שנבחר
        mask = (1 << bit_width) - 1
        val_masked = val & mask
        
        # יצירת המחרוזות
        bin_str = format(val_masked, f'0{bit_width}b')
        hex_str = format(val_masked, f'0{bit_width // 4}X')
        
        # חישוב ערך דצימלי עם סימן (Signed)
        if val_masked & (1 << (bit_width - 1)):
            signed_dec = val_masked - (1 << bit_width)
        else:
            signed_dec = val_masked
            
        st.divider()
        st.subheader("תוצאות ההמרה")
        
        # תצוגה בסגנון חומרה
        st.code(f"Binary: {bit_width}'b{bin_str}", language="verilog")
        st.code(f"Hex:    {bit_width}'h{hex_str}", language="verilog")
        st.code(f"Signed Decimal (2's Comp):   {signed_dec}", language="text")
        st.code(f"Unsigned Decimal:            {val_masked}", language="text")
        
    except ValueError:
        st.error("❌ הערך שהוזן לא חוקי עבור הבסיס שנבחר. (למשל: אל תכניס אותיות לבסיס דצימלי)")
