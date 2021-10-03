import string

# Encriptar texto

def criptografar_permuta(text, key):
    # Atribuir números a palavras-chave
    keyword_to_num_list = keyword_num_assign(key)

    # Caso os caracteres não se encaixem em toda a grade perfeitamente.
    extra_letters = len(text) % len(key)
    dummy_characters = len(key) - extra_letters

    if extra_letters != 0:
        for i in range(dummy_characters):
            text += "."

    num_of_rows = int(len(text) / len(key))

    # Convertendo a mensagem em uma grade
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0

    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = text[z]
            z += 1

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)

    # Obter localizações de números
    num_loc = get_number_location(key, keyword_to_num_list)

    # Cifra
    texto_encriptografado = ""
    k = 0

    for i in range(num_of_rows):
        if k == len(key):
            break

        else:
            d = int(num_loc[k])

        for j in range(num_of_rows):
            texto_encriptografado += arr[j][d]
        k += 1
    return texto_encriptografado

def get_number_location(key, keyword_to_num_list):
    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if keyword_to_num_list[j] == i:
                num_loc += str(j)
    return num_loc

def keyword_num_assign(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    keyword_to_num_list = list(range(len(key)))
    init = 0

    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                keyword_to_num_list[j] = init
    return keyword_to_num_list

# Descriptografar

def descriptografar_permuta(text, key):
    # atribuir números a palavras-chave
    keyword_to_num_list = keyword_num_assign(key)
    num_of_rows = int(len(text) / len(key))

    # obtendo localizações de números
    num_loc = get_number_location(key, keyword_to_num_list)

    # Conversão de mensagem em grade
    arr = [[0] * len(key) for i in range(num_of_rows)]

    # Descriptografar
    texto_descriptografado = ""
    k = 0
    itr = 0

    for i in range(len(text)):
        d = 0
        if k == len(key):
            k = 0

        else:
            d: int = int(num_loc[k])

        for j in range(num_of_rows):
            arr[j][d] = text[itr]
            itr += 1

        if itr == len(text):
            break
        k += 1

    for i in range(num_of_rows):
        for j in range(len(key)):
            texto_descriptografado += str(arr[i][j])
    return texto_descriptografado