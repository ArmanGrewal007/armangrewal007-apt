from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich.spinner import Spinner
import time
import shutil


contact_info = [
    ("📞", "+91 7009782005", "tel:+917009782005"),
    ("✉️", "armancode4u@gmail.com", "mailto:armancode4u@gmail.com"),
    ("💻", "ArmanGrewal007", "https://github.com/ArmanGrewal007/"),
    ("🔗", "ArmanGrewal007", "https://linkedin.com/in/armangrewal007/"),
    ("📍", "Punjab, India", "https://www.google.com/maps/place/Punjab,+India")
]

experience_data = [
    {
        "title": "Software Engineer Trainee (R&D)",
        "company": "Informatica - Bengaluru, KA",
        "tech_stack": "Python, LLMs, Java",
        "duration": "Aug 2024 - present",
        "details": [
            "Currently working on developing Claire™GPT prototype, which is built upon GPT-4o APIs."
        ]
    },
    {
        "title": "Software Engineer Intern",
        "company": "Xperi (TiVo) - Bengaluru, KA",
        "tech_stack": "Python, Bash, SQL, NoSQL",
        "duration": "Aug 2023 - Jun 2024",
        "details": [
            "Developed and improved processes to collect and enrich metadata for movies before sending it to the next team.",
            "Wrote a Python script to sync data b/w ElasticSearch and MSSQL, reducing sync time from 72 to 4hrs.",
            "Used Telegraf to collect data from Burrow and send it to Splunk for monitoring using interactive dashboards."
        ]
    }
]

projects = [
    {
        "title": "File Manager Website",
        "url": "https://github.com/ArmanGrewal007/FileManager",
        "date": "July 2023",
        "tech_stack": "HTML, EJS, Node.js, Express.js, AWS S3, PostgreSQL",
        "details": [
            "• Website to Upload, Rename, Move, Delete files/folders from local disk to a private AWS S3 bucket.",
            "• Express.js for routing. PostgreSQL for storing metadata of files and validation."
        ]
    },
    {
        "title": "Satellite Image Analysis",
        "url": "https://github.com/ArmanGrewal007/ndvi_vals",
        "date": "April 2023",
        "tech_stack": "Python, Data analysis, Machine Learning",
        "details": [
            "• Analysis of satellite images over Philippines, detecting trends in vegetation over time using Normalized Difference Vegetation Index.",
            "• Visualizations on dashboard using matplotlib, seaborn, autoviz, explainerdashboard.",
            "• Fitted a machine learning model with over 97% accuracy."
        ]
    },
    {
        "title": "Suicide Data Analysis",
        "url": "https://github.com/ArmanGrewal007/suicide_pandas",
        "date": "April 2021",
        "tech_stack": "Python, Data analysis",
        "details": [
            "• Preprocessing, Visualization, and Analysis on a Kaggle dataset.",
            "• Used Libraries like NumPy, Pandas, Matplotlib, and Seaborn."
        ]
    }
]

skills_data = [
    ("Languages", "Python, Shell scripting, Java, C++, C, SQL, Ruby"),
    ("Web Technologies", "Node.js, Express.js, Vue.js, HTML, CSS, JS, JQuery, Flask, Django, Spring Boot"),
    ("Databases", "MySQL, MSSQL, PostgreSQL, Redis, ElasticSearch, Neo4j, MongoDB, Flyway"),
    ("Machine Learning", "Scikit-learn, Tensorflow, Pytorch, Keras, Splunk, Excel, MatLab, LLMs"),
    ("DevOps", "Docker, Jenkins, RunDeck, Kubernetes, Chef, Terraform"),
    ("Miscellaneous", "GitHub, RabbitMQ, Apache Kafka, Telegraf")
]

left_items = [
    ("•", "[blue][bold]Neo4j[/bold] Certified Professional[/blue]", "https://graphacademy.neo4j.com/c/5fc672a6-5bf9-4611-aaba-bbe70f24ede8/"),
    ("•", "[blue]Specialization in Natural Language Processing[/blue]", "https://www.coursera.org/account/accomplishments/specialization/MPYFQ8ZQ6CFU?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=s12n"),
    ("•", "[blue]Level: [bold]Contributor[/bold] on Kaggle[/blue]", "https://www.kaggle.com/armangrewal007"),
    ("•", "[blue][bold]RabbitMQ[/bold] Course by CloudAMQP[/blue]", "https://training.cloudamqp.com/certificate/baf7532e-4c44-42c0-b648-5be37e25782c"),
    ("•", "[blue]Competitive Programming Course by Coding Spoon[/blue]", "https://certifier-production-storage.s3.eu-west-1.amazonaws.com/683f7a6a-470c-42bd-b283-623e009780ad/pdf-files/393e3982-3da1-45f5-9fa7-ca764f6a7b5e.pdf"),
]

