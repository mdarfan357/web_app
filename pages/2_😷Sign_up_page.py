import streamlit as st
import os
import time

os.chdir("../web_app")

from helper import append_to_csv


st.title("Registration form")
st.info("All * fields are mandatory")

first,last = st.columns(2)
first = first.text_input("First Name")
last = last.text_input("Last Name")
   

email,mob = st.columns([3,1])
email = email.text_input("Email ID")
mob = mob.text_input("Mob number")
   
    
user,pw,pw2 = st.columns(3)
user = user.text_input("Username*")
    
pw = pw.text_input("Password*",type="password")
pw2 = pw2.text_input("Retype your password*",type="password")
    
    
    
ch,bl,sub = st.columns(3)
submit = sub.button("Submit")


if submit:
   if ((user != "") or (pw != "") or (pw2 != "")):
        if pw == pw2:
            append_to_csv(first,last,email,mob,user,pw)
            st.success("Success")
            st.write(f'''
             <a target="_self" href="https://mdarfan357-web-app-1-home-page-56su7f.streamlitapp.com/">
                 <button>
                     Please login via the home page
                 </button>
             </a>
             ''',unsafe_allow_html=True)
            time.sleep(2)
#                 pyautogui.hotkey('ctrl', 'f5')
        else:
            st.error("Passwords don't match")
   else:
      st.error("Please fill all the * credentials")

st.write("""---""")
