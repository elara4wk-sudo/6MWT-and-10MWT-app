import streamlit as st

st.set_page_config(
    page_title = ("行走能力測試計算機"),
    page_icon = (":walking_woman:"),
    layout = ("wide"),
    initial_sidebar_state = ("auto"),
    menu_items={
        "Get help": "https://docs.streamlit.io",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About":"這是一個可供所有人初步掌握自身身體狀況的臨床測試應用"
        }
)



st.title("行走能力測試計算 :abacus:")
st.divider()
st.markdown('''
    請在左欄先選擇所做測試，再依據提示填入相關資料，以便獲得行走能力的估算!  
    也會有相關衛教喔~嘗試看看吧! 
    ''')

# #sidebar設定
# with st.sidebar:
#     test_choice = st.selectbox(
#         "想計算的測試是......",
#         ["10公尺行走測試 (10MWT)", "6分鐘行走測試 (6MWT)"]
#     )


# #選擇後變化
# if test_choice == "10公尺行走測試 (10MWT)":
#     st.subheader("10公尺行走測試:(注意事項)")
# elif test_choice == "6分鐘行走測試 (6MWT)" :
#     st.write("6分鐘行走測試:(注意事項)")

#streamlit run 首頁.py