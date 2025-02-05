# Framework CRUD Simples em Java

Este é um framework simples para operações CRUD genéricas em Java, utilizando Generics para permitir a reutilização de código para diferentes tipos de entidades. Ele oferece suporte para armazenar dados tanto em memória quanto em arquivos.

## 🚀 Funcionalidades

- 📌 Implementação de uma interface genérica `CrudRepository<T>`.
- 🛠 Implementações concretas:
  - `InMemoryRepository<T>`: Armazena dados temporariamente em uma estrutura de dados (Map).
  - `InFileRepository<T>`: Persiste os dados em um arquivo JSON.
- 📂 Entidades de exemplo (`Produto` e `Cliente`).
- 🔧 Programa principal demonstrando o uso do framework.
- 🏗 Empacotamento como `.jar` para fácil distribuição.

## 📂 Estrutura do Projeto

```
📂 MeuFrameworkJava/
│── 📂 src/
│   ├── 📂 entities/
│   │   ├── Cliente.java
│   │   ├── Produto.java
│   ├── 📂 repository/
│   │   ├── CrudRepository.java
│   │   ├── InMemoryRepository.java
│   │   ├── InFileRepository.java
│   ├── 📂 main/
│   │   ├── Main.java
│── 📂 target/  (gerado após compilar)
│── pom.xml
│── README.md
│── produtos.json  (caso já tenha testado)
│── clientes.json  (caso já tenha testado)
```

## 🔧 Como Configurar e Rodar

### 1️⃣ Clonar o repositório

```sh
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio
```

### 2️⃣ Compilar e gerar o JAR

Se estiver usando **Maven**, execute:

```sh
mvn clean package
```

Isso criará um `.jar` dentro da pasta `target/`.

### 3️⃣ Executar o programa

```sh
java -jar target/framework-java-1.0-SNAPSHOT-jar-with-dependencies.jar
```

## 🚀 Exemplo de Uso

### Criando e salvando produtos em memória

```java
InMemoryRepository<Produto> repo = new InMemoryRepository<>();
repo.save(new Produto("Notebook", 3500.0));
repo.findAll().forEach(System.out::println);
```

### Salvando clientes em arquivo JSON

```java
InFileRepository<Cliente> clienteRepo = new InFileRepository<>("clientes.json");
clienteRepo.save(new Cliente("João Silva", "joao@email.com"));
clienteRepo.findAll().forEach(System.out::println);
```


## 🛠 Tecnologias Utilizadas

- **Java 11+**
- **Maven** (Gerenciador de dependências)
- **Gson** (Manipulação de JSON)

