import streamlit as st
import pandas as pd

st.set_page_config(page_icon =(":walking_woman:"))

st.title("行走能力測試計算 :abacus:")
st.divider()
st.subheader("6分鐘行走測試(6MWT)")
st.markdown(":round_pushpin: 評估心肺耐力，常用於肺部疾患")
st.markdown('''
    :round_pushpin: 測試說明:
    測試前須先平靜坐在測試起點5分鐘，並測量心率、血壓、呼吸速率、呼吸困難指數、血氧飽和濃度。
    ''')


st.markdown(":round_pushpin: 理想值計算公式")
prediction = {
    "gender" : ["男性","女性"],
    "formula" :[
        "7.57*(身高)-5.02*(年齡)-1.76*(體重)-309公尺",
        "2.11*(身高)-5.78*(年齡)-1.76*(體重)+667公尺"
    ]
}

st.table(prediction)
st.divider()

with st.container(border = True):
    gender = st.selectbox("請選擇生理性別",["男性","女性"], index = None, placeholder = "請選擇")
    height = st.number_input(
    label = "請輸入您的身高(公分):",  key = "height_input",
    format = "%.1f"
)
    age = st.number_input(
    label = "請輸入您的年齡(歲):", key = "age_input",
    step =1, format = "%d"
)
    weight = st.number_input(
    label = "請輸入您的體重(公斤):", key = "weight_input",
    format = "%.1f"
)
    calculate_button = st.button(label = "計算", key = "calculate_button")


result = 0
result_m= 7.57*height - 5.02*age - 1.76*weight - 309
result_f = 2.11*height - 5.78*age - 1.76*weight + 667
if calculate_button:
    if gender == "男性":
        result = result_m
    elif gender == "女性":
        result = result_f
    else:
        result = 0
st.info(f":heavy_check_mark: 您的6分鐘行走距離理想數值為 **:green[{result:.1f}公尺]**" )

st.write(":heavy_minus_sign:" * 32) 
st.markdown(":zap: 臨床而言，健康成年人步行距離應落在 :blue[400 至 700 公尺]。")
st.markdown(":zap: 步行距離若 :red[僅有300公尺或更短]，則與慢性阻塞性肺病、心臟衰竭和肺動脈高壓等疾病的預後不良有關。")
st.markdown(":zap: 若對自身狀況有任何疑問，仍建議回診或是找專業治療師評估情況!")

st.divider()
st.subheader(":sparkles:相關資料連結:sparkles:")
with st.expander("衛教資源連結"):
    st.markdown("""
- [肺部復健衛教手冊](https://asthma-copd.tw/images/files/Brochure/0005.pdf)
- [衛教單張｜中國醫藥大學附設醫院](https://www.cmuh.cmu.edu.tw/HealthEdus/Detail?no=9149)
- [心臟衰竭病患的運動訓練計劃｜中山醫學大學附設醫院](https://web.csh.org.tw/web/doctor/wp-content/uploads/2024/04/D1-1.pdf)
""")
with st.expander("參考資料"):
    st.markdown("""
- 吳英黛。呼吸循環系統物理治療：基礎實務。四版。台北:金名圖書；2016.
- Matos Casano HA, Ahmed I, Anjum F. Six-Minute Walk Test. [Updated 2025 Jul 7]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2025 Jan-.
- [Academy Of Neurologic Physical Therapy](https://neuropt.org/)
- [10mwt-pocket-guide](https://neuropt.org/docs/default-source/cpgs/core-outcome-measures/10mwt-pocket-guide-proof8-(2)28db36a5390366a68a96ff00001fc240.pdf?sfvrsn=e4d85043_0_10)
- [6mwt-pocket-guide](https://www.neuropt.org/docs/default-source/cpgs/core-outcome-measures/6mwt-pocket-guide-proof9.pdf?sfvrsn=9ee25043_0)
""")