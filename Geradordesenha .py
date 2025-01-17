import random
import string

def gerar_senha(tamanho=12):
    """Função que gera uma senha segura com o tamanho especificado"""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("Digite o tamanho da senha desejada: "))

senha = gerar_senha(tamanho)
print(f"Sua senha segura é: {senha}")
5