import streamlit as st
import random

st.title("🎮 阪大文系数学ゲーム（整数）")

# 問題ID保持
if "problem" not in st.session_state:
    st.session_state.problem = random.choice([1, 2, 3])

if "step" not in st.session_state:
    st.session_state.step = 0

def next_step(n):
    st.session_state.step = n
    st.rerun()

def reset():
    st.session_state.problem = random.choice([1, 2, 3])
    st.session_state.step = 0
    st.rerun()

# ====================
# 問題1（偶奇）
# ====================
def problem1():
    st.write("【問題】")
    st.write("正の整数 n に対して n(n+1) が偶数であることを示せ。")

    if st.session_state.step == 0:
        st.write("どこに注目する？")
        if st.button("展開する"):
            st.error("❌ 本質が見えにくい")
        if st.button("偶奇に注目する"):
            st.success("✅ 正解！")
            next_step(1)
        if st.button("具体例を試す"):
            st.error("❌ 弱い")

    elif st.session_state.step == 1:
        st.write("どんな事実を使う？")
        if st.button("連続する2整数は一方が偶数"):
            st.success("✅ 正解！")
            next_step(2)
        if st.button("平方数"):
            st.error("❌ 関係ない")

    elif st.session_state.step == 2:
        st.write("結論は？")
        if st.button("必ず偶数になる"):
            st.success("🎉 クリア！")
        if st.button("奇数もある"):
            st.error("❌ 違う")

# ====================
# 問題2（合同式）
# ====================
def problem2():
    st.write("【問題】")
    st.write("n^2 ≡ 0 (mod 4) なら n は偶数であることを示せ。")

    if st.session_state.step == 0:
        st.write("どう考える？")
        if st.button("偶奇で場合分け"):
            st.success("✅ 正解！")
            next_step(1)
        if st.button("平方根"):
            st.error("❌ 不適切")

    elif st.session_state.step == 1:
        st.write("奇数の場合？")
        if st.button("1になる"):
            st.success("✅ 正解！")
            next_step(2)
        if st.button("0になる"):
            st.error("❌ 違う")

    elif st.session_state.step == 2:
        st.write("結論は？")
        if st.button("偶数"):
            st.success("🎉 クリア！")
        if st.button("わからない"):
            st.error("❌")

# ====================
# 問題3（互いに素）
# ====================
def problem3():
    st.write("【問題】")
    st.write("ax + by = 1 を満たすとき a と b は互いに素であることを示せ。")

    if st.session_state.step == 0:
        st.write("何に注目？")
        if st.button("最大公約数"):
            st.success("✅ 正解！")
            next_step(1)
        if st.button("グラフ"):
            st.error("❌ 不要")

    elif st.session_state.step == 1:
        st.write("どう使う？")
        if st.button("共通の約数は1のみ"):
            st.success("✅ 正解！")
            next_step(2)
        if st.button("偶奇"):
            st.error("❌")

    elif st.session_state.step == 2:
        st.write("結論は？")
        if st.button("互いに素"):
            st.success("🎉 クリア！")
        if st.button("不明"):
            st.error("❌")

# ====================
# 出題
# ====================
if st.session_state.problem == 1:
    problem1()
elif st.session_state.problem == 2:
    problem2()
else:
    problem3()

st.write("---")
if st.button("🔄 次の問題"):
    reset()
