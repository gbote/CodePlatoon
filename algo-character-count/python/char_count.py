def char_count(str):
  # Your code here
  char_dict = {}
  list_str_sort = sorted(str.replace(" ", ""))
  for i in list_str_sort:
    if i not in char_dict:
      char_dict[i] = 1
    else:
      char_dict[i] += 1
  char_dict = dict(sorted(char_dict.items(), reverse=True, key=lambda x: x[1]))
  return char_dict