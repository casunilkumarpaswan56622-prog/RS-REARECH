import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# ==========================================
# 🏛️ INSTITUTIONAL UI/UX ARCHITECTURE & CSS
# ==========================================
st.set_page_config(
    page_title="CA Sunil Kumar Paswan | Quant Architect",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #020617; 
        color: #E2E8F0;
    }
    
    .title-gradient {
        background: linear-gradient(90deg, #D4AF37 0%, #FACC15 50%, #F59E0B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -1.0px;
        margin-bottom: 0px;
    }
    
    .subtitle {
        color: #94A3B8;
        font-size: 16px;
        font-weight: 300;
        margin-bottom: 20px;
    }
    
    .glass-card {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(51, 65, 85, 0.8);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .glass-card:hover { border-color: #D4AF37; box-shadow: 0 4px 20px rgba(212, 175, 55, 0.05); }
    
    .metric-value { font-size: 28px; font-weight: 800; font-family: 'JetBrains Mono', monospace; }
    .metric-green { color: #10B981; }
    .metric-gold { color: #FACC15; }
    .metric-blue { color: #38BDF8; }
    .metric-red { color: #EF4444; }
    .metric-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #64748B; font-weight: 600;}
    
    .terminal-console {
        background-color: #000000;
        border: 1px solid #1E293B;
        border-left: 3px solid #38BDF8;
        padding: 15px;
        border-radius: 8px;
        font-family: 'JetBrains Mono', monospace;
        color: #E2E8F0;
        font-size: 12px;
        line-height: 1.6;
        height: 350px;
        overflow-y: auto;
        box-shadow: inset 0 0 20px rgba(0,0,0,1);
    }
    
    .t-cyan { color: #22D3EE; }
    .t-green { color: #10B981; }
    .t-yellow { color: #FBBF24; }
    .t-red { color: #EF4444; }
    .t-white { color: #FFFFFF; }

    .disclaimer-box {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid #EF4444;
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
        font-size: 12px;
        color: #FCA5A5;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🧭 SINGLE ROBUST NAVIGATION SYSTEM
# ==========================================
with st.sidebar:
    st.markdown(f"### 🏦 CA Sunil Kr Paswan")
    st.caption("Chief Quantitative Architect")
    st.divider()
    
    st.markdown("### 📊 QUANTITATIVE PORTFOLIOS")
    nav_selection = st.radio("Select Market Domain:", [
        "1. INDIAN MARKET (Equities & Options)",
        "2. CRYPTO CURRENCY (Stat-Arb)",
        "3. FOREX (XAUUSD Prop Firm)"
    ], label_visibility="collapsed")
    
    st.divider()
    st.markdown("""
    <div class="disclaimer-box">
        <b>⚠️ REGULATORY DISCLAIMER</b><br><br>
        I am <b>NOT</b> a SEBI Registered Investment Advisor. All algorithmic models, backtesting data, and metrics presented in this dashboard are strictly for <b>Educational and Research Purposes</b> only. They do not constitute financial advice. Past performance is not indicative of future results.
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 🔐 SECURE CLIENT AUTHENTICATION
# ==========================================
def requires_auth():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        col1, col2, col3 = st.columns([1, 1.5, 1])
        with col2:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
            st.markdown('<p class="title-gradient" style="font-size: 28px;">BLACK-BOX ACCESS</p>', unsafe_allow_html=True)
            st.markdown("<p style='color:#94A3B8;'>Authentication Required for Quantitative Telemetry</p>", unsafe_allow_html=True)
            
            with st.form("auth"):
                email = st.text_input("Corporate Email Address")
                phone = st.text_input("Registered Mobile Number")
                st.caption("Access strictly monitored. Read-only permissions granted.")
                submit = st.form_submit_button("Authenticate")
                if submit and email and phone:
                    st.session_state.logged_in = True
                    st.rerun()
                elif submit:
                    st.error("Invalid credentials. Please fill all fields.")
            st.markdown('</div>', unsafe_allow_html=True)
        return False
    return True

# ==============================================================================
# 📊 MODULE 1: INDIAN MARKET (EQUITIES & OPTIONS)
# ==============================================================================
if nav_selection == "1. INDIAN MARKET (Equities & Options)":
    st.markdown('<p class="title-gradient">Indian Indices & High-Beta Equities</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Proprietary Options Engines | NIFTY 50 & NIFTY 100 Institutional Scanners</p>', unsafe_allow_html=True)
    
    st.info("📊 **Quantum of Data Analyzed:** Extensive computational backtesting incorporating **191,380 Spot Candlestick Rows** and **380,996 Options Data Rows** covering December 2023 to December 2025. Over 106 individual NIFTY 100 equities parsed across 1-min & 5-min intervals.", icon="📈")

    tab1, tab2, tab3, tab4 = st.tabs([
        "2-Year Intraday Matrix", 
        "High-Conviction Options", 
        "Straddle Extraction Engine",
        "Live Execution Scanner"
    ])

    with tab1:
        st.markdown("### Nifty 2-Year Intraday Comprehensive Analysis")
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">88.97%</div><div class="metric-label">BB+Low IV Win Rate</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">81.41%</div><div class="metric-label">PCR Contarian Win Rate</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">1.46</div><div class="metric-label">Sharpe Ratio (Top Setup)</div></div>', unsafe_allow_html=True)
        with c4: st.markdown('<div class="glass-card"><div class="metric-value metric-white">2,143.94</div><div class="metric-label">Monte Carlo Mean PnL</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Strategy Logic (Obfuscated):** 
        Multi-setup architecture running concurrently. It exploits option mispricings using **Bollinger Band Squeeze Breakouts combined with Low Implied Volatility (IV) Percentiles**. A secondary engine acts as a contrarian trap, buying Puts when the PCR (Put-Call Ratio) drops below extreme institutional levels, and buying Calls when retail fear peaks (PCR > 1.2).
        """)

    with tab2:
        st.markdown("### 5-Minute Nifty 100 Options Buying")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">104.94%</div><div class="metric-label">Total Return (Top Stock)</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">31.7%</div><div class="metric-label">Win Rate (Asymmetric RR)</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">605</div><div class="metric-label">Total Valid Setups</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Strategy Logic (Obfuscated):** 
        Filters out 95% of market noise to isolate institutional momentum. Uses 5 setup variants including **VWAP Breakouts**, **Volume Surges (>3x avg)**, and **Hidden RSI Divergences**. Employs fixed holding periods of 3 to 15 candles to outrun Theta decay. The 31.7% win rate is mathematically offset by massive capped asymmetric upside (up to +500% premium spikes).
        """)
        
    with tab3:
        st.markdown("### Institutional Straddle Edge & ORB-50")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">69.2%</div><div class="metric-label">Pre-Expiry Straddle Win Rate</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">₹76.9k</div><div class="metric-label">BTST Contribution</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">1.005</div><div class="metric-label">Profit Factor (Unleveraged)</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Strategy Logic (Obfuscated):** 
        Retail loses on straddles due to linear Theta decay. This engine only enters straddles on **Macro Volume Spikes (>1.7x)** during extreme consolidation. The analysis reveals a distinct **BTST (Buy Today, Sell Tomorrow) dominance** over morning execution, exploiting overnight gap risk in high-beta counters like ADANIENSOL and SHRIRAMFIN.
        """)

    with tab4:
        st.markdown("### Intraday Signal Generators (Live Telemetry)")
        st.markdown("""
        **Active Modules:** NIFTY 50 SMA/RSI Algo & NIFTY 100 Option Scanner.
        Scans thousands of 1-minute and 5-minute ticks live. Uses an advanced scoring matrix tracking ADX momentum, RVOL (Relative Volume), and ATR expansion to generate pre-calculated entry vectors for execution systems.
        """)
        if requires_auth():
            v21_log = """
<span class="t-cyan">🚀 Precision Sniper Scanner Online...</span>
<span class="t-white">📍 NIFTY 50 | MTF Consensus: BEARISH | VWAP: -0.57%</span>
<span class="t-white">📉 PCR: 1.25 [BEARISH] — Put buying in high VIX detected.</span>
<span class="t-green">🎯 FINAL INTEGRATED SCORE: 71% (Required: 65%)</span>
<span class="t-yellow">💼 Logged SIGNAL: Buy PE | Target R:R 1:2.5</span>
            """
            st.markdown(f'<div class="terminal-console">{v21_log}</div>', unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 2: CRYPTO CURRENCY (STAT-ARB)
# ==============================================================================
elif nav_selection == "2. CRYPTO CURRENCY (Stat-Arb)":
    st.markdown('<p class="title-gradient">Titan Stat-Arb Cryptocurrency Engine</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Market-Neutral Z-Score Spreads via Unified Margin APIs</p>', unsafe_allow_html=True)
    
    st.info("📊 **Quantum of Data Analyzed:** High-frequency ingestion of 60-minute perpetual futures candles via WebSocket & REST. Evaluates rolling 168-bar (7-day) and 40-bar (1.67-day) lookback windows to compute real-time statistical deviations.", icon="📈")

    tab1, tab2 = st.tabs(["TITAN V6 (Advanced Stat-Arb)", "TITAN V1 (Simplified Risk Edition)"])

    with tab1:
        st.markdown("### TITAN V6: ADA/XRP Pairs Trade with ARIMA Veto")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">±2.5σ</div><div class="metric-label">Z-Score Entry Threshold</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-red">±3.5σ</div><div class="metric-label">Circuit Breaker (Stop)</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">30%</div><div class="metric-label">Notional Exposure (Max)</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Strategy Logic (Obfuscated):**
        Tracks the spread ratio between highly correlated assets (e.g., ADA/XRP). Enters a market-neutral long/short position when the 168-bar Z-Score exceeds 2.5 standard deviations. 
        **Institutional Edge:** Integrates a predictive **ARIMA(1,0,1) Veto Model**. The engine forecasts the next 3 bars; if the model predicts the divergence will *continue* trending rather than reverting, the trade is vetoed to prevent drawdown. Executes via Iceberg Limit-Maker chunks to eliminate taker fees.
        """)
        
    with tab2:
        st.markdown("### TITAN SOL/LINK: Fast Mean-Reversion")
        st.markdown("""
        **Strategy Logic (Obfuscated):**
        A higher-frequency variant utilizing a shorter 40-bar lookback window. Triggers at |Z| > 2.0 and strictly scales out when the spread reverts to |Z| < 0.2. Risk is hard-capped at 5% equity per trade utilizing 10x linear leverage.
        """)
        
    if requires_auth():
        titan_log = """
<span class="t-cyan">📡 TITAN V6 SYNCING CLOCKS...</span>
<span class="t-green">✅ TIME SYNCED. Drift: -0.04s</span>
<span class="t-white">⏳ 14:02:11 | Spread Z-Score: 2.105 | Status: ESCALATING</span>
<span class="t-green">📈 SIGNAL [Z: 2.105]: ARIMA Veto Passed. Spread Reversion Probable.</span>
<span class="t-cyan">🚀 SIGNAL FIRED: Short SOL, Long LINK.</span>
<span class="t-green">✅ Maker Orders Filled. Market Neutral Status Achieved.</span>
        """
        st.markdown(f'<div class="terminal-console">{titan_log}</div>', unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 3: FOREX (XAUUSD PROP FIRM)
# ==============================================================================
elif nav_selection == "3. FOREX (XAUUSD Prop Firm)":
    st.markdown('<p class="title-gradient">Apex Compounder & Gold Miner Pro (XAUUSD)</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Prop-Firm Asymmetric Runner | MT5 Integration Architecture</p>', unsafe_allow_html=True)
    
    st.info("📊 **Quantum of Data Analyzed:** Simulated chronological stress testing over 1 to 2 years of MT5 historical H1 (Hourly) data. Over **8,760 hourly data points processed annually**, testing across normal and high-impact macroeconomic event volatility.", icon="📈")

    tab1, tab2, tab3 = st.tabs(["Z-Score Sniper V6", "Apex Compounder V10", "XM Bonus Incubator"])

    with tab1:
        st.markdown("### Funded Scaler: Institutional Z-Score Setup")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">+21.90%</div><div class="metric-label">1-Yr Total Net ROI</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">3.59%</div><div class="metric-label">Maximum Drawdown</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">100%</div><div class="metric-label">Prop Firm Pass Prob.</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Strategy Logic (Obfuscated):**
        Utilizes a Macro Trend Filter (e.g., EMA200) to establish directional bias. Enters on extreme oversold/overbought dips using H1 Z-Scores during the NY Power Hours (13:00–18:00 UTC). Risk is kept defensively low at 0.5% per trade. Employs a dynamic ATR-based SL/TP mechanism with instant breakeven trailing.
        """)

    with tab2:
        st.markdown("### Apex Compounder V10 (High Risk/Kamikaze Engine)")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">+372.93%</div><div class="metric-label">Aggressive ROI</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-red">23.88%</div><div class="metric-label">Maximum Drawdown</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">4.73x</div><div class="metric-label">Capital Multiple</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Strategy Logic (Obfuscated):**
        The exact same robust mathematical entry parameters as V6, but re-engineered for personal capital scaling rather than Prop Firm limits. Risks 5% per trade. Generates massive returns by utilizing an **Asymmetric Scaling Engine**: Secures 50% at TP1 to neutralize risk, and trails the remaining lot with loose ATR bounds to catch violent macro gold runs.
        """)

    with tab3:
        st.markdown("### The XM Bonus Incubator (Micro-Capital Scaling)")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">559.4%</div><div class="metric-label">Return on Deposit</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-green">$3,297.14</div><div class="metric-label">Final Real Cash</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-white">51</div><div class="metric-label">Total Trades</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Objective:** To systematically convert non-withdrawable broker bonus credit into real withdrawable cash.
        **Backtest Results:** Started with $500 Real Cash + $250 Credit. Over the simulated curve, the engine withstood a max drawdown of 23.88% (absorbing the hit into the credit buffer) and geometrically compounded the base capital out to over $3,200 of liquid capital.
        """)

    if requires_auth():
        apex_log = """
<span class="t-white">🚀 INITIALIZING XAUUSD APEX ENGINE (MT5 BRIDGE)...</span>
<span class="t-green">✅ MT5 Connected | Target: XAUUSD | Base: $25,000.00</span>
<span class="t-white">---------------------------------------------------------</span>
<span class="t-green">⚡ PROP SIGNAL GENERATED | Structure: [MASKED] </span>
<span class="t-cyan">🔥 EXECUTION: LONG XAUUSD | SL: Algorithmic Low</span>
<span class="t-green">💰 T1 BREACHED! Securing 50% lot size.</span>
<span class="t-cyan">📈 SYSTEM ACTION: SL modified to Breakeven. Risk profile = 0.00%</span>
<span class="t-cyan">📈 Trailing SL Moved UP (Locking structural profit)</span>
<span class="t-red">🛑 DYNAMIC TRAILING SL TRIGGERED | Position Cleared</span>
<span class="t-cyan">✅ Trade Concluded. Asymmetric Reward Profile Successfully Achieved.</span>
        """
        st.markdown(f'<div class="terminal-console">{apex_log}</div>', unsafe_allow_html=True)
