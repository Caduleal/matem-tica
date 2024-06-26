Calculadora de Raízes e Classificação de Triângulos
Este repositório contém dois programas em Python. O primeiro programa calcula as raízes de uma equação quadrática ou de primeiro grau. O segundo programa define uma classe para triângulos, permitindo calcular seu perímetro, tipo de lados, área e verificar se é retângulo.

Calculadora de Raízes
Este programa calcula as raízes de uma equação quadrática da forma ax^2 + bx + c = 0. Se a equação for de primeiro grau, basta definir a = 0 e usar bx + c = 0.

Funcionamento
O programa solicita ao usuário os valores de a, b e c.
Verifica se a equação é de primeiro grau ou uma constante.
Calcula o discriminante (delta) e, dependendo do valor de delta, determina as raízes reais da equação.
Exibe o resultado para o usuário.
Classificação de Triângulos
Este programa define uma classe Triangulo que permite calcular o perímetro, determinar o tipo de triângulo (Equilátero, Isósceles ou Escaleno), calcular a área e verificar se o triângulo é retângulo.

Funcionamento
A classe Triangulo é inicializada com os comprimentos dos três lados.

Métodos disponíveis:
perímetro: Calcula o perímetro do triângulo.
tipo_lado: Determina o tipo de triângulo com base nos comprimentos dos lados.
calcular_area: Calcula a área do triângulo usando a fórmula de Heron.
retangulo: Verifica se o triângulo é retângulo usando o teorema de Pitágoras.
