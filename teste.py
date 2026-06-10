import os
import sys
import json

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from dao.map import mapear_tabelas
from controllers.livro_controller import LivroController

dados_json = [
  {
    "titulo": "Bhagavad Gita",
    "autor": "Kṛṣṇa Dvaipayana",
    "qtd": 1
  }, 
  {
    "titulo": "1984",
    "autor": "George Orwell",
    "qtd": 5
  },
  {
    "titulo": "Dom Quixote",
    "autor": "Miguel de Cervantes",
    "qtd": 2
  },
  {
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "qtd": 3
  },
  {
    "titulo": "O Pequeno Príncipe",
    "autor": "Antoine de Saint-Exupéry",
    "qtd": 4
  },
  {
    "titulo": "A Revolução dos Bichos",
    "autor": "George Orwell",
    "qtd": 3
  },
  {
    "titulo": "Cem Anos de Solidão",
    "autor": "Gabriel García Márquez",
    "qtd": 2
  },
  {
    "titulo": "O Alquimista",
    "autor": "Paulo Coelho",
    "qtd": 5
  },
  {
    "titulo": "Harry Potter e a Pedra Filosofal",
    "autor": "J.K. Rowling",
    "qtd": 4
  },
  {
    "titulo": "O Código Da Vinci",
    "autor": "Dan Brown",
    "qtd": 3
  },
  {
    "titulo": "Memórias Póstumas de Brás Cubas",
    "autor": "Machado de Assis",
    "qtd": 5
  },
  {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "qtd": 4
  },
  {
    "titulo": "O Cortiço",
    "autor": "Aluísio Azevedo",
    "qtd": 3
  },
  {
    "titulo": "Vidas Secas",
    "autor": "Graciliano Ramos",
    "qtd": 2
  },
  {
    "titulo": "Grande Sertão: Veredas",
    "autor": "João Guimarães Rosa",
    "qtd": 1
  },
  {
    "titulo": "A Hora da Estrela",
    "autor": "Clarice Lispector",
    "qtd": 3
  },
  {
    "titulo": "O Auto da Compadecida",
    "autor": "Ariano Suassuna",
    "qtd": 4
  },
  {
    "titulo": "Ensaio sobre a Cegueira",
    "autor": "José Saramago",
    "qtd": 2
  },
  {
    "titulo": "Os Miseráveis",
    "autor": "Victor Hugo",
    "qtd": 1
  },
  {
    "titulo": "Crime e Castigo",
    "autor": "Fiódor Dostoiévski",
    "qtd": 2
  },
  {
    "titulo": "Os Irmãos Karamázov",
    "autor": "Fiódor Dostoiévski",
    "qtd": 1
  },
  {
    "titulo": "Orgulho e Preconceito",
    "autor": "Jane Austen",
    "qtd": 4
  },
  {
    "titulo": "O Morro dos Ventos Uivantes",
    "autor": "Emily Brontë",
    "qtd": 2
  },
  {
    "titulo": "Jane Eyre",
    "autor": "Charlotte Brontë",
    "qtd": 2
  },
  {
    "titulo": "Frankenstein",
    "autor": "Mary Shelley",
    "qtd": 3
  },
  {
    "titulo": "Drácula",
    "autor": "Bram Stoker",
    "qtd": 3
  },
  {
    "titulo": "O Médico e o Monstro",
    "autor": "Robert Louis Stevenson",
    "qtd": 2
  },
  {
    "titulo": "O Retrato de Dorian Gray",
    "autor": "Oscar Wilde",
    "qtd": 4
  },
  {
    "titulo": "Alice no País das Maravilhas",
    "autor": "Lewis Carroll",
    "qtd": 5
  },
  {
    "titulo": "As Aventuras de Sherlock Holmes",
    "autor": "Arthur Conan Doyle",
    "qtd": 4
  },
  {
    "titulo": "O Hobbit",
    "autor": "J.R.R. Tolkien",
    "qtd": 5
  },
  {
    "titulo": "As Crônicas de Nárnia",
    "autor": "C.S. Lewis",
    "qtd": 3
  },
  {
    "titulo": "A Guerra dos Tronos",
    "autor": "George R.R. Martin",
    "qtd": 2
  },
  {
    "titulo": "O Nome do Vento",
    "autor": "Patrick Rothfuss",
    "qtd": 2
  },
  {
    "titulo": "Duna",
    "autor": "Frank Herbert",
    "qtd": 3
  },
  {
    "titulo": "Fundação",
    "autor": "Isaac Asimov",
    "qtd": 2
  },
  {
    "titulo": "Eu, Robô",
    "autor": "Isaac Asimov",
    "qtd": 4
  },
  {
    "titulo": "Admirável Mundo Novo",
    "autor": "Aldous Huxley",
    "qtd": 3
  },
  {
    "titulo": "Fahrenheit 451",
    "autor": "Ray Bradbury",
    "qtd": 4
  },
  {
    "titulo": "O Guia do Mochileiro das Galáxias",
    "autor": "Douglas Adams",
    "qtd": 5
  },
  {
    "titulo": "Blade Runner",
    "autor": "Philip K. Dick",
    "qtd": 2
  },
  {
    "titulo": "Neuromancer",
    "autor": "William Gibson",
    "qtd": 1
  },
  {
    "titulo": "O Conto da Aia",
    "autor": "Margaret Atwood",
    "qtd": 3
  },
  {
    "titulo": "A Ilha do Tesouro",
    "autor": "Robert Louis Stevenson",
    "qtd": 2
  },
  {
    "titulo": "Vinte Mil Léguas Submarinas",
    "autor": "Júlio Verne",
    "qtd": 3
  },
  {
    "titulo": "A Volta ao Mundo em 80 Dias",
    "autor": "Júlio Verne",
    "qtd": 4
  },
  {
    "titulo": "Viagem ao Centro da Terra",
    "autor": "Júlio Verne",
    "qtd": 2
  },
  {
    "titulo": "Moby Dick",
    "autor": "Herman Melville",
    "qtd": 1
  },
  {
    "titulo": "O Velho e o Mar",
    "autor": "Ernest Hemingway",
    "qtd": 3
  },
  {
    "titulo": "O Grande Gatsby",
    "autor": "F. Scott Fitzgerald",
    "qtd": 2
  },
  {
    "titulo": "O Sol é para Todos",
    "autor": "Harper Lee",
    "qtd": 4
  },
  {
    "titulo": "O Apanhador no Campo de Centeio",
    "autor": "J.D. Salinger",
    "qtd": 3
  },
  {
    "titulo": "A Metamorfose",
    "autor": "Franz Kafka",
    "qtd": 5
  },
  {
    "titulo": "O Processo",
    "autor": "Franz Kafka",
    "qtd": 2
  },
  {
    "titulo": "A Divina Comédia",
    "autor": "Dante Alighieri",
    "qtd": 1
  },
  {
    "titulo": "A Ilíada",
    "autor": "Homero",
    "qtd": 2
  },
  {
    "titulo": "A Odisseia",
    "autor": "Homero",
    "qtd": 2
  },
  {
    "titulo": "A Arte da Guerra",
    "autor": "Sun Tzu",
    "qtd": 4
  },
  {
    "titulo": "O Príncipe",
    "autor": "Nicolau Maquiavel",
    "qtd": 3
  },
  {
    "titulo": "Meditações",
    "autor": "Marco Aurélio",
    "qtd": 2
  },
  {
    "titulo": "Assim Falou Zaratustra",
    "autor": "Friedrich Nietzsche",
    "qtd": 1
  },
  {
    "titulo": "A República",
    "autor": "Platão",
    "qtd": 1
  },
  {
    "titulo": "O Banquete",
    "autor": "Platão",
    "qtd": 2
  },
  {
    "titulo": "Ética a Nicômaco",
    "autor": "Aristóteles",
    "qtd": 1
  },
  {
    "titulo": "Tao Te Ching",
    "autor": "Laozi",
    "qtd": 3
  },
  {
    "titulo": "Sapiens: Uma Breve História da Humanidade",
    "autor": "Yuval Noah Harari",
    "qtd": 5
  },
  {
    "titulo": "Homo Deus",
    "autor": "Yuval Noah Harari",
    "qtd": 3
  },
  {
    "titulo": "O Poder do Hábito",
    "autor": "Charles Duhigg",
    "qtd": 4
  },
  {
    "titulo": "Rápido e Devagar",
    "autor": "Daniel Kahneman",
    "qtd": 2
  },
  {
    "titulo": "Uma Breve História do Tempo",
    "autor": "Stephen Hawking",
    "qtd": 2
  },
  {
    "titulo": "Cosmos",
    "autor": "Carl Sagan",
    "qtd": 4
  },
  {
    "titulo": "O Mundo Assombrado pelos Demônios",
    "autor": "Carl Sagan",
    "qtd": 3
  },
  {
    "titulo": "A Origem das Espécies",
    "autor": "Charles Darwin",
    "qtd": 1
  },
  {
    "titulo": "O Gene Egoísta",
    "autor": "Richard Dawkins",
    "qtd": 2
  },
  {
    "titulo": "Sítio do Picapau Amarelo",
    "autor": "Monteiro Lobato",
    "qtd": 5
  },
  {
    "titulo": "O Menino Maluquinho",
    "autor": "Ziraldo",
    "qtd": 4
  },
  {
    "titulo": "A Bolsa Amarela",
    "autor": "Lygia Bojunga",
    "qtd": 2
  },
  {
    "titulo": "Capitães da Areia",
    "autor": "Jorge Amado",
    "qtd": 3
  },
  {
    "titulo": "Gabriela, Cravo e Canela",
    "autor": "Jorge Amado",
    "qtd": 2
  },
  {
    "titulo": "Tieta do Agreste",
    "autor": "Jorge Amado",
    "qtd": 2
  },
  {
    "titulo": "Iracema",
    "autor": "José de Alencar",
    "qtd": 3
  },
  {
    "titulo": "O Guarani",
    "autor": "José de Alencar",
    "qtd": 2
  },
  {
    "titulo": "Triste Fim de Policarpo Quaresma",
    "autor": "Lima Barreto",
    "qtd": 3
  },
  {
    "titulo": "O Alienista",
    "autor": "Machado de Assis",
    "qtd": 5
  },
  {
    "titulo": "Macunaíma",
    "autor": "Mário de Andrade",
    "qtd": 2
  },
  {
    "titulo": "A Rosa do Povo",
    "autor": "Carlos Drummond de Andrade",
    "qtd": 1
  },
  {
    "titulo": "O Corvo",
    "autor": "Edgar Allan Poe",
    "qtd": 4
  },
  {
    "titulo": "It: A Coisa",
    "autor": "Stephen King",
    "qtd": 2
  },
  {
    "titulo": "O Iluminado",
    "autor": "Stephen King",
    "qtd": 3
  },
  {
    "titulo": "Assassinato no Expresso do Oriente",
    "autor": "Agatha Christie",
    "qtd": 4
  },
  {
    "titulo": "E Não Sobrou Nenhum",
    "autor": "Agatha Christie",
    "qtd": 5
  },
  {
    "titulo": "Os Homens que Não Amavam as Mulheres",
    "autor": "Stieg Larsson",
    "qtd": 2
  },
  {
    "titulo": "A Menina que Roubava Livros",
    "autor": "Markus Zusak",
    "qtd": 4
  },
  {
    "titulo": "O Caçador de Pipas",
    "autor": "Khaled Hosseini",
    "qtd": 3
  },
  {
    "titulo": "O Diário de Anne Frank",
    "autor": "Anne Frank",
    "qtd": 5
  },
  {
    "titulo": "A Culpa é das Estrelas",
    "autor": "John Green",
    "qtd": 3
  },
  {
    "titulo": "Jogos Vorazes",
    "autor": "Suzanne Collins",
    "qtd": 4
  },
  {
    "titulo": "Crepúsculo",
    "autor": "Stephenie Meyer",
    "qtd": 2
  },
  {
    "titulo": "Percy Jackson e o Ladrão de Raios",
    "autor": "Rick Riordan",
    "qtd": 5
  },
  {
    "titulo": "A Bússola de Ouro",
    "autor": "Philip Pullman",
    "qtd": 3
  }
]

with open("livros_teste.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_json, arquivo, ensure_ascii=False, indent=4)

mapear_tabelas()

controller = LivroController()
quantidade_inserida = controller.importar_livros_json("livros_teste.json")

print(f"Total de livros inseridos pelo JSON: {quantidade_inserida}")
print("-" * 50)

livros_banco = controller.listar_livros()
for livro in livros_banco:
    print(f"ID: {livro.id} | Titulo: {livro.titulo} | Autor: {livro.autor} | Qtd: {livro.qtd}")

os.remove("livros_teste.json")