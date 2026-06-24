import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# --- PAGE ARCHITECTURE ---
st.set_page_config(
    page_title="CA Sunil Kumar Paswan | Quant Hub",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App Custom Styling - Institutional Dark/Clean Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .gradient-text {
        background: linear-gradient(90deg, #10B981 0%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 0px;
    }
    
    .sub-text {
        color: #9CA3AF;
        font-size: 16px;
        margin-top: -5px;
        margin-bottom: 25px;
    }
    
    .premium-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .terminal-box {
        background-color: #0F172A;
        border-left: 4px solid #F59E0B;
        padding: 15px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
        color: #E2E8F0;
        margin-bottom: 20px;
        font-size: 14px;
    }
    
    .highlight-green { color: #10B981; font-weight: bold; }
    .highlight-blue { color: #3B82F6; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR EXECUTIVE PROFILE ---
st.sidebar.markdown("### 🏛️ Architecture Console")
st.sidebar.markdown("**CA Sunil Kr Paswan**\n*Quantitative Systems Architect*")
st.sidebar.write("📍 *Jamadoba, Jharkhand, India*")
st.sidebar.write("✉️ *sunilbla.acc@gmail.com*")
st.sidebar.divider()

st.sidebar.markdown("### 🔬 Research Exhibits")
active_module = st.sidebar.radio(
    "Select System Report:",
    [
        "👤 Executive Portfolio", 
        "📈 NIFTY 50 Temporal Alpha", 
        "⚡ High-Beta Volatility Arbitrage",
        "🎯 5-Asset Alpha Suite"
    ]
)

st.sidebar.divider()
st.sidebar.warning("🔒 **IP Protection:** Algorithmic logic and execution thresholds are strictly classified.")

# ==========================================
# PANEL 1: EXECUTIVE PORTFOLIO
# ==========================================
if active_module == "👤 Executive Portfolio":
    st.markdown('<p class="gradient-text">Institutional Profile</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Bridging Chartered Accountancy frameworks with algorithmic execution systems.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="premium-card">
            <h3 style='margin-top:0; color: #F8FAFC;'>🎓 Professional Background</h3>
            <p style='color: #CBD5E1;'><strong>Chartered Accountant (ICAI)</strong> - Qualified Aug 2019</p>
            <ul style='color: #CBD5E1;'>
                <li><strong>Corporate Tenure:</strong> Assistant Manager Finance at Bharat Coking Coal Limited (BCCL/Coal India) & Junior Exec at WBSEDCL.</li>
                <li><strong>Audit & Compliance:</strong> Expertise in SAP ERP Accounts Finalization, Statutory Audits, and financial oversight for mega projects exceeding 10 MT capacity.</li>
            </ul>
            <hr style='border-color: #334155;'>
            <h3 style='margin-top:0; color: #F8FAFC;'>⚙️ Quantitative Engineering</h3>
            <ul style='color: #CBD5E1;'>
                <li><strong>Training:</strong> Python & Algorithmic Architecture from ISM Dhanbad.</li>
                <li><strong>Systemic Edge:</strong> Designing mechanical trailing stop-loss (TSL) handlers and delta-proxy modeling to completely eliminate psychological trading friction and discretionary errors.</li>
                <li><strong>Data Science:</strong> Specializing in Monte Carlo simulations, temporal inefficiency tracking, and volume-weighted momentum algorithms.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("### 📄 Official Credentials")
        st.info("Verified CV detailing financial timeline and engineering milestones available upon request to institutional partners.")
        st.link_button("✉️ Request Official Resume", "mailto:sunilbla.acc@gmail.com", use_container_width=True)
        
        st.markdown("### 🔬 Core Philosophy")
        st.markdown("""
        <div class="terminal-box">
            > "Abdicate the role of the Trader.<br>
            > Assume the role of the Systems Architect."<br><br>
            <i>Extract from Proprietary Risk Management Protocol.</i>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# PANEL 2: NIFTY 50 TEMPORAL ALPHA
# ==========================================
elif active_module == "📈 NIFTY 50 Temporal Alpha":
    st.markdown('<p class="gradient-text">NIFTY 50 Intraday Momentum Engine</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Deep data-science extraction of early-session momentum anomalies and opening-gap imbalances.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Data Sample Size", "191,380 Candles", "2 Years of 1-Min Data")
    col2.metric("Options Contracts Analyzed", "380,996", "Deep Liquidity Focus")
    col3.metric("System Profit Factor", "1.89", "Highly Asymmetric")

    st.divider()

    st.markdown("### 🧠 Executive Overview")
    st.write("This quantitative model was engineered to capture opening structural inefficiencies within the NIFTY 50 index. Rather than relying on discretionary forecasting, the system utilizes a high-frequency Python data parser to evaluate opening volatility, filtering for specific volume multipliers and price-action confirmation.")
    
    st.markdown("### ⚙️ Institutional Edge (Black Box Metrics)")
    st.markdown("""
    <div class="premium-card">
        <h4 style="color:#3B82F6;">1. Temporal Optimization (Time-Based Edge)</h4>
        <p style="color:#CBD5E1;">Data mining revealed massive structural inefficiencies during the first 90 minutes of the trading session. The algorithm mathematically restricts trade initiation exclusively to this power-hour window, bypassing midday institutional chop.</p>
        <h4 style="color:#10B981;">2. Volatility Band Reversion</h4>
        <p style="color:#CBD5E1;">By isolating specific volatility percentiles and standard deviation compressions, the options-buying sub-system achieved an <b>88.97% historical accuracy rate</b> on targeted proprietary setups.</p>
        <h4 style="color:#F59E0B;">3. Monte Carlo Risk Architecture</h4>
        <p style="color:#CBD5E1;">Subjected to 1,000 Monte Carlo simulation sequences, the system's risk architecture utilizes absolute mechanical execution. It mandates strictly calculated Good-Till-Cancel (GTC) trailing stops, ensuring maximum daily drawdown limits are mathematically impossible to breach.</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PANEL 3: HIGH-BETA VOLATILITY ARBITRAGE
# ==========================================
elif active_module == "⚡ High-Beta Volatility Arbitrage":
    st.markdown('<p class="gradient-text">Volatility Squeeze Arbitrage Engine</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Non-directional options buying strategy capitalizing on extreme volatility compression in high-beta energy assets.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Backtest Horizon", "5 Years", "605 Executions")
    col2.metric("Cumulative Return", "+104.94%", "Post-Slippage")
    col3.metric("System Sharpe Ratio", "0.43", "Institutional Grade")

    st.divider()

    st.markdown("### 🧠 Executive Overview")
    st.write("This proprietary engine operates on a highly positive-skew profile. Utilizing an At-The-Money (ATM) options straddle methodology, it identifies severe Bollinger/ATR compressions prior to explosive directional action. While the base win rate is mathematically conservative, the magnitude of winning executions drastically outpaces mitigated losses.")

    row1, row2 = st.columns([2, 1.5])
    
    with row1:
        st.markdown("### 📊 Temporal Execution Edge")
        st.write("The system maximizes capital efficiency by heavily weighting late-session entries (Buy-To-Sell-Tomorrow), capturing overnight macroeconomic expansion while minimizing intraday theta decay.")
        
        # Plotting the PnL Distribution based on the actual report data
        pnl_data = pd.DataFrame({
            "Execution Window": ["BTST (Overnight)", "Morning Intraday", "Event-Driven (News)"],
            "Net PnL Generated (k)": [76.9, 28.1, 0.0]
        })
        fig = px.bar(
            pnl_data, x="Execution Window", y="Net PnL Generated (k)", 
            color="Execution Window",
            color_discrete_sequence=["#10B981", "#3B82F6", "#EF4444"],
            title="Net Profit Distribution by Algorithmic Execution Window"
        )
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#CBD5E1"))
        st.plotly_chart(fig, use_container_width=True)

    with row2:
        st.markdown("### 🛡️ Core Constraints")
        st.markdown("""
        <div class="premium-card">
            <ul style="color:#CBD5E1;">
                <li><b>Capital Allocation:</b> Algorithmically capped at 1% to 2% of total portfolio equity to survive extended loss sequences.</li>
                <li><b>Drawdown Breakers:</b> Incorporates a strict circuit breaker that pauses execution if volatility regimes shift unfavorably.</li>
                <li><b>Mechanical Decay Defense:</b> Forces liquidation at the subsequent open to neutralize overnight theta bleed.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# PANEL 4: 5-ASSET ALPHA SUITE
# ==========================================
elif active_module == "🎯 5-Asset Alpha Suite":
    st.markdown('<p class="gradient-text">The 5-Asset Institutional Portfolio</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">A multi-strategy architecture utilizing directional and delta-neutral systems across highly liquid equities.</p>', unsafe_allow_html=True)

    st.divider()
    
    st.markdown("### 🧠 Executive Overview")
    st.write("Subjected to a rigorous 10+ year historical simulation involving 387 trades per strategy, this portfolio extracts highly asymmetric returns. By classifying market regimes into distinct volatility environments, the engine seamlessly transitions between directional options buying and non-directional straddles.")

    st.markdown("### 📊 Backtested Edge & Sharpe Ratios")
    
    # Portfolio Data from the "Comprehensive Option Trading Report"
    portfolio_data = pd.DataFrame({
        "Asset": ["BHARTIARTL", "BRITANNIA", "BOSCHLTD", "BEL", "BANKBARODA"],
        "Strategy Phase": ["Directional", "Directional", "Non-Directional", "Directional", "Non-Directional"],
        "Win Rate (%)": [95.35, 94.06, 92.51, 94.83, 86.30],
        "Sharpe Ratio": [16.75, 16.21, 13.91, 12.65, 11.30]
    })
    
    fig2 = px.scatter(
        portfolio_data, x="Win Rate (%)", y="Sharpe Ratio", 
        color="Strategy Phase", size="Sharpe Ratio", text="Asset",
        title="Portfolio Analytics: Win Rate vs. Risk-Adjusted Returns",
        color_discrete_sequence=["#3B82F6", "#F59E0B"]
    )
    fig2.update_traces(textposition='top center')
    fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#CBD5E1"), xaxis=dict(range=[80, 100]))
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### 🛡️ Risk Management Hierarchy")
    st.markdown("""
    <div class="premium-card">
        <p style="color:#CBD5E1;">Success in this architecture is solely reliant on executing the <b>Risk Management Pyramid:</b></p>
        <ol style="color:#CBD5E1;">
            <li><b>Position Sizing:</b> Absolute ceiling of 2% capital risk per trade.</li>
            <li><b>Profit Target Trailing:</b> Mechanical lock-in of profits by adjusting trailing stops to break-even after +15% momentum gain.</li>
            <li><b>Time-Based Exits:</b> Mandatory liquidation prior to extreme late-session settlement volatility.</li>
        </ol>
        <p style="color:#9CA3AF; font-size:12px; margin-top:15px;">*Note: The exact technical triggers, support/resistance formulas, and volume multipliers governing entry are heavily classified and retained internally.*</p>
    </div>
    """, unsafe_allow_html=True)
