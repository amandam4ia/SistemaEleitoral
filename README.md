# Projeto Sistema Eleitoral



## Sobre o Projeto

O sistema é consiste em uma plataforma digital de votação para instituições de ensino, com objetivo de modernizar e tornar o processo eleitoral mais seguro e eficiente. Ele garante que cada aluno tenha acesso único, permitindo apenas um voto por pessoa, sem possibilidade de alterações após o registro. Conta com níveis de acesso (administrador e eleitor), assegura a confidencialidade da escolha do voto, gerencia inscrições de chapas e realiza a apuração automática, fornecendo relatórios confiáveis para a comissão eleitoral.

## Recursos Utilizados

* Django 4.2.2
* Python 3.x
* SQLite
* HTML/CSS/Bootstrap

## Funcionalidades

CRUD de Chapas
CRUD de Eleição

## Instalação

### Pré-requisitos

Certifique-se de ter o **Python** e o **Django** instalados em seu computador com Windows.
Se ainda não tiver, instale pelo site oficial:

* [Python](https://www.python.org/downloads/)
* [Django](https://docs.djangoproject.com/en/4.2/topics/install/)

### Passos para instalação

1. **Clone o repositório**

```bash
git clone https://github.com/amandam4ia/SistemaEleitoral.git
```

2. **Crie um ambiente virtual**

```bash
python -m venv venv
```

3. **Ative o ambiente virtual**

```bash
venv\Scripts\activate
```

4. **Instale as dependências do projeto**

```bash
pip install -r requirements.txt
```

5. **Execute as migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Inicie o servidor**

```bash
python manage.py runserver
```

Agora, o sistema estará disponível em `http://localhost:8000`.