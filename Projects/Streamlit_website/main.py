import streamlit as st

st.title("ANAMTA's PORTFOLIO 🦋🎀🌻")
st.write("Welcome to my portfolio, where you can find my projects and achievements.")

st.button("Download Resume")

st.header("About me")
st.write("""Hello! I'm Anamta, an aspiring developer learning Python and Streamlit.
I love creating small projects like BMI calculators and portfolio websites.""")

st.header("My Projects")
st.write("Here are some of my projects:")
st.subheader("💪 BMI Calculator")
st.write("A simple BMI calculator app built with Python and Streamlit.")

st.subheader("🌸 Portfolio Website")
st.write("This very website you’re looking at — built using Python and Streamlit.")

st.header("Contact me")
st.write("📧 Email: anamta@example.com")
st.write("📞 WhatsApp: +1234567890")

# Footer
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by Anamta</p>", unsafe_allow_html=True)