right_items = [
    ("•", "[blue][bold]Redis[/bold] Certified Developer[/blue]", "https://www.credential.net/cb32c58d-9454-4170-9d56-4da8edaafab2#gs.bxuysm"),
    ("•", "[blue]Java/Python/SQL certificates on HackerRank[/blue]", "https://www.hackerrank.com/profile/armansinghgrewal"),
    ("•", "[blue]DSA self-paced course from GFG[/blue]", "https://media.geeksforgeeks.org/courses/certificates/b8aa98918f9316c64809221070cf861e.pdf"),
    ("•", "[blue]RH-124 and RH-134 from RedHat[/blue]", "https://rha.ole.redhat.com/rha/api/certificates/attendance/uuid/25af4309-51c1-42bd-9c83-4653423b454c"),
    ("•", "[blue]DBMS-1 and DBMS-2 from Infosys[/blue]", "https://drive.google.com/file/d/13pBxS03kjjsSEkm9PChN73F3Vn5aaET3/view"),
]

activities_data = [
    ("Captain, Volleyball Team", "Led the team to a gold medal in the inter-house championship.", "IIT Madras"),
    ("Class Representative", "Competed with over 30 sections and won Section of the Year 2022.", "LPU"),
]

education_data = [
    {
        "degree": "BTech Computer Science and Engineering (Hons.)",
        "years": "2020 - 2024",
        "institution": "Lovely Professional University, Phagwara, Punjab",
        "cgpa": "CGPA 8.84"
    },
    {
        "degree": "BS Data Science and Programming",
        "years": "2020 - variable",
        "institution": "IIT Madras, Chennai, Tamil Nadu",
        "cgpa": "CGPA 7.5",
        "link": "https://study.iitm.ac.in/ds/"
    },
    {
        "degree": "Higher Secondary",
        "years": "2018 - 2019",
        "institution": "Spring Dale School, Ludhiana, Punjab",
        "cgpa": "CGPA 10"
    },
]


arman = r"""
          (       *                )           (                           (     
   (      )\ )  (  `     (      ( /(   (       )\ )      (  (       (      )\ )  
   )\    (()/(  )\))(    )\     )\())  )\ )   (()/( (    )\))(   '  )\    (()/(  
((((_)(   /(_))((_)()\((((_)(  ((_)\  (()/(    /(_)))\  ((_)()\ )((((_)(   /(_)) 
 )\ _ )\ (_))  (_()((_))\ _ )\  _((_)  /(_))_ (_)) ((_) _(())\_)())\ _ )\ (_))   
 (_)_\(_)| _ \ |  \/  |(_)_\(_)| \| | (_)) __|| _ \| __|\ \((_)/ /(_)_\(_)| |    
  / _ \  |   / | |\/| | / _ \  | .` |   | (_ ||   /| _|  \ \/\/ /  / _ \  | |__  
 /_/ \_\ |_|_\ |_|  |_|/_/ \_\ |_|\_|    \___||_|_\|___|  \_/\_/  /_/ \_\ |____|
"""


arman = r"""
   ('-.     _  .-')  _   .-')      ('-.         .-') _                   _  .-')     ('-.    (`\ .-') /`  ('-.               
  ( OO ).-.( \( -O )( '.( OO )_   ( OO ).-.    ( OO ) )                 ( \( -O )  _(  OO)    `.( OO ),' ( OO ).-.           
  / . --. / ,------. ,--.   ,--.) / . --. /,--./ ,--,'         ,----.    ,------. (,------.,--./  .--.   / . --. / ,--.      
  | \-.  \  |   /`. '|   `.'   |  | \-.  \ |   \ |  |\        '  .-./-') |   /`. ' |  .---'|      |  |   | \-.  \  |  |.-')  
.-'-'  |  | |  /  | ||         |.-'-'  |  ||    \|  | )       |  |_( O- )|  /  | | |  |    |  |   |  |,.-'-'  |  | |  | OO ) 
 \| |_.'  | |  |_.' ||  |'.'|  | \| |_.'  ||  .     |/        |  | .--, \|  |_.' |(|  '--. |  |.'.|  |_)\| |_.'  | |  |`-' | 
  |  .-.  | |  .  '.'|  |   |  |  |  .-.  ||  |\    |        (|  | '. (_/|  .  '.' |  .--' |         |   |  .-.  |(|  '---.' 
  |  | |  | |  |\  \ |  |   |  |  |  | |  ||  | \   |         |  '--'  | |  |\  \  |  `---.|   ,'.   |   |  | |  | |      |  
  `--' `--' `--' '--'`--'   `--'  `--' `--'`--'  `--'          `------'  `--' '--' `------''--'   '--'   `--' `--' `------'  
"""

arman = r"""
    _,                             ,___                   _
   / |                            /   /                  //
  /--|  _   _ _ _   __,  _ _     /  ___   _  , , , __,  // 
_/   |_/ (_/ / / /_(_/(_/ / /_  (___// (_(/_(_(_/_(_/(_(/_ 
                                                           
"""

