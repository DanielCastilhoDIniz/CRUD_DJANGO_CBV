# CRUD Django com Class-Based Views e Paginação

Projeto simples e didático desenvolvido com **Django**, com foco em **boas práticas**, uso de **Class-Based Views (CBV)** e **paginação nativa** do framework. O objetivo é demonstrar domínio dos conceitos fundamentais do Django voltados ao backend, servindo como base para projetos maiores (ex.: sistemas administrativos ou SaaS).

---

## 🎯 Objetivo do Projeto

* Implementar um **CRUD completo** (Create, Read, Update, Delete)
* Utilizar **Class-Based Views** em vez de Function-Based Views
* Aplicar **paginação** com `ListView`
* Manter código organizado, legível e alinhado às boas práticas do Django

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Django 4/5/6** (compatível)
* **SQLite** (banco padrão para desenvolvimento)
* **HTML + Django Templates**
* **Bootstrap** (opcional, para estilização)

---

## 📂 Estrutura do Projeto

A organização do projeto segue o padrão recomendado pelo Django, separando claramente **configuração**, **lógica de negócio**, **templates** e **persistência de dados**.

```text
CRUD-DJANGO/
│
├── core/                     # App principal do projeto
│   ├── migrations/           # Migrações do banco de dados
│   ├── templates/            # Templates HTML
│   │   ├── base.html         # Template base
│   │   ├── navbar.html       # Barra de navegação
│   │   ├── index.html        # Listagem de produtos
│   │   ├── paginacao.html    # Componente de paginação
│   │   ├── produto_form.html # Criação e edição
│   │   └── produto_del.html  # Confirmação de exclusão
│   ├── admin.py              # Registro de models no admin
│   ├── apps.py               # Configuração do app
│   ├── forms.py              # Forms (extensível para validações)
│   ├── models.py             # Model Produto
│   ├── tests.py              # Testes automatizados
│   ├── urls.py               # Rotas do app
│   └── views.py              # Views baseadas em classes (CBV)
│
├── crudCBV/                  # Configuração do projeto
│   ├── settings.py           # Configurações globais
│   ├── urls.py               # URLs principais
│   ├── asgi.py               # ASGI
│   └── wsgi.py               # WSGI
│
├── db.sqlite3                # Banco de dados (desenvolvimento)
├── manage.py                 # CLI do Django
└── venv/                     # Ambiente virtual
```

Essa estrutura favorece:

* Manutenção
* Escalabilidade
* Clareza arquitetural

---

## 📦 Model

O projeto utiliza um model simples `Produto`, representando uma entidade típica de sistemas CRUD.

Exemplo de campos:

* `nome`
* `preço`

---

### Model

O projeto utiliza um model simples `Produto`, representando uma entidade típica de sistemas CRUD.

Exemplo de campos:

* `nome`
* `preço`

---

## 🔁 Views (CBV)

### 📄 Listagem com Paginação

* Implementada com `ListView`
* Paginação configurada com `paginate_by = 3`
* Ordenação explícita por `id`

Responsabilidades:

* Exibir a lista de produtos
* Controlar navegação entre páginas

---

### ➕ Criação de Produto

* Implementada com `CreateView`
* Uso de `reverse_lazy` para redirecionamento seguro

---

### ✏️ Atualização de Produto

* Implementada com `UpdateView`
* Reutilização do mesmo template de formulário

---

### 🗑️ Exclusão de Produto

* Implementada com `DeleteView`
* Tela de confirmação antes da exclusão

---

## 📄 Templates

O projeto utiliza templates separados para cada responsabilidade:

* `index.html` → listagem + paginação
* `produto_form.html` → criação e edição
* `produto_del.html` → confirmação de exclusão

Essa separação melhora:

* Clareza
* Manutenção
* Reutilização

---

## 📑 Paginação

A paginação é feita nativamente pelo Django:

* Controle automático de páginas
* Suporte a navegação (anterior / próxima)
* Ideal para listas grandes

---

## 🚀 Como Executar o Projeto

1. Criar e ativar um ambiente virtual
2. Instalar as dependências
3. Aplicar as migrações
4. Criar superusuário (opcional)
5. Executar o servidor

---

## 🧠 Conceitos Demonstrados

* Class-Based Views (CBV)
* Reuso de templates
* Paginação eficiente
* Organização de responsabilidades
* Fluxo CRUD completo

---

## 📈 Possíveis Extensões

Este projeto pode evoluir facilmente para:

* Autenticação e permissões
* API REST com Django REST Framework
* Integração com frontend moderno (React / Vue)
* Controle de estoque
* Projeto SaaS educacional ou administrativo

---

## 📌 Observações Finais

Este projeto tem caráter **educacional e técnico**, focado no domínio do Django backend. Ele serve como uma base sólida para projetos maiores e demonstra compreensão prática dos principais recursos do framework.

---

📚 Referências Oficiais:

* [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
* [https://docs.djangoproject.com/en/stable/topics/class-based-views/](https://docs.djangoproject.com/en/stable/topics/class-based-views/)
* [https://docs.djangoproject.com/en/stable/topics/pagination/](https://docs.djangoproject.com/en/stable/topics/pagination/)
