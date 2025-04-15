def media(nota1, nota2, nota3, letra):
    if letra == 'A':
        mediaNotas = (nota1 + nota2 + nota3) / 3
        return mediaNotas
    elif letra == 'P':
        mediaPonderada = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / (5+3+2)
        return mediaPonderada
    
