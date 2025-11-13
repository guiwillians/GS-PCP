# -*- coding: utf-8 -*-
# main.py

from sistema_carreiras import SistemaCarreiras

def main():
    """
    Função principal para inicializar e executar o sistema de orientação de carreiras.
    """
    sistema = SistemaCarreiras()
    
    while True:
        print("\n--- Ferramenta Inteligente de Orientação de Carreiras ---")
        print("1. Cadastrar Novo Perfil")
        print("2. Analisar Perfil Existente")
        print("3. Listar Perfis Cadastrados")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            sistema.cadastrar_perfil()
        elif escolha == '2':
            sistema.analisar_perfil()
        elif escolha == '3':
            sistema.listar_perfis()
        elif escolha == '4':
            print("Obrigado por usar a Ferramenta de Orientação de Carreiras. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
