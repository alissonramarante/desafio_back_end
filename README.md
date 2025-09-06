# Desafio Back-End Volcann — Processo Seletivo
Este repositório contem soluções do desafio proposto pela Valcann para vaga de estágio em Back-End.

## Resumo do Desafio
O desafio é composto por três partes:

1. **Banco de Dados (conceitual + índices básicos)**
- Mini-Mundo com os requisitos do banco de dados.
- Entidades Benchmarks, Controle e Histórico de Controle
- Definição de índices básicos conforme os cenários Q1, Q2 e Q3

### Questão 1 — Modelo Conceitual
![Banco de Dados MER - Benchmark](questao1/modelo_banco.png)

- Acesse a imagem do modelo conceitual em [`questao1/modelo_banco.png`](questao1/modelo_banco.png).
### Modelo Conceitual
- Link público do diagrama no BrModelo:  
  [Clique aqui!](https://app.brmodeloweb.com/#!/publicview/68bc20e90ec1bb87cf05d)

## Índices básicos
- **Chaves Primárias (PKs)**: Criar indices nas colunas `id` das tabelas **Benchmark**, **Controle** e **Histórico_estado**. Esses indices permitem localizar registo específico com mais rapizes, conforme o cenário Q1 e Q3.
- **Chaves Estrangeiras (FKs)**: Criar indices nas colunas `id_benchmark` da tabela **Controle** e `id_controle` na tabela **Historico_Estado**. Esses indices ajuda a acelerar as operações de junção (`JOIN`) entre as tabelas.
- **Coluna de Data/Hora**: Criar indice na coluna `date` na tabela **Historico_Estado**, para otimizar as buscas por um intervalo de tempo, conforme o cenário Q2 ou encontrar o estado mais cerente de um controle conforme o cenário Q3