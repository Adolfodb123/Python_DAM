"""
Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.
Figura para n=5:
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""
def imprimir_diamante_hueco(n):
    if n < 1:
        return

    for i in range(n):
        espacios_izquierda = n - 1 - i
        if i == 0:
            print(" " * espacios_izquierda + "*") 
        else:
            espacios_centro = 2 * i - 1
            print(" " * espacios_izquierda + "*" + " " * espacios_centro + "*")
    for i in range(n - 2, -1, -1):
        espacios_izq = n - 1 - i
        if i == 0:
            print(" " * espacios_izq + "*")
        else:
            espacios_centro = 2 * i - 1
            print(" " * espacios_izq + "*" + " " * espacios_centro + "*")
            
imprimir_diamante_hueco(5)
         
     

