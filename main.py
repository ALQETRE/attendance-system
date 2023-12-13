import pandas as pd
from js import document

df = pd.DataFrame(columns=["name", "email"])

def update_dataset(*args):
    df = pd.read_csv(".\\database.csv")

    name = document.getElementById("name").value
    email = document.getElementById("email").value

    if name == "" or email == "":
        return

    if not df["email"].isin([email]).any():
        df.loc[-1] = [name, email]
        df.reset_index(drop= True, inplace= True)

    pd.to_csv(".\\database.csv")