import unittest
from tarefas import tarefas, adicionar_tarefa, listar_tarefas, filtrar_tarefas, remover_concluidas

class TestGerenciamentoTarefas(unittest.TestCase):
    def setUp(self):
        # Reinicializa a lista de tarefas para cada teste
        global tarefas
        tarefas.clear()
        tarefas.extend([
            {"id": 1, "descricao": "Estudar Python", "categoria": "Estudos", "status": "pendente"},
            {"id": 2, "descricao": "Fazer exercícios", "categoria": "Saúde", "status": "em andamento"},
            {"id": 3, "descricao": "Finalizar projeto", "categoria": "Trabalho", "status": "concluída"}
        ])
    
    def test_adicionar_tarefa(self):
        adicionar_tarefa("Ler livro", "Lazer", "pendente")
        self.assertEqual(len(tarefas), 4)
        self.assertEqual(tarefas[-1]["descricao"], "Ler livro")
    
    def test_listar_tarefas(self):
        lista = listar_tarefas()
        self.assertTrue(any("Estudar Python" in t for t in lista))
        self.assertTrue(any("Fazer exercícios" in t for t in lista))
        self.assertTrue(any("Finalizar projeto" in t for t in lista))

    
    def test_filtrar_tarefas_pendentes(self):
        pendentes = filtrar_tarefas(lambda t: t["status"] == "pendente")
        self.assertEqual(len(pendentes), 1)
        self.assertEqual(pendentes[0]["descricao"], "Estudar Python")
    
    def test_remover_tarefas_concluidas(self):
        remover_concluidas()
        ids_restantes = [t["id"] for t in tarefas]
        print("IDs restantes após remoção:", ids_restantes)  # Depuração
        self.assertNotIn(3, ids_restantes)
        self.assertEqual(len(tarefas), 2)  # Deve restar apenas 2 tarefas

        
        
        

if __name__ == "__main__":
    unittest.main()






