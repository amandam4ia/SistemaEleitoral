# Projeto Sistema Eleitoral



## Sobre o Projeto



## Recursos Utilizados

* Django 4.2.2
* Python 3.x
* SQLite
* HTML/CSS/Bootstrap

## Funcionalidades



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

6. **Carregue os dados iniciais de cidades e cursos**

```bash
python manage.py loaddata dados_iniciais.json
```

7. **Inicie o servidor**

```bash
python manage.py runserver
```

Agora, o sistema estará disponível em `http://localhost:8000`.