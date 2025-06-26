saldo = 1000
limite = 500

# Comparando identidade (se são o mesmo objeto na memória)
print(f"saldo ({saldo}) is limite ({limite}): {saldo is limite}")
print(f"saldo ({saldo}) is not limite ({limite}): {saldo is not limite}")

# Comparando valor (mais comum e adequado para números)
print(f"saldo ({saldo}) == limite ({limite}): {saldo == limite}")
print(f"saldo ({saldo}) != limite ({limite}): {saldo != limite}")
