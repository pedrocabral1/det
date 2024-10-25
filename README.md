<img src="https://www.unifor.br/o/unifor-theme/images/unifor-logo-horizontal.svg" width="250px">

# **Engenharia de Dados II**

**Equipe:**  
- Paulo Dario Soares Coelho  
- Pedro Henrique de Araújo Cabral  
- Thiago Pinto Pereira  

**Professor:** Nauber Gois  
**Curso:** MBA em Ciência de Dados  
**Turma:** 07  
**Data de Criação:** 23/10/2024

## 1. Introdução ao Estudo de Dados de Eventos de Terrorismo

O objetivo da análise do dataset de eventos de terrorismo é compreender a natureza e distribuição dos ataques terroristas por região e ao longo do tempo. A exploração das diversas colunas do dataset permite identificar padrões e tendências, revelando características fundamentais desses eventos. Esta análise é essencial para entender as motivações, impactos sociais e padrões de comportamento associados ao fenômeno do terrorismo.

### 1.1 Detalhes das Colunas

- **Colunas Numéricas**: incluem identificadores, datas, locais e coordenadas dos eventos.
- **Colunas Textuais**: contêm informações descritivas, como localizações, grupos responsáveis, tipos de ataques e alvos, além dos motivos e reivindicações dos ataques.

---

## 2. Configuração do Ambiente

1. **Instalação de Dependências**: 
    ```bash
    pip install -q pyspark
    ```

2. **Importação de Bibliotecas**:  
   Inclui Spark, PySpark e módulos auxiliares para tratamento de dados.

3. **Organização dos Diretórios**:  
   Estabelece diretórios para o pipeline de dados, como `bronze`, `silver`, e `gold`.

---

## 3. Importação e Análise Exploratória Inicial do Dataset

1. **Importação do Dataset**:  
   O arquivo bruto é carregado e armazenado no diretório `bronze` para futuras análises.

2. **Exploração Inicial dos Dados**:  
   Exibimos o cabeçalho e a estrutura do dataset, estatísticas descritivas e a quantidade de valores nulos para identificar possíveis ajustes.

---

## 4. Transformação e Criação da Camada Silver

1. **Limpeza e Transformação de Dados**:  
   O dataset bruto é transformado e armazenado na camada `silver`, onde duplicatas são removidas e colunas desnecessárias são excluídas para facilitar a análise posterior.

2. **Validação dos Dados**:  
   Verificamos se as transformações foram realizadas corretamente e se o dataset `silver` está pronto para a etapa de análise agregada.

---

## 5. Análises e Agregações dos Dados

1. **Distribuição dos Eventos por País**:  
   Analisamos quais países são mais afetados por eventos terroristas.

2. **Tipos de Ataque Mais Frequentes**:  
   Identificação das táticas mais usadas.

3. **Evolução das Mortes por Ano**:  
   Análise das tendências temporais de mortes associadas ao terrorismo.

4. **Principais Armas Utilizadas**:  
   Compreensão das armas preferidas nos ataques.

5. **Ataques Suicidas por País**:  
   Foco em padrões específicos de ataques suicidas.

6. **Distribuição das Mortes por Região**:  
   Perspectiva geográfica dos efeitos dos ataques.

7. **Atividade dos Grupos Terroristas**:  
   Compilação de dados sobre grupos mais ativos e suas características.

---

## 6. Armazenamento dos Dados na Camada Gold

Salvamos os dados processados e agregados na camada `gold`, organizados para análises avançadas e visualizações futuras. Os dados são salvos nos formatos `parquet`, `json` e `csv` para fácil acesso.

---

## 7. Download dos Resultados

Um arquivo `.zip` com os dashboards foi criado para facilitar o download e visualização dos dados finais processados.
