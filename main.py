import pandas as pd
from js import document

df1 = pd.DataFrame(columns=["name", "email"])

def test(*args):
  print(document.getElementById("name").value)

def update_dataset(*args):
    name = document.getElementById("name").value
    email = document.getElementById("email").value

    df1.append([name, email])