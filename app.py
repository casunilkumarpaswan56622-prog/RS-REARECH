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
        font-size: 42px;
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
    
    .metric-value { font-size: 32px; font-weight: 800; font-family: 'JetBrains Mono', monospace; }
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
        height: 450px;
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
# 🔐 SECURE CLIENT AUTHENTICATION (FOR LIVE LOGS)
# ==========================================
def requires_auth():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.license_expiry = None

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
                    st.session_state.license_expiry = datetime.now() + timedelta(days=7)
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
    st.markdown('<p class="subtitle">Proprietary Options Engines | NIFTY 50 & NIFTY 100 Scanners</p>', unsafe_allow_html=True)
    
    # Data Quantum Callout
    st.info("📊 **Data Quantum Analyzed:** Over 191,380 Spot Candlestick Rows and 380,996 Options Data Rows processed. Backtesting horizon covers December 2023 to December 2025 across 1-minute and 5-minute timeframes.", icon="📈")

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">88.97%</div><div class="metric-label">Peak Setup Win Rate</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">104.9%</div><div class="metric-label">Max Straddle ROI</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">0.0017</div><div class="metric-label">Base Sharpe Ratio</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="glass-card"><div class="metric-value metric-red">69.2%</div><div class="metric-label">Pre-Expiry Win Rate</div></div>', unsafe_allow_html=True)

    colA, colB = st.columns([1, 1])
    with colA:
        st.markdown("#### ⏱️ Optimal Execution Windows")
        time_data = pd.DataFrame({
            "Market Phase": ["Morning Edge (9:15-10:30)", "Consolidation (12:00-14:00)", "BTST Setup (15:15+)"],
            "Algorithmic Win Rate": [65.0, 45.0, 81.4],
        })
        fig = px.bar(time_data, x="Market Phase", y="Algorithmic Win Rate", color="Algorithmic Win Rate", color_continuous_scale="RdYlGn")
        fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        fig.add_hline(y=50, line_dash="dash", line_color="white")
        st.plotly_chart(fig, use_container_width=True)

    with colB:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color:#D4AF37;">Core Institutional Framework (Masked Logic)</h4>
            <p style="color:#94A3B8; font-size: 14px;">
            The algorithms utilize multi-layered institutional footprint tracking without relying on standard retail lagging indicators.<br><br>
            <ul>
                <li><b>Volatility Squeeze Extraction:</b> Proprietary variance filters identify anomalous compressions in high-beta stocks (e.g., Energy/Infra sector) prior to explosive directional moves.</li>
                <li><b>Contrarian Options Flow:</b> Utilizes dynamic PCR (Put-Call Ratio) divergence thresholds alongside rolling IV (Implied Volatility) percentiles to trade against retail sentiment.</li>
                <li><b>The BTST Edge:</b> Structural market analysis shows overnight gaps in selected equities mathematically outpace theta decay when strictly executed under specific algorithmic conditions.</li>
            </ul>
            <i>Note: Exact indicator lengths, thresholds, and ML-assisted scoring parameters are strictly confidential black-box IP.</i>
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 2: CRYPTO CURRENCY (STAT-ARB)
# ==============================================================================
elif nav_selection == "2. CRYPTO CURRENCY (Stat-Arb)":
    if requires_auth():
        st.markdown('<p class="title-gradient">Titan Stat-Arb Cryptocurrency Engine</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Market-Neutral Z-Score Spreads via Unified Margin APIs</p>', unsafe_allow_html=True)
        
        st.info("📊 **Data Quantum Analyzed:** Rolling multi-day lookbacks generating continuous statistical evaluation of perpetual futures. Live integration executed over 60-minute interval chunks via REST/WebSocket.", icon="📈")

        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">SOL/LINK</div><div class="metric-label">Active Cointegration Pair</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-green">Dynamic</div><div class="metric-label">Adaptive Z-Score Triggers</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">10x</div><div class="metric-label">Linear Leverage</div></div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h4 style="color:#D4AF37;">Statistical Arbitrage Methodology</h4>
            <p style="color:#94A3B8; font-size: 14px;">
            The Titan series leverages pairs trading based on cointegration. By calculating the standard deviation of the spread between two historically correlated assets (e.g., ADA/XRP or SOL/LINK), the bot shorts the outperforming asset and goes long on the underperforming asset when statistical divergence occurs. <b>Logic is augmented with proprietary macroeconomic trend vetoes to avoid trending deviations.</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

        titan_log = """
<span class="t-white">--- 🏛️ TITAN V6: INSTITUTIONAL MAKER EDITION ---</span>
<span class="t-white">  🎯 Target Pool: SOLUSDT / LINKUSDT / ADAUSDT / XRPUSDT</span>
<span class="t-white">  🛡️ Risk Protocol: Strict Circuit Breakers Active</span>

<span class="t-cyan">📡 SYNCING EXCHANGE CLOCKS...</span>
<span class="t-green">✅ TIME SYNCED. Drift: -0.02s</span>
<span class="t-cyan">📡 INITIALIZING LIVE SESSION...</span>

<span class="t-cyan">📡 MONITORING MARKET VOLATILITY SPREADS...</span>
<span class="t-white">⏳ 14:02:11 | Z-Spread Divergence: [MASKED] | Status: MONITORING</span>
<span class="t-white">⏳ 14:02:21 | Z-Spread Divergence: [MASKED] | Status: ESCALATING</span>

<span class="t-green">📈 PROPRIETARY SIGNAL TRIGGERED: Cross-Asset Divergence Detected.</span>
<span class="t-cyan">🚀 SIGNAL FIRED: Initiating Market Neutral Hedge</span>
<span class="t-green">✅ [Asset A] Fill Success (LimitMaker Post-Only).</span>
<span class="t-green">✅ [Asset B] Fill Success (LimitMaker Post-Only).</span>

<span class="t-white">⏳ 14:15:30 | Spread Mean-Reverting...</span>
<span class="t-green">🎯 TARGET REACHED. Mean Reversion Complete.</span>
<span class="t-cyan">🛑 CLOSING ALL POSITIONS VIA ICEBERG CHUNKER...</span>
<span class="t-green">✅ LIQUIDITY SECURED. Net Profit Extracted.</span>
<span class="t-white">⏳ Cooldown activated. Letting the spread mathematical bounds reset.</span>
        """
        st.markdown(f'<div class="terminal-console">{titan_log}</div>', unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 3: FOREX (XAUUSD PROP FIRM)
# ==============================================================================
elif nav_selection == "3. FOREX (XAUUSD Prop Firm)":
    if requires_auth():
        st.markdown('<p class="title-gradient">Apex Compounder & Gold Miner Pro (XAUUSD)</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Prop-Firm Asymmetric Runner | MT5 Integration Architecture</p>', unsafe_allow_html=True)
        
        st.info("📊 **Data Quantum Analyzed:** Simulated chronological testing over 1-2 years of H1 (Hourly) XAUUSD MT5 Data. Over 8,760 hourly bars processed annually to validate stress test parameters against Prop Firm limits.", icon="📈")

        c1, c2, c3 = st.columns(3)
        with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">+21.9%</div><div class="metric-label">1-Year Base Net ROI</div></div>', unsafe_allow_html=True)
        with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">100%</div><div class="metric-label">Prop Firm Pass Rate (Sim)</div></div>', unsafe_allow_html=True)
        with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-red">3.59%</div><div class="metric-label">Maximum Drawdown</div></div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #FACC15;">
            <h4 style="color:#FACC15; margin-top:0;">Asymmetric Risk Management & Trade Scaling</h4>
            <p style="color:#94A3B8; font-size: 14px;">
            The Gold Miner Pro algorithm does not rely on single-target exits. It uses a <b>Proprietary Dynamic Scale-Out Engine</b> designed explicitly to survive rigid Prop Firm drawdown rules.<br><br>
            <b>Mechanics (Obfuscated):</b><br>
            • Entry triggered by multi-timeframe structural exhaustion and proprietary variance models.<br>
            • The algorithm aggressively secures a partial position at an initial threshold, instantly mathematically eliminating risk by adjusting the trailing stop to breakeven.<br>
            • The remainder of the position acts as a "Free Runner", trailing strictly behind dynamic volatility bands to catch macro-level economic expansions.
            </p>
        </div>
        """, unsafe_allow_html=True)

        apex_log = """
<span class="t-white">🚀 INITIALIZING XAUUSD PROP-FIRM APEX ENGINE (MT5 BRIDGE)...</span>
<span class="t-green">✅ MT5 Connected | Target: XAUUSD | Base: $25,000.00</span>
<span class="t-yellow">⚠️ Risk Protocol: Prop-Firm Safe (0.5% - 5.0% Dynamic Allocation)</span>
<span class="t-white">---------------------------------------------------------</span>
<span class="t-cyan">⏳ APEX SCANNER ACTIVE. Waiting for Institutional Volatility Signatures...</span>

<span class="t-green">⚡ PROP SIGNAL GENERATED | Structure: [MASKED] | Volatility: [MASKED]</span>
<span class="t-cyan">🔥 EXECUTION: LONG XAUUSD | Size Calculated dynamically</span>
<span class="t-white">🔹 XAUUSD | T1: Primary Securitization Target | SL: Algorithmic Low</span>

<span class="t-green">💰 T1 BREACHED! Securing 50% lot size.</span>
<span class="t-cyan">📈 SYSTEM ACTION: SL modified to Breakeven. Risk profile = 0.00%</span>

<span class="t-white">🔹 XAUUSD Trailing Engine Active. Following market structure.</span>
<span class="t-cyan">📈 Trailing SL Moved UP (Locking structural profit)</span>

<span class="t-red">🛑 DYNAMIC TRAILING SL TRIGGERED | Position Cleared</span>
<span class="t-cyan">✅ Trade Concluded. Asymmetric Reward Profile Successfully Achieved.</span>
<span class="t-green">✅ Equity Protected. Updating Metrics Dashboard.</span>
        """
        st.markdown(f'<div class="terminal-console">{apex_log}</div>', unsafe_allow_html=True)
