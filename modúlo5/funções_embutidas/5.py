import emoji
import emoji

# Mostra lista de emojis disponíveis
print("Emojis disponíveis:\n")
print(f"{emoji.emojize(':red_heart:')} - :red_heart:")
print(f"{emoji.emojize(':thumbs_up:')} - :thumbs_up:")
print(f"{emoji.emojize(':thinking_face:')} - :thinking_face:")
print(f"{emoji.emojize(':partying_face:')} - :partying_face:")

# Pede a frase
frase = input("\nDigite uma frase e ela será emojizada:\n")

# Converte shortcodes para emojis
frase_emojizada = emoji.emojize(frase)

# Mostra resultado
print("Frase emojizada:", frase_emojizada)