arman = r"""
       d8888                                               .d8888b.                                         888 
      d88888                                              d88P  Y88b                                        888 
     d88P888                                              888    888                                        888 
    d88P 888 888d888 88888b.d88b.   8888b.  88888b.       888        888d888 .d88b.  888  888  888  8888b.  888 
   d88P  888 888P"   888 "888 "88b     "88b 888 "88b      888  88888 888P"  d8P  Y8b 888  888  888     "88b 888 
  d88P   888 888     888  888  888 .d888888 888  888      888    888 888    88888888 888  888  888 .d888888 888 
 d8888888888 888     888  888  888 888  888 888  888      Y88b  d88P 888    Y8b.     Y88b 888 d88P 888  888 888 
d88P     888 888     888  888  888 "Y888888 888  888       "Y8888P88 888     "Y8888   "Y8888888P"  "Y888888 888 

"""

console = Console()

def display_resume():
    global console

    # Name
    terminal_width = shutil.get_terminal_size().columns
    ruler = "[white]" + "-" * terminal_width + "[/white]"
    # console.print();     console.print(ruler)
    print_centered_ascii(arman)
    console.print()
    # console.print(ruler); console.print()

    # Contact Information
    formatted_contact_info = []
    for icon, text, link in contact_info:
        formatted_contact_info.append(f"[link={link}]{icon} {text}[/link]")
    contact_line = " | ".join(formatted_contact_info)
    console.print(contact_line, justify="center")
    console.print()

    # Experience
    console.print("\n[bold underline]EXPERIENCE:[/]")

    experience = Table(show_header=False, box=None, expand=True)
    for exp in experience_data:
        experience.add_row(
            Text(exp["title"], style="bold"),
            Text(exp["company"], style="bold")
        )
        experience.add_row(
            Text(f"Tech Stack: {exp['tech_stack']}", style="italic"),
            Text(exp["duration"], style="bold")
        )
        for detail in exp["details"]:
            experience.add_row(Text(f"• {detail}", style="white"))
        experience.add_row()  # Add a blank row for spacing after each job
    console.print(experience)

    # Projects
    console.print("\n[bold underline]PROJECTS:[/]")

    for project in projects:
        title_text = f"[bold][link={project['url']}]{project['title']}[/link][/bold]"
        title = Table(show_header=False, box=None, expand=True)
        title.add_column("name", justify="left")
        title.add_column("date", justify="right")
        title.add_row(title_text, Text(project['date']))
        console.print(title)
        console.print(f"Tech Stack: {project['tech_stack']}")
        for detail in project['details']:
            console.print(detail)
        console.print() 

    # Skills 
    console.print("\n[bold underline]SKILLS:[/]")

    skills = Table(show_header=False, box=None, expand=True)
    for category, sk in skills_data:
        skills.add_row(category, sk)
    console.print(skills)

    # Achievements and Certifications
    console.print("\n[bold underline]ACHIEVEMENTS AND CERTIFICATIONS:[/]")
    
    anc = Table(show_header=False, box=None, expand=True)
    anc.add_column("Left Column", width=40)
    anc.add_column("Right Column", width=40)
    for left, right in zip(left_items, right_items):
        left_text = f"{left[0]} [link={left[2]}]{left[1]}[/link]"
        right_text = f"{right[0]} [link={right[2]}]{right[1]}[/link]"
        anc.add_row(left_text, right_text)
    console.print(anc)

    # Extra curricular activities
    console.print("\n[bold underline]EXTRA-CURRICULAR ACTIVITIES:[/]")

    activities = Table(show_header=False, box=None, expand=True)
    activities.add_column("Role", justify="left", style="bold")
    activities.add_column("Description", justify="left")
    activities.add_column("Institution", justify="right")
    for role, description, institution in activities_data:
        activities.add_row(role, description, institution)
    console.print(activities)

    # Education
    console.print("\n[bold underline]EDUCATION:[/]")
    education = Table(show_header=False, box=None, expand=True)
    education.add_column("left", justify="left")
    education.add_column("right", justify="right")
    for edu in education_data:
        degree = Text(edu["degree"])
        if "link" in edu:
            degree = Text.from_markup(f"[link={edu['link']}]{edu['degree']}[/link]")  # Adding hyperlink
        education.add_row(degree, edu["years"])
        education.add_row(edu["institution"], edu["cgpa"])
        education.add_row()
    console.print(education)
    console.print(Text("Thanks for reading!", style="bold italic on yellow"), justify="center")

# Fake progress bar
def display_progress():
    with Progress(transient=True) as progress:
        task = progress.add_task("[bold yellow]Rendering...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.01)  # Simulate work being done

# Fake spinner
def display_spinner():
    with console.status("[bold green]Loading...[/bold green]", spinner="dots") as status:
        for _ in range(10):  # Simulate some work
            time.sleep(0.1)  # Adjust this to change the speed of the spinner



def print_centered_ascii(ascii_art):
    terminal_width = shutil.get_terminal_size().columns
    ascii_lines = ascii_art.splitlines()
    num_lines = len(ascii_lines)

    for line_num, line in enumerate(ascii_lines, start=1):
        padding = (terminal_width - len(line)) // 2
        red = 255
        green = int(255 * line_num / num_lines)
        blue = 0
        console.print(f"{' ' * padding}[rgb({red},{green},{blue})]{line}[/rgb({red},{green},{blue})]")


def main():
    display_progress()
    # display_spinner()
    display_resume()
    
    

if __name__ == "__main__":
    main()