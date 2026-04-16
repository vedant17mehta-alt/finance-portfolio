import streamlit as st

# Page configuration
st.set_page_config(page_title="Vedant Mehta | Portfolio", page_icon="📈", layout="wide")

# Sidebar - Contact Info
st.sidebar.title("Contact Information")
st.sidebar.write("📍 Toronto, Ontario, Canada")
st.sidebar.write("📧 [vedant17mehta@gmail.com](mailto:vedant17mehta@gmail.com)")
st.sidebar.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/vedant-mehta-023041173/)")
st.sidebar.write("✍️ [Personal Blog](https://vedantonmoney.wordpress.com/)")

# --- Header Section ---
st.title("Vedant Mehta")
st.subheader("CFA Level 1 Candidate | Financial Analyst")
st.write("""
Investment Fund in Canada certificate holder with in-depth knowledge of financial analysis 
and investment management. I specialize in utilizing data-driven models to forecast 
market trends and optimize portfolio performance.
""")

st.markdown("---")

# --- Navigation Tabs ---
tab1, tab2, tab3 = st.tabs(["🚀 Experience & Projects", "🧠 Market Insights", "🛠 Skills"])

with tab1:
    st.header("Professional Highlights")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Quantitative Research Simulation")
        st.caption("JPMorgan Chase & Co. (via Forage)")
        st.write("""
        - Analyzed price data and valued commodity storage contracts.
        - Performed credit risk analysis using FICO scores.
        - Developed a deeper understanding of quant roles in major investment banks.
        """)

    with col2:
        st.subheader("Academic & Leadership")
        st.write("**Humber College / Enactus Humber Polytechnic**")
        st.write("- Active member of the Humber Finance Society.")
        st.write("- Focused on Portfolio Optimization and DCF Modeling.")

with tab2:
    st.header("Thought Leadership & Analysis")
    st.info("I regularly analyze how geopolitics and policy shift global markets.")
    
    with st.expander("Oil & Commodity Shifts (U.S.-Cuba Case Study)"):
        st.write("""
        Analyzed how U.S. oil embargos on Cuba created a ripple effect in global 
        Nickel and Cobalt supply chains, impacting the EV battery market.
        """)
        
    with st.expander("Bank of Canada: Interest Rate Outlook"):
        st.write("""
        A deep dive into the 'fragile middle ground' of the Canadian economy, 
        evaluating the trade-offs between holding, cutting, or hiking rates in 2026.
        """)

with tab3:
    st.header("Technical & Financial Toolkit")
    
    c1, c2, c3 = st.columns(3)
    c1.markdown("**Modeling**\n- DCF & Gordon Growth\n- Portfolio Returns\n- Standard Deviation & Correlation")
    c2.markdown("**Tools**\n- Bloomberg Terminal\n- Python (Data Analysis)\n- Excel Financial Modeling")
    c3.markdown("**Knowledge**\n- Investment Funds in Canada\n- Macroeconomic Forecasting\n- Credit Risk Analysis")

# Footer
st.markdown("---")
st.center = st.write("Built with ❤️ using Python & Streamlit")
streamlit run portfolio.py
