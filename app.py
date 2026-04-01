import streamlit as st

st.title("🎮 阪大文系数学ゲーム（整数・合同式）")

if "step" not in st.session_state:
    st.session_state.step = 0

st.write("【問題】")
st.write("整数 n に対して、n^2 ≡ 0 (mod 4) ならば n は偶数であることを示せ。")

def next_step(n):
    st.session_state.step = n
    st.rerun()

def step1():
    st.write("どう考える？")
    if st.button("具体例を試す"):
        st.error("❌ 方針として弱い")
    if st.button("偶奇で場合分けする"):
        st.success("✅ 正解！")
        next_step(1)
    if st.button("平方根を取る"):
        st.error("❌ 一般にはできない")

def step2():
    st.write("n が奇数の場合どうなる？")
    if st.button("n^2 ≡ 1 (mod 4) になる"):
        st.success("✅ 正解！")
        next_step(2)
    if st.button("n^2 ≡ 0 (mod 4)"):
        st.error("❌ 奇数の平方は1になる")
    if st.button("バラバラ"):
        st.error("❌ 規則性がある")

def step3():
    st.write("結論は？")
    if st.button("n は偶数である"):
        st.success("🎉 クリア！")
        st.write("【解説】")
        st.write("n が奇数なら n = 2k+1 と書ける。")
        st.write("(2k+1)^2 = 4k(k+1)+1 ≡ 1 (mod 4)")
        st.write("したがって n^2 ≡ 0 (mod 4) なら n は偶数。")
    if st.button("奇数の可能性もある"):
        st.error("❌ 矛盾する")

if st.session_state.step == 0:
    step1()
elif st.session_state.step == 1:
    step2()
elif st.session_state.step == 2:
    step3()