simbolos = { 
"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", 
"f": "..-.", "g": ".-", "h": "....","i": "..", "j": ".---", 
"k": "-.-",  "l": ".-..", "m": "--", "n": "-.", "o": "---", 
"p": ".--.", "q": "--.-",  "r": ".-.",  "s": "...", "t": "-", 
"u": "..-", "v": "...-",  "w": ".--", "x": "-..-", "y": "-.--", "z": "--..",
}

#msg = input('Digite a msg que deseja traduzir para código morse: ')
msg = 'hello'
tamanho = len(msg)
saida = ""

for i in range(tamanho):
    if msg[i] in simbolos.keys(): 
        saida += simbolos.get(msg[i]) + ' '      
print(saida)       