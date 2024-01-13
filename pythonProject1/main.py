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

ethereum=pars_res_list[1]
print(f"ethereum - {ethereum}")

USDT=pars_res_list[2]
print(f"USDT - {USDT}")

BNB=pars_res_list[3]
print(f"BNB - {BNB}")

SOL=pars_res_list[4]
print(f"SOL - {SOL}")

XRP=pars_res_list[5]
print(f"XRP - {XRP}")

USDC=pars_res_list[6]
print(f"USDC - {USDC}")

ADA=pars_res_list[7]
print(f"XRP - {XRP}")

XRP=pars_res_list[8]
print(f"XRP - {XRP}")

XRP=pars_res_list[9]
print(f"XRP - {XRP}")