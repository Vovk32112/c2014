import requests
pars_res_list=[]
respons=requests.get("https://coinmarketcap.com/")
respons_text=respons.text
respons_parse=respons_text.split("<span>")
for parse_elem_1 in respons_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                pars_res_list.append(parse_elem_2)

bitcoin=pars_res_list[0]
print(f"bitcoin - {bitcoin}")