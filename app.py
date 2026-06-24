import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os

# --- PAGE ARCHITECTURE ---
st.set_page_config(
    page_title="CA Sunil Kumar Paswan | Quant Hub",
    page_icon="⚡",
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
        border-left: 4px solid #3B82F6;
        padding: 15px;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
        color: #E2E8F0;
        margin-bottom: 20px;
        font-size: 14px;
    }
    
    .highlight-green { color: #10B981; font-weight: bold; }
    .highlight-blue { color: #3B82F6; font-weight: bold; }
    .highlight-orange { color: #F59E0B; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Helper function to safely load files
def load_file(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return f.read()
    return None

def create_download_button(label, filename, mime_type=None):
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
        st.error(f"⚠️ '{filename}' not found on server.")

# --- SIDEBAR EXECUTIVE PROFILE ---
st.sidebar.markdown("### 🏛️ System Architecture")
st.sidebar.markdown("**CA Sunil Kr Paswan**\n*Quantitative Systems Architect*")
st.sidebar.markdown("<span style='font-size: 13px; color: #9CA3AF;'>Jamadoba, Jharkhand, India<br>sunilbla.acc@gmail.com</span>", unsafe_allow_html=True)
st.sidebar.divider()

# Navigation
st.sidebar.markdown("### 🛠️ Research Modules")
active_module = st.sidebar.radio(
    "",
    [
        "👤 Executive Portfolio", 
        "🎯 Equities & Index (Sniper Engine)", 
        "🏛️ Stat-Arb & Global Macros (Titan)"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()
st.sidebar.success("🟢 **Live Status:** Backtest Engines Active")

# ==========================================
# PANEL 1: EXECUTIVE PORTFOLIO
# ==========================================
if active_module == "👤 Executive Portfolio":
    st.markdown('<p class="gradient-text">Institutional Profile</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Bridging Chartered Accountancy frameworks with high-frequency algorithmic execution.</p>', unsafe_allow_html=True)
    
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
                <li><strong>Tech Stack:</strong> Pandas, Numpy, Plotly, Dhan V2.0 API, Bybit WebSockets, MT5 Integration.</li>
                <li><strong>Systemic Edge:</strong> Engineering absolute mechanical rulesets (Time-lockouts, Delta-Proxy valuation, autonomous trailing stops) to completely eliminate psychological trading friction and discretionary errors.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("### 📄 Official Credentials")
        st.info("Download my verified CV detailing my financial timeline and engineering milestones.")
        create_download_button("Download Official Resume", "Sunil_KRPaswan_Resume  FINAL.pdf", "application/pdf")
        
        st.markdown("### 🔬 Core Philosophy")
        st.markdown("""
        <div class="terminal-box">
            > "Abdicate the role of the Trader.<br>
            > Assume the role of the Systems Architect."<br><br>
            <i>Extract from Proprietary Strategy Documentation.</i>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# PANEL 2: SNIPER ENGINE (EQUITIES & INDEX)
# ==========================================
elif active_module == "🎯 Equities & Index (Sniper Engine)":
    st.markdown('<p class="gradient-text">Qualified Sniper: Breakout Velocity</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Mechanical Breakout Architecture utilizing Delta-Proxy Option execution and strict temporal constraints.</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["⚙️ System Logic & Constraints", "📊 Equity Alpha Profile", "📉 Index Confluence Router"])
    
    with tab1:
        st.markdown("### 🧠 The Mathematical Edge")
        st.write("The Sniper architecture operates by isolating moments of intense institutional volume and volatility expansion, mathematically removing market noise.")
        
        col1, col2, col3 = st.columns(3)
        st.markdown("""
        <div style="display:flex; justify-content:space-between; gap: 15px; margin-bottom: 20px;">
            <div class="metric-box" style="flex:1;">
                <h4 style="margin:0; color:#3B82F6;">ADX Trend Filter</h4>
                <h2 style="margin:5px 0;">> 25.0</h2>
                <span style="font-size:12px; color:#64748B;">Requires established directional momentum.</span>
            </div>
            <div class="metric-box" style="flex:1;">
                <h4 style="margin:0; color:#10B981;">Relative Volume (RVOL)</h4>
                <h2 style="margin:5px 0;">> 2.0x</h2>
                <span style="font-size:12px; color:#64748B;">2x the 20-period moving average volume.</span>
            </div>
            <div class="metric-box" style="flex:1;">
                <h4 style="margin:0; color:#F59E0B;">Volatility Expansion</h4>
                <h2 style="margin:5px 0;">> 1.5x</h2>
                <span style="font-size:12px; color:#64748B;">True Range vs ATR (Squeeze Breakout).</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🛑 Immutable System Constraints")
        st.markdown("""
        <div class="terminal-box">
        <span class="highlight-orange">[RULE 1] Temporal Lockout (The 12:30 PM Rule):</span> Morning breakouts frequently display high-frequency stop-hunting behavior. The system ignores data prior to 12:30 PM IST, syncing execution with European open volatility.<br><br>
        <span class="highlight-orange">[RULE 2] Ammunition Limits:</span> Engine forcibly powers down after 2 triggered signals per day to prevent overtrading.<br><br>
        <span class="highlight-orange">[RULE 3] Autonomous Exits:</span><br>
        &nbsp;&nbsp;1. <b>Hard SL:</b> Spot crosses breakout candle boundary.<br>
        &nbsp;&nbsp;2. <b>Dynamic TSL:</b> Spot pulls back 0.5% from the peak high/low.<br>
        &nbsp;&nbsp;3. <b>Theta Limit:</b> Position held > 65 minutes with no momentum triggers automatic market exit.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📄 Read The Research")
        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            create_download_button("Download Comprehensive Report", "CA_Sunil_Kumar_Comprehensive_Report.pdf", "application/pdf")
        with col_dl2:
            create_download_button("Download Redacted Architecture", "Sniper_V5_System_Architecture_CA_Sunil_Paswan_Redacted.pdf", "application/pdf")

    with tab2:
        st.markdown("### 📈 Target Universe Optimization (1-Year Audit)")
        st.write("Not all volatile assets suit the architecture. The deep analytics engine profiled historical edge, filtering out 'Bleeders' and 'Theta Traps'.")
        
        performance_data = pd.DataFrame([
            {"Ticker": "ADANIENSOL", "Trades": 1, "Net PnL (₹)": 16257.21, "Status": "Core Alpha"},
            {"Ticker": "VEDL", "Trades": 1, "Net PnL (₹)": 10299.11, "Status": "Core Alpha"},
            {"Ticker": "ADANIENT", "Trades": 3, "Net PnL (₹)": 8234.77, "Status": "Core Alpha"},
            {"Ticker": "LODHA", "Trades": 1, "Net PnL (₹)": 2968.93, "Status": "Approved Suite"},
            {"Ticker": "CGPOWER", "Trades": 2, "Net PnL (₹)": 2082.61, "Status": "Approved Suite"},
        ])
        
        fig = px.bar(
            performance_data.sort_values(by="Net PnL (₹)", ascending=False),
            x="Ticker", y="Net PnL (₹)", color="Status",
            color_discrete_map={"Core Alpha": "#10B981", "Approved Suite": "#3B82F6"},
            title="Realized PnL Tracker - Top 5 Performers (Capital Model: ₹1,00,000)"
        )
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### 💻 Source Notebooks")
        st.write("Access the raw Pandas and DhanHQ API testing environments.")
        create_download_button("Download Final Stock Option Analysis", "FINAL STOCK OPTION .ipynb")

    with tab3:
        st.markdown("### 📉 Advanced Indian Index Signal Generator")
        st.write("The v21.2 Precision Sniper Engine is built specifically for NIFTY and BANKNIFTY, combining multiple sophisticated technical modules into a single, weighted confidence score.")
        
        st.markdown("""
        <div class="premium-card" style="margin-top: 20px;">
            <h4 style="color:#3B82F6;">🧠 The Confluence Matrix</h4>
            <p>The system evaluates the underlying spot price against an array of institutional indicators, penalizing conflicts and demanding a <b>>70% Confidence Score</b> to trigger.</p>
            <ul>
                <li><b>Supertrend (10x3):</b> Primary directional filter.</li>
                <li><b>Multi-Timeframe (MTF):</b> Requires alignment across 5m, 15m, and 1H windows.</li>
                <li><b>VWAP Sigma Bands:</b> Checks distance from Volume Weighted Average Price; penalizes extreme deviations.</li>
                <li><b>Cumulative Delta & Order Flow:</b> Tracks underlying buying/selling pressure imbalances.</li>
                <li><b>Options Data (PCR & IV Skew):</b> Factors in Put-Call Ratio and Implied Volatility skew based on VIX proxy.</li>
            </ul>
            <hr style="border-color: #334155;">
            <h4 style="color:#10B981;">🛡️ Delta & Target Execution</h4>
            <p>Once a signal is passed, the engine queries the live option chain to select strikes with a precise <b>Delta between 0.30 and 0.55</b>. Targets (T1/T2) and Trailing Stops are then calculated dynamically based on current ATR and session volatility multipliers.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 💻 Index Source Notebooks")
        col_i1, col_i2, col_i3 = st.columns(3)
        with col_i1:
            create_download_button("Option Buying Scanner", "OPTION BUYING NEW SCANNER .ipynb")
        with col_i2:
            create_download_button("Final Index Option Core", "FINAL INDEX OPTION .ipynb")
        with col_i3:
            create_download_button("Index Option (v1)", "FINAL INDEX OPTION  (1).ipynb")

# ==========================================
# PANEL 3: STAT-ARB & MACROS (TITAN)
# ==========================================
elif active_module == "🏛️ Stat-Arb & Global Macros (Titan)":
    st.markdown('<p class="gradient-text">Titan V6: Statistical Arbitrage</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Quantitative mean-reversion frameworks operating across highly cointegrated pairs (SOL/LINK) and Global Macro commodities (XAUUSD).</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="premium-card">
        <h3 style="color:#3B82F6;">🔗 Pairs Arbitrage Architecture (SOL / LINK)</h3>
        <p>Built for the Bybit Unified account structure, this engine trades the spread between two historically correlated assets.</p>
        <ul>
            <li><b>The Logic:</b> Calculates a rolling Z-Score of the ratio between Asset A and Asset B over a 168-hour window.</li>
            <li><b>Entry & Veto:</b> Triggers at a Z-Score deviation of ±2.5. An <b>ARIMA model</b> is deployed as a final veto check to predict if the spread is likely to continue diverging before entering.</li>
            <li><b>Iceberg Execution:</b> Uses "LimitMaker" orders to capture rebate fees, splitting large institutional positions into smaller chunks to bypass exchange notional limits.</li>
            <li><b>Dynamic Sizing:</b> Position sizing is volatility-weighted; the more volatile asset receives a proportionally smaller allocation to maintain true neutrality.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Visualization of Z-Score
    st.markdown("#### 📈 Theoretical Z-Score Spread Dynamics")
    np.random.seed(42)
    time_series = pd.date_range(start="00:00", periods=200, freq="5min")
    # Simulate a mean reverting walk
    z_scores = np.zeros(200)
    for i in range(1, 200):
        z_scores[i] = z_scores[i-1] * 0.95 + np.random.randn() * 0.2
    
    # Force a spike
    z_scores[50:60] += np.linspace(0, 3, 10)
    z_scores[60:80] -= np.linspace(0, 3, 20)
    
    z_df = pd.DataFrame({"Time": time_series, "Z-Score": z_scores})
    
    fig_z = go.Figure()
    fig_z.add_trace(go.Scatter(x=z_df["Time"], y=z_df["Z-Score"], name="Spread Z-Score", line=dict(color="#3B82F6", width=2)))
    fig_z.add_hline(y=2.5, line_dash="dash", line_color="#EF4444", annotation_text="Short Spread Entry (+2.5)")
    fig_z.add_hline(y=-2.5, line_dash="dash", line_color="#10B981", annotation_text="Long Spread Entry (-2.5)")
    fig_z.add_hline(y=0, line_color="#9CA3AF", annotation_text="Mean Equilibrium Target (0)")
    
    fig_z.update_layout(
        plot_bgcolor="rgba(0,0,0,0)", 
        paper_bgcolor="rgba(0,0,0,0)", 
        font=dict(color="#CBD5E1"),
        height=350,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig_z, use_container_width=True)
    
    st.markdown("""
    <div class="premium-card">
        <h3 style="color:#F59E0B;">🏆 GOLD (XAUUSD) Global Macro Architectures</h3>
        <p>Operating via MetaTrader 5 (MT5), these modules apply quantitative analysis to high-leverage prop-firm environments.</p>
        <ul>
            <li><b>The Asymmetric Sniper (v8):</b> Focuses on massive runner extraction. Uses an ADX chop-filter (>25) and enters on Z-Score extremes. Implements aggressive trailing stops to capture multi-day trends.</li>
            <li><b>The Apex Compounder (v10):</b> A high-leverage "kamikaze" protocol utilizing 5% account risk per trade. Backtesting shows extreme capital multipliers, heavily dependent on the ADX filter to avoid drawdown sequences.</li>
            <li><b>Institutional Breakeven Logic:</b> Moves stop-loss to entry cost immediately upon capturing 50% partial profits (TP1), ensuring risk-free exposure on the remaining runner volume.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💻 Source Notebooks")
    col_t1, col_t2, col_t3 = st.columns(3)
    with col_t1:
        create_download_button("Z-Score Pairs Engine", "Z SCORE SOL LINK .ipynb")
    with col_t2:
        create_download_button("XRP Institutional Engine", "XRP ADVXUSD.ipynb")
    with col_t3:
        create_download_button("Gold MT5 Architecture", "GOLD XAUSD.ipynb")
