import pandas as pd
from js import document

df1 = pd.DataFrame(columns=["name", "email"])

def update_dataset(*args):
    name = document.getElementById("name").value
    email = document.getElementById("email").value

    if name == "" or email == "":
        return

    if not df1["email"].isin([email]).any():
        df1.loc[-1] = [name, email]
        df1.reset_index(drop= True, inplace= True)

    print(df1)