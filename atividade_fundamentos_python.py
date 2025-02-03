def par_ou_impar(numero):
  """
  Verifica se um número inteiro é par ou ímpar.

  Args:
      numero: Um número inteiro.

  Returns:
      Uma string "Par" se o número for par, ou "Ímpar" se for ímpar.
  """
  if numero % 2 == 0:
    return "Par"
  else:
    return "Ímpar"

# Entrada do usuário
numero = int(input())

# Verifica se a entrada é um número inteiro
if not isinstance(numero, int):
    raise ValueError("A entrada deve ser um número inteiro.")


# Obtém a saída
resultado = par_ou_impar(numero)

# Imprime a saída
print(resultado)
