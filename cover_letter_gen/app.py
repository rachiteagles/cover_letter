from langchain.llms import CTransformers
from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

def generate_pet_name(resume,jd):
    llm = HuggingFaceHub(repo_id='google/gemma-1.1-7b-it',model_kwargs={'temperature':0.4})
    

    resume_summarization = PromptTemplate(
        input_variables=['resume','jd'],
        template=" If my resume is {resume} and the job description is {jd}. A short 50 words message to the hiring manager mentioning how I am good for this role will be; "
        # job description looks like {jd} then my cover letter is, " 
    )
    name = LLMChain(llm=llm,prompt=resume_summarization)

    response = name({'resume':resume,'jd':jd})
    return response['text']

def multiline_to_singleline(multiline_text):
    # Replace newline characters with a single space
    singleline_text = multiline_text.replace('\n', '.')
    
    # Replace multiple spaces with a single space
    singleline_text = ' '.join(singleline_text.split())
    
    return singleline_text

with st.form("my_form"):
    resume = st.text_input("resume")
    jd = st.text_input("job_description")

    submit_button = st.form_submit_button("Generate")

if submit_button:
    if resume and jd:
        st.write("cover letter: ",generate_pet_name(multiline_to_singleline(resume),multiline_to_singleline(jd)).split(';')[-1])

# resume = """
#  EDUCATION
# University of San Francisco
# Master's, Data Science
# PSIT College of Engineering
# Bachelor's, Mechanical Engineering
# PROFESSIONAL EXPERIENCE
# Meta via SGS Consulting
# Data Engineer
# July 2021 - July 2022
# GPA: 3.7
# June 2012 - June 2016
# GPA: 3.5
# San Francisco, CA, USA
# November 2022 - Present
# Cerenetics
# Data Scientist
# San Francisco, CA, USA
# October 2021 - June 2022
# RACHIT YADAV
# +14156057445 | rachit1405@gmail.com | San Francisco, CA, USA | linkedin.com/in/rachity
#   • Built new dataswarm data pipelines to automate daily data transfer between multiple systems
# • Worked on standardizing table structure to create a single source of truth of metric information across multiple teams
# • Developed and implemented pipelines and tables to automate monthly reports accessed by diverse stackeholders
# • Scynchronized bento notebook, dataswarm pipelines, conditionally formated google sheets and google docs
# • Implemented linear regression algorithm on bento notebook using fluent2 and used the model in dataswarm pipelines
# • Improved query performance by implementing TDigest to calculate the 5th, 25th, 50th, and 75th percentiles of various
# metrics on Presto
# • Utilized data visualization tool Unidash to validate and monitor data status across multiple applications on a daily basis
# • As a Data Scientist developed a model to detect the presence of mental illness using fMRI data
# • Used PySpark to process the data by implementing custom functions through UDF
# • Built new CI/CD pipelines, to deploy the model on production by leveraging github actions, docker and AWS
# • Experimented and evaluated various machine learning models like CNN (Convolutional Neural Network) (Pytorch),
# Decision Tree, Random Forest, and Gradient Boosting across multiple metrics to classify patient group
# • Achieved maximum AUC metric of 0.85 on validation data sets by using the Convolutional Neural Network model
# KPMG Global Services Bengaluru, Karnataka, India
# Data Engineer September 2020 - July 2021
# • Designed and developed new scalable data pipelines to perform data ingestion of high volume of financial data
# • Used various ETL data warehousing strategy and stored it in a relational database using PySpark
# • Processed large amount of data present in parquet files using AWS S3, lambda functions and EMR by using boto3 library
# • Built POC to utilized Airflow to create, execute, and terminate AWS EMR instances to run PySpark jobs
# • Converted the legacy data pipeline into PySpark jobs, including fetching the files from the Hadoop file system
# • Achieved reduction in execution time from 12 hours to 7 hours
# Cognizant
# Data Engineer
# Pune, Maharashtra, India
# January 2020 - May 2020
# • Analyzed high-volume data including transactions, events, and costs of a large pharmaceutical company
# • Revamped old data pipelines and SQL queries resulting in a 10% reduction in execution time of jobs
# Infosys Pune, Maharashtra, India
# Data Engineer January 2017 - January 2020
# • Implemented the design to develop new data pipelines to perform ETL operations by implementing SCD1 and SCD2 strategy on data present in Relational Databases (Oracle) and csv files present at unix shell environment
# • Performed data analytics on data present on csv files using Pandas (Python) to find the cause of production bugs
# • Automated the data pipeline by leveraging ETL tool (Informatica PowerCenter) and shell scripting to pre process flat files
# which resulted in a 20% reduction in monthly production issues
# PROJECTS & OUTSIDE EXPERIENCE
# Scalable Product Deduplication System on e-commerce website San Francisco, CA, USA
# Data Scientist November 2022 - December 2022
# • Identified ~11000 unique products present on e-commerce websites using highly diverse text and image data
# • Used PyTorch’s pre-trained word and image embeddings coupled with machine learning (ML) and neural network
# algorithms in databricks’s distributed environment. Attained an accuracy of 80% on validation data
# • Link to project
# SKILLS
# Skills: Python, Airflow, SQL, Data Science, Data Structures & Algorithms, Data Analysis, AWS, Apache Spark, Git, Business Analytics
#    """

