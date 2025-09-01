import streamlit as st

st.set_page_config(page_title="SmartInvest", page_icon="💸", layout="centered")

# --- Session state for page navigation ---
if "page" not in st.session_state:
    st.session_state.page = "start"

def go_to(page):
    st.session_state.page = page

# --- START PAGE ---
if st.session_state.page == "start":
    st.title("💸 Welcome to SmartInvest")
    st.subheader("Your Personal Investment Recommender")

    st.write("""
    🚀 This app helps you decide where to invest based on your salary 
    and risk preference.  
    ✅ Simple, beginner-friendly, and educational.  
    ⚠️ Not financial advice.
    """)

    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)

    st.button("👉 Get Started", on_click=lambda: go_to("main"))

# --- MAIN PAGE ---
elif st.session_state.page == "main":
    st.title("💸 SmartInvest – Personal Investment Recommender")

    salary = st.number_input("Enter your monthly salary (₹)", min_value=1000, step=1000)

    percent_invest = st.slider("What % of your salary do you want to invest?", 1, 50, 20)

    investment_info = {
        "Mutual Funds / ETFs": {
            "desc": "✅ Professionally managed, diversified, medium risk. Good for beginners.",
            "link": "https://www.groww.in/mutual-funds"
        },
        "Bonds / FD": {
            "desc": "✅ Safe & stable, low returns but secure. Protects capital.",
            "link": "https://www.rbi.org.in/Scripts/BS_ViewBonds.aspx"
        },
        "Gold": {
            "desc": "✅ Hedge against inflation, stable over long term. Can invest via ETFs or Gold Bonds.",
            "link": "https://www.nseindia.com/products-services/etf-gold"
        },
        "Stocks": {
            "desc": "⚠️ High risk, high return. Needs research & patience.",
            "link": "https://www.moneycontrol.com/stocksmarketsindia/"
        },
        "Crypto": {
            "desc": "⚠️ Very high risk, very volatile. Only invest small % if you understand it.",
            "link": "https://www.coinmarketcap.com/"
        },
        "Recurring Deposit (RD)": {
            "desc": "✅ Bank product, fixed savings each month, very safe but low returns.",
            "link": "https://www.sbi.co.in/web/personal-banking/investments-deposits/rd"
        }
    }

    if salary > 0:
        invest_amount = (salary * percent_invest) / 100
        st.subheader(f"You can invest: ₹{invest_amount:,.2f} per month")

        if invest_amount < 5000:
            suggestion = ["Recurring Deposit (RD)", "Mutual Funds / ETFs"]
            st.info("💡 Suggestion: Start small & safe → RD or Mutual Funds / ETFs.")
        elif 5000 <= invest_amount < 20000:
            suggestion = ["Mutual Funds / ETFs", "Bonds / FD", "Gold"]
            st.info("💡 Suggestion: Mix it up → 60% Mutual Funds, 30% Bonds/FD, 10% Gold.")
        else:
            suggestion = ["Mutual Funds / ETFs", "Bonds / FD", "Gold", "Stocks", "Crypto"]
            st.info("💡 Suggestion: Higher salary = higher flexibility → diversified portfolio.")

        st.subheader("📊 Explore Your Options")
        choice = st.selectbox("Select an investment to learn more:", suggestion)

        if choice:
            st.write(investment_info[choice]["desc"])
            st.markdown(f"[🌐 Learn More Here]({investment_info[choice]['link']})")

        st.caption("⚠️ Disclaimer: This is not financial advice. Do your own research before investing.")

    st.button("⬅️ Back to Home", on_click=lambda: go_to("start"))
