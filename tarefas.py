# Sistema de Gerenciamento de Tarefas utilizando Programação Funcional

# Closure para gerar IDs automáticos
def gerador_id():
    contador = 0
    def proximo_id():
        nonlocal contador
        contador += 1
        return contador
    return proximo_id

# Criando instância do gerador de ID
gerar_id = gerador_id()

# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar tarefas
def adicionar_tarefa(descricao, categoria, status="pendente"):
    tarefa = {
        "id": gerar_id(),
        "descricao": descricao,
        "categoria": categoria,
        "status": status
    }
    tarefas.append(tarefa)

# Função para listar todas as tarefas
def listar_tarefas():
    return [f"ID: {t['id']} | Descrição: {t['descricao']} | Categoria: {t['categoria']} | Status: {t['status']}" for t in tarefas]

# Função de alta ordem para filtrar tarefas
def filtrar_tarefas(criterio):
    return list(filter(criterio, tarefas))

# Função para remover tarefas concluídas
def remover_concluidas():
    global tarefas
    tarefas[:] = [t for t in tarefas if t["status"] != "concluída"]

# --- Testes ---
if __name__ == "__main__":
    # Adicionando tarefas
    adicionar_tarefa("Estudar Python", "Estudos")
    adicionar_tarefa("Fazer exercícios", "Saúde", "em andamento")
    adicionar_tarefa("Finalizar projeto", "Trabalho", "concluída")
    
    # Listando tarefas
    print("\nTodas as Tarefas:")
    print("\n".join(listar_tarefas()))
    
    # Filtrando tarefas pendentes
    print("\nTarefas Pendentes:")
    print("\n".join([str(t) for t in filtrar_tarefas(lambda t: t["status"] == "pendente")]))
    
    # Removendo concluídas
    remover_concluidas()
    print("\nTarefas Após Remover Concluídas:")
    print("\n".join(listar_tarefas()))