# jd = """About the job
# Element Critical provides hybrid infrastructure solutions in an expanding portfolio of data center facilities across the country. Our mission is to meet the diverse needs of today’s business and technology leaders by delivering superior service and product offerings, cultivating trusted relationships with our customers, and motivating and enabling our employees. 



# OVERVIEW 

# Department: Facility Operations
# FLSA Status: Exempt
# Job Location: Sunnyvale, CA
# Reports to: Operations Facility Manager
# Salary: $130,000-$144,000


# Element Critical is seeking to add a Chief Engineer who aligns with our company values of accountability, integrity, grit, and problem-solving. Led by a team of savvy and experienced executives with a history of success, this is an opportunity to get involved near the ground level and grow exponentially with a company that is poised to execute. Come join our team! 



# Our experienced team works to maintain the critical physical infrastructure that supports Element Critical. The Data Center Engineer serves as a technical resource to support Element Critical equipment that supports critical servers to maintain better than a 99.999% uptime. The Chief Engineer is accountable for the operational management and effective daily oversite and administration of the site’s operational and maintenance tasks with the objectives of safely, efficiently, and effectively operating equipment and systems in a cost-effective manner. As this is a working supervisor role, the Chief Engineer is expected to perform maintenance and service on equipment as needed.


# RESPONSIBILITIES

# Responsibilities will include, but are not limited to, the following: 

# Provides leadership to the site facilities team and responsible for the on-site supervision of shift technicians, senior shift technicians, sub-contractors, and vendors.
# Oversees operation and management of routine and emergency services on a variety of critical systems such as but not limited to: Stand-by diesel generators, Switchgear, Automatic Transfer Switches, Uninterrupted Power Supplies, Power Distribution Units, Air Handling Units, Computer Room Air Conditioners, Chillers, Cooling towers, Chemical treatment systems, Pumps, Power monitoring, Electric motors, Variable Frequency Drives, Fire & Life Safety Systems, and Building Automation Systems.
# Ensures that all electrical, mechanical, and fire/life safety equipment within the data center is operating at peak efficiency, including planned preventative maintenance of equipment, daily corrective work, and emergency response.
# Serves as an expert technical resource interacting with onsite technicians, engineers, and any third-party vendors.
# Acknowledge and respond to all alarms, keeping the site Operations Facility Manager and service desk updated on status of equipment.
# Identify safety hazards within the building and incorporate the remediation of such hazards to ensure that the building’s staff and occupants work in a safe environment. Assist the Operations Facility Manager with implementing and administering the safety training program.
# Ensure that compliance of all regulatory laws and guidelines are met as they relate to the operation of the building’s infrastructure. Responsible for alerting management of building discrepancies.
# Attend all assigned meetings, acting as SME for technical questions/inquiries regarding facility critical and non-critical assets and infrastructure.
# Oversee the maintenance and continuous operation of all building systems including fire/life safety, mechanical (HVAC, plumbing, controls) electrical (lighting, UPS, PDU, generators, switch gear), lighting and temperature controls systems, light construction (painting, doors, revamping, locks) utilizing onsite staff and contracting with outside vendors as necessary.
# Responsible for protecting and improving the value of customer critical and non-critical assets and ensuring that building engineering systems continue to perform their intended function as designed.
# Develop, write, and regularly review MOP’s, SOP’s and EOP’s for all critical maintenance and operations supporting the data center.
# Assist in the development of a Capital plan which would include planning for infrastructure upgrades, equipment replacements and building modifications to ensure the building’s future capabilities are maintained.
# Responsible for overseeing major projects performed at the building to ensure they are properly executed and closed out in accordance with standard industry practices.
# Deliver quality service and ensure all customer demands are met.
# Asset, inventory, and document management.
# Responds to Facility Related Emergency call outs – second level escalation point for Data Center facilities related issues / failures.
# Creates operational procedures for critical equipment.
# Record and track work in the Computerized Maintenance Management System (CMMS)
# Maintain all infrastructure and compliance documentation for the building including up-to-date building drawings and electrical one-lines as well as documentation mandated for the purpose of maintaining regulatory compliance with Federal, State or Local law.
# Responsible for reviewing records of buildings rounds and readings, all engineering logs and engineering data sheets.
# Responsible for advance training and notification to all contractors so that they are informed and knowledgeable with respect to the building’s critical functions and the work they are to perform, including an incident contact response list.
# Responsible for understanding and complying with emergency escalation procedures.
# Ensure strict adherence to technical bulletins, established engineering guidelines, processes, and procedures.
# Perform additional job duties as requested.


