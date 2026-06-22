# Sistema de Gestão de Biblioteca

**Aluno:** Gabriel Rizzatto  
**Disciplinas:** Linguagem de Programação Orientada a Objetos (LPOO) e Análise e Projeto de Sistemas (APS)  

---

## Descrição do Sistema

O Sistema de Gestão de Biblioteca é uma aplicação desktop desenvolvida em Python com interface gráfica em Tkinter e banco de dados relacional PostgreSQL. O projeto tem como objetivo principal informatizar e modernizar o controle de acervos e empréstimos literários. 

A arquitetura garante integridade referencial e controle de acesso, dividindo os usuários entre "Administradores" (com permissão total para gerenciar acervo e usuários) e "Comuns" (focados apenas no aluguel de obras). O sistema foi rigorosamente estruturado utilizando o padrão MVC (Model-View-Controller), Padrão DAO para persistência de dados (via SQLAlchemy) e o Padrão Strategy para renderização dinâmica da interface gráfica.

---

## Diagrama de Classes

![Diagrama de Classes](img/diagrama_classes.png)

---

## Documentação Completa

Para acessar os Casos de Uso, Requisitos Funcionais e Não Funcionais, e Regras de Negócio completas, acesse o link abaixo:

**[Acessar a Documentação do Projeto Completa](Documentação%20do%20Projeto.md)**


## Instruções de Execução

### Pré-requisitos
* **Python 3.x** instalado na máquina.

* **PostgreSQL** instalado e a correr localmente.

### Passo a passo para executar a aplicação

1. **Abre o terminal** na pasta raiz do projeto.
2. **Cria e ativa um ambiente virtual** (Recomendado):
   ```bash
   python -m venv venv
   
   # Para ativar no Windows:
   venv\Scripts\activate
   
   # Para ativar no Linux/Mac:
   source venv/bin/activate
   ```

3. Instala as dependências listadas no arquivo `requirements.txt:`

    ```bash
    pip install -r requirements.txt
    ```

4.  Configura a Base de Dados:
    * Cria uma base de dados vazia no teu PostgreSQL (ex: `biblioteca_db`).
    * Na pasta raiz do projeto (onde está o `main.py`), cria um ficheiro chamado `.env`.
    * Cola a seguinte linha dentro do `.env`, ajustando as tuas credenciais (`utilizador:senha` e o `nome_da_base_de_dados`):

    ```
    DB_URL=postgresql://postgres:postgres@localhost:5432/nome_da_base_de_dados
    ```

5.  Inicia o sistema:

    ```bash
    python main.py
    ```

---

##  Conclusão e Aprendizado

### Dificuldades Enfrentadas e Soluções
Durante o desenvolvimento do projeto, um dos maiores desafios foi manter a separação de responsabilidades (MVC) intacta ao conectar a interface gráfica do Tkinter com as operações de banco de dados do SQLAlchemy. No início, havia uma tendência a colocar lógicas de negócios nas Views. Essa dificuldade foi superada com a implementação do padrão **DAO (Data Access Object)**, que isolou a persistência, permitindo que as Views apenas coletassem dados e os enviassem aos Controllers.

Outro desafio significativo foi o gerenciamento de exclusões (de usuários e livros) sem quebrar a integridade do banco de dados (histórico de empréstimos). A solução adotada foi a transição da exclusão física para a **Exclusão Lógica** (adicionando um campo `ativo` booleano nas tabelas), garantindo que os registros sejam apenas inativados e o histórico permaneça preservado para futuras consultas.

### Principais Aprendizados
* **Design Patterns:** A aplicação do padrão *Strategy* demonstrou ser uma ferramenta poderosa para evitar o uso excessivo de blocos `if/else` na construção de interfaces dinâmicas (como alternar botões baseados no nível de permissão do usuário).
* **ORM e Banco de Dados:** O uso do SQLAlchemy facilitou imensamente a manipulação orientada a objetos no banco PostgreSQL, eliminando a necessidade de escrever queries SQL puras e garantindo mais segurança e manutenibilidade.
* **Componentização UI:** A estruturação da interface com classes separadas herdando de `tk.Toplevel` permitiu que a aplicação ficasse escalável e fácil de debugar.

---

## Declaração de Uso de Inteligência Artificial

**Ferramenta Utilizada:** Google Gemini  
**Modelo Utilizado:** Gemini (Advanced / 1.5 Pro)

* **Resolução de Bugs (Tkinter e SQLAlchemy):** Auxílio na identificação e correção de erros de manipulação do banco de dados e erros visuais no Tkinter.

**Aprendizado com o uso da IA:**
O maior aprendizado foi entender como o Tkinter funciona.