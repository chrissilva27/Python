def orderna_array(array):
    # Recebe um array e retorna o array ordenado
    array_ordenado = []
    array_ordenado.append(int(array[0]))
    del array[0]

    for i in array:
        num_atual = int(i)
        j = len(array_ordenado)
        pos=0
        for j in array_ordenado:
            if num_atual > (j):
                pos = pos + 1
        array_ordenado.insert(pos, num_atual)
    return array_ordenado

def num_faltando(array_ordenado):
    # Percorre array e retorna número que está faltando
    tamanho=len(array_ordenado)
    k=0
    while (k < tamanho):
        num_atual=array_ordenado[k]
        if k+1 < tamanho:
            proximo_num=array_ordenado[k+1]
            proximo_num_esperado=num_atual+1
            if proximo_num_esperado != proximo_num:
                return proximo_num_esperado
                k=tamanho + 1
        k += 1
    return ('##')


#################### ARRAY MISSING NUMBER  ####################
qtd_inputs = input('Informe a quantidade de arrays:')
count = 0
 
while count <= int(qtd_inputs):

    array = input('Informe os arrays []:')[1:-1].split(',')
   
    # Ordena o array informado
    array_ordenado=orderna_array(array)
    print(array_ordenado)
    
    # Retorna o número que está faltando caso contrário retorna ##
    numero_faltando=num_faltando(array_ordenado)
    print('Número faltando: ' + str(numero_faltando))

    count += 1