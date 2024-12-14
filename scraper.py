import os
import re

import pandas as pd
from bs4 import BeautifulSoup

folder_path = "faculty_members"

data = []

for page in os.listdir("faculty_members"):
    if page.endswith(".html"):
        with open(file=f"{folder_path}/{page}", mode="r") as file:
            content = file.read()

            soup = BeautifulSoup(content, "html.parser")

            name = soup.find("h1")
            name = name.contents[0]

            mail = soup.find("a", href=re.compile("mailto"))
            mail = mail.contents[0]

            data.append((name, mail))

df = pd.DataFrame(data, columns=["Name", "Email"])
df.to_csv("Faculty_Emails.csv", index=False)
