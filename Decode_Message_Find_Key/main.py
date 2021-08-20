
def retorna_array_palavras_separadas_n(senha_codificada):
    # Retorna um array separando as palavras de acordo com o tamanho da senha informado pelo usuário
    v_localizar=' '
    posicao=senha_codificada.find(v_localizar)
    palavra=senha_codificada[(posicao +1):len(senha_codificada)]
    Qtde=senha_codificada[0:posicao]
    count=0
    array = []
    tamanho_final=(len(palavra) -(int(Qtde) -1))
    while count < tamanho_final:
        palavra_separada=palavra[(count):(count+ int(Qtde))]
        array.append(palavra_separada)
        count=count+1
    return (array)

def retorna_palavra_maior_ocorrencia(array):
    # percorre o array de palavras e retorna a palavra que apareceu maior quantidade de vezes
    palavra_maior=array[0]
    qtde_maior=0
    while len(array) != 0:
        count=0
        palavra_busca=array[count]
        qtde=0
        while count< len(array):
            palavra_valida=array[count]
            if palavra_busca== palavra_valida:
                qtde=qtde+1
                array.remove(palavra_busca) 
                count = count -1
            count = count +1
        if qtde_maior< qtde:
            qtde_maior=qtde
            palavra_maior=palavra_busca
    return (palavra_maior)

#################### DECODE MESSAGE TO FIND KEY ACCORDING TO THE SIZE INFORMED BY USER ####################
qtd_inputs = input("Informe a quantidade de senhas: ")
print ("Exemplo Entrada: 3 onetwoone \n Saída: Senha one")
count = 0
while count < int(qtd_inputs):
    
    senha_codificada = input("Informe o tamanho da senha do dia e depois a mensagem codificada contendo a senha: ")

    array=[]
    array=retorna_array_palavras_separadas_n(senha_codificada)
    palavra_maior_ocorrencia=retorna_palavra_maior_ocorrencia (array)
    print ("Senha: (" + palavra_maior_ocorrencia + ")")

    count += 1

