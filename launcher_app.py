import streamlit as st

# --- ページ基本設定 ---
st.set_page_config(
    page_title="🌏 Planetary Wellness | アプリランチャー",
    page_icon="🌏",
    layout="wide"
)

# ---------------------------
# 🪐 ヘッダー（ロゴ + タイトル）
# ---------------------------
header_col1, header_col2 = st.columns([1, 9])  # 左に少し、右に広く

with header_col1:
    st.image("planet.png", width=90)  # ← ロゴが左上に表示される

with header_col2:
    st.title("Planetary Wellness アプリ選択メニュー")
    st.write("ご利用になるアプリを選択してください👇")

st.write("---")  # 区切り線

# ---------------------------
# アプリの2カラムレイアウト
# ---------------------------
col1, col2 = st.columns(2, gap="large")

# --- 不登校・ひきこもり相談エージェント ---
with col1:
    st.subheader("📘 不登校・ひきこもり相談エージェント")
    st.image("hikikomori_logo.png", use_column_width=True)
    st.link_button(
        "👉 アプリを開く",
        "https://hikikomorichatbot-planetarywellnessdvmweppwl7zaknee.streamlit.app/"
    )

# --- 発達支援相談エージェント ---
with col2:
    st.subheader("🧩 発達支援相談エージェント")
    st.image("hattatsu_logo.png", use_column_width=True)
    st.link_button(
        "👉 アプリを開く",
        "https://hattatsu-support-ai-bpr6um2plg4gj28qqczgos.streamlit.app/"
    )

st.write("---")
st.caption("© 2025 Planetary Wellness / Developed by TM,TN,IY")