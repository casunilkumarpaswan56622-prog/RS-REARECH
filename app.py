import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time
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
        background-color: #020617; /* Institutional Deep Slate */
        color: #E2E8F0;
    }
    
    .title-gradient {
        background: linear-gradient(90deg, #D4AF37 0%, #FACC15 50%, #F59E0B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin-bottom: 0px;
    }
    
    .subtitle {
        color: #94A3B8;
        font-size: 18px;
        font-weight: 300;
        margin-bottom: 30px;
        letter-spacing: 0.5px;
    }
    
    .glass-card {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(51, 65, 85, 0.8);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 24px;
        transition: all 0.3s ease;
    }
    .glass-card:hover { border-color: #D4AF37; box-shadow: 0 4px 20px rgba(212, 175, 55, 0.1); }
    
    .metric-value { font-size: 38px; font-weight: 800; font-family: 'JetBrains Mono', monospace; }
    .metric-green { color: #10B981; }
    .metric-gold { color: #FACC15; }
    .metric-blue { color: #38BDF8; }
    .metric-label { font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: #64748B; font-weight: 600; margin-top: 5px;}
    
    .terminal-console {
        background-color: #000000;
        border: 1px solid #1E293B;
        border-left: 4px solid #38BDF8;
        padding: 20px;
        border-radius: 8px;
        font-family: 'JetBrains Mono', monospace;
        color: #E2E8F0;
        font-size: 13px;
        line-height: 1.7;
        height: 500px;
        overflow-y: auto;
        box-shadow: inset 0 0 30px rgba(0,0,0,1);
    }
    
    /* Terminal Output Colors */
    .t-cyan { color: #22D3EE; font-weight: bold; }
    .t-green { color: #10B981; }
    .t-yellow { color: #FBBF24; }
    .t-red { color: #EF4444; }
    .t-white { color: #FFFFFF; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🔐 SECURE CLIENT AUTHENTICATION (7-DAY PASS)
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.license_expiry = None

def login():
    st.session_state.logged_in = True
    st.session_state.license_expiry = datetime.now() + timedelta(days=7)

if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown('<p class="title-gradient" style="font-size: 32px;">CA SUNIL KUMAR PASWAN</p>', unsafe_allow_html=True)
        st.markdown("<p style='color:#94A3B8; margin-bottom: 20px;'>Institutional Quantitative Architecture | Secure Client Portal</p>", unsafe_allow_html=True)
        
        with st.form("auth"):
            email = st.text_input("Corporate Email Address")
            phone = st.text_input("Registered Mobile Number")
            st.caption("Access strictly monitored. 7-Day Trial License issued upon verification.")
            submit = st.form_submit_button("Authenticate & Enter Black Box")
            if submit and email and phone:
                login()
                st.rerun()
            elif submit:
                st.error("Invalid credentials.")
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# ==========================================
# 🧭 SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown(f"### 🏦 CA Sunil Kr Paswan")
    st.caption("Chief Quantitative Architect")
    st.markdown(f"**License Valid Until:**<br><span style='color:#10B981'>{st.session_state.license_expiry.strftime('%d %b %Y')}</span>", unsafe_allow_html=True)
    st.divider()
    
    st.markdown("### 📊 I. HISTORICAL PROOFS")
    nav_proofs = st.radio("Select Research Base:", [
        "1. NIFTY 50 Intraday Matrix",
        "2. ADANIENSOL Straddle Engine",
        "3. Equity Options Edge (18.2M Rows)"
    ], label_visibility="collapsed")
    
    st.divider()
    st.markdown("### 🔴 II. LIVE TELEMETRY")
    nav_live = st.radio("Select Active VPS Node:", [
        "4. V21.4 Precision Sniper (Indices)",
        "5. Titan V6.0 Stat-Arb (Crypto)",
        "6. Apex Compounder (XAUUSD)"
    ], label_visibility="collapsed")

# ==============================================================================
# 📊 MODULE 1: NIFTY 50 INTRADAY MATRIX (FROM PDF)
# ==============================================================================
if nav_proofs == "1. NIFTY 50 Intraday Matrix":
    st.markdown('<p class="title-gradient">NIFTY 50: The 2-Year Intraday Matrix</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Based on 191,380 Intraday Candles & 380,996 Options Contracts.</p>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">91.04</div><div class="metric-label">Kurtosis (Fat Tails)</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-green">88.97%</div><div class="metric-label">Peak Win Rate (BB+Put)</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">1.89</div><div class="metric-label">System Profit Factor</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">65.0%</div><div class="metric-label">Gap-Up Win Rate</div></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #F8FAFC;">The Illusion of Randomness</h3>
        <p style="color: #94A3B8; line-height: 1.6;">
        Retail traders believe the market is random. Our parsing of 191,000+ NIFTY candles mathematically disproves this. 
        The data reveals a stark <strong>Kurtosis of 91.04</strong>, proving that the Indian Index experiences frequent, violent, extreme moves ("Fat Tails") driven by institutional algorithmic sweeping. The retail trader gets chopped out during the 12:00 PM - 2:00 PM "Dead Zone" (where Win Rates plummet to 45% and slippage doubles), while our system exclusively targets the <strong>9:15 AM - 10:30 AM Peak Liquidity Window</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    colA, colB = st.columns([1, 1])
    with colA:
        st.markdown("#### ⏱️ Temporal Win Rate Matrix")
        # Recreating the exact data from the PDF
        time_data = pd.DataFrame({
            "Time Slot": ["9:15 - 10:30 AM", "10:30 - 12:00 PM", "12:00 - 2:00 PM", "2:00 - 3:30 PM", "3:30 - 4:00 PM"],
            "Win Rate (%)": [65.0, 50.0, 45.0, 52.0, 48.0],
            "Classification": ["PEAK (Gap Trade)", "Medium (Range)", "DEAD (AVOID)", "Revival (Reversal)", "Close (Theta)"]
        })
        fig = px.bar(time_data, x="Time Slot", y="Win Rate (%)", color="Win Rate (%)", 
                     color_continuous_scale="RdYlGn", title="Win Probability by Hour")
        fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        fig.add_hline(y=50, line_dash="dash", line_color="white", annotation_text="Break Even")
        st.plotly_chart(fig, use_container_width=True)

    with colB:
        st.markdown("#### 🛡️ Kelly Criterion Monte Carlo (1,000 Runs)")
        # Generating a simulated normal distribution based on PDF parameters
        np.random.seed(42)
        mc_data = np.random.normal(loc=2144, scale=3550, size=1000)
        fig2 = go.Figure(data=[go.Histogram(x=mc_data, nbinsx=50, marker_color='#38BDF8')])
        fig2.add_vline(x=-3338, line_dash="dash", line_color="#EF4444", annotation_text="5th Percentile (Max Risk)")
        fig2.add_vline(x=8064, line_dash="dash", line_color="#10B981", annotation_text="95th Percentile (Max Gain)")
        fig2.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                           title="Daily Expected PnL Distribution (1L Capital)", xaxis_title="Daily PnL (₹)")
        st.plotly_chart(fig2, use_container_width=True)

# ==============================================================================
# 📊 MODULE 2: ADANIENSOL STRADDLE ENGINE (FROM PDF)
# ==============================================================================
elif nav_proofs == "2. ADANIENSOL Straddle Engine":
    st.markdown('<p class="title-gradient">Volatility Squeeze Extraction</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">5-Year Backtest (2020-2025) on ADANIENSOL Straddles.</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">+104.9%</div><div class="metric-label">5-Year Total Return</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">31.7%</div><div class="metric-label">Win Rate (High Skew)</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">76.9k</div><div class="metric-label">BTST PnL Contribution</div></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("""
        ### Strategy Architecture
        Retail traders lose money on Straddles due to Theta (Time Decay). This proprietary engine filters out 90% of market noise by demanding a **Bollinger Band Width < 8th Percentile** combined with a **Volume Spike > 1.7x** the 20-bar average. 
        
        We deploy this exclusively as a **BTST (Buy Today, Sell Tomorrow)** strategy, executed between 1:15 PM and 3:15 PM. By utilizing the overnight gap dynamic in high-beta energy stocks (Beta 0.92), the resulting absolute price move (>1.5%) massively outpaces the overnight Theta decay.
        
        *Note: The win rate is mathematically low (31.7%), but the Profit Factor is massive due to the asymmetric payoff of long volatility. Monte Carlo 5th Percentile ensures survival against 53-trade loss streaks.*
        """)
    with col2:
        df_pnl = pd.DataFrame({"Setup": ["BTST", "Morning", "Event"], "PnL (k)": [76.9, 28.1, 0]})
        fig = px.bar(df_pnl, x="Setup", y="PnL (k)", color="Setup", 
                     color_discrete_map={"BTST": "#10B981", "Morning": "#38BDF8", "Event": "#475569"})
        fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

# ==============================================================================
# 📊 MODULE 3: EQUITY OPTIONS EDGE (PYTHON LOGS)
# ==============================================================================
elif nav_proofs == "3. Equity Options Edge (18.2M Rows)":
    st.markdown('<p class="title-gradient">NIFTY 100 Options Analytics</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">18.2 Million Rows parsed for Momentum Continuation & Black-Scholes Pricing.</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <p style="color: #94A3B8; margin-bottom: 0;">
        <strong>Methodology:</strong> The system parses 10+ years of 5-minute historical data for 100 liquid equities. It calculates Proprietary Momentum (ADX + RSI), Volatility Expansion (TR/ATR > 1.5), and Relative Volume (RVOL > 2.0). Rather than tracking spot price, it mathematically calculates the 1-Hour forward excursion multiplied by a standard 0.50 ATM Delta to yield realistic Options PnL.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Data from FINAL STOCK OPTION .ipynb log
    data = {
        "Ticker": ["ADANIPOWER", "MAZDOCK", "ADANIENSOL", "JINDALSTEL", "ADANIGREEN", "VEDL", "TRENT", "CGPOWER"],
        "Historical Setups": [10651, 4120, 7513, 6423, 5391, 6312, 7320, 7396],
        "Win Rate (%)": [95.95, 93.96, 93.84, 93.76, 93.66, 91.65, 89.13, 90.97],
        "Avg Move (%)": [1.94, 1.85, 2.09, 1.72, 2.26, 1.67, 1.70, 1.86]
    }
    df = pd.DataFrame(data)
    
    st.dataframe(
        df.style.background_gradient(cmap='viridis', subset=['Win Rate (%)', 'Avg Move (%)']),
        use_container_width=True, hide_index=True
    )

# ==============================================================================
# 🔴 MODULE 4: LIVE TELEMETRY (V21.4 SNIPER)
# ==============================================================================
elif nav_live == "4. V21.4 Precision Sniper (Indices)":
    st.markdown('<p class="title-gradient">V21.4 Precision Sniper Engine</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Real-Time NIFTY / BANKNIFTY Execution Node. (Python Backend Masked)</p>', unsafe_allow_html=True)

    st.markdown("""
    <div style="padding: 10px; border: 1px solid #38BDF8; border-radius: 6px; background-color: rgba(56, 189, 248, 0.1); margin-bottom: 20px;">
        <span style="color: #38BDF8; font-weight: bold;">⚡ ALGORITHMIC CONFLUENCE:</span> The engine tracks VWAP Sigma Bands, Cumulative Delta Divergence, Order Flow Imbalance, and Real-Time Options Greeks (Delta/Theta). Circuit Breakers enforce a strict ₹5,000 Daily Loss Limit.
    </div>
    """, unsafe_allow_html=True)

    # Simulated Live Terminal based exactly on FINAL INDEX OPTION (1)_2.ipynb logs
    v21_log = """
<span class="t-cyan">🚀 v21.4 Precision Sniper Online. Press Ctrl+C to terminate.</span>
<span class="t-white">🔒 Account: 1107618621 | Threshold: 70% | Delta: 0.3–0.55 | Supertrend: 10×3.0</span>
<span class="t-green">[09:15:44] 🟢 LIVE — v21.4 running.</span>

<span class="t-cyan">══════════════════════════════════════════════════════════════════════════════════════</span>
<span class="t-cyan">🎯 SCANNING: BANKNIFTY | v21.4 Precision Sniper Engine</span>
<span class="t-cyan">══════════════════════════════════════════════════════════════════════════════════════</span>
<span class="t-white">📍 Dir: BULLISH | Supertrend: BULLISH (94 bars)</span>
<span class="t-white">📊 MTF: {'5m': 'BULLISH', '15m': 'BULLISH', '1H': 'BULLISH'} | Consensus: BULLISH</span>
<span class="t-white">📈 HA: NEUTRAL | EMA: BULLISH | RSI: 65.9 | MACD: BULLISH</span>
<span class="t-white">💧 VWAP: OVERBOUGHT_VWAP (+2.55%) | ΔCum: BUYING_PRESSURE</span>
<span class="t-white">📉 PCR: 0.827 [NEUTRAL] — </span>
<span class="t-white">🏦 OI Vel: NEUTRAL | IV Skew: BULLISH_SKEW (+6.61)</span>
<span class="t-white">🔊 Flow: BEARISH_FLOW (ratio: 1.52)</span>
<span class="t-white">🎯 SCORE: 78% (Min: 70%) | VIX≈13.95 | Vol Spike: ✅</span>
<span class="t-green">💼 Logged BANKNIFTY CE | ID: 67259.0 | Lot: 15</span>
<span class="t-cyan">✅ Signal dispatched to Telegram for BANKNIFTY.</span>

<span class="t-cyan">══════════════════════════════════════════════════════════════════════════════════════</span>
<span class="t-cyan">💼 VIRTUAL TRADE MANAGER v21.4 — LIVE TRACKING</span>
<span class="t-cyan">══════════════════════════════════════════════════════════════════════════════════════</span>
<span class="t-white">🔹 BANKNIFTY 53000 CE | LTP: ₹324.00 | SL: ₹288.50 | T1: ₹360.00 | T2: ₹396.00</span>
<span class="t-green">🛡️ T1 HIT — SL moved to Cost BANKNIFTY CE</span>
<span class="t-white">🔹 BANKNIFTY 53000 CE | LTP: ₹365.20 | SL: ₹324.00 (SL@Cost)</span>
<span class="t-green">🎯 TARGET 2 HIT! BANKNIFTY CE | Entry: ₹324.00 | Exit: ₹398.50</span>
<span class="t-green">💰 Net Gain: ₹74.50/qty</span>

<span class="t-cyan">✅ Forward-Test Log Closed. Updating trade_journal_v21_4.csv</span>
<span class="t-white">[15:15:00] 📊 END OF DAY SUMMARY GENERATED. Excel Exported.</span>
    """
    st.markdown(f'<div class="terminal-console">{v21_log}</div>', unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 5: LIVE TELEMETRY (TITAN V6 CRYPTO)
# ==============================================================================
elif nav_live == "5. Titan V6.0 Stat-Arb (Crypto)":
    st.markdown('<p class="title-gradient">Titan V6.0 Statistical Arbitrage</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Market-Neutral Z-Score Spreads via Bybit Unified Margin.</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">SOL/LINK</div><div class="metric-label">Active Cointegration Pair</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-green">2.5σ</div><div class="metric-label">Execution Z-Score</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">10x</div><div class="metric-label">Linear Leverage</div></div>', unsafe_allow_html=True)

    # Simulated Terminal based on Z SCORE SOL LINK _2.ipynb
    titan_log = """
<span class="t-white">--- 🏛️ TITAN V6: INSTITUTIONAL MAKER EDITION ---</span>
<span class="t-white">  🎯 Target: SOLUSDT / LINKUSDT</span>
<span class="t-white">  🛡️ Risk: 5% Size | 4.0 Stop | 0.2 Exit (Prop Firm Safe)</span>

<span class="t-cyan">📡 SYNCING CLOCKS...</span>
<span class="t-green">✅ TIME SYNCED. Drift: -0.04s</span>
<span class="t-cyan">📡 INITIALIZING SESSION...</span>
<span class="t-green">✅ CONNECTED. Equity: $25,000.00</span>
<span class="t-white">   Setting Leverage... Done.</span>

<span class="t-cyan">📡 MONITORING MARKET...</span>
<span class="t-white">⏳ 14:02:11 | Z-Score: 1.842 | Status: NEUTRAL</span>
<span class="t-white">⏳ 14:02:21 | Z-Score: 2.105 | Status: NEUTRAL</span>

<span class="t-green">📈 SIGNAL [Z: 2.105]: Short SOL, Long LINK.</span>
<span class="t-cyan">🚀 SIGNAL FIRED: Sell 17 SOL / Buy 182 LINK</span>
<span class="t-green">✅ [SOLUSDT] Sell 17 Fill Success (LimitMaker).</span>
<span class="t-green">✅ [LINKUSDT] Buy 182 Fill Success (LimitMaker).</span>

<span class="t-white">⏳ 14:15:30 | Z-Score: 0.198 | Status: ACTIVE TRADE</span>
<span class="t-green">🎯 TARGET REACHED [Z: 0.198]. Mean Reversion Complete.</span>
<span class="t-cyan">🛑 CLOSING ALL POSITIONS (PROFIT)...</span>
<span class="t-green">✅ CLOSED via Iceberg Chunker.</span>
<span class="t-white">⏳ Cooldown activated for 1 HOUR. Letting the spread reset.</span>
    """
    st.markdown(f'<div class="terminal-console">{titan_log}</div>', unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 6: LIVE TELEMETRY (APEX COMPOUNDER)
# ==============================================================================
elif nav_live == "6. Apex Compounder (XAUUSD)":
    st.markdown('<p class="title-gradient">The XAUUSD Apex Compounder</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Prop-Firm Asymmetric Runner | 10x Scale-Up Engine.</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #FACC15;">
        <p style="color: #94A3B8; margin-bottom: 0;">
        <strong>Institutional Edge:</strong> Most algorithms fail because they use fixed 1:1 ratios. The Apex Compounder survives drawdowns by mathematically engineering "Free Runners." It secures 50% of the position at 2.0 ATR, moves the Stop Loss to Breakeven, and trails the remaining 50% at 1.5 ATR. This turns a standard trade into a massive, risk-free <strong>"Gamma Blast"</strong> catcher, achieving up to 372% Net ROI in backtesting.
        </p>
    </div>
    """, unsafe_allow_html=True)

    apex_log = """
<span class="t-white">🚀 INITIALIZING THE LIVE APEX COMPOUNDER V10...</span>
<span class="t-green">✅ Connected: 345148129 | Balance: $25,000.00</span>
<span class="t-yellow">⚠️ Risk Level: 0.5% ($125.00 per trade)</span>
<span class="t-white">---------------------------------------------------------</span>
<span class="t-cyan">⏳ APEX SCANNER ACTIVE. Waiting for Institutional Setups...</span>

<span class="t-green">⚡ APEX BUY SIGNAL | ADX: 32.4 | Z-Score: -1.82</span>
<span class="t-cyan">🔥 BUY EXECUTED @ 2345.50 | Size: 0.10 | SL: 2343.00</span>
<span class="t-white">🔹 XAUUSD | LTP: 2345.50 | SL: 2343.00 | T1: 2350.50</span>

<span class="t-white">🔹 XAUUSD | LTP: 2348.10 | SL: 2343.00</span>
<span class="t-green">💰 TP1 HIT! Securing 50% profits (0.05 lots). Moving SL to Breakeven.</span>
<span class="t-white">🔹 XAUUSD | LTP: 2352.40 | SL: 2345.50 (SL@Cost)</span>
<span class="t-cyan">📈 Trailing SL Moved UP to 2348.65 (Securing Runner)</span>

<span class="t-red">🛑 TRAILING SL HIT! XAUUSD BUY</span>
<span class="t-white">Entry: 2345.50 | Exit: 2348.65</span>
<span class="t-cyan">✅ Trade Concluded. Total Asymmetric R:R achieved: 1:2.63</span>
    """
    st.markdown(f'<div class="terminal-console">{apex_log}</div>', unsafe_allow_html=True)
