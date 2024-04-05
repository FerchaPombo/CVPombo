from pathlib import Path

import streamlit as st
from PIL import Image

#---- PATH SETTINGS ----

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir/ 'styles' / 'main.css'
resume_file = current_dir/ 'assets/' / 'MariaFernandaBecerrilPomboResume_(1).pdf'
profile_pic = current_dir/ 'assets' / 'profile-pic.png'



# ------ General Settings----- 
PAGE_TITLE = 'Digital CV | Fernanda Pombo'
PAGE_ICON = '💻'
NAME = 'Fernanda Pombo'
DESCRIPTION = """
Junior Graduate on Predictive Analitics and Machine Learning.
"""
EMAIL = 'ferchapombo@gmail.com'
LOCATION = 'Berlin,Germany'
SOCIAL_MEDIA = {
    'Linkedin': 'www.linkedin.com/in/fpombo',
    'GitHub': 'https://github.com/FerchaPombo',
    'Instagram': 'www.instagram.com/ferchapombo',
}
PROJECTS = {
    '🌱 Mildew Detection in Cherry Leaves - ML model that predicts weather a cherry leaf is fungal-infected or not with Powdery Mildew': 'https://powdery-mildew-detector-fp-c8dd417a4db2.herokuapp.com/',
    '🇲🇽 MexicoisMagic - Python trivia quiz game about Mexicos magical facts': 'https://magicmexico-92655f369bba.herokuapp.com/',
    '🤜 Paper, Rock , Scissors - JavaScript game to play against the computer':'https://github.com/FerchaPombo/paper-rock-scissors',
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# -- Load resources Css, PDf  & Profile Pic --- 
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Hero Section ---
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, use_column_width=True)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=' 📄 Download Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime='application/octet-stream' # type of file we want to download , could be /pdf. in this case its unknown
    )
    st.write('✉️', EMAIL)
# --- Social Links -- 
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f'[{platform}]({link})')


# -- Experience & Qualifications --
st.write('#')
st.subheader('About me')
st.write(
    """
    Background in art, event organization, and a new career in software
development. Seeking a role that allows me to apply my growing passion for
data analysis, machine learning, and AI. Eager to contribute with my creativity,
adaptability, and problem-solving abilities to a dynamic team.
"""
)
# -- Experience & Qualifications --
st.write('#')
st.subheader('Experience & Qualifications')

# Create two columns
col1, col2 = st.columns(2)

# Content for column 1
with col1:
    st.write("- ✨ Adaptability")
    st.write("- ✨ Ability to Work Under Pressure")
    st.write("- ✨ Detail Oriented")
    st.write("- ✨ Multitasking Ability")
    st.write("- ✨ Creative Problem Solving")

# Content for column 2
with col2:
    st.write("- ✨ Communication Customer Service")
    st.write("- ✨ Interpersonal Skills Teamwork")
    st.write("- ✨ Management Skills Problem-Solving")
    st.write("- ✨ Time Management")
    st.write("- ✨ Problem-Solving")


# --- Technical Skills --
st.write('#')
st.subheader('Technical Skills')

# Create two columns
col1, col2, = st.columns(2)

# Content for column 1

with col1:
    st.write('FrontEnd Development:')
    st.write("- ✨ HTML Essentials")
    st.write("- ✨ CSS Essentials")
    st.write("- ✨ User Experience Design")
    st.write("- ✨ Bootstrap")
    st.write("- ✨ jQuery")

# Content for column 2
with col2:
    st.write('Methodologies:')
    st.write("- ✨ Design Thinking")
    st.write("- ✨ Agile Development")
    st.write("- ✨ Object-Oriented Programming")
    st.write("- ✨ CRUD")
    st.write("- ✨ CRISP-DM")

st.write('#')

col1, col2, = st.columns(2)

with col1:
    st.write('Frameworks and Libraries:')
    st.write("- ✨ Flask")
    st.write("- ✨ Django")
    st.write("- ✨ NumPy")
    st.write("- ✨ Pandas")
    st.write("- ✨ Matplotlib")

with col2:
    st.write('#')
    st.write("- ✨ Seaborn")
    st.write("- ✨ Plotly")
    st.write("- ✨ Scikit-learn")
    st.write("- ✨ TensorFlow")

st.subheader('Education')
st.write(
    """
    - 💻 Full Stack Software Development (Predictive Analytics), Predictive
    Analytics: Code Institute-> 03/2023 - 03/2024.

    - 📐 Bachelor of Architecture: UAM Universidad Autónoma Metropolitana-> 01/2008 - 02/2011
"""
)
# -- Languages --
st.write('#')
st.subheader("Languages")
st.write(
    """
    - Spanish : Native
    - English : Proficient
    - Portuguese : Advanced
    - German : Intermediate

"""
)
st.write("---")

# --- Work History ---

st.write('🖌️','Tattoo Artist and Illustrator | Self Employed')
st.write('07/2010 - Present')

# --- Projects and Acomplishments -- 
st.write('#')
st.subheader('Projects & Acompllishments')
st.write('---')

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


