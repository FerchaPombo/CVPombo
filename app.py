from pathlib import Path

import streamlit as st
from PIL import Image

#---- PATH SETTINGS ----

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir/ 'styles' / 'main.css'
resume_file = current_dir/ 'assets/' / 'CVPomboPhotonew.pdf'
profile_pic = current_dir/ 'assets' / 'profile-pic.png'



# ------ General Settings----- 
PAGE_TITLE = 'Digital CV | Fernanda Pombo'
PAGE_ICON = '💻'
NAME = 'Fernanda Pombo'
DESCRIPTION = """
JUNIOR FULL STACK SOFTWARE DEVELOPER
|Predictive Analytics and Machine Learning|
"""
EMAIL = 'ferchapombo@gmail.com'
LOCATION = 'Berlin,Germany'
SOCIAL_MEDIA = {
    'Linkedin': 'https://www.linkedin.com/in/fpombo/',
    'GitHub': 'https://github.com/FerchaPombo',
}
PROJECTS = {
    '🌱 Mildew Detection in Cherry Leaves': {
        'link': 'https://powdery-mildew-detector-fp-c8dd417a4db2.herokuapp.com/',
        'description': (
            "Utilized a machine learning model to predict if a cherry tree is infected with Powdery Mildew by analyzing an image of a leaf. "
            "The model uses binary classification to determine the presence or absence of fungal infection, providing insights that can inform "
            "business decisions in agriculture."
        ),
        'technologies': "Python, TensorFlow, Matplotlib, Seaborn, Kaggle, Jupyter Notebooks",
        'skills': "Machine learning, Python programming, data visualization, data analysis"
    },
    '🌐 Findit! Berlin': {
    'link': 'https://finditberlin-943ba7305bd2.herokuapp.com/',
    'description': (
        "I developed a fully functional photoblog using Django and Bootstrap, incorporating complete "
        "CRUD functionalities and following Agile methodologies."
        ),
        'technologies': "Python",
        'skills': "Django, Bootstrap, Python, HTML, CSS, CRUD, Agile, Full-Stack Development, Security, Authentication, UX|UI"
    },
    '🇲🇽 MexicoisMagic': {
        'link': 'https://magicmexico-92655f369bba.herokuapp.com/',
        'description': (
            "A Python-based trivia quiz game about Mexico's magical facts. The project showcases skills in Python programming, "
            "user interface design, and data management."
        ),
        'technologies': "Python",
        'skills': "Python programming, Data Management"
    },
    '🤜 Paper, Rock, Scissors': {
        'link': 'https://github.com/FerchaPombo/paper-rock-scissors',
        'description': (
            "A JavaScript game where players compete against a computer in a classic game of rock-paper-scissors. The project demonstrates "
            "JavaScript programming, game logic implementation, and user interface design."
        ),
        'technologies': "JavaScript, HTML, CSS",
        'skills': "JavaScript programming, game logic, user interface design"
    }
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
    st.write('📍',LOCATION)
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

     I bring a unique blend of creativity, technical expertise, and a global perspective, driven by a passion for using data to create impactful solutions. With a solid foundation in Python, Java, HTML, CSS, and JavaScript, I have hands-on experience in tools such as NumPy, Pandas, Matplotlib, Seaborn, and TensorFlow, allowing me to navigate both front and back-end development. My exposure to diverse cultures and work environments has sharpened my adaptability and problem-solving abilities, making me an effective collaborator in dynamic, fast-paced settings.

Starting as an artist and freelancer, I developed a strong appreciation for client satisfaction and the importance of continuous learning. This mindset now drives my enthusiasm for building data-driven projects that provide meaningful results. I thrive in environments where I can contribute creatively and technically, and I’m highly motivated to grow my skills in real-world applications, leveraging both my technical foundation and a passion for innovative problem-solving.

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

# Content for column 2
with col2:
    st.write("- ✨ Communication- Customer Service")
    st.write("- ✨ Teamwork")
    st.write("- ✨ Management Skills-Problem Solving")
    st.write("- ✨ Empathy ")


# --- Technical Skills --
st.write('#')
st.subheader('Technical Skills')

# Create two columns
col1, col2, = st.columns(2)

# Content for column 1

with col1:
    st.write('FrontEnd Development:')
    st.write("- ✨ HTML")
    st.write("- ✨ CSS")
    st.write("- ✨ UX|UI")
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
    st.write("- ✨ Azure")

with col2:
    st.write('#')
    st.write("- ✨ Seaborn")
    st.write("- ✨ Plotly")
    st.write("- ✨ Scikit-learn")
    st.write("- ✨ TensorFlow")
    st.write("- ✨ NextJS")

st.write('#')
st.write('---')
st.subheader('Projects')

# Introductory text about the projects
st.write('The following projects were completed as part of my full-stack software development program at Code Institute. Each project adhered to specific guidelines and was designed to demonstrate specific skills, providing an opportunity to apply theoretical knowledge in practical scenarios.')

# Iterate over the PROJECTS dictionary to display project details
for project_name, project_info in PROJECTS.items():
    st.write(f"**{project_name}**")
    st.write(f"[Link to Project]({project_info['link']})")
    st.write(f"{project_info['description']}")
    st.write(f"Technologies Used: {project_info['technologies']}")
    st.write(f"Skills Demonstrated: {project_info['skills']}")


st.write('---')
st.subheader('Education')

st.write('💻', 'Full Stack Software Development (Specialisation on Predictive Analytics and AI) : Code Institute-> 03/2023 - 03/2024.')

st.write('📐',' Bachelor of Architecture: UAM Universidad Autónoma Metropolitana-> 01/2008 - 02/2011')

st.write('💾',' Course|University of California, Davis: Big Data, Artificial Intelligence, and Ethics -> 18.04 - 13.06.2024')


# -- Languages --
st.write('#')
st.write('---')
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
    *  -Brand development and identity design.
    *  -Business operations and client management.
    *  -Website development and Management.
    *  -Social Media marketing and content creation. 
"""
)

st.write('🧾','Community Organizer & Event Planner |Self Employed')
st.write('Distanz,Culoka, Soli Tattoo Events, Berlin')
st.write('2010 - Present')
st.write(
    '''
    *  -Co-founded and organized events with Dis/tanz, a collective raising funds for global social justice projects, raising up to 4,000 euros per event.
    *  -Managed digital and analog promotion for events.
    *  -Designed promotional materials and coordinated event logistics.
    *  -Contributed to the creation of safe and inclusive spaces for queer and FLINTA* communities.

    '''
)


# --- Projects and Acomplishments -- 
st.write('#')
st.write('---')
st.subheader('Acomplishments')

st.write('🦄','Unicorns in Tech Hackathon [UIT](https://www.unicornsintech.com/uithack24/), Berlin: April 12-13, 2024')
st.write(
"""
Unicorns in Tech Hackathon - Getting Connected - Mental Health Issue
We designed and conceptualized an App for the community and therapist to find each other more easily. 
* Skills Demonstrated: Teamwork, Problem-Solving, Adaptability
"""
)
st.write('📓', 'Big Data, Artificial Intelligence, and Ethics , University of California. Coursera - 18.04.2024-18.06.2024 , Online: April 12-13, 2024 [Coursera](https://www.coursera.org/learn/big-data-ai-ethics)')

st.write('🔉','Attended Digital Futures - Advancing gender and ethnic equality and diversity [Digital futures](https://www.eventbrite.co.uk/e/digital-futures-advancing-gender-and-ethnic-equality-and-diversity-tickets-913957480427)')

st.write('🖥️', 'Attended We Are Developers -Queer in Tech conferences [Queer in Tech](https://www.wearedevelopers.com/en/live-events/10/queer-tech-day-june-2024)')