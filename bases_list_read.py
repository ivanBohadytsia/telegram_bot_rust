from json import load

with open("bases_list.json", "r", encoding="utf-8") as json_file:
    data_pictures = load(json_file)
