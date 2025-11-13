# -*- coding: utf-8 -*-
# sistema_carreiras.py

from typing import List, Dict, Tuple

# --- Classes de Modelo de Dados ---

class Competencia:
    """
    Representa uma competência, que pode ser técnica ou comportamental.
    """
    def __init__(self, nome: str, tipo: str):
        """
        Inicializa uma nova competência.
        :param nome: Nome da competência (ex: 'Lógica', 'Criatividade').
        :param tipo: Tipo da competência ('tecnica' ou 'comportamental').
        """
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return f"{self.nome} ({self.tipo.capitalize()})"

class Carreira:
    """
    Representa uma carreira profissional e as competências-chave associadas.
    """
    def __init__(self, nome: str, descricao: str, competencias_chave: Dict[str, int]):
        """
        Inicializa uma nova carreira.
        :param nome: Nome da carreira (ex: 'Cientista de Dados').
        :param descricao: Breve descrição da carreira.
        :param competencias_chave: Dicionário de competências e o peso ideal (1 a 5).
        """
        self.nome = nome
        self.descricao = descricao
        self.competencias_chave = competencias_chave # {'nome_competencia': peso_ideal}

    def __str__(self):
        return f"{self.nome}: {self.descricao}"

class Perfil:
    """
    Representa um perfil profissional com suas competências avaliadas.
    """
    def __init__(self, nome: str, rm: str, avaliacoes: Dict[str, int]):
        """
        Inicializa um novo perfil.
        :param nome: Nome completo do profissional.
        :param rm: Registro de Matrícula (RM) ou identificador.
        :param avaliacoes: Dicionário de competências e a avaliação do perfil (1 a 5).
        """
        self.nome = nome
        self.rm = rm
        self.avaliacoes = avaliacoes # {'nome_competencia': nota_perfil}

    def __str__(self):
        return f"Perfil: {self.nome} (RM: {self.rm})"

# --- Classe Principal do Sistema ---

