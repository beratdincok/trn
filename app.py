import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta


# =============================================================================
# SAYFA AYARLARI VE KURUMSAL TASARIM
# =============================================================================
st.set_page_config(
    page_title="İstasyon TRN Takip Portalı",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    :root {
        --navy:#05164D; --yellow:#FFAC00; --bg:#F4F6F9; --white:#FFFFFF;
        --green:#16845B; --red:#C93F49; --text:#18243D; --muted:#738096;
    }
    html, body, [class*="css"] { font-family:'Inter',sans-serif; }
    .stApp { background:var(--bg); color:var(--text); }
    .block-container { max-width:1450px; padding-top:1.35rem; padding-bottom:3rem; }
    #MainMenu, footer { visibility:hidden; }
    .hero { background:linear-gradient(125deg,#05164D 0%,#0A2B70 72%,#153A83 100%);
        border-radius:18px; padding:24px 28px; color:white; margin-bottom:18px;
        box-shadow:0 12px 30px rgba(5,22,77,.18); position:relative; overflow:hidden; }
    .hero:after { content:""; position:absolute; width:180px; height:180px;
        border:30px solid rgba(255,172,0,.14); border-radius:50%; right:-55px; top:-76px; }
    .hero-row { display:flex; gap:17px; align-items:center; position:relative; z-index:2; }
    .brand-badge { width:58px; height:58px; min-width:58px; border-radius:50%;
        display:flex; align-items:center; justify-content:center; background:var(--yellow);
        color:var(--navy); font-size:28px; box-shadow:0 5px 16px rgba(0,0,0,.18); }
    .hero h1 { margin:0; font-size:clamp(1.35rem,3vw,2.15rem); letter-spacing:-.03em; }
    .hero p { margin:6px 0 0; opacity:.82; font-size:.92rem; }
    .login-wrap { max-width:760px; margin:16px auto 0; }
    .login-shell { background:linear-gradient(145deg,#FFFFFF 0%,#F7F9FD 100%);
        border:1px solid #DFE6F0; border-radius:20px; padding:24px;
        box-shadow:0 18px 48px rgba(5,22,77,.11); margin-bottom:14px; }
    .login-intro { display:grid; grid-template-columns:1.35fr .65fr; gap:18px;
        align-items:center; margin-bottom:18px; }
    .login-title { color:var(--navy); font-size:1.35rem; font-weight:850; line-height:1.25; }
    .login-copy { color:#6C788D; font-size:.84rem; margin-top:7px; line-height:1.6; }
    .login-shield { width:74px; height:74px; margin-left:auto; border-radius:20px;
        display:flex; align-items:center; justify-content:center; font-size:34px;
        color:var(--navy); background:linear-gradient(145deg,#FFBE35,#FFAC00);
        box-shadow:0 9px 22px rgba(255,172,0,.25); }
    .feature-row { display:grid; grid-template-columns:repeat(3,1fr); gap:9px; margin:12px 0 18px; }
    .feature-chip { background:#F1F4FA; color:#43516B; border-radius:10px; padding:9px;
        font-size:.72rem; font-weight:700; text-align:center; border:1px solid #E5EAF2; }
    div[data-testid="stForm"] { background:white; border:1px solid #E4E9F0; border-radius:14px;
        padding:18px; box-shadow:0 5px 18px rgba(15,33,65,.06); }
    .eyebrow { color:#8C6500; font-size:.72rem; font-weight:800; letter-spacing:.08em;
        text-transform:uppercase; margin-bottom:5px; }
    .section-title { color:var(--navy); font-size:1.12rem; font-weight:800; margin:18px 0 10px; }
    .subtle { color:var(--muted); font-size:.8rem; }
    .metric-card { background:white; border-radius:14px; padding:17px 18px; min-height:120px;
        box-shadow:0 5px 18px rgba(15,33,65,.07); border-top:4px solid var(--accent); }
    .metric-label { color:#697386; font-size:.75rem; font-weight:700; text-transform:uppercase;
        letter-spacing:.05em; min-height:35px; }
    .metric-value { color:var(--navy); font-size:1.9rem; font-weight:800; margin-top:7px; }
    .metric-note { color:#8B95A7; font-size:.72rem; }
    .info-card { background:white; border:1px solid #E5EAF0; border-radius:13px;
        padding:15px 17px; box-shadow:0 3px 12px rgba(20,33,61,.05); height:100%; }
    .info-label { color:#8893A4; font-size:.69rem; text-transform:uppercase; font-weight:800; }
    .info-value { color:var(--navy); font-size:1rem; font-weight:750; margin-top:3px; }
    .demo-box { background:#FFF8E5; border:1px solid #F0D58C; border-radius:10px;
        padding:11px 13px; color:#68501B; font-size:.78rem; }
    .hint { background:#EDF3FF; border-left:4px solid #315AAB; border-radius:8px;
        padding:10px 13px; color:#2A3D65; font-size:.82rem; }
    .audit-note { background:#fff; border:1px solid #E5E9EF; border-radius:11px;
        padding:12px 14px; margin:7px 0; }
    .evaluation-card { background:#FFFFFF; border:1px solid #E2E7EF; border-radius:16px;
        padding:18px; margin:8px 0 14px; box-shadow:0 7px 22px rgba(12,31,71,.07);
        position:relative; overflow:hidden; min-height:305px; }
    .evaluation-card:before { content:""; position:absolute; left:0; top:0; bottom:0;
        width:5px; background:var(--card-accent,#315AAB); }
    .evaluation-head { display:flex; justify-content:space-between; align-items:flex-start;
        gap:10px; padding-left:3px; }
    .evaluation-name { color:var(--navy); font-size:1.02rem; font-weight:850; }
    .evaluation-id { color:#8993A3; font-size:.69rem; margin-top:3px; }
    .score-circle { width:46px; height:46px; min-width:46px; border-radius:50%;
        display:flex; align-items:center; justify-content:center; color:white;
        background:var(--card-accent,#315AAB); font-weight:850; font-size:1rem; }
    .flight-band { display:flex; justify-content:space-between; align-items:center; gap:8px;
        background:#F3F6FB; border-radius:10px; padding:10px 11px; margin:14px 0 12px;
        color:#243651; font-weight:750; font-size:.77rem; }
    .evaluation-grid { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:12px; }
    .evaluation-label { color:#929CAB; font-size:.63rem; font-weight:800;
        text-transform:uppercase; letter-spacing:.04em; }
    .evaluation-value { color:#334058; font-size:.76rem; font-weight:650; margin-top:2px; }
    .note-box { background:#F8FAFD; border-radius:9px; padding:10px 11px; margin-top:8px;
        color:#46536A; font-size:.75rem; line-height:1.45; border:1px solid #EDF0F5; }
