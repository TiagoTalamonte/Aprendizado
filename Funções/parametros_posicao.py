def realizar_pagamento(valor, forma_pagamento, parcelas):
    print(f" Valor total: R$ {valor:.2f}")
    print(f" Forma de pagamento: {forma_pagamento}")
    print(f" Parcelas: {parcelas}x de R$ {valor / parcelas:.2f}")
    print("-" * 40)

# Chamadas usando **somente posição** (sem nomear os parâmetros)
realizar_pagamento(300.00, "cartão de crédito", 3)
realizar_pagamento(120.00, "boleto", 1)
realizar_pagamento(1000.00, "PIX", 2)
