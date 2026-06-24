import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os

st.set_page_config(
    page_title="CA Sunil Kumar Paswan | Quant Hub",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Premium Color Palette and Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Gradient Headers */
    .gradient-text {
        background: linear-gradient(90deg, #10B981 0%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0px;
    }
    
    /* Sub-headers */
    .sub-text {
        color: #9CA3AF;
        font-size: 18px;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    
    /* Premium Cards */
    .premium-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .premium-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
        border-color: #3B82F6;
    }
    
    /* Sidebar styling */
    .sidebar-text {
        font-size: 14px;
        color: #CBD5E1;
    }
    
    /* Custom Dividers */
    hr {
        border-color: #334155;
        margin-top: 30px;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

def load_file(filename):
    """Safely loads a file from the current directory for download buttons."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return f.read()
    return None

def create_download_button(label, filename, mime_type=None):
    """Generates a styled download button or a warning if file is missing."""
    file_data = load_file(filename)
    if file_data:
        st.download_button(
            label=f"📥 {label}",
            data=file_data,
            file_name=filename,
            mime=mime_type,
            use_container_width=True
        )
    else:
        st.error(f"⚠️ '{filename}' not found. Upload it to GitHub.")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2103/2103106.png", width=80) # Placeholder generic icon
st.sidebar.markdown("### 🏛️ CA Sunil Kr Paswan")
st.sidebar.markdown("<p class='sidebar-text'>Quantitative Systems Architect<br>Jamadoba, Jharkhand, India<br>✉️ sunilbla.acc@gmail.com</p>", unsafe_allow_html=True)

st.sidebar.divider()

st.sidebar.markdown("### 🛠️ System Navigation")
active_module = st.sidebar.radio(
    "",
    [
        "👤 Executive Portfolio", 
        "🎯 Equities & Index (Sniper V5)", 
        "🏛️ Crypto & Forex Engines", 
        "🛒 Commercial Storefront"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.success("🟢 **Live Status:** Systems Operational")

if active_module == "👤 Executive Portfolio":
    st.markdown('<p class="gradient-text">Executive Portfolio</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Bridging Institutional Chartered Accountancy with Algorithmic Execution Systems.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="premium-card">
            <h3 style='margin-top:0;'>🎓 Professional Background</h3>
            <p><strong>Chartered Accountant (ICAI)</strong> - Qualified Aug 2019</p>
            <ul>
                <li><strong>Corporate Tenure:</strong> Assistant Manager Finance at Bharat Coking Coal Limited (BCCL/Coal India) & Junior Exec at WBSEDCL.</li>
                <li><strong>Expertise:</strong> SAP ERP Accounts Finalization, Statutory Audits, and Mega Project Finance oversight (>10 MT capacity).</li>
            </ul>
            <hr style='margin:10px 0;'>
            <h3 style='margin-top:0;'>⚙️ Quantitative Engineering</h3>
            <ul>
                <li><strong>Training:</strong> Python & Algorithmic Architecture from ISM Dhanbad.</li>
                <li><strong>Stack:</strong> Pandas, Numpy, Plotly, Dhan V2.0 API, Bybit WebSockets, MT5.</li>
                <li><strong>Edge:</strong> Designing mechanical trailing stop-loss (TSL) handlers and delta-proxy modeling to eliminate psychological friction.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("### 📄 Official Credentials")
        st.info("Download my verified CV detailing my financial and quantitative engineering milestones.")
        create_download_button("Download Official Resume", "Sunil_KRPaswan_Resume  FINAL.pdf", "application/pdf")
        
        st.markdown("### 📺 Introductory Video")
        # Replace this link with your actual YouTube introduction video
        st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")

elif active_module == "🎯 Equities & Index (Sniper V5)":
    st.markdown('<p class="gradient-text">Sniper V5 & Index Architectures</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Mechanical Breakout Velocity & Delta-Proxy Option Engines.</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Performance Dashboard", "📂 Equities Research", "📂 Index Options Research"])
    
    with tab1:
        st.markdown("### ⚙️ System Threshold Audit")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="ADX Trend Filter Strength", value="> 25.0", delta="Noise Filter Active")
        with col2:
            st.metric(label="Relative Volume (RVOL)", value="> 2.0x", delta="Institutional Volume Active")
        with col3:
            st.metric(label="Volatility Expansion (ATR)", value="> 1.5x", delta="Squeeze Breakout Active")

        st.markdown("<br>", unsafe_allow_html=True)
        
        performance_data = pd.DataFrame([
            {"Ticker": "ADANIENSOL", "Trades": 1, "Net PnL (₹)": 16257.21, "Status": "Core Alpha"},
            {"Ticker": "VEDL", "Trades": 1, "Net PnL (₹)": 10299.11, "Status": "Core Alpha"},
            {"Ticker": "ADANIENT", "Trades": 3, "Net PnL (₹)": 8234.77, "Status": "Core Alpha"},
            {"Ticker": "LODHA", "Trades": 1, "Net PnL (₹)": 2968.93, "Status": "Approved Suite"},
            {"Ticker": "CGPOWER", "Trades": 2, "Net PnL (₹)": 2082.61, "Status": "Approved Suite"}
        ])
        
        fig = px.bar(
            performance_data.sort_values(by="Net PnL (₹)", ascending=False),
            x="Ticker", y="Net PnL (₹)", color="Status",
            color_discrete_map={"Core Alpha": "#10B981", "Approved Suite": "#3B82F6"},
            title="Realized PnL Tracker - Top 5 Performers"
        )
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("### 📈 Sniper V5 Equities Documentation")
        st.write("Access the core mathematical theories and scripts driving the equity breakout models.")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="premium-card"><h4>📄 Comprehensive Report</h4><p>Deep analytics on edge discovery.</p></div>', unsafe_allow_html=True)
            create_download_button("Download Comprehensive Report", "CA_Sunil_Kumar_Comprehensive_Report.pdf", "application/pdf")
        with c2:
            st.markdown('<div class="premium-card"><h4>🔒 System Architecture</h4><p>Redacted blueprint of the Sniper V5.</p></div>', unsafe_allow_html=True)
            create_download_button("Download Architecture", "Sniper_V5_System_Architecture_CA_Sunil_Paswan_Redacted.pdf", "application/pdf")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="premium-card"><h4>💻 Final Stock Option Engine</h4><p>Jupyter Notebook containing raw backtest data for equities.</p></div>', unsafe_allow_html=True)
        create_download_button("Download Final Stock Option Code", "FINAL STOCK OPTION .ipynb")

    with tab3:
        st.markdown("### 📉 Nifty & BankNifty Architectures")
        st.write("Advanced algorithmic signals generated specifically for high-liquidity Indian Indices.")
        i1, i2, i3 = st.columns(3)
        with i1:
            st.markdown('<div class="premium-card"><h4>📊 Option Scanner</h4><p>Momentum & Volatility Scanner.</p></div>', unsafe_allow_html=True)
            create_download_button("Download Scanner", "OPTION BUYING NEW SCANNER .ipynb")
        with i2:
            st.markdown('<div class="premium-card"><h4>⚙️ Index Engine 1</h4><p>Core Index Option Framework.</p></div>', unsafe_allow_html=True)
            create_download_button("Download Index Core", "FINAL INDEX OPTION .ipynb")
        with i3:
            st.markdown('<div class="premium-card"><h4>⚙️ Index Engine 2</h4><p>Advanced Confluence Router.</p></div>', unsafe_allow_html=True)
            create_download_button("Download Index Advanced", "FINAL INDEX OPTION  (1).ipynb")

elif active_module == "🏛️ Crypto & Forex Engines":
    st.markdown('<p class="gradient-text">Titan Arbitrage & Global Macros</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">MT5 Gold Algorithms, Ripple Momentum, and Statistical Cointegration.</p>', unsafe_allow_html=True)
    
    col_vid, col_stats = st.columns([1, 1])
    with col_vid:
        st.markdown("### 📺 Engine Backtest Proof")
        # Replace this link with your actual screen recording of MT5/Bybit
        st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")
    
    with col_stats:
        st.markdown("""
        <div class="premium-card">
            <h4 style="color:#F59E0B;">🏆 GOLD (XAUUSD) Miner Pro</h4>
            <p><strong>Platform:</strong> MetaTrader 5 (MT5)</p>
            <p><strong>Logic:</strong> Hourly trend flip mechanics with dynamic ATR stops and daily loss guardrails.</p>
        </div>
        <div class="premium-card">
            <h4 style="color:#3B82F6;">🔗 TITAN Pairs Arbitrage</h4>
            <p><strong>Platform:</strong> Bybit WebSockets</p>
            <p><strong>Logic:</strong> Z-Score mean reversion on highly cointegrated crypto pairs (SOL/LINK).</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### 📥 Download Global Market Scripts")
    d1, d2, d3 = st.columns(3)
    
    with d1:
        create_download_button("Gold MT5 Architecture", "GOLD XAUSD.ipynb")
    with d2:
        create_download_button("Z-Score Pairs Engine", "Z SCORE SOL LINK .ipynb")
    with d3:
        create_download_button("XRP Institutional Engine", "XRP ADVXUSD.ipynb")

elif active_module == "🛒 Commercial Storefront":
    st.markdown('<p class="gradient-text">Production Source Code Store</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Acquire the proprietary execution frameworks securely via Gumroad.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="premium-card" style="text-align:center;">
            <h2>🎯 Sniper V5 Option Core</h2>
            <h1 style="color:#10B981;">₹4,999</h1>
            <p style="text-align:left;">
                ✔️ Complete Python (.py) Source Script<br>
                ✔️ Dhan V2.0 API WebSocket Integrations<br>
                ✔️ Mechanical Trailing Stop Loss (TSL)<br>
                ✔️ Telegram Telemetry & Alert Routers
            </p>
            <a href="https://gumroad.com/" target="_blank" style="text-decoration:none;">
                <button style="width:100%; background:#3B82F6; color:white; border:none; padding:15px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:16px;">
                    🛒 Purchase Securely
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="premium-card" style="text-align:center;">
            <h2>🏛️ Titan Mean Reversion</h2>
            <h1 style="color:#10B981;">₹8,499</h1>
            <p style="text-align:left;">
                ✔️ Complete Bybit API Source Script<br>
                ✔️ Real-Time Orderbook WebSockets<br>
                ✔️ Dynamic Z-Score & Lookback Formulas<br>
                ✔️ Circuit Breaker Safety Constraints
            </p>
            <a href="https://gumroad.com/" target="_blank" style="text-decoration:none;">
                <button style="width:100%; background:#3B82F6; color:white; border:none; padding:15px; border-radius:8px; font-weight:bold; cursor:pointer; font-size:16px;">
                    🛒 Purchase Securely
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><p style='text-align:center; color:#64748B;'>*All transactions are securely processed via Stripe/Gumroad. Code files are delivered instantly via email post-purchase.*</p>", unsafe_allow_html=True)
