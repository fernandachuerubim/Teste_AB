Este é um projeto fictício. A empresa, o contexto e as perguntas de negócios não são reais. Este portfólio está seguindo as recomendações do blog  da [Comunidade DS](https://comunidadeds.com/).

O painel com os produtos de dados pode ser acessado via [streamlit](https://testeab-fc.streamlit.app/).
O dataset são produzidos usando a [página de newsletter](https://teste-ab-sdpa.onrender.com/home).

## 1. O problema de negócio
### 1.1 Problema
A empresa Isketch, localizada em São Paulo, fabrica e disponibiliza um software com foco no desenvolvimento 3D de projetos para a construção civil, como forma de prototipagem de grandes projetos.
Para usar o software, o cliente precisa adquirir uma licença de uso que se renova anualmente.

Uma das melhores estratégias de aquisição de clientes de iSketch é a captura do email dos clientes em troca de um Newsletter com conteúdos semanais sobre construção civil. A assinatura da newsletter permite começar um relacionamento entre a iSketch e as pessoas, a fim de mostrar as vantagens de utilizar o software para criar protótipos de construções civis.

Portanto, a melhoria da conversão da página de captura de email, ofertando a newsletter em troca, é crucial para o crescimento do número de clientes.

Sendo assim, o coordenador de Marketing da empresa pediu ao time de Designers que criassem uma nova página de captura de email com uma pequena modificação nas cores do botão de "Sim", a fim de aumentar a conversão da página.

O time de Designers criaram uma página com o botão de "Sim" vermelho para ser testada contra a página atual que possui o botão "Sim" azul. O coordenador de marketing tem pressa em testar a nova página, pois a empresa vem adquirindo poucos clientes nas últimas semanas e isso pode comprometer o faturamento anual da empresa.

O time de Cientistas de Dados da iSketch foi acionado com a missão de testar a nova página de captura de email o mais rápido possível. A primeira ideia foi planejar um experimento de teste A/B entre as duas páginas por um período de 7 dias, para concluir a efetividade da mudança da cor do botão. Porém, o coordenador de marketing categoricamente disse ao time de dados que não poderia esperar 7 dias e solicitou que concluíssem em menos tempo.

### 1.2 Desafio 
Você foi alocado no projeto de validação do novo layout da página, junto com o time de marketing a fim de ajudar na avaliação da nova página de captura.
O time de marketing espera que você consiga concluir se a conversão da nova página é realmente melhor, pior ou igual a conversão da página atual em menos de 7 dias.

### 1.2 Motivação
A empresa vem adquirindo poucos clientes nas últimas semanas e como a captura de email é uma das estrategias para a aquisição de clientes, o time de marketing pediu uma alteração da pagina para aumentar a consersão da página. 

### 1.3 Demandas de negócio
Produto de dados solicitado:
- Conseguir saber a conversão da página em menos de 7 dias.
- Um painel para visualizar a conversão da página.

## 2. Premissas de negócio
 - O painel de visualização terá duas opções de escolha para a realização do teste A/B:

    Manual: Nesta opção, o visitante escolherá entrar na página de controle ou na página de tratamento de acordo com o teste.

    Automático: Nesta opção, o teste será realizado automaticamente, sendo que 30% das vezes o botão "Sim" na página A (controle) será clicado, enquanto 32% das vezes o botão "Sim" na página B (tratamento) será acionado."

- Também haverá a opção de excluir o experimento.

As variáveis do dataset são:

Variável | Definição
------------ | -------------
|ID | Um id unico dentro do conjunto de teste. |
|click | Um indicador para saber em qual botão o visitante apertou. 0 = não, 1 = sim |
|visit | Quantidade de visitantes|
|group | Grupo que que o visitante pertence (control ou treatment) |

## 3. Planejamento da solução

### 3.1. Escolha o método

- 1.1. Teste de hipotese estatistica

Método escolhido foi o metodo bayesiano, para estimar os parâmetros de um modelo estatístico.

- 1.2. Algoritmo de Thompson Sampling

Séra usado o Algoritmo de Thompson Sampling para resolver o problema de multi-armed bandit(problema com varias probabilidades) para substituir o um teste A/B tradicional, pois, o MAB usa um agente para  explora as opções e faz a escolha da ação com base em uma política, essa escolha é levada para o ambiente que retorna uma recompensa sobre essa ação. 

### 3.2. Design do Experimento
 
- 3.2.1 Escolha da variavel

    Definição da métrica de avaliação.

- 3.2.2 Escolha da perda máxima aceitável

    Qual a perda máxima aceitavel se a página desafiante for escolhida?

- 3.2.3 Separação dos grupos

    Separação do grupo de controle.
    
    Separação do grupo de tratamento.
    
### 3.3 Colentando e preparando os dados

- 3.3.1 Coleta dos dados

    Crianção das flag do A/B.
    Escolha das ferramentas de teste A/B.
    
- 3.3.2 Preparação dos dados

    Limpeza e verificação dos dados.
    
- 3.3.3 Conversões dos grupos

    Calculo da conversão do grupo de controle.
    
    Calculo da conversão do grupo de tratamento.

### 3.4 Testando as Hipoteses

- 3.4.1 Definição do método de inferência estatística

    Definição da Posteriori (Distribuição de probabilidade)
            Distribuição beta
        
    Definição da Priori (Distribuição de probabilidade)
            Distribuição Uniforme
    
- 3.4.2 Cálculo da probabilidade conjunta

    Qual a probabilidade de B ser melhor que A.

- 3.4.3. Cálculo do risco esperado

    Qual o risco esperado se escolhermos a página B.

### 3.5 Tirando as conclusões

- Valor da probabilidade de B ser melhor do que A.

- Valor do risco esperado ao escolher a opção B.

## 4. Conclusão

O projeto envolveu a implementação de um teste A/B para determinar a eficácia de uma nova página de captura de email para a empresa Isketch. A equipe de cientistas de dados da Isketch foi responsável por planejar e executar o teste, com o objetivo de determinar se a mudança na cor do botão "Sim" na nova página resultaria em uma maior taxa de conversão.

O teste foi realizado utilizando o método bayesiano para estimar os parâmetros de um modelo estatístico e o Método de Bandido Múltiplo (MAB) para substituir um teste A/B tradicional. A coleta de dados foi feita através da criação de flags A/B e a preparação dos dados envolveu a limpeza e verificação dos dados coletados.

Após a coleta e preparação dos dados, as hipóteses foram testadas. A probabilidade de a página B (com o botão vermelho) ser melhor que a página A (com o botão azul) foi calculada, assim como o risco esperado de escolher a opção B.

Os resultados do teste A/B serão analisados para determinar se a mudança na cor do botão resultou em uma maior taxa de conversão. Se a nova página for mais eficaz, isso pode levar a uma maior captura de emails e, consequentemente, a um aumento no número de clientes para a Isketch.

## 5. Próximos passos

- Otimizar ou substituir o sql, pois, atualmente ele está tendo uma demorar nas respostas.

- Transformar o teste em A/B/n, podendo ter varias páginas de tratamento.