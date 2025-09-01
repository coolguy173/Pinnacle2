import streamlit as st
import pandas as pd

# --- App Config ---
st.set_page_config(
    page_title="Pinnacle - Smarter Investments",
    page_icon="📈",
    layout="wide"
)

# --- Header ---
st.title("📈 Pinnacle")
st.subheader("Smarter Investments, Made Simple")

# --- Navigation ---
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "🔎 Research", "💰 Mutual Funds", "📊 Strategies", "ℹ️ About"]
)

# --- Home Page ---
if page == "🏠 Home":
    st.header("🏠 Welcome to Pinnacle")
    st.write("""
    **Pinnacle** helps you explore **mutual funds, strategies, and insights** 
    so you can grow your money smarter.  

    👉 Use the **sidebar** to start exploring.
    """)

    st.markdown("### Why Choose Pinnacle?")
    st.success("✔ Beginner-friendly explanations")
    st.success("✔ Salary-based recommendations (coming soon!)")
    st.success("✔ Clear breakdown of risk vs reward")

# --- Research Page ---
elif page == "🔎 Research":
    st.header("🔎 Research Mutual Funds")

    # Demo dataset
    data = {
        "Fund Name": [
            "Axis Bluechip Fund",
            "HDFC Hybrid Equity Fund",
            "SBI Small Cap Fund",
            "ICICI Prudential Balanced Advantage",
            "Kotak Emerging Equity Fund"
        ],
        "Category": [
            "Large Cap Equity",
            "Hybrid Equity + Debt",
            "Small Cap Equity",
            "Dynamic Asset Allocation",
            "Mid Cap Equity"
        ],
        "Risk": ["Moderate", "Moderately High", "High", "Moderate", "High"],
        "3Y Returns": ["12.5%", "10.2%", "18.7%", "9.8%", "16.3%"],
        "Rating (★)": [5, 4, 4, 3, 4]
    }

    df = pd.DataFrame(data)

    # Show table
    st.dataframe(df, use_container_width=True)

    # Select fund for details
    fund = st.selectbox("Pick a fund to learn more:", df["Fund Name"])

    fund_details = df[df["Fund Name"] == fund].iloc[0]
    st.subheader(f"📊 {fund}")
    st.write(f"**Category:** {fund_details['Category']}")
    st.write(f"**Risk Level:** {fund_details['Risk']}")
    st.write(f"**3Y Returns:** {fund_details['3Y Returns']}")
    st.write(f"**Rating:** {'⭐' * fund_details['Rating (★)']}")

    st.info("⚠ Past returns do not guarantee future results.")

# --- Mutual Funds (Basic View) ---
elif page == "💰 Mutual Funds":
    st.header("💰 Mutual Funds (Quick View)")
    st.write("Explore some popular funds:")

    funds = {
        "Axis Bluechip Fund": "Large cap equity, long-term growth.",
        "HDFC Hybrid Equity Fund": "Mix of equity + debt, balanced returns.",
        "SBI Small Cap Fund": "High-risk, high-reward small cap equity.",
        "ICICI Balanced Advantage": "Shifts between debt & equity dynamically.",
    }

    for name, desc in funds.items():
        with st.expander(name):
            st.write(desc)

# --- Strategies Page ---
elif page == "📊 Strategies":
    st.header("📊 Investment Strategies")
    st.write("""
    Coming soon: **personalized recommendations** based on  
    - your **salary percentage** you want to invest  
    - your **risk appetite**  
    - your **time horizon**  
    """)
    st.warning("🚧 Feature in progress...")

# --- About Page ---
elif page == "ℹ️ About":
    st.header("ℹ️ About Pinnacle")
    st.write("""
    **Pinnacle** is built to make investment knowledge **accessible** to everyone.  

    - Beginner-friendly explanations  
    - Mutual fund insights  
    - Future scope: salary-based recommendations  
    """)
    st.caption("🚀 Built with simplicity and growth in mind.")

