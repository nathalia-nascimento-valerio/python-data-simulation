# Lista com saldos
saldos = [100, 3500, 23, 4950, -20, 300, 78, -150, 3400]

# Média dos saldos em R$
media = sum(saldos) / len(saldos)
print('Média dos saldos: R${:.2f}'.format(media))

# Saldo maior e saldo menor
maior_saldo = max(saldos)
menor_saldo = min(saldos)
print('\nO menor saldo é R$ {:.2f}'.format(menor_saldo))
print('O maior saldo é R$ {:.2f}'.format(maior_saldo))

# Clientes com saldo negativo
print("\nClientes com saldo Negativo: ")
for saldo in saldos:
    if saldo <0:
       print('ALERTA: Cliente com saldo de R${:.2f}'.format(saldo))
 
 # Contar quantos clientes tem saldo negativo e quantos tem saldo positivo
positivo = 0
negativo = 0
for saldo in saldos:
    if saldo >= 0:
       positivo += 1
    else:
        negativo += 1
print('\nClientes com saldos positivo: {}'.format(positivo))
print('Clientes com saldos negativos: {}'.format(negativo))

# Lista com saldos negativos
saldos_negativos = [saldo for saldo in saldos if saldo < 0]
print(f"Saldos negativos: {saldos_negativos}")

# Quanto é necessário para zerar os saldos negativos
total_para_zerar = -sum(saldos_negativos)
print('Total necessário para zerar saldos negativos: R$'.format(total_para_zerar))
  