class SistemaCarreiras:
    """
    Gerencia as competências, carreiras e perfis, e realiza a análise e recomendação.
    """
    def __init__(self):
        """
        Inicializa o sistema com dados pré-definidos (simulando um banco de dados).
        """
        # Lista de objetos Competencia
        self.competencias: List[Competencia] = self._carregar_competencias()
        
        # Lista de objetos Carreira
        self.carreiras: List[Carreira] = self._carregar_carreiras()
        
        # Dicionário de objetos Perfil, usando o RM como chave
        self.perfis: Dict[str, Perfil] = {}

    def _carregar_competencias(self) -> List[Competencia]:
        """
        Carrega as competências técnicas e comportamentais iniciais.
        """
        dados_competencias: Tuple[Tuple[str, str], ...] = (
            ("Lógica de Programação", "tecnica"),
            ("Estrutura de Dados", "tecnica"),
            ("Orientação a Objetos", "tecnica"),
            ("Criatividade", "comportamental"),
            ("Colaboração", "comportamental"),
            ("Adaptabilidade", "comportamental"),
            ("Comunicação", "comportamental"),
        )
        return [Competencia(nome, tipo) for nome, tipo in dados_competencias]

    def _carregar_carreiras(self) -> List[Carreira]:
        """
        Carrega as carreiras e suas competências-chave ideais.
        """
        # Os pesos (1 a 5) representam a importância da competência para a carreira.
        dados_carreiras: Tuple[Tuple[str, str, Dict[str, int]], ...] = (
            ("Desenvolvedor Backend", 
             "Foco na lógica de servidor, APIs e banco de dados.",
             {"Lógica de Programação": 5, "Estrutura de Dados": 4, "Orientação a Objetos": 5, 
              "Criatividade": 2, "Colaboração": 4, "Adaptabilidade": 3, "Comunicação": 3}),
            
            ("UX/UI Designer", 
             "Foco na experiência do usuário e design de interfaces.",
             {"Lógica de Programação": 2, "Estrutura de Dados": 1, "Orientação a Objetos": 2, 
              "Criatividade": 5, "Colaboração": 4, "Adaptabilidade": 5, "Comunicação": 4}),
              
            ("Cientista de Dados", 
             "Foco em análise de dados, estatística e modelos preditivos.",
             {"Lógica de Programação": 4, "Estrutura de Dados": 5, "Orientação a Objetos": 3, 
              "Criatividade": 3, "Colaboração": 3, "Adaptabilidade": 4, "Comunicação": 3}),
              
            ("Gerente de Projetos", 
             "Foco em planejamento, execução e gestão de equipes.",
             {"Lógica de Programação": 3, "Estrutura de Dados": 2, "Orientação a Objetos": 2, 
              "Criatividade": 4, "Colaboração": 5, "Adaptabilidade": 5, "Comunicação": 5}),
        )
        
        return [Carreira(nome, desc, comp) for nome, desc, comp in dados_carreiras]

    def cadastrar_perfil(self):
        """
        Coleta dados do usuário via CLI e cadastra um novo Perfil.
        """
        print("\n--- Cadastro de Novo Perfil ---")
        nome = input("Nome Completo: ")
        rm = input("RM (Registro de Matrícula): ")
        
        if rm in self.perfis:
            print(f"Erro: Já existe um perfil cadastrado com o RM {rm}.")
            return

        avaliacoes: Dict[str, int] = {}
        print("\nAvalie cada competência de 1 (Baixo) a 5 (Alto):")
        
        for comp in self.competencias:
            while True:
                try:
                    nota = int(input(f"Nota para {comp.nome} ({comp.tipo.capitalize()}): "))
                    if 1 <= nota <= 5:
                        avaliacoes[comp.nome] = nota
                        break
                    else:
                        print("A nota deve ser entre 1 e 5.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        
        novo_perfil = Perfil(nome, rm, avaliacoes)
        self.perfis[rm] = novo_perfil
        print(f"\nPerfil de {nome} cadastrado com sucesso!")

    def listar_perfis(self):
        """
        Lista todos os perfis cadastrados.
        """
        if not self.perfis:
            print("\nNenhum perfil cadastrado ainda.")
            return
            
        print("\n--- Perfis Cadastrados ---")
        for rm, perfil in self.perfis.items():
            print(f"- {perfil.nome} (RM: {rm})")

    def analisar_perfil(self):
        """
        Solicita um RM e realiza a análise e recomendação de carreira.
        """
        if not self.perfis:
            print("\nNenhum perfil cadastrado para análise. Cadastre um primeiro.")
            return
            
        self.listar_perfis()
        rm_analise = input("\nDigite o RM do perfil que deseja analisar: ")
        
        if rm_analise not in self.perfis:
            print(f"Erro: Perfil com RM {rm_analise} não encontrado.")
            return
            
        perfil = self.perfis[rm_analise]
        print(f"\n--- Análise de Perfil para {perfil.nome} ---")
        
        # 1. Calcular a pontuação de adequação para cada carreira
        pontuacoes_carreiras: List[Tuple[str, float]] = []
        
        for carreira in self.carreiras:
            pontuacao_total = 0
            peso_total = 0
            
            # Itera sobre as competências-chave da carreira
            for comp_nome, peso_ideal in carreira.competencias_chave.items():
                # Pega a nota do perfil para aquela competência
                nota_perfil = perfil.avaliacoes.get(comp_nome, 0) # 0 se não avaliada
                
                # O cálculo de adequação é a nota do perfil multiplicada pelo peso ideal
                # Isso prioriza carreiras que exigem competências onde o perfil é forte.
                pontuacao_competencia = nota_perfil * peso_ideal
                
                pontuacao_total += pontuacao_competencia
                peso_total += peso_ideal
            
            # Evita divisão por zero
            if peso_total > 0:
                # Normaliza a pontuação para uma escala de 1 a 5 (média ponderada)
                adequacao = pontuacao_total / peso_total
                pontuacoes_carreiras.append((carreira.nome, adequacao))
            
        # 2. Ordenar as carreiras pela pontuação de adequação (do maior para o menor)
        pontuacoes_carreiras.sort(key=lambda item: item[1], reverse=True)
        
        # 3. Gerar Recomendações
        
        # Recomendação de Carreira Principal
        carreira_principal, pontuacao_principal = pontuacoes_carreiras[0]
        print(f"\n**Recomendação de Carreira Principal:** {carreira_principal}")
        print(f"Pontuação de Adequação: {pontuacao_principal:.2f} (em 5.0)")
        
        # Recomendação de Aprimoramento (Competências com maior diferença negativa)
        print("\n**Recomendações de Aprimoramento:**")
        
        # Encontra a carreira principal (objeto Carreira)
        carreira_obj = next(c for c in self.carreiras if c.nome == carreira_principal)
        
        diferencas: List[Tuple[str, int]] = []
        for comp_nome, peso_ideal in carreira_obj.competencias_chave.items():
            nota_perfil = perfil.avaliacoes.get(comp_nome, 0)
            
            # Se a nota do perfil for significativamente menor que o peso ideal (importância)
            # A diferença negativa indica uma área de melhoria
            diferenca = peso_ideal - nota_perfil
            if diferenca > 1: # Foca em gaps maiores que 1 ponto
                diferencas.append((comp_nome, diferenca))
                
        diferencas.sort(key=lambda item: item[1], reverse=True)
        
        if diferencas:
            print(f"Para se destacar como {carreira_principal}, foque em aprimorar:")
            for comp_nome, diferenca in diferencas[:3]: # Top 3 gaps
                print(f"- {comp_nome} (Gap de {diferenca} pontos)")
        else:
            print(f"Seu perfil já está bem alinhado com as competências-chave de {carreira_principal}!")
            
        # Outras Carreiras Sugeridas
        print("\n**Outras Carreiras Sugeridas:**")
        for nome, pontuacao in pontuacoes_carreiras[1:3]: # Próximas 2 carreiras
            print(f"- {nome} (Adequação: {pontuacao:.2f})")
            
        print("\nAnálise concluída.")
