import string
import difflib

# Master dictionary: English to Spanish
en_to_es = {
    "short": "corto", "long": "largo", "ear": "oreja", "mouth": "boca", "nose": "nariz", "eye": "ojo",
    "shoulders": "hombros", "heart": "corazon", "knee": "rodilla", "ankle": "tobillo", "forehead": "frente",
    "lip": "labio", "mustache": "bigote", "pink": "rosa", "orange": "anaranjado", "yellow": "amarillo",
    "green": "verde", "purple": "violeta", "brown": "marron", "gray": "gris", "black": "negro",
    "to be": "tener", "lucky": "suerte", "hungry": "hambre", "thirsty": "sed", "scared": "miedo",
    "careful": "cuidado", "tired": "sueno", "i have": "tengo", "i am": "soy", "you are": "eres", "he is": "el es",
    "grandfather": "abuelo", "grandmother": "abuela", "husband": "esposo", "wife": "esposa", "brother": "hermano",
    "sister": "hermana", "stepbrother": "hermanastro", "stepsister": "hermanastra", "children": "hijos",
    "son": "hijo", "daughter": "hija", "parents": "padres", "father": "padre", "mother": "madre",
    "chicken": "pollo", "cousins": "primos", "uncle": "tio", "aunt": "tia", "nephew": "sobrino", "niece": "sobrina",
    "older": "mayor", "younger": "menor", "light": "claro", "dark": "oscuro", "computer": "computadora",
    "history": "historia", "read": "leer", "favorite": "favorito", "click": "clic", "about": "sobre",
    "table": "mesa", "dog": "perro", "backpack": "mochila", "book": "libro", "paper": "papel", "notebook": "cuaderno",
    "pencil": "lapiz", "fish": "pez", "culture": "cultura", "exam": "examen", "number": "numero", "code": "codigo",
    "big": "grande", "small": "pequeno", "time": "hora", "which": "cual", "bathroom": "bano", "easy": "facil",
    "fun": "divertido", "calculator": "calculadora", "may": "mayo", "june": "junio", "july": "julio",
    "august": "agosto", "september": "septiembre", "october": "octubre", "november": "noviembre",
    "december": "diciembre", "christmas": "navidad", "weather": "tiempo", "person": "persona", "class": "clase",
    "devil": "diablo", "shoes": "zapatos", "movies": "peliculas", "blue": "azul", "red": "rojo", "white": "blanco",
    "soccer": "futbol", "football": "futbol americano", "bicycle": "bicicleta", "dad": "papa", "mom": "mama",
    "i": "yo", "me": "mi", "cars": "coches", "video games": "videojuegos", "travel": "viajar",
    "calendar": "calendario", "secret": "secreto", "one": "uno", "two": "dos", "three": "tres", "four": "cuatro",
    "five": "cinco", "six": "seis", "seven": "siete", "eight": "ocho", "nine": "nueve", "ten": "diez",
    "hello": "hola", "thank you": "gracias", "name": "nombre", "cold": "frio", "hot": "calor", "rain": "lluvia",
    "sunny": "soleado", "winter": "invierno", "spring": "primavera", "summer": "verano", "fall": "otono",
    "cool": "fresco", "windy": "viento", "cloudy": "nublado", "months": "meses", "seasons": "estaciones",
    "foggy": "niebla", "humid": "humedo", "student": "estudiante", "expression": "expresion", "teacher": "profesor",
    "yes": "si", "no": "no", "please": "por favor", "sorry": "lo siento", "good": "bueno", "bad": "malo",
    "happy": "feliz", "sad": "triste", "angry": "enojado", "tired": "cansado", "where": "donde", "when": "cuando",
    "why": "por que", "who": "quien", "how": "como", "goodbye": "adios", "good morning": "buenos dias",
    "good afternoon": "buenas tardes", "good night": "buenas noches"
}

# Build reverse dictionary (Spanish → English)
es_to_en = {v: k for k, v in en_to_es.items()}

# Function to clean and split input
def preprocess(text):
    return text.translate(str.maketrans("", "", string.punctuation)).lower().split()

# Fuzzy match helper
def fuzzy_lookup(word, dictionary):
    matches = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.8)
    return matches[0] if matches else None

# Translation function
def translate(text, direction="en_to_es"):
    words = preprocess(text)
    dictionary = en_to_es if direction == "en_to_es" else es_to_en

    translated_words = []
    for word in words:
        translated = dictionary.get(word)
        if not translated:
            fuzzy = fuzzy_lookup(word, dictionary)
            if fuzzy:
                translated = dictionary[fuzzy] + "?"
            else:
                translated = f"[{word}]"
        translated_words.append(translated)

    return " ".join(translated_words)

# Main interface
print("+++++++++++++")
print(" English ↔ Spanish Translator")
print(" Type a sentence to translate.")
print(" Use `>` at start for Spanish → English.")
print(" Type 'q' to quit.")
print("+++++++++++++\n")

while True:
    user_input = input("Translate: ").strip()
    if user_input.lower() == 'q':
        break

    if user_input.startswith(">"):
        result = translate(user_input[1:].strip(), direction="es_to_en")
    else:
        result = translate(user_input, direction="en_to_es")

    print(f"→ {result}\n")
