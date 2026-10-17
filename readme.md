# 📄 Imposição de PDF: A5 para A4

Esta aplicação web, desenvolvida em Python com Streamlit e PyMuPDF, automatiza a preparação de arquivos PDF em tamanho A5 (frente e verso) para impressão em folhas A4. 

Para contornar limitações de impressoras que não fazem duplex automático em papéis pequenos, o sistema ajusta a orientação automaticamente, duplica as artes lado a lado em uma página A4 e desenha uma linha de corte central para facilitar o uso da guilhotina.

## 🛠️ Uso Online em: https://atelieatalia.streamlit.app/

## 🛠️ Pré-requisitos para Rodar Localmente

* [Python 3.8+](https://www.python.org/downloads/) instalado no seu sistema.
* Editor de código (recomendado: Visual Studio Code).

## 📦 Arquivo de Dependências (`requirements.txt`)

Certifique-se de ter um arquivo chamado `requirements.txt` na raiz do seu projeto com o seguinte conteúdo:

```text
streamlit>=1.30.0
pymupdf>=1.23.0
```

## 🚀 Como configurar e executar localmente

Siga os passos abaixo no seu terminal (como o PowerShell no Windows) para configurar o ambiente e rodar a aplicação:

### 1. Criar o ambiente virtual
Navegue até a pasta do seu projeto e crie um ambiente virtual isolado para manter as dependências organizadas:
```powershell
python -m venv venv
```

### 2. Ativar o ambiente virtual
Ative o ambiente virtual que você acabou de criar:
```powershell
.\venv\Scripts\Activate.ps1
```
*(Dica para usuários do VS Code: Após criar o ambiente, o editor geralmente detecta a pasta `venv` e sugere ativá-la automaticamente ao abrir um novo terminal).*

### 3. Instalar as dependências
Com o ambiente ativado (você verá um prefixo `(venv)` no seu terminal), instale as bibliotecas necessárias:
```powershell
pip install -r requirements.txt
```

### 4. Iniciar a aplicação
Execute o comando do Streamlit para iniciar o servidor local:
```powershell
streamlit run app.py
```
*(Nota: Se o seu arquivo principal tiver outro nome, substitua `app.py` pelo nome correto).*

O seu navegador padrão abrirá automaticamente uma nova guia com a aplicação rodando no endereço `http://localhost:8501`.

## 🛑 Como parar o servidor
Para encerrar a aplicação, volte ao terminal e pressione as teclas `Ctrl + C`. 
Para sair do ambiente virtual e voltar ao terminal normal, digite:
```powershell
deactivate
```