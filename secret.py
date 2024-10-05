from secrets import token_hex

#génération d'une clé secrète...
secret = token_hex(16)

print(secret)