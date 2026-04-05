import finnhub

# 1. Configura tu API Key
configuration = finnhub.Configuration(
    api_key={
        'token': 'TU_API_KEY_AQUI'
    }
)

# 2. Crea la instancia del cliente
finnhub_client = finnhub.Client(configuration=configuration)

# 3. Obtener el precio actual (Quote) de una empresa (ej: Apple)
quote = finnhub_client.quote('AAPL')

print(f"Precio actual de AAPL: ${quote['c']}")
print(f"Cambio del día: {quote['d']} ({quote['dp']}%)")