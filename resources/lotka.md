# Modelo predador-presa (Lotka-Volterra)

O modelo de preador-presa, ou equações de Lotka-Volterra, foi desenvolvido para simular a dinâmica 
entre populações de diferentes espécies. O modelo é descrito como um sistema de equações 
diferenciais ordinárias (ODEs) de primeira ordem não lineares,
\[
    \begin{aligned}
        \frac{\dd x}{\dd t} &=& \alpha x - \beta x y \\
        \frac{\dd y}{\dd t} &=&  \delta xy  - \gamma y \, ,
    \end{aligned}
\]
onde \(x(t)\) e \(y(t)\) representam respectivamente as populações de presas e predadores, 
\\(\alpha$ descreve a taxa de crescimento da população de presas, \(\beta\) representa a taxa de mortalidade
das presas devido a presença de predadores,
 \(\delta\) e \(\gamma\) são as taxas de crescimento e de mortalidade dos predadores nesta ordem.


## Método de integração

 Existem vários métodos disponíveis para 
 integrar equações diferenciais ordinárias que variam em 
 níveis de complexidade (e.g. Runge-Kutta, métodos implícitos e semi-implícitos, etc). 
 Neste trabalho vamos utilizar um método simples que permite uma 
 implementação rápida, o método de Euler. Considerando que podemos escrever a derivada de 
 uma função temporal $f(t)$ aproximadamente como
\[
     \frac{\dd f}{\dd t} \approx \frac{ f(t+\delta t) - f(t)}{ \delta t} \, ,
 \]
onde $\delta t$ é um intervalo de tempo finito suficientemente pequeno $\delta t \ll 1$ 
para garantir congerg\^encia numérica. Considerando uma ODE do tipo
\[
    \frac{\dd f }{\dd t} = g(t) \, ,
\]
temos que
\[
    \frac{ f(t+\delta t) - f(t)}{ \delta t} = g(t) \, ,
\]
como estamos interessados em obter o valor da  função no passo temporal seguinte $f(t+\delta t)$,
aplicamos o teorema fundamental do cálculo 
\[
f(t+\delta t) = f(t) + \delta t \cdot g(t) \, ,
\]
sendo o erro global associado a este método \(\mathcal{O}(\delta t^2) \). Em resumo, utiliza-se a informação 
do passo \(t\) para determinar a evolução do sistema em $t+\delta t$.


## Implementação computacional


### Condições iniciais
Para realizar a integração devemos primeiro fixar as condições iniciais \(x(t=0)\) e \(y(t=0)\). 
Experimente diferentes condições e analise os resultados: \(x(0) > y(0)\), \(x(0) = y(0)\) e \(x(0) < y(0)\). 
Utilize valores da ordem das dezenas (e.g. \(x=y=10\) ). 


### Parâmetros
A tabela~\ref{tab:parameters} apresenta um conjunto de parâmetros 
para testar se o código está a funcionar corretamente.  O resultado expectável para este
conjunto de parâmetros é apresentado na Fig.~\ref{fig:result}.

| Parameter  | Description                 | Value |
|------------|-----------------------------|-------|
| \(\alpha\)   | Prey growth rate            | 0.5   |
| \(\beta\)    | Prey death rate             | 0.2   |
| \(\delta\)   | Predator growth rate        | 0.1   |
| \(\gamma\)   | Predator natural death rate | 0.2   |
| \(x_0\)      | Initial prey population     | 10    |
| \(y_0\)      | Initial predator poulation  | 10    |
| \(\delta t\) | Time step                   | 0.1   |
| \(T\)        | Total time steps            | 1000  |


Utilize uma versão recente de Python (\(>= 3.6\)) com os packages NumPy, SciPy e matplotlib para gráficos.
Utilize arrays do NumPy para guardar os valores de \(x\) e \(y\) ao longo do tempo, 
evite a utilização do objeto nativo list pois o custo computacional é mais elevado. 
