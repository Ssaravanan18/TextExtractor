import re

def Aadhaar_extractor(file):
    with open("records.txt","r") as file:
        records=file.read() # str object
        Aadhaar_pattern=r"Aadhaar :^\d{4}\s\d{4}\s\d{4}$"
        Aadhaar=re.findall(pattern=Aadhaar_pattern,string=records)

    return Aadhaar
print(Aadhaar_extractor("records.txt"))