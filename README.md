# Movie-Analytics-Pro
Movie Analytics Pro - WSistemas Este repositório documenta a evolução técnica de um projeto de análise de dados e Inteligência Artificial, originalmente concebido em um ambiente acadêmico e agora modernizado para padrões profissionais de Data Science.

📜 A Origem do Projeto
Em 2024, durante um trabalho acadêmico, aceitei o desafio de construir um sistema de Machine Learning utilizando PHP. O objetivo era processar um dataset de filmes para realizar predições através de algoritmos de KNN e Árvore de Decisão, além de gerar visualizações estatísticas.

Na época, embora o PHP apresentasse limitações severas para o cálculo computacional intensivo e manipulação de matrizes, a implementação serviu como uma prova de conceito fundamental para entender a lógica por trás dos algoritmos.

🚀 A Modernização: Python & Pandas
Hoje, o projeto foi totalmente remodelado. Substituímos a estrutura legada por um ecossistema robusto em Python, otimizando a performance e a precisão das análises. A transição permitiu tratar dados de forma analítica, lidando com inconsistências e valores nulos de maneira estatística, algo que no sistema anterior era processado de forma manual e limitada.

Recurso, Implementação PHP (Legada), Implementação Python (Atual)
Processamento, Loops procedurais while e fgetcsv, Operações vetoriais com Pandas
Cálculo KNN, Função manual de distância euclidiana, Algoritmo otimizado via Scikit-Learn
Gráficos, Imagens estáticas via PHPlot, Dashboards interativos via Plotly
Interface, HTML/CSS misturado ao código lógico, Interface reativa com Streamlit

🛠️ Tecnologias e Bibliotecas Utilizadas
Pandas: Utilizado para a manipulação e limpeza do dataset summer_movies.csv, garantindo a tipagem correta de dados e tratamento de valores ausentes.

Scikit-Learn: Biblioteca responsável pelo motor de IA. Implementamos o KNeighborsRegressor para predição de notas e o DecisionTreeClassifier para classificação de sucesso.

Streamlit: Framework utilizado para criar a interface web de alta performance, permitindo a interação em tempo real com os modelos.

Plotly: Responsável pela geração de gráficos dinâmicos e multidimensionais (Dispersão, Tendência Temporal e Distribuição).

Joblib: Utilizado para a persistência dos modelos treinados, permitindo que a aplicação realize predições instantâneas sem re-treinamento.

FPDF2: Implementação de motor para exportação de relatórios técnicos em PDF.

🏗️ Estrutura Analítica do Sistema
O projeto foi dividido em camadas para facilitar a manutenção:

Data Layer: Armazenamento e integridade do arquivo CSV.

Processing Layer: Scripts Python que transformam variáveis categóricas (gêneros) em dados numéricos através de Label Encoding.

Model Layer: Modelos treinados e salvos em formato .pkl.

Presentation Layer: O Dashboard da WSistemas, onde o usuário final consome as análises e realiza simulações.

📈 Resultados obtidos
A transição para Python permitiu um ganho direto na precisão dos modelos. Ao incluir a variável "Categoria" (Gênero) no treinamento, o modelo KNN apresentou uma evolução significativa na métrica de erro, enquanto a Árvore de Decisão atingiu uma acurácia superior a 75% na classificação de filmes bem avaliados.

Desenvolvido por WSistemas. (Wesley Samuel Ferreira Rodrigues)

projeto_movies_v2/
├── data/                       # Onde guardamos os nossos dados
│   └── summer_movies.csv       # O seu ficheiro original
├── models/                     # Scripts de treino e salvamento de modelos
│   ├── knn_regressor.py        # Evolução do seu knn_model.php
│   └── decision_tree.py        # Evolução do seu arvore_decisao.php
├── app/                        # A nossa interface gráfica (Frontend/Backend)
│   ├── main.py                 # Ficheiro principal do Streamlit (Menu e Home)
│   └── pages/                  # Subpáginas (Gráficos, Predições, Base de Dados)
├── utils/                      # Funções auxiliares (Limpeza de dados e cálculos)
│   └── data_processor.py       # Lógica de tratamento do CSV
├── requirements.txt            # Lista de bibliotecas para instalar (Pandas, Scikit-Learn, etc)
└── README.md                   # Documentação do projeto
