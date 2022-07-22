from app.models import User
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import requests
from app.models import Institution
# from app.models import Institution

import sys

def get_student_info(uni : str) -> dict:
    """
    Description
    -----------


    """
    info = {}
    
    try:
        url = "https://directory.columbia.edu/people/uni?"
        print(url + urlencode({"code":uni}))
        res = requests.get(url + urlencode({"code":uni}))
        soup = BeautifulSoup(res.text, "html.parser")
        tbody = soup.body.div.tbody.contents[4].find("div").tbody
        
        title = tbody.contents[1].contents[1].contents[0]
        if "Student" in title:

            info['name'] = str(tbody.find("th").contents[0])
            info['email'] = str(tbody.find("a", class_="mailto").contents[0])
            
            school = None
            try:
                school = str(tbody.findAll("td")[1].contents[0]).split(", ")[1]
            except:
                if "Barnard" in str(tbody.findAll("td")[5]):
                    school = "Barnard College"
            
            schools_abrvs = {"SCHOOL OF GENERAL STUDIES":"GS","COLUMBIA COLLEGE": "CC","FU FOUNDATN SCHL OF ENGINEERING & APPLIED SCIENCE:UGRAD": "SEAS","Barnard College": "BC"}
            if not school or school not in schools_abrvs:
                return None 
            info["school"] = schools_abrvs[school]

        return info

    except (UnicodeEncodeError, AttributeError, IndexError):
        return None



def decompose_email(email : str) -> dict:

    uni, institution = email.split('@')
    
    institution = institution.split('.')[0]

    return {"uni": uni, "institution":institution}

def email_to_institution_id(email) -> str:
    email_code = decompose_email(email).get('institution')
    institution = Institution.query.filter_by(email_code=email_code).first()
    if institution:
        return institution.id


def scrape_name(email : str):
    try:
        info = get_student_info(decompose_email(email).get('uni'))
        if info:
            return info["name"]
    except:
        return None