import requests
pars_res_list=[]
respons=requests.get("https://finance.i.ua/")
respons_text=respons.text
respons_parse=respons_text.split("<span>")
for parse_elem_1 in respons_parse:
    if parse_elem_1.startswith("USD"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("USD") and parse_elem_2[1].isdigit():
                pars_res_list.append(parse_elem_2)

print(f"USD - {parse_elem_1}")
