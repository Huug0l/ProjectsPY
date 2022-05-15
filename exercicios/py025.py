## Procurando uma string dentro de outra
nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome possui "VICENTE"? {}'.format('VICENTE' in nome.upper().split()))