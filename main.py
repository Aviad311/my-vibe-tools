import streamlit as st

st.set_page_config(
    page_title="הכלים שלי",
    page_icon="🛠️",
    layout="wide" # פותח את המסך לרוחב, נראה הרבה יותר טוב
)

# כותרת ראשית
st.markdown("<h1 style='text-align: center;'>🛠️ מרכז הכלים האישי</h1>", unsafe_allow_html=True)
st.write("---")

# יצירת גריד של כפתורים גדולים (2 עמודות)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💰 פיננסים")
    # כפתור מעוצב למחשבון תשואה
    if st.button("🏠 מחשבון תשואת שכירות", use_container_width=True):
        st.switch_page("pages/1_rental_yield.py")
    
    # כפתור מעוצב לריבית דריבית
    if st.button("📈 מחשבון ריבית דריבית", use_container_width=True):
        st.switch_page("pages/2_compound_interest.py")

with col2:
    st.markdown("### ⚙️ הנדסה וכלים")
    # כאן תוכל להוסיף כפתורים לכלים הבאים שנבנה
    st.info("כאן יתווספו הכלים ההנדסיים שלך בקרוב...")
    
    # דוגמה לכפתור עתידי (מושבת כרגע)
    st.button("🔢 ממיר בסיסים (בקרוב)", disabled=True, use_container_width=True)

# תוספת עיצובית למטה
st.write("---")
st.caption("פותח ככלי עזר אישי לניהול פרויקטים ופיננסים.")
