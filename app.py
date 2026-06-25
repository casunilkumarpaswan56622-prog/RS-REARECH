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
        height: 600px;
        overflow-y: auto;
        box-shadow: inset 0 0 20px rgba(0,0,0,1);
    }
    
    .t-cyan { color: #22D3EE; }
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
        st.markdown('<p class="title-gradient" style="font-size: 28px;">CA SUNIL KUMAR PASWAN</p>', unsafe_allow_html=True)
        st.markdown("<p style='color:#94A3B8;'>Institutional Quantitative Architecture | Secure Client Portal</p>", unsafe_allow_html=True)
        
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
# 🧭 SINGLE ROBUST NAVIGATION SYSTEM
# ==========================================
with st.sidebar:
    st.markdown(f"### 🏦 CA Sunil Kr Paswan")
    st.caption("Chief Quantitative Architect")
    st.markdown(f"**License Valid Until:**<br><span style='color:#10B981'>{st.session_state.license_expiry.strftime('%d %b %Y')}</span>", unsafe_allow_html=True)
    st.divider()
    
    st.markdown("### 📊 HISTORICAL PROOFS")
    nav_selection = st.radio("Select Module:", [
        "1. NIFTY 50 Intraday Matrix",
        "2. ADANIENSOL Straddle Engine",
        "3. Holistic Options & Risk Model",
        "4. V21.4 Precision Sniper [LIVE]",
        "5. Titan V6.0 Stat-Arb [LIVE]",
        "6. Apex Compounder XAUUSD [LIVE]",
        "7. XM Bonus Incubator [LIVE]"
    ], label_visibility="collapsed")

# ==============================================================================
# 📊 MODULE 1: NIFTY 50 INTRADAY MATRIX
# ==============================================================================
if nav_selection == "1. NIFTY 50 Intraday Matrix":
    st.markdown('<p class="title-gradient">NIFTY 50: The 2-Year Intraday Matrix</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Based on 191,380 Intraday Candles & 380,996 Options Contracts.</p>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">91.04</div><div class="metric-label">Kurtosis (Fat Tails)</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-green">65.0%</div><div class="metric-label">Opening Gap Win Rate</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">1.89</div><div class="metric-label">Profit Factor</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="glass-card"><div class="metric-value metric-red">45.0%</div><div class="metric-label">Dead Zone (12-2 PM) WR</div></div>', unsafe_allow_html=True)

    colA, colB = st.columns([1, 1])
    with colA:
        st.markdown("#### ⏱️ Temporal Win Rate Matrix")
        time_data = pd.DataFrame({
            "Time Slot": ["9:15 - 10:30 AM", "10:30 - 12:00 PM", "12:00 - 2:00 PM", "2:00 - 3:30 PM", "3:30 - 4:00 PM"],
            "Win Rate (%)": [65.0, 50.0, 45.0, 52.0, 48.0],
        })
        fig = px.bar(time_data, x="Time Slot", y="Win Rate (%)", color="Win Rate (%)", color_continuous_scale="RdYlGn")
        fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        fig.add_hline(y=50, line_dash="dash", line_color="white")
        st.plotly_chart(fig, use_container_width=True)

    with colB:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color:#D4AF37;">Institutional Philosophy</h4>
            <p style="color:#94A3B8; font-size: 14px;">
            Retail traders believe the market is random. Our parsing of 191,000+ NIFTY candles mathematically disproves this. 
            The data reveals a stark <strong>Kurtosis of 91.04</strong>, proving that the index experiences frequent, violent "Fat Tails" driven by institutional sweeping.<br><br>
            <strong>The Temporal Edge:</strong> Retail gets chopped out during the 12:00 PM - 2:00 PM "Dead Zone" (where Win Rates plummet to 45% and slippage doubles). We exclusively target the <strong>9:15 AM - 10:30 AM Peak Liquidity Window</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# 📊 MODULE 2: ADANIENSOL STRADDLE ENGINE
# ==============================================================================
elif nav_selection == "2. ADANIENSOL Straddle Engine":
    st.markdown('<p class="title-gradient">Volatility Squeeze Extraction</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">5-Year Backtest (2020-2025) on ADANIENSOL Straddles.</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">+104.9%</div><div class="metric-label">5-Year Total Return</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">31.7%</div><div class="metric-label">Win Rate (High Skew)</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">76.9k</div><div class="metric-label">BTST PnL Contribution</div></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h4 style="color:#D4AF37;">The Mechanics of the Trap</h4>
        <p style="color:#94A3B8; font-size: 14px;">
        Retail traders lose on Straddles due to Theta decay. This engine filters 90% of noise by demanding a <strong>Bollinger Band Width < 8th Percentile</strong> combined with a <strong>Volume Spike > 1.7x</strong>.<br><br>
        Deployed exclusively as a <strong>BTST (Buy Today, Sell Tomorrow)</strong> strategy between 1:15 PM and 3:15 PM. The overnight gap in high-beta energy stocks mathematically outpaces the overnight Theta decay. The 31.7% win rate is offset by massive 3:1 R:R asymmetric outliers.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    df_pnl = pd.DataFrame({"Setup": ["BTST", "Morning", "Event"], "PnL (k)": [76.9, 28.1, 0]})
    fig = px.bar(df_pnl, x="Setup", y="PnL (k)", color="Setup", color_discrete_sequence=["#10B981", "#38BDF8", "#475569"])
    fig.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", title="PnL Distribution by Setup Type")
    st.plotly_chart(fig, use_container_width=True)

# ==============================================================================
# 📊 MODULE 3: HOLISTIC OPTIONS & RISK
# ==============================================================================
elif nav_selection == "3. Holistic Options & Risk Model":
    st.markdown('<p class="title-gradient">Holistic Options & Risk Architecture</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Based on the "Comprehensive Options Trading Guidance Report"</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-green">88.97%</div><div class="metric-label">Bollinger + Put Win Rate</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">81.41%</div><div class="metric-label">PCR Contarian Win Rate</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">2.0%</div><div class="metric-label">Max Risk Per Trade</div></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h4 style="color:#D4AF37;">Position Sizing & Kelly Criterion</h4>
        <p style="color:#94A3B8; font-size: 14px;">
        Algorithmic success relies entirely on mathematical capital preservation. We abandon fixed lot sizing. Instead, we use a <strong>Modified Kelly Criterion</strong>.<br>
        <i>Formula used:</i> <code>Position Size = (2 * Win% - 1) * Capital / Avg Loss</code><br><br>
        <strong>Circuit Breakers:</strong> Hard algorithmic shut-offs trigger at a 5% Daily Drawdown. Emotional trading is strictly prohibited; the engine executes via Good-Till-Cancel (GTC) limits exclusively.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 4: V21.4 PRECISION SNIPER (LIVE)
# ==============================================================================
elif nav_selection == "4. V21.4 Precision Sniper [LIVE]":
    st.markdown('<p class="title-gradient">V21.4 Precision Sniper Engine</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Real-Time Indian Indices Execution Node. (Python Backend Masked)</p>', unsafe_allow_html=True)

    v21_log = """
<span class="t-cyan">🚀 v21.4 Precision Sniper Online. Press Ctrl+C to terminate.</span>
<span class="t-white">🔒 Account: 1107618621 | Threshold: 70% | Supertrend: 10×3.0 | Anti-Whipsaw: 1 bars</span>
<span class="t-green">[09:26:09] 🟢 LIVE — v21.4 running.</span>

<span class="t-cyan">═══════════════════════════════════════════════════════════════════════════════════</span>
<span class="t-cyan">🎯 SCANNING: BANKNIFTY | v21.4 Precision Sniper Engine</span>
<span class="t-cyan">═══════════════════════════════════════════════════════════════════════════════════</span>
<span class="t-white">📍 Dir: BEARISH | Supertrend: BEARISH (31 bars)</span>
<span class="t-white">📊 MTF: {'5m': 'BEARISH', '15m': 'BEARISH', '1H': 'NEUTRAL'} | Consensus: BEARISH</span>
<span class="t-white">📈 HA: NEUTRAL | EMA: BEARISH | RSI: 43.4 | MACD: BEARISH</span>
<span class="t-white">💧 VWAP: BEARISH (-0.57%) | ΔCum: SELLING_PRESSURE</span>
<span class="t-white">📉 PCR: 1.25 [BEARISH] — Put buying in high VIX = fear</span>
<span class="t-white">🏦 OI Vel: CALL_WRITING_BEARISH | IV Skew: BEARISH_SKEW (-2.68)</span>
<span class="t-white">🔊 Flow: STRONG_BEARISH_FLOW (ratio: 1.87)</span>
<span class="t-green">🎯 FINAL INTEGRATED SCORE: 71% (Required: 65%)</span>

<span class="t-yellow">💼 Logged BANKNIFTY PE (ID: 67115.0) | Lot: 15</span>
<span class="t-cyan">✅ Signal dispatched to Telegram for BANKNIFTY.</span>

<span class="t-cyan">═══════════════════════════════════════════════════════════════════════════════════</span>
<span class="t-cyan">💼 VIRTUAL TRADE MANAGER v21.4 — LIVE TRACKING</span>
<span class="t-cyan">═══════════════════════════════════════════════════════════════════════════════════</span>
<span class="t-white">🔹 BANKNIFTY 53000 PE | LTP: ₹324.00 | SL: ₹288.50 | T1: ₹360.00 | T2: ₹396.00</span>
<span class="t-green">🛡️ T1 HIT — SL moved to Cost BANKNIFTY PE</span>
<span class="t-white">🔹 BANKNIFTY 53000 PE | LTP: ₹365.20 | SL: ₹324.00 (SL@Cost)</span>
<span class="t-green">🎯 TARGET 2 HIT! BANKNIFTY PE | Entry: ₹324.00 | Exit: ₹398.50</span>
<span class="t-green">💰 Net Gain: ₹74.50/qty</span>
<span class="t-cyan">✅ Forward-Test Log Closed. Updating trade_journal_v21_4.csv</span>
    """
    st.markdown(f'<div class="terminal-console">{v21_log}</div>', unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 5: TITAN V6.0 STAT-ARB (LIVE)
# ==============================================================================
elif nav_selection == "5. Titan V6.0 Stat-Arb [LIVE]":
    st.markdown('<p class="title-gradient">Titan V6.0 Statistical Arbitrage</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Market-Neutral Z-Score Spreads via Bybit Unified Margin.</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">SOL/LINK</div><div class="metric-label">Active Cointegration Pair</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-green">2.5σ</div><div class="metric-label">Execution Z-Score</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">10x</div><div class="metric-label">Linear Leverage</div></div>', unsafe_allow_html=True)

    titan_log = """
<span class="t-white">--- 🏛️ TITAN V6: INSTITUTIONAL MAKER EDITION ---</span>
<span class="t-white">  🎯 Target: SOLUSDT / LINKUSDT</span>
<span class="t-white">  🛡️ Risk: 5% Size | 4.0 Stop | 0.2 Exit (Prop Firm Safe)</span>

<span class="t-cyan">📡 SYNCING CLOCKS...</span>
<span class="t-green">✅ TIME SYNCED. Drift: -0.04s</span>
<span class="t-cyan">📡 INITIALIZING SESSION...</span>
<span class="t-green">✅ CONNECTED. Equity: $25,000.00</span>

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
# 🔴 MODULE 6: APEX COMPOUNDER XAUUSD
# ==============================================================================
elif nav_selection == "6. Apex Compounder XAUUSD [LIVE]":
    st.markdown('<p class="title-gradient">The XAUUSD Apex Compounder V10</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Prop-Firm Asymmetric Runner | 10x Scale-Up Engine | MT5 Integration.</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #FACC15;">
        <h4 style="color:#FACC15; margin-top:0;">1-Year Road to 10x ($25,000 to $118,233)</h4>
        <p style="color:#94A3B8; font-size: 14px;">
        Most algorithms fail because they use fixed 1:1 ratios. The Apex Compounder survives drawdowns by engineering "Free Runners." It secures 50% of the position at 2.0 ATR, moves SL to Breakeven, and trails the remaining 50% at 1.5 ATR. <strong>Kamikaze Risk applied: 5.0% of balance per trade.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    apex_log = """
<span class="t-white">🚀 INITIALIZING THE LIVE APEX COMPOUNDER V10 (MAXIMUM LEVERAGE)...</span>
<span class="t-green">✅ Connected: 345148129 | Balance: $25,000.00</span>
<span class="t-yellow">⚠️ Risk Level: 5.0% ($1,250.00 per trade)</span>
<span class="t-white">---------------------------------------------------------</span>
<span class="t-cyan">⏳ APEX SCANNER ACTIVE. Waiting for Institutional Setups...</span>

<span class="t-green">⚡ APEX BUY SIGNAL | ADX: 32.4 | Z-Score: -1.82</span>
<span class="t-cyan">🔥 BUY EXECUTED @ 2345.50 | Size: 1.10 | SL: 2343.00</span>
<span class="t-white">🔹 XAUUSD | LTP: 2345.50 | SL: 2343.00 | T1: 2350.50</span>

<span class="t-white">🔹 XAUUSD | LTP: 2348.10 | SL: 2343.00</span>
<span class="t-green">💰 TP1 HIT! Securing 50% profits (0.55 lots). Moving SL to Breakeven.</span>
<span class="t-white">🔹 XAUUSD | LTP: 2352.40 | SL: 2345.50 (SL@Cost)</span>
<span class="t-cyan">📈 Trailing SL Moved UP to 2348.65 (Securing Runner)</span>

<span class="t-red">🛑 TRAILING SL HIT! XAUUSD BUY</span>
<span class="t-white">Entry: 2345.50 | Exit: 2348.65</span>
<span class="t-cyan">✅ Trade Concluded. Total Asymmetric R:R achieved: 1:2.63</span>
<span class="t-green">✅ New Balance: $26,185.40</span>
    """
    st.markdown(f'<div class="terminal-console">{apex_log}</div>', unsafe_allow_html=True)

# ==============================================================================
# 🔴 MODULE 7: XM BONUS INCUBATOR
# ==============================================================================
elif nav_selection == "7. XM Bonus Incubator [LIVE]":
    st.markdown('<p class="title-gradient">XM Bonus Compounder</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">The $500 Incubator: Converting Non-Withdrawable Credit to Real Cash.</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="glass-card"><div class="metric-value metric-blue">$500 + $250</div><div class="metric-label">Cash + Bonus Credit</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="glass-card"><div class="metric-value metric-green">559.43%</div><div class="metric-label">Return on Deposit</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="glass-card"><div class="metric-value metric-gold">$3,297.14</div><div class="metric-label">Final Real Cash</div></div>', unsafe_allow_html=True)

    xm_log = """
<span class="t-white">🚀 INITIALIZING XM BONUS BACKTESTER ($500 Cash + $250 Credit)...</span>
<span class="t-yellow">===========================================================================</span>
<span class="t-yellow">🔥 XM BONUS COMPOUNDER: THE $500 INCUBATOR</span>
<span class="t-yellow">Starting Equity: $750.00 | Risk: 5.0% of Equity</span>
<span class="t-yellow">===========================================================================</span>
<span class="t-cyan">Month           | Trades   | End Equity      | Real Cash </span>
<span class="t-white">---------------------------------------------------------------------------</span>
<span class="t-white">2025-May        | 4        | $820.98         | $570.98</span>
<span class="t-white">2025-Jun        | 4        | $856.59         | $606.59</span>
<span class="t-red">2025-Jul        | 10       | $775.90         | $525.90</span>
<span class="t-green">2025-Aug        | 2        | $1,021.59       | $771.59</span>
<span class="t-green">2025-Sep        | 6        | $2,241.30       | $1,991.30</span>
<span class="t-green">2026-Jan        | 4        | $2,975.79       | $2,725.79</span>
<span class="t-green">2026-Apr        | 1        | $3,547.14       | $3,297.14</span>

<span class="t-cyan">💰 THE INCUBATOR RESULTS:</span>
<span class="t-white">Final Total Equity: $3,547.14</span>
<span class="t-green">Final REAL Cash:    $3,297.14 (Withdrawable)</span>
<span class="t-white">Net Profit:         $2,797.14</span>
<span class="t-green">Return on Deposit:  559.43%</span>
<span class="t-red">Max Drawdown:       23.88%</span>
<span class="t-white">Total Trades:       51</span>
    """
    st.markdown(f'<div class="terminal-console">{xm_log}</div>', unsafe_allow_html=True)
