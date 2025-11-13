**Integrantes
Guilherme Willians de Souza Inácio (RM565319)
Kauã da Silva Lazarim (RM564625) 
Nelson Troccoli Santos Neto (RM562815)

Ferramenta Inteligente de Orientação de Carreiras (GS2025.2)

Descrição do Projeto e Propósito

Este projeto é uma solução desenvolvida em Python, seguindo os princípios da Programação Orientada a Objetos (POO), para simular uma Ferramenta Inteligente de Orientação de Carreiras.

O principal objetivo é analisar perfis profissionais com base em um conjunto de competências técnicas e comportamentais e, a partir dessa análise, gerar recomendações personalizadas de carreiras e áreas de aprimoramento.

O sistema utiliza classes para modelar os dados (Competência, Carreira e Perfil) e estruturas de dados nativas do Python (listas, tuplas e dicionários) para armazenar e manipular as informações, conectando a lógica de programação ao desenvolvimento humano e profissional.

Instruções de Execução

Para executar o sistema, siga os passos abaixo:

1.
Pré-requisitos: Certifique-se de ter o Python 3.x instalado em seu sistema.

2.
Arquivos: Baixe ou clone os seguintes arquivos para um diretório local:

•
main.py

•
sistema_carreiras.py



3.
Execução: Abra o terminal ou prompt de comando, navegue até o diretório onde os arquivos foram salvos e execute o script principal:

4.
Interação: O sistema apresentará um menu de opções (Cadastrar Novo Perfil, Analisar Perfil Existente, Listar Perfis Cadastrados, Sair). Siga as instruções na tela para interagir com a ferramenta.

Estrutura de Arquivos e Classes

O projeto é modularizado em dois arquivos principais, seguindo o paradigma de Orientação a Objetos:

main.py

Contém a função principal (main) que inicializa o sistema e gerencia a interface de linha de comando (CLI), apresentando o menu de opções e chamando os métodos da classe SistemaCarreiras.

sistema_carreiras.py

Este módulo contém toda a lógica de negócios e as classes de modelo de dados:

Classe
Descrição
Atributos Principais
Competencia
Representa uma competência individual.
nome (str), tipo (str: 'tecnica' ou 'comportamental')
Carreira
Representa uma carreira e as competências ideais.
nome (str), descricao (str), competencias_chave (dict: nome da competência e peso ideal 1-5)
Perfil
Representa o perfil de um profissional.
nome (str), rm (str), avaliacoes (dict: nome da competência e nota do perfil 1-5)
SistemaCarreiras
Classe principal que gerencia os dados e a lógica de análise.
competencias (list), carreiras (list), perfis (dict)


Métodos Principais de SistemaCarreiras:

•
_carregar_competencias(): Carrega a lista inicial de competências (usando tupla de dados).

•
_carregar_carreiras(): Carrega a lista inicial de carreiras e seus pesos ideais (usando tupla de dados).

•
cadastrar_perfil(): Coleta dados do usuário e cria um novo objeto Perfil (usando dicionário para avaliações).

•
listar_perfis(): Exibe os perfis já cadastrados.

•
analisar_perfil(): Implementa a lógica de recomendação, calculando a adequação do perfil a cada carreira (média ponderada) e sugerindo áreas de aprimoramento.

Demonstração (Exemplo de Interação)

1.
Início:

2.
Cadastro: O usuário insere nome, RM e avalia as competências de 1 a 5.

3.
Análise:

