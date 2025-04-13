from pathlib import Path
import streamlit as st
from PIL import Image


#Path settings
current_path = Path(__file__).parent
css_file = current_path/"styles"/"main.css"
resume_file = current_path/"assets"/"GIZEM_TELCEKEN_CV.pdf"
profile_pic = current_path/"assets"/"profile-pic.JPG"

#General Settings
page_title = "Digital CV - Gizem Telceken"
page_icon = ":rocket:"
name = "Gizem Telceken"
description = """Deployment & Validation Lead | PaaS team | Strategic Program Management"""
address = "Kadikoy | Istanbul"
email = "gizemtelceken.gmail.com"
phone = "+905552550302"
social_media = {
    "Linkedin" : "https://www.linkedin.com/in/gizem-telceken/",
    "Git" : "https://github.com/gizemte"
}

st.set_page_config(page_title=page_title, page_icon=page_icon)

#CSS settings & inject custom css into streamlit
#markdow = style formatting
with open(css_file, "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf:
    pdfbyte = pdf.read()
    profile_pic = Image.open(profile_pic)

#top section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.subheader(name)
    st.markdown(f"""
    <span style='color:#616060; font-size:14px;  font-weight:bold;'>{description}</span>""",
                unsafe_allow_html=True)
    st.download_button(
        label="⬇️Download Resume as Pdf",
        data = pdfbyte,
        file_name=resume_file.name,
        mime="application/pdf"
    )
    st.markdown(f"""
       <span style='font-size:13px;'> ✉️{email}</span>""",
                unsafe_allow_html=True)
    st.markdown(f"""
           <span style='font-size:13px;'>📱{phone}</span>""",
                unsafe_allow_html=True)
    st.markdown(f"""
           <span style='font-size:13px;'>📍{address}</span>""",
                unsafe_allow_html=True)

with col2:
    st.image(profile_pic, width=190)

#Social media links array
cols= st.columns(len(social_media), gap="small")
for index, (key, value) in enumerate(social_media.items()):
    cols[index].write(f"[{key}]({value})")

#Summary
st.write("---")
st.subheader("PROFESSIONAL SUMMARY")
st.write("""
Highly motivated Lead Engineer with 9 years of experience 
in deployment, validation, IT operations and system integration 
within Telecom and Cloud-based environments. 
Proven expertise in digital service deployment, automation, 
monitoring, and troubleshooting. Adept at leading teams, 
optimizing processes, and driving technical excellence. 
Strong analytical and problem-solving skills with a 
customer-oriented approach. 
Currently pursuing an MBA to enhance leadership and business strategy capabilities.
""")

st.write("---")
st.subheader("KEY SKILLS & TECHNOLOGIES")
st.write(f"""
- **Deployment & Integration:** Ansible basics, Rest API Management
- **Cloud & Infrastructure:** Linux (RHEL, CentOS, Rocky), Nginx, AWS
- **Monitoring & Troubleshooting:** Zabbix, Grafana, Wireshark, Tcpdump
- **Databases & Storage:** MySQL, Oracle PL/SQL, MongoDB, OpenSearch/Elasticsearch, Logstash, Pentaho
- **Scripting & Automation:** Bash, Shell Scripting, Python basics
- **Testing & Validation:** Postman, Robot Framework basics, TestRail
- **Incident & Change Management:** Agile, JIRA, Confluence, HP ALM
- **Telecom Domain Expertise:** DSP (Digital Service Provider), Billing & Charging Systems, Mediation, Header Enrichment
""")

st.write("---")
st.subheader("PROFESSIONAL EXPERIENCE")
st.write("**Deployment & Validation Lead Engineer Telenity, Istanbul | 08/2022 – Present**")
st.write("""
- Leading the deployment and validation of Digital Service Platforms (DSPs) for 7+ customized projects, including **Ooredoo Algeria, Djezzy, and Telecel Ghana**, with a 95% deployment success rate
- Overseeing ticket management and tracking enhancement requests (ERs)
- Supporting for over 30 content providers in service integration and resolving technical challenges during onboarding
- Conducting UAT validations, system testing and end-to-end testing of DSP ERs
- Mentoring team member and enhancing their technical and problem-solving skills and delegating task across team members
- Spearheading **Ooredoo Algeria Phase 2 & Migration Project** (+3.5milion subscription base)
- To take responsibility and leadership **Evina Integration with DSP Widget** project of Djezzy Algeria
- Test support for internal customers like RnD, Operation, Business Unit and QA & Solution architect teams
- Led a team of 4 engineers, coordinating tasks for multiple projects concurrently
""")

st.write("**Master Expert Application Operation Engineer**")
st.write("Turkcell, Istanbul | 04/2022 – 08/2022")
st.write("""
- Manage charging and rating systems, ensuring high availability and stability
- Deploy application patches and upgrades, assuring seamless service continuity
- Responsible for offline re-rating application management
- Resolve customer cases and findings
""")

st.write("**IT Charging Operation Senior Specialist**")
st.write("Turk Telekom, Istanbul | 05/2018 – 04/2022")
st.write("""
- Managing and maintaining real-time production charging systems in the company’s prepaid domain on a 7/24 basis with 99% SLA compliance
- Keeping system within minimum service failure time and ensuring high availability of services within SLAs
- Daily operation activities and address incidents/system cases
- Resolve customer cases and findings & track issues, system defects end-to-end
- Implement change requests and custom requests
- Troubleshooting, analysing system logs, identify root cause of the problems
- Deploy patches, upgrades, and system enhancements within Agile frameworks
- Plan capacity and sizing strategies for system performance optimization
- Operation Phase Leader for major projects such as **WiFi Calling, VoLTE Phase 2, Voucher Management System Replacement, and Provisioning Replacement**
""")

st.write("**IT Billing & Mediation Operation Specialist**")
st.write("Vodafone, Istanbul | 07/2016 – 05/2018")
st.write("""
- Maintain and monitored billing and mediation systems with 99% SLA compliance
- Manage Bulk SMS services of VFNET, collaborated with vendors, and resolved technical issues.
- Responsible bill cycle operations periodically & bill-cycle checks
- Supporting on project based with Solution and CRM teams
""")

st.write("**Assistant Quality Engineer**")
st.write("Huawei Technologies Co., Istanbul | 09/2014 – 06/2016")
st.write("""
- Support team leaders in terms of version management, software release processes, and audits under CMMi Level 5 standards
- Managed JIRA, SVN, and defect tracking systems, assuring project compliance
- Training Version Management and Release Process to related stakeholders or newcomers
- Prepare version report & CM status report to upper management
""")

st.write("---")
st.subheader("🎓EDUCATION")
st.write("**Master of Business Administration**")
st.write("Galatasaray University, Istanbul, 2024 – Ongoing")
st.write("**Bachelor of Science in Electronics & Communications Engineering**")
st.write("Yıldız Technical University, Istanbul, 2014, GPA 3.50/4.00")

st.write("---")
st.subheader("🏅CERTIFICATIONS & TRAINING")
st.write(f"""
- **Dive Into Ansible - Beginner to Expert in Ansible - DevOps**, Udemy, April 2025
- **Jira Work Management Fundamentals**, Turkey, February 2024
- **Devops For Developers**, Turkey, October 2022
- **CBAP (Certified Business Analysis Professional) Prep – IIBA Advanced BABOK v3**, Turkey, October 2021
- **Linux operating system Network services and system administration**, Turkey, May 2016
- **Introduction to Linux system administration**, Turkey, March 2016
- **CMMi High Maturity Training**, Turkey, August 2015
""")