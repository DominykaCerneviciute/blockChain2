# python-bitcoinlib naudojimas

## main4.py 
  #### Programa apskaičiuoja bet kurios Bitcoin tinkle esančios transakcijos mokestį. 
  #### Kad būtų apskaičiuotas mokestis, turi būti įvestas transakcijos hash'as

### Programoje:
    Apskaičiuotas transakcijos "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2" mokestis
    Apskaičiuojamas bet kurios įvestos transakcijos mokestis
    Apskaičiuotas vienos iš vertingiausių transakcijų mokestis
      
### Veikimas
    1. Įvedamas transakcijos hash'as
    2. Apskaičiuojama transakcijos visų output'ų suma
    3. Apskaičiuojama visų input'ų transakcijų output'ų suma
    4. Iš input'ų sumos atimama outputų suma
    5. Gaunamas ir atspausdinamas mokestis
      
 | Transakcijos hash                                                |    Mokestis    |
 |------------------------------------------------------------------|----------------|
 |"0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"|     0.0005     |
 |"4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"| 12666.33684590 |
 |"3500b0e3452e801e648a0aff1a5a7bd6f2c3f9ce26fd4b1920a391e18d1f9d53"|     0.05       |
 
 ### Paleidimas
      python main4.py
      
## main5.py
   #### Programa apskaičiuoja įvesto bloko hash'ą
   #### Programa išveda tiek esamą, tiek apskaičiuotą bloko hash'ą
   
### Veikimas
    1. Įvedamas bloko numeris
    2. Paimama versija ir pakeičiama į little endian
    3. Paimamas prieš tai buvusio bloko hash'as ir pakeiciamas į little endian
    4. Paimamas merkle root hash'as ir pakeičiamas į little endian
    5. Paimamas time ir pakeičiamas į little endian
    6. Paimamas bits ir pakeičiamas i little endian
    7. Paimamas nonce ir pakeičiamas į little endian
    8. Visos reikšmės sudedamos iš eilės į kintamąjį ir suhash'uojamos
    9. Paimamas suskaičiuoto hash'o little endian
    10. Išvedamas esamas ir apskaičiuotas bloko hash'ai
    
### Paleidimas
    python main5.py

### Pavyzdys
##### Bloko numeris:  95000
##### Gautas hash:  0000000000074a6f7e2d07cd8e5dd6dc8183993ee3b84666af499bc5b439d21b
##### Bloko hash:  0000000000074a6f7e2d07cd8e5dd6dc8183993ee3b84666af499bc5b439d21b
