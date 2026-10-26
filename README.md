<div align="center">

# 🐍 Minha jornada no Python

**Do `print('olá, mundo')` a um sistema de cadastro com pacotes e arquivos.**<br>
Todos os exercícios e aulas que fiz no curso de Python do **Curso em Vídeo** (Prof. Gustavo Guanabara), organizados por módulo.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Desafios](https://img.shields.io/badge/desafios-115%20resolvidos-2ea44f?style=for-the-badge)
![Módulos](https://img.shields.io/badge/módulos-3%20de%203-blueviolet?style=for-the-badge)
![Licença](https://img.shields.io/badge/licença-MIT-lightgrey?style=for-the-badge)

</div>

---

## 👋 Sobre este repositório

Foi aqui que comecei a programar em Python, em 2022. Cada arquivo é um passo do caminho: as **aulas** são os testes que eu fazia enquanto assistia, e os **desafios** são os exercícios que resolvi sozinho no fim de cada aula.

Hoje trabalho como **Analista de Dados** e uso Python no dia a dia (pandas, Streamlit, automação de relatórios). Guardo este repositório como registro de onde tudo começou — e como prova de que a base faz diferença.

## 🗺️ Trilha percorrida

| Módulo | Assuntos | Aulas do curso | Desafios |
|:--|:--|:--:|:--:|
| [**Módulo 1** — Fundamentos](modulo%201) | `print`/`input`, tipos primitivos, operadores aritméticos, módulos (`math`, `random`), manipulação de strings, condições `if/else`, cores no terminal | 4 a 11 | [001 – 035](modulo%201/desafios) |
| [**Módulo 2** — Estruturas de controle](modulo%202) | condições aninhadas (`elif`), laço `for` com `range`, laço `while`, `while True` com `break` | 12 a 15 | [036 – 071](modulo%202/desafios) |
| [**Módulo 3** — Estruturas compostas e funções](modulo%203) | tuplas, listas, dicionários, funções, docstrings, módulos e pacotes, tratamento de erros (`try/except`) | 16 a 23 | [072 – 115](modulo%203/desafios) |

**Progresso:** ██████████████████████ 115 / 115 desafios ✅

## ⭐ Destaques

Alguns exercícios que mostram bem a evolução:

| Desafio | O que faz | Conceitos |
|:--|:--|:--|
| [035](modulo%201/desafios/desafio%2035.py) | Diz se três retas podem formar um triângulo | condições, operadores lógicos |
| [071](modulo%202/desafios/desafio%2071.py) | Simula um **caixa eletrônico** que entrega o menor número de cédulas | `while True`, controle de fluxo |
| [107 – 110](modulo%203/desafios/desafio%20107) | Módulo `moeda` com aumento, redução, dobro, metade e um **resumo formatado** em R$ | criação de módulos, parâmetros opcionais, f-strings |
| [111 – 112](modulo%203/desafios/desafio%20111) | Pacote `utilsCEV` que lê valores em reais (aceita vírgula) e gera o resumo | pacotes, `__init__.py`, validação de entrada |
| [113](modulo%203/desafios/desafio%20113.py) | Funções `leiaInt()` e `leiaFloat()` que não quebram com entrada inválida nem com Ctrl+C | `try/except`, `ValueError`, `KeyboardInterrupt` |
| [115](modulo%203/desafios/desafio%20115) | 🏆 **Sistema de cadastro de pessoas** com menu colorido, gravação e leitura em arquivo `.txt` | pacotes, arquivos, `match/case`, tratamento de erros |

## 📁 Estrutura

```
python/
├── modulo 1/
│   ├── aulas/       # testes feitos durante as aulas 4 a 11
│   └── desafios/    # desafios 001 a 035
├── modulo 2/
│   ├── aulas/       # aulas 12 a 15
│   └── desafios/    # desafios 036 a 071
└── modulo 3/
    ├── aulas/       # aulas 16 a 22 (inclui exemplos de módulos e pacotes)
    └── desafios/    # desafios 072 a 115 (os maiores estão em pastas próprias)
```

O nome de cada arquivo segue o número da aula ou do desafio no curso (ex.: `aula 17.3.py` é o 3º teste da aula 17).

## ▶️ Como rodar

Precisa do **Python 3.12 ou mais recente** (alguns desafios usam `match/case` e f-strings com aspas aninhadas).

```bash
git clone https://github.com/mateusrosa0901/python.git
cd python

# um desafio simples
python "modulo 1/desafios/desafio 35.py"

# desafios em pasta (pacotes): entre na pasta antes de rodar
cd "modulo 3/desafios/desafio 115"
python index.py
```

> Os nomes de pasta têm espaços, por isso as aspas nos comandos.

## 🧠 O que ficou desse estudo

- **Lógica primeiro:** quebrar o problema em passos antes de pensar na sintaxe.
- **Não confiar na entrada:** validar o que o usuário digita (`try/except`, laços até vir um valor válido).
- **Organizar conforme cresce:** de scripts soltos para funções, depois módulos e pacotes.
- **Saída que se lê bem:** tabelas alinhadas, cores e mensagens claras para quem usa o programa.

## 🔗 Créditos e contato

- Curso: [Python — Curso em Vídeo](https://www.cursoemvideo.com/curso/python-3-mundo-1/), do Prof. Gustavo Guanabara.
- Mais projetos meus: [github.com/mateusrosa0901](https://github.com/mateusrosa0901)

<div align="center">

Feito com ☕ e muitos `print()` por **Mateus Rosa**

</div>
