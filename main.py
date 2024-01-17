import requests
import streamlit as st
from streamlit_option_menu import option_menu
from Assets import Animations
from streamlit_lottie import st_lottie
from PIL import Image
import smtplib
from email.mime.text import MIMEText

st.set_page_config(layout="wide", page_title="Hamdan Portfolio", page_icon="Assets/Free_Sample_By_Wix (1).jpg")


def load_lottieAnime(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()


coderanime = load_lottieAnime(Animations.codingAnimation)
img = Image.open("Assets/exoy2ijl.png")

st.write("##")
st.subheader("Hello Guys :wave:")
st.title("Welcome to my portfolio")
st.write("""My name is Hamdan and I am a passionate Python enthusiast with a keen interest in artificial intelligence and new technologies. 
My curiosity drives me to explore and learn new skills, enabling me to create innovative projects. I thrive on 
challenges and enjoy engaging with the community to share knowledge and ideas. My commitment to open-source 
innovation is evident in my active contributions and collaborations. With a positive outlook, I am dedicated to 
continuous learning and development in the field of technology.""")
if st.button("Read about me"):
    st.switch_page("pages/about.py")
st.write("---")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About", "Projects", "Contact me"],
        icons=["Person", "code-slash", "chat-left-text-fill"],
        orientation="horizontal"
    )

if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.write("##")
            st.subheader("Hamdan Khubaib")

        with col2:
            st_lottie(coderanime)

    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("""
            Current Skills
            - Expert in Python
                - 3 years of Experience in Python
                - Learning Web frame Works
                - Learning AI Development""")

        with col4:
            st.subheader("""
            Future Plan
            - Learn Java and Kotlin
                - Basic understanding of App Development
                - Basic understanding of Game Development 
            - Learn C++
                - Intermediate Knowledge of arduino
                - Learn Robotics          
            - Learn Web Development
                - Basic Knowledge of Web Development
            - Master AI Development
                - Learn Machine Learning
                - Learn Deep Learning
                - Learn Computer Vision
                
            - Build AI based advanced Robots
                - Build AI robots which construct whole building
                - Build AI robots which are capable to do all house hold based works
                - Build AI robots which can operate patients""")

if selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns(2)

        with col5:
            st.image(img)

        with col6:
            st.subheader("""
            Luna: Your Personal AI Assistant
            
            Luna is an innovative AI assistant designed to streamline your daily tasks and manage your digital life 
            with ease. With voice command capabilities, Developed with a focus on user interaction and automation, 
            Luna is the perfect companion for enhancing productivity and simplifying your digital experience.""")
            st.markdown("[Visit Github Repo](https://github.com/GitCoder052023/Luna)")

if selected == "Contact me":
    st.header("Get in Touch")
    st.write("##")
    st.write("Hello dear user,")
    st.write("Please take a moment to enter your name and email address. This will help us to directly contact with "
             "you via email")

    with st.form("Login form"):
        username = st.text_input("Username")
        Email = st.text_input("Email Address")
        if st.form_submit_button("Send request"):
            st.success("Request sent successfully")


            def send_email():
                # Set up the SMTP server
                smtp_server = 'smtp.gmail.com'
                port = 587
                sender_email = "K.alam93899@gmail.com"
                password = "zuqo cirk mcau wbyx"
                recipient_email = Email

                # Create the message
                message = MIMEText(f"""Dear {username},

Thank you for contacting us regarding your request to connect with Hamdan. We have received your request and are currently processing it.

As a bot, I'm able to handle the initial stages of communication to ensure your request is routed efficiently. This allows our team to focus on providing you with the best possible service.

Please know that we value your time and are working diligently to fulfill your request. You can expect to hear from us soon with an update on the status of your connection with Hamdan.

In the meantime, feel free to reach out if you have any questions or concerns. We're always happy to help!

Sincerely,

[Hamdan Portfolio] Bot""")
                message['Subject'] = "Processing Your Request to Connect with Hamdan"
                message['From'] = sender_email
                message['To'] = recipient_email

                # Send the message
                with smtplib.SMTP(smtp_server, port) as server:
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, recipient_email, message.as_string())


            send_email()

            smtp_server = 'smtp.gmail.com'
            port = 587
            sender_email = "K.alam93899@gmail.com"
            password = "zuqo cirk mcau wbyx"
            recipient_email = sender_email

            message = MIMEText(f"Dear Hamdan Khubaib,"
                               f"I got a request of contact from {username}, please contact him at {Email}")

            message['Subject'] = f"Contact request from {username}"
            message['From'] = sender_email
            message['To'] = recipient_email

            # Send the message
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, message.as_string())
