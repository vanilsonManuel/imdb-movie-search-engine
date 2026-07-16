# 🎬 IMDb Movie Search Engine

Aplicação web interativa desenvolvida em **Python** para pesquisar filmes do IMDb através de correspondência aproximada de texto (*fuzzy matching*).

O projeto permite encontrar títulos mesmo quando o nome é escrito de forma incompleta ou com pequenos erros ortográficos. Foi desenvolvido como **Projeto Final do curso de Programação em Python e Análise de Dados da Master D**.

![Demonstração da aplicação](imagem/screenshot.png)

## ✨ Funcionalidades

- Pesquisa inteligente de filmes por título;
- Correspondência aproximada com **RapidFuzz**;
- Filtro por classificação mínima do IMDb;
- Filtro por ano mínimo de lançamento;
- Seleção da quantidade de resultados apresentados;
- Exibição do título, ano, classificação, duração e descrição do filme;
- Indicação da percentagem de similaridade da pesquisa;
- Estatísticas gerais do conjunto de dados;
- Pré-visualização dos dados tratados;
- Interface web responsiva criada com **Streamlit**;
- Limpeza e tratamento de dados com **Pandas**;
- Código organizado de forma modular.

## 🛠️ Tecnologias utilizadas

- **Python** — linguagem principal do projeto;
- **Pandas** — leitura, limpeza e tratamento dos dados;
- **RapidFuzz** — pesquisa aproximada e cálculo de similaridade;
- **Streamlit** — criação da interface web interativa.

## 📁 Estrutura do projeto

```text
imdb-movie-search-engine/
│
├── data/
│   └── top_1000_imdb_movies.csv
│
├── docs/
│   └── Relatorio_Final_IMDb_Vanilson_Manuel.pdf
│
├── imagem/
│   └── screenshot.png
│
├── src/
│   ├── preprocess.py
│   └── search_engine.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/vanilsonManuel/imdb-movie-search-engine.git
cd imdb-movie-search-engine
```

### 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## ▶️ Executar a aplicação

Na pasta principal do projeto, execute:

```bash
streamlit run app.py
```

Depois, abra no navegador o endereço apresentado pelo Streamlit, normalmente:

```text
http://localhost:8501
```

## 🔎 Como utilizar

1. Escreva o nome de um filme no campo de pesquisa;
2. Ajuste os filtros de classificação, ano e número de resultados na barra lateral;
3. Consulte os filmes encontrados e a respetiva percentagem de similaridade.

A pesquisa aceita pequenos erros de escrita. Por exemplo:

```text
Hary Ptter
```

Mesmo com o título escrito incorretamente, a aplicação procura os nomes mais semelhantes disponíveis no conjunto de dados.

## 🧠 Como funciona

O ficheiro `src/preprocess.py` é responsável por:

- carregar o ficheiro CSV;
- remover colunas desnecessárias;
- eliminar registos sem título;
- extrair e converter o ano de lançamento;
- preencher valores em falta.

O ficheiro `src/search_engine.py` utiliza o método `process.extract()` do RapidFuzz para comparar o termo introduzido com os títulos disponíveis. Por padrão, apenas resultados com similaridade mínima de **60%** são considerados.

O ficheiro `app.py` reúne a interface, os filtros e a apresentação dos resultados.

## 📊 Conjunto de dados

A aplicação utiliza o ficheiro:

```text
data/top_1000_imdb_movies.csv
```

O conjunto contém informações como:

- nome do filme;
- ano de lançamento;
- classificação no IMDb;
- duração;
- descrição.

## 🎯 Competências demonstradas

- Desenvolvimento de aplicações em Python;
- Manipulação e limpeza de dados com Pandas;
- Pesquisa aproximada de texto;
- Desenvolvimento de interfaces com Streamlit;
- Organização modular de código;
- Tratamento de exceções;
- Utilização de Git e GitHub;
- Documentação técnica de projetos.

## 🚀 Melhorias futuras

- Pesquisa por género, realizador ou elenco;
- Ordenação por classificação, ano ou similaridade;
- Inclusão de cartazes dos filmes;
- Página individual com mais detalhes;
- Testes automatizados;
- Publicação da aplicação online.

## 👨‍💻 Autor

**Vanilson Manuel**

- GitHub: [github.com/vanilsonManuel](https://github.com/vanilsonManuel)
- LinkedIn: [Vanilson Manuel](https://linkedin.com/in/vanilson-manuel-806b821ba)

---

