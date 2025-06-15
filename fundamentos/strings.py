# Métodos úteis
palavra = '   python  '

print(palavra.upper())        # Tudo maiúsculo: '   PYTHON  '
print(palavra.lower())        # Tudo minúsculo: '   python  '
print(palavra.title())        # Primeira letra de cada palavra maiúscula: '   Python  '
print(palavra.strip())        # Remove espaços das extremidades: 'python'
print(palavra.lstrip())       # Remove espaços da esquerda: 'python  '
print(palavra.rstrip())       # Remove espaços da direita: '   python'
print(palavra.center(16, '#'))# Centraliza a string, preenchendo com '#': '###   python  ###'
print(".".join(palavra))      # Insere '.' entre cada caractere: ' . . .p.y.t.h.o.n. . '

# Métodos adicionais úteis
print(palavra.replace('py', 'PY'))    # Substitui substring: '   PYthon  '
print(palavra.find('th'))             # Retorna o índice da primeira ocorrência: 5
print(palavra.count(' '))             # Conta quantos espaços tem: 5
print(palavra.strip().startswith('py')) # Verifica se começa com 'py': True
print(palavra.strip().endswith('on'))   # Verifica se termina com 'on': True
print(len(palavra))                   # Tamanho total da string: 11
print()
# Fatiamento de strings
nome = 'Stênio Medeiros Freitas'

print(nome[0])        # Primeiro caractere: 'S'
print(nome[-1])       # Último caractere: 's'
print(nome[:8])       # Do início até o índice 7: 'Stênio M'
print(nome[9:])       # Do índice 9 até o final: 'edeiros Freitas'
print(nome[0:6:2])    # Do índice 0 ao 5, pulando de 2 em 2: 'Sei'
print(nome[:])        # A string inteira
print(nome[::-1])     # String invertida: 'satiertF sori edeM oinêtS'
print(nome[7:15])     # Parte do meio: ' Medeiro'
print(nome.split())   # Divide em lista de palavras: ['Stênio', 'Medeiros', 'Freitas']

print()
#string de mutiplas linhas
nome = "Stênio"
curso = "Ciência da Computação"

mensagem = f"""
Olá, {nome}!
Bem-vindo ao curso de {curso}.
Aproveite seus estudos!
"""
print(mensagem)
