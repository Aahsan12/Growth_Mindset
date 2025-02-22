#streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon=":shark:", layout="wide")
st.title("Growth Mindset AI Project")

st.header("Welcome to the Growth Mindset AI Project!")
st.write("The Growth Mindset AI project leverages artificial intelligence to foster a positive and adaptive learning approach. It provides personalized feedback, encourages resilience, and helps users develop problem-solving skills. By analyzing behavior and offering tailored guidance, the AI empowers individuals to embrace challenges and persist through obstacles.")

#quote section
st.header("Inspirational Quote")
st.write("Here is an inspirational quote to motivate you:")

st.header("What's Your Challage Today?")
user_input = st.text_input("Enter your challenge for today:") 

#conditional statement
if user_input:
    st.success(f"Your challenge for today is: {user_input}. keep pushing forward towards your Goal!")
else:
    st.warning("Please enter your challenge for today to get started.")
    
#reflexing 
st.header("Reflect on Your Progress")
reflexion = st.text_area("Write your relfection on the challenge you faced today:")

if reflexion:
    st.success("Great Insight! Keep up the good work.")
else:
    st.info("Reflexion on past experiences can help you grow. Write your thoughts above.")
    
#achievements
st.header("Celebrate Your Achievements")
acheivements = st.text_area("List your achievements for today:")

if acheivements:
    st.success("🥳Congratulations on your achievements! Keep up the great work.")
else:
    st.info("🥳Celebrate your wins, no matter how small. List your achievements above.") 
    
#footer
st.write("_._")
st.write("Keep Believing in Yourself! :muscle:")
st.write("**© Created by M.Ahsan**")
