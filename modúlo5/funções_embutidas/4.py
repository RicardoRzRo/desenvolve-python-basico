import datetime

agora = datetime.datetime.now()

# Data no formato dd/mm/aaaa
print(f"Data: {agora.strftime('%d/%m/%Y')}")

# Hora no formato HH:MM (sem segundos)
print(f"Hora: {agora.strftime('%H:%M')}")
