import subprocess
import re

cmd_output = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode("utf-8", "ignore")


profile_names = re.findall(
    "Todos os Perfis de Usurios: (.*)\r", cmd_output)

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}

        wifi_profile["ssid"] = name

        profile_info_pw = subprocess.run(
            ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode("utf-8", "ignore")

        password = re.search(
            "Contedo da Chave            : (.*)\r", profile_info_pw)

        if password == None:
            wifi_profile["password"] = ""
        else:
            wifi_profile["password"] = password[1]

        wifi_list.append(wifi_profile)

# for x in range(len(wifi_list)):
#     print(wifi_list[x])

print(wifi_list)
