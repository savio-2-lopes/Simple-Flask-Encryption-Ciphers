import string

# Criptografar

def encryption_caesar(text, shift, alphabets):
  def shift_alphabet(alphabet):
    i_shift = 26-shift
    return alphabet[i_shift:] + alphabet[:i_shift]

  shifted_alphabets = tuple(map(shift_alphabet, alphabets))
  final_alphabet = ''.join(alphabets)
  final_shifted_alphabet = ''.join(shifted_alphabets)
  table = str.maketrans(final_alphabet, final_shifted_alphabet)
  return text.translate(table)

# Descriptografar

def descryption_caesar(text, shift, alphabets):
  def shift_alphabet(alphabet):
    return alphabet[shift:] + alphabet[:shift]

  shifted_alphabets = tuple(map(shift_alphabet, alphabets))
  final_alphabet = ''.join(alphabets)
  final_shifted_alphabet = ''.join(shifted_alphabets)
  table = str.maketrans(final_alphabet, final_shifted_alphabet)
  return text.translate(table)