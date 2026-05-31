# Documentação do Projeto - Gestão de Biblioteca

## 1. Descrição e Delimitação do Escopo

**Cenário do Sistema**
O sistema de Gestão de Biblioteca é uma aplicação desktop desenvolvida para informatizar e modernizar o controle de acervos e empréstimos literários. O propósito principal é substituir controles manuais ou planilhas descentralizadas por uma plataforma unificada que garanta a integridade dos dados e o controle de acesso.

O público-alvo é dividido em duas categorias: administradores (bibliotecários ou gestores) e leitores comuns. O sistema resolve o problema da falta de rastreabilidade do acervo, impedindo a perda de livros e centralizando o histórico de quem está em posse de qual obra, além de restringir ações críticas (como alterar o catálogo) apenas a funcionários autorizados.

As principais funcionalidades contemplam o controle de acesso seguro (login), o cadastro e manutenção de usuários, o gerenciamento do acervo de livros (cadastro, edição, exclusão e listagem) e o fluxo completo de empréstimos, desde a retirada até a devolução.

---

## 2. Fase de Análise

### a) Requisitos Funcionais
Abaixo estão detalhadas as funcionalidades diretas que o sistema fornecerá aos seus usuários:

* **RF01:** O sistema deve permitir o cadastro de usuários contendo nome, cpf, login, senha e tipo de permissão (administrador ou comum).
* **RF02:** O sistema deve autenticar o acesso do usuário exigindo um login e uma senha válidos cadastrados no banco de dados.
* **RF03:** O sistema deve adaptar a interface gráfica de acordo com o nível de permissão do usuário logado, ocultando ou exibindo menus específicos.
* **RF04:** O sistema deve permitir que usuários administradores cadastrem novos livros informando o título e o autor da obra.
* **RF05:** O sistema deve permitir que usuários administradores editem as informações dos livros já cadastrados.
* **RF06:** O sistema deve permitir que usuários administradores excluam livros do acervo.
* **RF07:** O sistema deve permitir a listagem de todos os livros cadastrados, incluindo uma funcionalidade de busca.
* **RF08:** O sistema deve permitir o registro de um novo empréstimo, vinculando um usuário a um livro e informando a data de retirada e a data de devolução prevista.
* **RF09:** O sistema deve permitir a atualização do status de um empréstimo para registrar a devolução de um livro.
* **RF10:** O sistema deve exibir uma tela "Sobre" contendo informações gerais do software e do desenvolvedor.

### b) Requisitos Não Funcionais
Abaixo estão as restrições técnicas, de qualidade e de arquitetura que o sistema deve respeitar:

* **RNF01 (Arquitetura):** O sistema deve ser implementado na linguagem Python, respeitando a separação de responsabilidades do padrão arquitetural MVC (Model-View-Controller).
* **RNF02 (Persistência):** Os dados devem ser obrigatoriamente persistidos em um banco de dados relacional PostgreSQL, utilizando a biblioteca SQLAlchemy para o mapeamento e comunicação.
* **RNF03 (Interface):** A aplicação deve possuir uma Interface Gráfica de Usuário (GUI) desenvolvida utilizando a biblioteca Tkinter.
* **RNF04 (Design Patterns):** A estruturação do código deve aplicar obrigatoriamente o padrão de projeto Data Access Object (DAO) para o acesso a dados e o padrão Strategy para o gerenciamento de permissões de interface.
* **RNF05 (Validação):** O sistema deve garantir a unicidade de registros críticos no banco de dados, não permitindo o cadastro de CPFs ou logins duplicados.

### c) Regras de Negócio
Abaixo estão as restrições lógicas e operacionais específicas do domínio da biblioteca:

* **RN01:** Um livro não pode ser excluído do sistema se possuir um registro de empréstimo ativo vinculado a ele, garantindo a integridade referencial do histórico no banco de dados.
* **RN02:** O sistema deve garantir que o botão e a funcionalidade de "Cadastrar Livro" sejam absolutamente inacessíveis para usuários que tenham efetuado login com o perfil "comum".