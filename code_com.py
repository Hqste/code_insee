
import pandas as pd


lien = "v_commune_2024.csv"
df = pd.read_csv(lien)


def trouver_commune(df, code_insee):
  resultat = df[df["COM"] == code_insee]["LIBELLE"]
  if resultat.empty :
    return "Commune introuvable"
  else :
    return resultat.iloc[0]

trouver_commune(df, '14106')

df.head()

df[df["COM"] == '14106']["LIBELLE"]

def main():
  code_insee = input("Entrez le code INSEE de la commune : ")
  nom_commune = trouver_commune(df, code_insee)
  if nom_commune:
    print(f"Le nom de la commune est : {nom_commune}")
  else:
    print("Code INSEE non trouvé.")

if __name__ == "__main__":
  main()
