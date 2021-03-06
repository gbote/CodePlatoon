# Don't forget to run the tests (and create some of your own)

def clean_str(str):
    str_arr = sorted(str.lower().replace(" ", ""))
    return "".join(str_arr)

def anagrams_for(word, list_of_words):
    dict_list = [{"original": single_word, "comparison": clean_str(single_word)} for single_word in list_of_words]
    return [entry["original"] for entry in dict_list if entry["comparison"] == clean_str(word)]
