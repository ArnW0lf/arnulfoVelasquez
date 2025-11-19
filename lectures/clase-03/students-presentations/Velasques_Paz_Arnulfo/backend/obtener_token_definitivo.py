import requests

# 1. PEGA AQUÍ EL TOKEN QUE TIENES AHORA MISMO EN EL EXPLORADOR
# (El que dice "Token del usuario" en el menú, no importa)
USER_TOKEN ="EAAK8zoOGmhcBP31nVOkqhZBI2lL5efJkZAw9YYBrV9mVDXtYQQtIgspPpVRu59hUoTKLuSOavKeq6qZAyWES21Q7a644FaV6jjkar4uGMCcqKXd1cXuhmjzLBWitWnUi0bsd6j7kB7pwZBooJSUPJ4jy7Al8UMMoMt4XkBZCUxthzZBaYoW9pNSBM4txxc6n0FJoZAhcZBXf3JkZAh9ZBDabLrHwaEV639vV8YzgjDC9FhIQkyMMAPgqpn51f8rnodCZBRvC6y8IRisPlZAwzNYZD"

# 2. PEGA AQUÍ EL ID DE TU PÁGINA (Ya lo tienes en tu .env)
PAGE_ID = "818138381393500" 

print("--- CANJEANDO TOKEN DE USUARIO POR TOKEN DE PÁGINA ---")

url = f"https://graph.facebook.com/v19.0/{PAGE_ID}"
params = {
    'fields': 'access_token',
    'access_token': USER_TOKEN
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    if 'access_token' in data:
        page_token = data['access_token']
        print("\n✅ ¡ÉXITO! AQUÍ ESTÁ TU TOKEN DE PÁGINA:")
        print("-" * 60)
        print(page_token)
        print("-" * 60)
        print("\n👉 Copia este token nuevo y ponlo en tu archivo .env en FACEBOOK_ACCESS_TOKEN")
    else:
        print("\n❌ Error al canjear:")
        print(data)

except Exception as e:
    print(f"Error de conexión: {e}")