import streamlit as st

# --- ページ基本設定 ---
st.set_page_config(
    page_title="🌏 Planetary Wellness | アプリランチャー",
    page_icon="🌏",
    layout="wide"
)

# --- タイトル ---
st.title("🌏 Planetary Wellness アプリ選択メニュー")
st.write("ご利用になるアプリを選択してください👇")

# --- 2カラムレイアウト ---
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

# --- フッター ---
st.write("---")
st.caption("© 2025 Planetary Wellness / Developed by Takuya Mori")
