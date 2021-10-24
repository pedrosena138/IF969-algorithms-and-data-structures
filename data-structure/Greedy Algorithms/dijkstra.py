def dijkstra(grafo, comeco, fim):
    menor_distancia = {}
    nos_nao_visitados = {}
    for i in grafo:
        nos_nao_visitados[i] = grafo[i]
        
    infinito = float('inf')

    for no in nos_nao_visitados:
        menor_distancia[no] = infinito
    menor_distancia[comeco] = 0
    
    while nos_nao_visitados != {}:
        menor_no_extraido = None
        for i in nos_nao_visitados:
            if menor_no_extraido is None:
                menor_no_extraido = i
            elif menor_distancia[i] < menor_distancia[menor_no_extraido]:
                menor_no_extraido = i

        for no_v, peso in grafo[menor_no_extraido]:
            if peso + menor_distancia[menor_no_extraido] < menor_distancia[no_v]:
                menor_distancia[no_v] = peso + menor_distancia[menor_no_extraido]
        nos_nao_visitados.pop(menor_no_extraido)
    return menor_distancia