# REQUIREMENTS & QUALIFICATIONS

# The ideal candidate will possess the following:
# Equivalent work experience or Trade School, Associates or Bachelors in applicable engineering field or mechanical or electrical trades.
# 5+ years of relevant work experience in a data center or other critical environment.
# 2-5 years leadership experience preferred.
# Ability to work under pressure and multi-task across multiple concurrent projects and priorities.
# Computer proficiency with a strong working knowledge of Microsoft Excel, PowerPoint, Outlook and Word.
# Strong writing skills, as well as verbal interpersonal/communication skills.
# Strong quantitative skills and demonstrated analytical and problem-solving ability.
# Ability to direct and manage both in a team-oriented setting and independently across all levels of people within the organization.
# Excellent organizational and time management skills.
# Demonstrates strong customer service skills and takes ownership of the customer experience treating all customer, vendors, contractors, and employees with respect and professionalism.
# Ability to develop and document procedures and train personnel on the procedures.
# Can proactively identify potential customer issues and communicate them to appropriate parties for resolution.
# Takes ownership for business performance.
# Provides constructive thought leadership on ways to improve service and pursues creative ways to reduce expenses when possible.
# Operates with a strong work ethic and a desire to do things the right way.
# Hands-on team-player leads by example in helping to build and sustain a healthy, supportive and results driven culture.
# Encourages constructive feedback on performance so lessons can be learned as part of a continuous improvement culture.


# Preference for one or more of the following licenses or certifications:
# Operating engineering licenses such as DC II, DC III, or equivalent
# Stationary Engineering or Building Engineering License
# Electrical or mechanical Journeyman License
# OSHA-10 or OSHA-30
# CFC license
# NFPA 70E
# First-Aid /CPR, Basic Life Saver Certification


# PHYSICAL REQUIREMENTS

# The physical demands listed below must be met for the employee to perform the essential job functions of the position.
# Walk job sites in uneven terrain.
# Work at heights and from ladders and at depths, such as under raised floors.
# Regularly lift and/or move up to 49 pounds; and participate in group lifts for 50 pounds or more.
# Work shifts up to twelve (12) hours in duration performing physical tasks all day without becoming overly tired.
# Coordinate body movements when using tools or equipment.
# Reach and stretch to position equipment and fixtures while maintaining balance.
# Bend or twist the body into unusual positions while working.
# Use hands to manipulate small wires and objects.
# Push or pull heavy objects into position.
# Work in a noisy environment.


# Element Critical is a well-funded, fast paced organization that is seeking to make several acquisitions over the next few years and develop into a very strong national player. We offer the following benefits, in addition to a focus on growing our culture and engagement.
# PPO and HDHP Healthcare Plans 
# FSA and HSA with above market Employer HSA Match 
# Dental and Vision Insurance 
# Employer Paid Disability and Life Insurance 
# Additional Group Insurances 
# Paid Vacation, Sick, and Personal Leave 
# 10 Company Paid Holidays 
# Paid Parental Leave
# 401k with up to 4% Employer Match 
# Personal Development and Learning Opportunities 
# Employee Referral Program"""
