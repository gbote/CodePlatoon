def is_vowel(c):
  return c in {'a', 'e', 'i', 'o', 'u'}

def translate(word_or_phrase):
  output = ''
  word_arr = word_or_phrase.split(' ')
  for word in word_arr:
    i = 0
    is_q = False
    while i < len(word) and ((not is_vowel(word[i])) or (word[i] == 'u' and is_q)):
      is_q = word[i] == 'q'
      i += 1
    output += word[i:] + word[:i] + 'ay '

  return output[:-1]