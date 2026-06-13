import streamlit as st

st.html('<script async src="https://www.googletagmanager.com/gtag/js?id=G-8D12RTXDHZ"></script><script>window.dataLayer = window.dataLayer || [];def gtag(){dataLayer.push(arguments);}gtag("js", new Date());gtag("config", "G-8D12RTXDHZ");</script>')

st.title("📅 地元イベント情報 & ブログ")

tab1, tab2 = st.tabs(["イベント情報", "ブログ"])

with tab1:
    st.header("今後のイベント予定")
    st.subheader("📢 夏祭り 2026")
    st.write("日時：2026年8月15日")
    st.write("場所：中央公園")
    if st.button("参加登録する"):
        st.success("登録が完了しました！")

with tab2:
    st.header("管理人ブログ")
    st.markdown("### PythonでWebサイトを作ってみた")
    st.write("2026年6月13日 投稿")
    st.write("iPadとPythonだけでサイトが作れました。")
