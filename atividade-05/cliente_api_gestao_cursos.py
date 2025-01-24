import requests

BASE_URL = "http://127.0.0.1:8000/cursos"

def listar_cursos():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Cursos cadastrados:")
        for curso in response.json():
            print(f"- {curso['titulo']}: {curso['descricao']} ({curso['carga_horaria']}h)")
    else:
        print("Erro ao listar cursos.")

def obter_curso(id):
    response = requests.get(f"{BASE_URL}/{id}")
    if response.status_code == 200:
        curso = response.json()
        print(f"Detalhes do curso {id}:")
        print(f"- Título: {curso['titulo']}")
        print(f"- Descrição: {curso['descricao']}")
        print(f"- Carga horária: {curso['carga_horaria']}h")
    else:
        print("Curso não encontrado.")

def criar_curso(titulo, descricao, carga_horaria):
    curso = {
        "titulo": titulo,
        "descricao": descricao,
        "carga_horaria": carga_horaria
    }
    response = requests.post(BASE_URL, json=curso)
    if response.status_code == 200:
        print("Curso criado com sucesso!")
    else:
        print("Erro ao criar curso.")

def atualizar_curso(id, titulo, descricao, carga_horaria):
    curso = {
        "titulo": titulo,
        "descricao": descricao,
        "carga_horaria": carga_horaria
    }
    response = requests.put(f"{BASE_URL}/{id}", json=curso)
    if response.status_code == 200:
        print("Curso atualizado com sucesso!")
    else:
        print("Erro ao atualizar curso.")

def excluir_curso(id):
    response = requests.delete(f"{BASE_URL}/{id}")
    if response.status_code == 200:
        print("Curso excluído com sucesso!")
    else:
        print("Erro ao excluir curso.")

# Exemplo de uso
if __name__ == "__main__":
    while True:
        print("\nGestão de Cursos")
        print("1. Listar cursos")
        print("2. Obter curso por ID")
        print("3. Criar curso")
        print("4. Atualizar curso")
        print("5. Excluir curso")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_cursos()
        elif opcao == "2":
            id_curso = int(input("Digite o ID do curso: "))
            obter_curso(id_curso)
        elif opcao == "3":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            carga_horaria = int(input("Carga horária (em horas): "))
            criar_curso(titulo, descricao, carga_horaria)
        elif opcao == "4":
            id_curso = int(input("Digite o ID do curso a ser atualizado: "))
            titulo = input("Novo título: ")
            descricao = input("Nova descrição: ")
            carga_horaria = int(input("Nova carga horária (em horas): "))
            atualizar_curso(id_curso, titulo, descricao, carga_horaria)
        elif opcao == "5":
            id_curso = int(input("Digite o ID do curso a ser excluído: "))
            excluir_curso(id_curso)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
