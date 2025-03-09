import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker",page_icon="🔑")

st.title("Password Strength Checker🔐")
st.markdown("""
## Welcome to the app to check if your password is strong 💪 !""")

password = st.text_input("Enter your Password",type="password")

feedback = []

score = 0

if password:
    if len(password)>=8:
        score +=1
    else:
        feedback.append("❌Password Should be atleast 8 character long")

    if re.search(r'[A-Z]',password) and  re.search(r'[a-z]',password):
        score +=1
    else:
        feedback.append("❌Password Should Contain both Upper Case and Lower Case")
    
    if re.search(r'[\d]',password):
        score +=1

    else:
        feedback.append("❌Password Should Conatin atleaset one numeber")

    if re.search(r'[!@#$%^&*]',password):
        score +=1

    else:
        feedback.append("❌Password Should Conatin atleaset one Character that are !@#$%^&*")

    if score==4:
        feedback.append("🟢Your Password is Strong")

    elif score==3:
        feedback.append("🟡 Your Password is Medium,It could be stronger")

    else:
        feedback.append("🔴 Your Password is Weak,Make it stronger")

    if feedback:
        st.markdown("## Imporvement Suggestions")
        for tip in feedback:
            st.write(tip)

else :
    st.info("Please enter your password to get started")

