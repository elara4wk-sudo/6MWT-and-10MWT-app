import streamlit as st
import pandas as pd

st.set_page_config(page_icon =(":walking_woman:"))

st.title("行走能力測試計算 :abacus: ")
st.divider()
st.subheader("10公尺行走測試(10MWT)")

st.image("./images/10MWT.png", caption = "測試示意圖")

st.write(":round_pushpin: 臨床評估使用可快速掌握個體短距離步行能力、有無跌倒風險等。")
st.write(":round_pushpin: 受測者要走完10公尺，但只會計算中間6公尺的秒數。需測試 2~3 次，然後算出平均。")
st.write(":round_pushpin: 最後的速度會用每秒幾公尺(m/s)記錄。")
st.divider()

# times = [
#     st.number_input(
#         f"請輸入您的第 {i} 次行走秒數 (s):",
#         key = f"test_{i}_input",
#         format="%.2f"
#     )
#     for i in range(1, 3)
# ]

# t3 = st.number_input(
#     "請輸入您的第 3 次行走秒數 (s):", 
#     key = "t3_input",
#     value = 0.0,
#     placeholder= "若僅測兩次可留空或輸入0"
# )

# calculate_button = st.button(label = "計算", key = "calculate_button")

# if calculate_button:
#     # 判斷 t3 是否有效（非 0）
#     valid_times = times.copy()
#     if t3 > 0:
#         valid_times.append(t3)

#     # 計算平均
#     avg_time = sum(valid_times) / len(valid_times)

#     # 行走速度（6 公尺）
#     speed = 6/avg_time
#     speed = round(speed,2)
#     # st.write(f":heavy_check_mark: 您的走路速度為 **:red[{speed} 公尺/秒]**")

times = [st.number_input(f"請輸入您的第{i+1}次測試秒數:", min_value=0.0, step=0.1, key=f"time{i}") for i in range(3)]

calculate_button = st.button(label="計算", key="calculate_button")

if calculate_button:
    # 過濾掉 0 秒的無效輸入
    valid_times = [t for t in times if t > 0]

    if len(valid_times) == 0:
        st.warning("⚠️ 無法計算，請輸入有效秒數！")
    else:
        avg_time = sum(valid_times) / len(valid_times)
        speed = 6 / avg_time  # 6 公尺測試
        st.info(f"✅ 您的走路速度為 **:red[{speed:.2f} 公尺/秒]**")

st.divider()


st.subheader("步行速度標準值")
st.write("請根據計算出的 **結果&年齡、性別** 對照以下表格:point_down:")
col1,col2 = st.columns(2)
with col1:
    with st.expander("中風患者/健康老年人"):
        st.write(" :red[✧ <0.4 公尺/秒]，建議只在家中走動")
        st.write(" :orange[✧ 0.4-0.8 公尺/秒]，能在社區短距離行走，建議使用輔具協助")
        st.write(" :green[✧ >0.8 公尺/秒]，可自由在社區走動")
        st.write(":heavy_minus_sign:" * 14) 
        st.write("✧ :blue[健康老年人:] 若 :red[<0.7 公尺/秒]，代表走路速度太慢且有較高跌倒風險")

with col2:
    with st.expander("健康成年人"):
        normal_speed =[
            [1.358, 1.341],
            [1.433, 1.337],
            [1.434, 1.390],
            [1.433, 1.313],
            [1.339, 1.241],
            [1.262, 1.132],
            [0.968, 0.943]
        ]
        index = ["20-29歲","30-39歲","40-49歲","50-59歲","60-69歲","70-79歲","80歲以上"]
        columns = ["男性","女性"]
        df = pd.DataFrame(normal_speed, index=index, columns=columns)
        st.dataframe(df)
       

st.divider()
st.subheader(":sparkles:衛教相關連結:sparkles:")
with st.expander("衛教資源連結"):
    st.markdown("""
- [提升老年人步行速度，改善生活品質｜台中物理治療所](https://www.eversolarpt.com/news/details.php?id=30381)
- [預防跌倒的運動｜雲林基督教醫院](https://yl.cch.org.tw/news_detial.aspx?cID=6&Key=694)
- [影音版｜跌倒預防三訓練](https://youtube.com/shorts/kegSitwf1zU?)
""")