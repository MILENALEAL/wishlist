with open ("index.txt", "r", encoding="utf-8") as f:
    text = f.read ()

valores_text = text.split("$")
valores = []
for vt in valores_text: 
    valores.append (vt.split("<")[0].replace(" ", "").replace (",", "."))

valores.pop (0)
total = 0.0
for valor in valores: 
    total+= float (valor)

print (total)