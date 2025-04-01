# Instrukcijas

## Programmas izmantošana vērtētājam
1. Lejupielādējiet projektu un palaižat `main.py` failu.

## Programmēšanas sākšana projekta veicējiem

### 1. Lejupielādējiet projektu (Clone)
```
git clone https://github.com/ArmandsVeksejs/AI_Projekts1.git
```
### 2. Branch izveide
- Vispirms izveidojiet jaunu zaru no galvenās koda bāzes (nosaukums "master")
- Branch sniedziet aprakstošu nosaukumu:
  ```
  git checkout -b funkcija/jusu-funkcijas-nosaukums
  ```
  vai
  ```
  git checkout -b bug/bug-fix-name
  ```
- Tikai pēc branch izveides sāciet strādāt pie izmaiņām

### 3. Veiciet izmaiņas
- Veiciet savas koda izmaiņas šajā atsevišķajā zarā
- Koncentrējieties uz vienu funkcionalitātes ieviešanu vai kļūdas izlabošanu katrā branch

### 4. Saglabājiet izmaiņas (Commit)
```
git add .
git commit -m "Īss jūsu izmaiņu apraksts"
```

### 5. Augšupielādējiet uz GitHub
```
git push origin funkcija/jusu-funkcijas-nosaukums
```

### 6. Iesniedziet izmaiņu pieprasījumu (Pull Request)
- Atveriet repozitoriju GitHub vietnē
- Noklikšķiniet uz "Pull Request" un tad "New Pull Request"
- Izvēlieties savu zaru un sniedziet skaidru aprakstu par veiktajām izmaiņām
- Šis kods tiks pārskatīts un, ja viss izskatīsies labi, tiks apvienots ar "master" zaru
- Pull request sadaļā citi var arī aplūkot veiktās izmaiņas, pievienot komentārus un piedāvāt izmaiņas

## Kontakti

Ja jums rodas jautājumi, rakstiet tos WhatsApp grupā

## Piezīmes

- Mēs izmantojam atsevišķus branches, lai nesabojātu galveno kodu
- Ja kaut ko sabojājat savā lokālajā kopijā, vienmēr varat sākt no jauna, lejupielādējot projektu vēlreiz
