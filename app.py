from pathlib import Path

import streamlit as st
from PIL import Image

#---- PATH SETTINGS ----

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir/ 'styles' / 'main.css'
resume_file = current_dir/ 'assets/' / 'MariaFernandaBecerrilPomboResume.pdf'
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
    Dear Reader,

    I am writing to express my keen interest in opportunities within the realm of predictive analytics, machine learning, and artificial intelligence. Having recently completed a comprehensive program in full-stack software development with a specialization in predictive analytics and AI from Code Institute, coupled with my extensive background as a tattoo artist and freelancer, I am eager to bring a unique blend of creativity, adaptability, and technical skills to a new team.
    
    While my journey began in the creative world of tattooing, where I cultivated a deep appreciation for artistic expression and client satisfaction, my thirst for knowledge and passion for innovation led me to pursue formal education in the field of technology. Throughout my studies, I have developed proficiency in various programming languages, including front and backend development, and gained a solid understanding of predictive analytics and AI principles.
    
    Despite not having traditional work experience in this domain, my years of traveling the world and managing my own business have endowed me with invaluable skills in communication, adaptability, and problem-solving—qualities that I believe are essential for success in any professional environment. I am adept at collaborating with diverse teams, quickly learning new concepts, and thriving in dynamic settings.
    
    I am particularly drawn to my commitment to push the boundaries of innovation and leveraging data-driven insights to drive meaningful impact. 
    
    Find my resume and the skillset I acquired for your review below, which includes a link to some of my projects. I am excited about the opportunity to discuss how my unique background and skill set align with the needs of any team. Thank you for considering my application. I look forward to the possibility of contributing to your company's success.
    
    Warm regards,
    
    Fernanda Pombo
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

st.write('💻', 'Full Stack Software Development (Specialisation on Predictive Analytics and AI) : Code Institute-> 03/2023 - 03/2024.')

st.write('📐',' Bachelor of Architecture: UAM Universidad Autónoma Metropolitana-> 01/2008 - 02/2011')

st.write('💾',' Course|University of California, Davis: Big Data, Artificial Intelligence, and Ethics -> 18.04 - 13.06.2024')


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
st.subheader('Work Experience')
st.write('🖌️','Tattoo Artist and Illustrator | Self Employed')
st.write('07/2010 - Present')
st.write(
    """
    *  Created custom tattoo designs for clients, handling all aspects of the business, including client consultations, scheduling, and social media promotion.
    *  Developed brand identity, logo, and website for personal business.
    *  Managed social media profiles, creating content and engaging with followers.
    *  Built a strong reputation through word-of-mouth and social media marketing.
"""
)

st.write('🧾','Community Organizer & Event Planner |Self Employed')
st.write('Various Collectives, Berlin')
st.write('2010 - Present')
st.write(
    '''
    *  Co-founded and organized events with Dis/tanz, a collective raising funds for global social justice projects, raising up to 4,000 euros per event.
    *  Managed digital and analog promotion for events, utilizing social media and traditional marketing techniques.
    *  Designed promotional materials and coordinated event logistics.
    *  Contributed to the creation of safe and inclusive spaces for queer and FLINTA* communities.

    '''
)


# --- Projects and Acomplishments -- 
st.write('#')
st.subheader('Acompllishments')
st.write('---')

st.write('🦄','Unicorns in Tech Hackathon [UIT](https://www.unicornsintech.com/uithack24/), Berlin: April 12-13, 2024')
st.write(
"""
Attended a hackathon focused on technology and LGBTQIA+ communities.
Contributed to a project aimed at improving mental health and well-being within the community by developing an insurance platform specifically designed for queer people.
Collaborated with a team of diverse individuals to develop the prototype for the platform, a business plan, and a data collection and management strategy.
This experience strengthened my teamwork, problem-solving, and adaptability skills.
"""
)
st.write('#')
st.subheader('Projects')
st.write('---')
st.write('The following projects were completed as part of my full-stack software development program at Code Institute. Each project adhered to specific guidelines and was designed to demonstrate particular skills, providing an opportunity to apply theoretical knowledge in practical scenarios.')
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


