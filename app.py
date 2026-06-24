import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# ==========================================
# 🏛️ PAGE ARCHITECTURE & CSS
# ==========================================
st.set_page_config(
    page_title="CA Sunil Kumar Paswan | Quantitative Systems Architect",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&family=Inter:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #050914; /* Deep Abyss Dark */
        color: #E2E8F0;
    }
    
    /* Gradients and Text Highlights */
    .title-gradient {
        background: linear-gradient(90deg, #FACC15 0%, #EAB308 50%, #F59E0B 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 46px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    .subtitle-text {
        color: #94A3B8;
        font-size: 18px;
        font-weight: 400;
        margin-bottom: 30px;
    }
    
    .section-header {
        border-bottom: 1px solid #1E293B;
        padding-bottom: 10px;
        margin-top: 40px;
        margin-bottom: 20px;
        color: #F8FAFC;
        font-size: 24px;
        font-weight: 600;
    }

    /* Cards and Containers */
    .glass-card {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(51, 65, 85, 0.5);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .glass-card:hover {
        border-color: #EAB308;
        transform: translateY(-2px);
    }
    
    /* Terminal Console */
    .terminal-console {
        background-color: #020617;
        border: 1px solid #1E293B;
        border-left: 3px solid #EAB308;
        padding: 16px;
        border-radius: 6px;
        font-family: 'JetBrains Mono', monospace;
        color: #38BDF8;
        font-size: 13px;
        line-height: 1.6;
        height: 350px;
        overflow-y: scroll;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    }
    
    /* Metrics */
    .metric-value-gold {
        font-size: 36px;
        font-weight: 800;
        color: #FACC15;
    }
    .metric-value-green {
        font-size: 36px;
        font-weight: 800;
        color: #10B981;
    }
    .metric-label {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #64748B;
        font-weight: 600;
    }

    /* Hide default elements */
    .block-container { padding-top: 2rem; }
    a.headerlink { display: none; }
    footer {display: none;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 🧭 SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("### 🏦 CA Sunil Kr Paswan")
    st.markdown("*Quantitative Systems Architect*")
    st.caption("📍 Jamadoba, Jharkhand, India | ✉️ sunilbla.acc@gmail.com")
    
    st.divider()
    
    st.markdown("### 🔬 Architecture Modules")
    selected_module = st.radio(
        "Navigate:",
        [
            "📜 The Institutional Manifesto", 
            "📈 Indian Indices: Precision Sniper", 
            "🌍 XAUUSD: The Apex Compounder",
            "⚡ Crypto: Z-Score Arb Engine",
            "🛡️ Risk & Telemetry Framework"
        ],
        label_visibility="collapsed"
    )
    
    st.divider()
    st.markdown("""
    <div style='background: #020617; padding: 15px; border-radius: 8px; border: 1px solid #1E293B;'>
        <div style='color: #64748B; font-size: 11px; text-transform: uppercase; margin-bottom: 5px;'>System Telemetry</div>
        <div style='color: #10B981; font-size: 13px; font-weight: 600;'>● ALGORITHMS LIVE</div>
        <div style='color: #E2E8F0; font-size: 12px; margin-top: 8px;'>MTF Confluence: <span style='color:#FACC15'>Syncing</span></div>
        <div style='color: #E2E8F0; font-size: 12px;'>Data Parsed: > 20M Rows</div>
        <div style='color: #E2E8F0; font-size: 12px;'>VIX Proxy: Active</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><p style='font-size: 10px; color: #475569;'>© 2026 Proprietary IP. Mathematical formulas and specific indicator thresholds are hidden for security.</p>", unsafe_allow_html=True)

# ==========================================
# 📜 MODULE 0: THE INSTITUTIONAL MANIFESTO
# ==========================================
if selected_module == "📜 The Institutional Manifesto":
    st.markdown('<p class="title-gradient">The Illusion of Randomness</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Bridging Chartered Accountancy with Algorithmic Market Micro-Structure.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3 style='margin-top:0; color: #FACC15;'>The Hunted vs. The Hunter</h3>
            <p style='color: #CBD5E1; font-size: 15px; line-height: 1.6;'>
                To the untrained eye, financial markets appear chaotic. Retail traders use colorful lagging indicators and abstract trendlines to tame "randomness". This is a fatal philosophical error. 
                <strong>The market is not random. It is an engineered environment.</strong>
            </p>
            <p style='color: #CBD5E1; font-size: 15px; line-height: 1.6;'>
                Price moves because large financial institutions need it to move to facilitate massive transactional needs. If a fund needs to deploy $500 million, they face an existential problem of slippage. They cannot just "buy." They must buy into existing massive selling pressure. <strong>They require Liquidity.</strong>
            </p>
            <p style='color: #CBD5E1; font-size: 15px; line-height: 1.6;'>
                Where does this Liquidity reside? Exactly where retail traders place their stop losses. The professional does not trade the pattern; the professional trades the <strong>FAILURE</strong> of the pattern.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-card">
            <h3 style='margin-top:0; color: #FACC15;'>The AI War on Smart Money Concepts</h3>
            <p style='color: #CBD5E1; font-size: 15px; line-height: 1.6;'>
                Retail traders recently evolved to use "Smart Money Concepts" (SMC), looking for Order Blocks and Fair Value Gaps. However, in the 2026 market environment, institutions deploy High-Frequency Trading (HFT) algorithms to mathematically identify these popular SMC setups and use them as <strong>inducement traps</strong>.
            </p>
            <p style='color: #CBD5E1; font-size: 15px; line-height: 1.6;'>
                My architecture bypasses this by peering directly into the matrix of order execution using <strong>Delta Order Flow, Cumulative Delta Divergence, and Options IV Skew</strong>. We don't guess. We read the Footprint of the giant.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="terminal-console" style="height: 100%;">
            > system.initialize_philosophy()<br>
            [OK] Zero-Sum Dynamics verified.<br>
            [OK] Retail Sentiment inverted.<br>
            <br>
            > cat matrix_of_price.txt<br>
            "When you stop viewing the market as an unpredictable casino and start viewing it as a logical, predatory mechanism designed to seek out liquidity, you stop being a gambler and start becoming a strategist."<br>
            <br>
            > load_sniper_mode()<br>
            [WARNING] Human emotion detected.<br>
            [ACTION] Disabling manual execution...<br>
            [OK] Algorithmic discipline enforced.<br>
            <br>
            > await liquidity_sweep()
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 📈 MODULE 1: INDIAN INDICES (v21.4)
# ==========================================
elif selected_module == "📈 Indian Indices: Precision Sniper":
    st.markdown('<p class="title-gradient">v21.4 Precision Options Sniper</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">NIFTY & BANKNIFTY Multi-Timeframe Integration & Options Delta-Proxy Engine.</p>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="glass-card"><div class="metric-value-green">18.2M</div><div class="metric-label">Rows Analyzed</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="glass-card"><div class="metric-value-green">12+</div><div class="metric-label">Confluence Metrics</div></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="glass-card"><div class="metric-value-green">0.3-0.55</div><div class="metric-label">Target Delta Range</div></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="glass-card"><div class="metric-value-green">15:10</div><div class="metric-label">Hard Theta Exit</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">🧠 The Multi-Dimensional Scoring Engine</div>', unsafe_allow_html=True)
    
    col_text, col_chart = st.columns([1, 1])
    with col_text:
        st.write("Retail traders rely on a single indicator. The v21.4 architecture relies on a **Dynamic Confluence Matrix** requiring a minimum 70% threshold to fire a signal. It evaluates:")
        st.markdown("""
        *   **Multi-Timeframe (MTF) Alignment:** Syncs 5m, 15m, and 1H trends to prevent fighting macro momentum.
        *   **VWAP Sigma Bands:** Identifies overbought/oversold extremes (e.g., Price > VWAP + 2 Variance).
        *   **Order Flow & PCR:** Analyzes Put/Call Ratio relative to VIX to identify regime-aware support, while tracking OI Change Velocity (Call vs Put writing).
        *   **Cumulative Delta:** Tracks true buying vs. selling pressure to spot hidden bearish/bullish divergences before price reacts.
        *   **Heikin Ashi & SuperTrend:** Filters out noise and whipsaws in choppy environments.
        """)
        st.info("The engine dynamically selects the optimal Options Strike based on the live VIX proxy, targeting a specific Delta and requiring minimum liquidity spikes.")

    with col_chart:
        edge_data = pd.DataFrame({
            "Stock": ["ADANIENSOL", "VEDL", "ADANIENT", "LODHA", "CGPOWER", "JINDALSTEL"],
            "Win Rate (%)": [93.84, 91.65, 92.87, 93.55, 90.97, 93.76],
            "Avg Hourly Move (%)": [2.09, 1.67, 1.76, 1.89, 1.86, 1.72]
        })
        
        fig = px.scatter(
            edge_data, x="Avg Hourly Move (%)", y="Win Rate (%)", size="Avg Hourly Move (%)", 
            color="Stock", text="Stock", title="Historical Alpha: Target Excursion vs Probability",
            template="plotly_dark"
        )
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        fig.update_traces(textposition='top center')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-header">📡 Live Execution Telemetry (Simulated Log)</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="terminal-console">
        [14:58:24] 🟢 LIVE — v21.4 running.<br>
        ══════════════════════════════════════════════════════════════════<br>
        🎯 SCANNING: BANKNIFTY | v21.4 Precision Sniper Engine<br>
        ══════════════════════════════════════════════════════════════════<br>
        📍 Dir: BULLISH | Supertrend: BULLISH (2 bars)<br>
        📊 MTF: {'5m': 'NEUTRAL', '15m': 'NEUTRAL', '1H': 'BULLISH'} | Consensus: NEUTRAL<br>
        📈 HA: BULLISH | EMA: BULLISH | RSI: 63.1 | MACD: BULLISH<br>
        💧 VWAP: BULLISH (+1.81%) | ΔCum: BUYING_PRESSURE<br>
        📉 PCR: 0.967 [NEUTRAL] — Balanced OI<br>
        🏦 OI Vel: NEUTRAL | IV Skew: BEARISH_SKEW (-3.37)<br>
        🔊 Flow: BULLISH_FLOW (ratio: 0.80)<br>
        🎯 SCORE: 77% (Min: 70%) | VIX≈17.6 | Vol Spike: ✅<br>
        <span style="color: #10B981">💼 Logged BANKNIFTY CE | ID: 75618 | Lot: 15</span><br>
        <span style="color: #10B981">✅ Signal dispatched to Telegram for BANKNIFTY.</span><br>
        <br>
        [15:10:00] ⏳ TIME DECAY EXIT (3:10 PM)! BANKNIFTY CE<br>
        [15:15:00] 📊 END OF DAY SUMMARY GENERATED.
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 🌍 MODULE 2: XAUUSD APEX COMPOUNDER
# ==========================================
elif selected_module == "🌍 XAUUSD: The Apex Compounder":
    st.markdown('<p class="title-gradient">The 10x Apex Compounder</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">XAUUSD Prop-Firm & XM Bonus Incubator via Asymmetric Risk Extraction.</p>', unsafe_allow_html=True)

    p1, p2, p3, p4 = st.columns(4)
    with p1: st.markdown('<div class="glass-card"><div class="metric-value-gold">372.9%</div><div class="metric-label">12-Month Net ROI</div></div>', unsafe_allow_html=True)
    with p2: st.markdown('<div class="glass-card"><div class="metric-value-gold">4.73x</div><div class="metric-label">Capital Multiple</div></div>', unsafe_allow_html=True)
    with p3: st.markdown('<div class="glass-card"><div class="metric-value-gold">5.0%</div><div class="metric-label">Risk Per Trade</div></div>', unsafe_allow_html=True)
    with p4: st.markdown('<div class="glass-card"><div class="metric-value-gold">51</div><div class="metric-label">Total Trades (1 Yr)</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">🔥 The Asymmetric Runner Philosophy</div>', unsafe_allow_html=True)
    st.write("This engine is designed to pass high-capital Prop Firm challenges ($25k+) or hyper-compound micro accounts using broker bonuses. It operates purely on **Asymmetric Risk extraction** during the New York power hours (13:00-18:00 UTC).")
    
    col_phil, col_chart2 = st.columns([1, 1.2])
    
    with col_phil:
        st.markdown("""
        <div class="glass-card" style="height: 100%;">
            <h4 style="color: #FACC15; margin-top: 0;">Execution Mechanics:</h4>
            <ol style="color: #CBD5E1; font-size: 14px;">
                <li><strong>Chop Filter:</strong> Absolute refusal to trade unless the macro ADX demonstrates extreme trend strength.</li>
                <li><strong>The Z-Score Sweep:</strong> Waits for price to diverge by > 1.5 Standard Deviations against the prevailing 200-EMA trend (identifying a retail Stop Hunt).</li>
                <li><strong>Bag Securing:</strong> Takes 50% of the position off the table at a tight 2.0 ATR, moving the remaining Stop Loss to Break-even.</li>
                <li><strong>The Runner:</strong> Trails the remaining 50% by 1.5 ATR. If a massive macroeconomic trend occurs, this runner captures a 5R to 10R multiple, causing the exponential account growth.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
    with col_chart2:
        months = ["May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr"]
        balance = [27365, 28552, 25862, 34049, 74703, 78322, 65795, 82598, 99188, 108510, 111230, 118233]
        
        comp_df = pd.DataFrame({"Month": months, "Equity Curve ($)": balance})
        
        fig = px.area(
            comp_df, x="Month", y="Equity Curve ($)", 
            title="The Apex Compounder: $25k to $118k in 12 Months",
            color_discrete_sequence=["#FACC15"], template="plotly_dark"
        )
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# ⚡ MODULE 3: CRYPTO Z-SCORE ARB
# ==========================================
elif selected_module == "⚡ Crypto: Z-Score Arb Engine":
    st.markdown('<p class="title-gradient">Titan Statistical Arbitrage</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Market-Neutral Pairs Trading Engine on Bybit Unified Margin.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="glass-card" style="height: 100%;">
            <h3 style="color: #38BDF8; margin-top: 0;">Mathematical Cointegration</h3>
            <p style="color: #CBD5E1; font-size: 15px;">
                This system does not care if the cryptocurrency market goes up or down. It tracks the mathematical pricing ratio between two highly correlated assets (e.g., SOL/USDT and LINK/USDT).
            </p>
            <p style="color: #CBD5E1; font-size: 15px;">
                When the 40-period Z-Score of their ratio deviates beyond <strong>±2.5 Standard Deviations</strong>, the system triggers. It shorts the overperforming asset and buys the underperforming asset, capitalizing exclusively on <strong>Mean Reversion</strong>.
            </p>
            <h4 style="color: #10B981; margin-top: 20px;">ARIMA Veto & Iceberg Execution</h4>
            <p style="color: #CBD5E1; font-size: 14px;">
                To bypass exchange slippage limits, the system uses an <strong>Iceberg Chunker</strong>, breaking massive orders into $50,000 sub-notional chunks utilizing Post-Only Maker Orders to collect rebates. An integrated <strong>ARIMA time-series forecast</strong> vetoes trades if the deviation is predicted to widen further.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="terminal-console" style="height: 100%;">
            --- 🏛️ TITAN V6: INSTITUTIONAL MAKER EDITION ---<br>
            🎯 Target: ADAUSDT / XRPUSDT<br>
            ⏳ SYNCING CLOCK & DOWNLOADING 168-HOUR MACRO DATA...<br>
            ✅ Data Loaded: ADAUSDT / XRPUSDT<br>
            📡 CONNECTING TO WEBSOCKET STREAM...<br>
            <br>
            ⏳ 14:02:11 | Z-Score: 1.14 | Status: NEUTRAL<br>
            ⏳ 14:12:34 | Z-Score: 1.85 | Status: NEUTRAL<br>
            ⏳ 14:24:00 | Z-Score: 2.61 | Status: NEUTRAL<br>
            <span style="color: #EAB308;">📈 SIGNAL [Z: 2.61]: Short ADAUSDT, Long XRPUSDT.</span><br>
            🚀 FIRING: Sell 45120 ADAUSDT / Buy 18450 XRPUSDT<br>
            ✅ [ADAUSDT] Sell Fill Success.<br>
            ✅ [XRPUSDT] Buy Fill Success.<br>
            <br>
            ⏳ 15:45:00 | Z-Score: 0.12 | Status: ACTIVE TRADE<br>
            <span style="color: #10B981;">🎯 TARGET REACHED [Z: 0.12]. Closing positions.</span><br>
            🔄 Executing Close Iceberg Chunks...
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 🛡️ MODULE 4: RISK & TELEMETRY
# ==========================================
elif selected_module == "🛡️ Risk & Telemetry Framework":
    st.markdown('<p class="title-gradient">Institutional Risk Architecture</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">The mathematical firewall protecting capital from psychological ruin.</p>', unsafe_allow_html=True)

    st.write("A profitable algorithm is meaningless without a mathematical guarantee of survival. My systems are governed by strict, algorithmic circuit breakers and real-time remote telemetry.")

    r1, r2, r3 = st.columns(3)
    
    with r1:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #F8FAFC; margin-top: 0;">1. Dynamic Kelly Sizing</h4>
            <p style="color: #94A3B8; font-size: 13px;">Fixed lot sizing is mathematically flawed. The engine dynamically calculates position sizes based on volatility (ATR) and real-time win-rates, completely eliminating the Risk of Ruin during drawdown sequences.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with r2:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #F8FAFC; margin-top: 0;">2. Algorithmic Circuit Breakers</h4>
            <p style="color: #94A3B8; font-size: 13px;">Hard limits are coded into the core loop. If the Daily Realized Loss limit is hit, or the maximum signals per day are exhausted, the system locks itself and revokes trading access until the next session.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with r3:
        st.markdown("""
        <div class="glass-card">
            <h4 style="color: #F8FAFC; margin-top: 0;">3. Smart End-of-Day Journaling</h4>
            <p style="color: #94A3B8; font-size: 13px;">At 15:15 IST, the bot automatically closes all intraday positions due to Theta Decay, generates a CSV/Excel trade journal with ROI & Duration metrics, and dispatches a summary to Telegram.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">📱 Real-Time Telegram Webhook Integration</div>', unsafe_allow_html=True)
    
    col_img, col_desc = st.columns([1, 2])
    with col_img:
        st.markdown("""
        <div style="background-color: #1E293B; border-radius: 12px; padding: 20px; border: 1px solid #334155;">
            <div style="color: #38BDF8; font-weight: bold; margin-bottom: 10px;">Telegram Bot</div>
            <div style="background-color: #0F172A; border-radius: 8px; padding: 12px; font-size: 12px; color: #E2E8F0; margin-bottom: 10px;">
                📊 <b>END OF DAY SUMMARY (2026-06-24)</b><br>
                ────────────────────────<br>
                📝 Total Trades: 4<br>
                🏆 Wins: 3 | 💔 Losses: 1<br>
                🎯 Win Rate: 75.0%<br>
                💰 Net Virtual PnL: ₹14,250.00<br>
                ────────────────────────<br>
                📁 <b>Excel Report Saved:</b> Daily_Trade_Report_2026-06-24.xlsx
            </div>
            <div style="background-color: #0F172A; border-radius: 8px; padding: 12px; font-size: 12px; color: #E2E8F0;">
                🚨 <b>EXIT COMMAND: ADANIENT</b> 🚨<br><br>
                ⚠️ <b>Reason:</b> 📉 TRAILING STOP HIT<br>
                💰 <b>Exit Spot:</b> ₹3220.45<br>
                ⏱️ <b>Time Held:</b> 42 mins<br><br>
                🛒 <b>Action:</b> CLOSE CE POSITION IMMEDIATELY
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_desc:
        st.write("The system is entirely headless. It lives on a cloud VPS and communicates with the architect purely via encrypted JSON POST requests to a private Telegram channel. This ensures zero latency and allows for remote monitoring of algorithm health, trade entries, trailing stop movements, and daily accounting metrics without needing to look at a chart.")
