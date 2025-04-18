import ipaddress

network = ipaddress.ip_network('192.168.108.157/26', strict=False)

for i, ip in enumerate(network):
    print(i, ip)
    # print(f"{ip:b}")

# ответ 29, так как составители в этйо задаче подразумевали,
# что брать первый (с нулями) и последний (с единицами) айпишник нельзя!
# поэтому нумерация пошла с нуля, а подразумевалось что должна с единицы

