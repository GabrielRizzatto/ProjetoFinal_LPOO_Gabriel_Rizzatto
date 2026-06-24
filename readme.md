# Sistema de Gestão de Biblioteca

**Aluno:** Gabriel Rizzatto  
**Disciplinas:** Linguagem de Programação Orientada a Objetos (LPOO) e Análise e Projeto de Sistemas (APS)  

---

## Descrição do Sistema

O Sistema de Gestão de Biblioteca é uma aplicação desktop desenvolvida em Python com interface gráfica em Tkinter e banco de dados relacional PostgreSQL. O projeto tem como objetivo principal informatizar e modernizar o controle de acervos e empréstimos literários. 

A arquitetura garante integridade referencial e controle de acesso, dividindo os usuários entre "Administradores" (com permissão total para gerenciar acervo e usuários) e "Comuns" (focados apenas no aluguel de obras). O sistema foi rigorosamente estruturado utilizando o padrão MVC (Model-View-Controller), Padrão DAO para persistência de dados (via SQLAlchemy) e o Padrão Strategy para renderização dinâmica da interface gráfica.

---

## Diagrama de Classes

```mermaid
classDiagram

    class TipoUsuario {
        <<enumeration>>
        ADMINISTRADOR
        COMUM
    }

    class Usuario {
        <<entity>>
        - id: int
        - nome: String
        - cpf: String
        - login: String
        - senha: String
        - tipo_usuario: TipoUsuario
        - ativo: boolean
        + validar_cpf(String): boolean$
    }

    class Livro {
        <<entity>>
        - id: int
        - titulo: String
        - autor: String
        - qtd: int
        - ativo: boolean
    }

    class Emprestimo {
        <<entity>>
        - id: int
        - id_usuario: int
        - id_livro: int
        - data_retirada: Date
        - data_devolucao_prevista: Date
        - status: String
    }

    Usuario --> TipoUsuario : possui
    Usuario "1" --> "0..*" Emprestimo : realiza
    Livro "1" --> "0..*" Emprestimo : compõe

    class GenericDAO {
        <<abstract>>
        + salvar(Object)*
        + buscar_todos()*
        + deletar(int)*
        + atualizar(Object)*
    }

    class UsuarioDAO {
        - session: Session
        + salvar(Usuario): Usuario
        + buscar_por_id(int): Usuario
        + buscar_todos(): List~Usuario~
        + buscar_ativos(): List~Usuario~
        + atualizar(Usuario): Usuario
        + deletar(int): boolean
        + buscar_por_login(String): Usuario
    }

    class LivroDAO {
        - session: Session
        + salvar(Livro): Livro
        + buscar_por_id(int): Livro
        + buscar_todos(): List~Livro~
        + atualizar(Livro): Livro
        + deletar(int): boolean
        + buscar_por_titulo(String): Livro
    }

    class EmprestimoDAO {
        - session: Session
        + salvar(Emprestimo): Emprestimo
        + atualizar(Emprestimo): Emprestimo
        + deletar(int): boolean
        + buscar_todos(): List~Emprestimo~
        + buscar_por_id(int): Emprestimo
        + buscar_ativos_por_id_usuario(int): List~Emprestimo~
    }

    GenericDAO <|.. UsuarioDAO : realiza
    GenericDAO <|.. LivroDAO : realiza
    GenericDAO <|.. EmprestimoDAO : realiza
    
    UsuarioDAO ..> Usuario : mapeia
    LivroDAO ..> Livro : mapeia
    EmprestimoDAO ..> Emprestimo : mapeia

    class UsuarioController {
        <<control>>
        - bycrypt_context: CryptContext
        + cadastrar_usuario(String, String, String, String, TipoUsuario): Usuario
        + efetuar_login(String, String): Usuario
        + listar_usuarios_ativos(): List~Usuario~
        + deletar_usuario(int): boolean
    }

    class LivroController {
        <<control>>
        + cadastrar_livro(String, String, int): Livro
        + listar_livros(): List~Livro~
        + atualizar_livro(int, String, String, int): Livro
        + deletar_livro(int): boolean
        + importar_livros_string_json(String): int
    }

    class EmprestimoController {
        <<control>>
        + realizar_emprestimo(int, int): Emprestimo
        + devolver_livro(int): Emprestimo
        + listar_emprestimo_usuario(int): List~Emprestimo~
    }

    UsuarioController --> UsuarioDAO : usa
    LivroController --> LivroDAO : usa
    EmprestimoController --> EmprestimoDAO : usa

    class LoginView {
        <<boundary>>
        + login()
        + voltar()
    }

    class CadastroUsuarioView {
        <<boundary>>
        + cadastrar()
        + limpar_campos()
        + voltar()
    }

    class LivrosView {
        <<boundary>>
        + atualizar_tabela(List)
        + buscar()
        + abrir_cadastro_livro()
        + abrir_gerenciar_livros()
        + gerenciar_usuarios()
        + alugar_livro_selecionado()
        + ver_meus_emprestimos()
        + abrir_sobre()
        + fechar_sistema_completo()
        + voltar_login()
        + recarregar_livros()
    }

    class CadastroLivroView {
        <<boundary>>
        + setup_aba_manual()
        + setup_aba_json()
        + cadastrar_manual()
        + limpar_manual()
        + importar_json()
        + voltar()
    }

    class GerenciarLivrosView {
        <<boundary>>
        + recarregar_livros()
        + preencher_formulario(Event)
        + limpar_campos()
        + salvar_edicao()
        + excluir_livro()
        + voltar()
    }

    class GerenciarUsuariosView {
        <<boundary>>
        + recarregar_usuarios()
        + atualizar_tabela(List)
        + buscar()
        + excluir_usuario()
        + voltar()
    }

    class EmprestimoView {
        <<boundary>>
        + devolver_livro()
        + atualizar_tabela(List)
        + voltar()
    }

    class SobreView {
        <<boundary>>
        + voltar()
    }

    LoginView --> UsuarioController : invoca
    CadastroUsuarioView --> UsuarioController : invoca
    LivrosView --> LivroController : invoca
    LivrosView --> EmprestimoController : invoca
    CadastroLivroView --> LivroController : invoca
    GerenciarLivrosView --> LivroController : invoca
    GerenciarUsuariosView --> UsuarioController : invoca
    EmprestimoView --> EmprestimoController : invoca

    class PermissaoStrategy {
        <<abstract>>
        + renderizar_botoes(Frame, LivrosView)*
    }

    class PermissaoAdmin {
        + renderizar_botoes(Frame, LivrosView)
    }

    class PermissaoComum {
        + renderizar_botoes(Frame, LivrosView)
    }

    class StrategyFactory {
        + obter_estrategia(TipoUsuario)$ PermissaoStrategy
    }

    PermissaoStrategy <|.. PermissaoAdmin : realiza
    PermissaoStrategy <|.. PermissaoComum : realiza
    StrategyFactory ..> PermissaoStrategy : instancia
    StrategyFactory ..> TipoUsuario : avalia
    LivrosView ..> StrategyFactory : utiliza
```

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

* **Auxílio na modelagem dos diagramas.**

**Aprendizado com o uso da IA:**
O maior aprendizado foi entender como o Tkinter funciona.