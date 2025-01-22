# Automação de Download com Selenium
Este projeto utiliza o Selenium para automatizar o download de arquivos do site Dev Samurai, que disponibilizou todos seus cursos gratuitamente. Com o uso de XPath dinâmico, o script percorre e clica automaticamente em links para iniciar os downloads.
---

## **Funcionalidades**
- Iteração por elementos de uma página web usando XPath dinâmico.
- Download automático de arquivos para uma pasta definida.
- Configuração personalizada para evitar janelas de confirmação de download.

---

## **Pré-requisitos**
Antes de executar o projeto, certifique-se de ter os seguintes itens instalados:

1. **Python** (versão 3.7 ou superior): [Baixar Python](https://www.python.org/downloads/)
2. **GeckoDriver** (gerenciado automaticamente pelo `webdriver_manager`).
3. As bibliotecas Python necessárias:
   ```bash
   pip install selenium webdriver-manager
   ```

---

## **Configuração do Ambiente**

### 1. Instalar as Dependências
Certifique-se de que o Selenium e o WebDriver Manager estão instalados. Para instalar, utilize o comando abaixo:
```bash
pip install selenium webdriver-manager
```

### 2. Configurar o Diretório de Download
No script, defina o caminho para a pasta onde os arquivos serão salvos. Substitua o valor de `browser.download.dir` por um caminho válido no seu sistema:
```python
options.set_preference(
    "browser.download.dir", r"C:\Users\SeuUsuario\Downloads"
)
```

---

## **Como Executar**

1. Clone ou baixe este repositório.
2. Abra um terminal na pasta do projeto.
3. Crie um ambiente virtual com:
   ```bash
   python -m venv .venv
   ```
4. Ative seu ambiente virtual:
   ```bash
   .venv/Scripts/activate
   ```
5. Baixe as dependencias necessarias: 
   ```bash
   pip install -r requirements.txt
   ```
6. Execute o script com o comando:
   ```bash
   python main.py
   ```

---

## **Dicas para Personalização**

- **Alterar o número total de links:**
  Ajuste o valor de `total_links` no script para corresponder ao número de links na sua página:
  ```python
  total_links = 67
  ```

- **Modificar o XPath base:**
  Caso o layout do site mude, edite o XPath dinâmico no script:
  ```python
  xpath = f"/html/body/div/ul/li[{i}]/a"
  ```

---

## **Avisos**
- O site deve permitir que os arquivos sejam baixados diretamente ao clicar nos links.
- Caso o site exija autenticação, você precisará incluir etapas para login no script.

---


## **Contribuições**
Sinta-se à vontade para contribuir com melhorias ou adaptações para outros tipos de automação. Basta abrir uma pull request neste repositório.

---

### **Autor**
Gabriel Nunes

Conecte-se comigo no [LinkedIn](www.linkedin.com/in/gabriel-nunes-72484b318)!
