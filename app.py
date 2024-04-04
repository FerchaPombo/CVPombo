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
st.subheader('Experience & Qualifications')
st.write(
    """
    -✨
    -✨
    -✨
    -✨
    -✨
 """

)

# --- Skills --
st.write('#')
st.subheader('Hard Skills')
st.write(
    """
    -
    -
    -
"""
)
st.subheader('Intesests')
st.write(
    """
    -
    -
    -
    -
"""
)


# --- Work History ---
st.write('#')
st.subheader("Work Experience")
st.write("---")

# --- Jobs --- 

st.write('🖌️','Tattoo Artist and Illustrator | Self Employed')
st.write('07/2010 - Present')
st.write(
    """
    - Experiences learned here 
    -
    -
    -
    -
    -
"""
)

st.write('🖌️','Tattoo Artist and Illustrator | Self Employed')
st.write('07/2010 - Present')
st.write(
    """
    - Experiences learned here 
    -
    -
    -
    -
    -
"""
)

# --- Projects and Acomplishments -- 
st.write('#')
st.subheader('Projects & Acompllishments')
st.write('---')

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


