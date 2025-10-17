# 🖥️ Monitor do Sistema

O **Monitor do Sistema** é um aplicativo leve e interativo desenvolvido em **Python + Flask**, que exibe métricas em tempo real de **CPU, memória, disco e rede** diretamente no navegador.  
O projeto foi empacotado para **Windows (.exe)**, permitindo fácil execução sem depender de ambiente Python instalado.

---

## 🚀 Funcionalidades

✅ **Painel Web Interativo**
- Interface simples e responsiva acessível em qualquer navegador.  
- Gráficos dinâmicos e atualizados em tempo real.  

✅ **Métricas Monitoradas**
- **CPU (%)** — Uso total do processador  
- **Memória RAM (%)** — Utilização da memória do sistema  
- **Disco (%)** — Espaço de armazenamento em uso  
- **Rede (KB/s)** — Taxa de upload e download em tempo real  

✅ **Execução simplificada**
- Basta abrir o arquivo `.exe` e o navegador será iniciado automaticamente na página do painel.

✅ **Visual moderno**
- Interface construída com **HTML5 + Chart.js** para gráficos suaves e responsivos.  

---

## 🪟 Versão Windows (.exe)

A versão empacotada já está pronta para uso.

### ▶️ Como usar

1. Extraia o arquivo `.zip` do projeto (se aplicável).  
2. Execute o arquivo:  
    `Monitor do Sistema.exe`
3. O navegador abrirá automaticamente em:
    **http://localhost:5000**
4. Acompanhe as métricas do seu sistema em tempo real!

---

## 🧠 Tecnologias Utilizadas

- **Python 3**
- **Flask** — Servidor web leve e rápido  
- **psutil** — Biblioteca para coleta de métricas do sistema  
- **Chart.js** — Gráficos dinâmicos e responsivos no front-end  
- **HTML5 / JavaScript**

---

## 🧩 Estrutura do Projeto

monitor-sistema/
├── app.py
├── templates/
│ └── index.html
├── icon.ico
└── dist/
└── Monitor do Sistema.exe


---

## 🧰 Para Desenvolvedores

Caso queira modificar o código-fonte e gerar uma nova versão do executável:

1. Instale as dependências:
   ```bash
   pip install flask psutil pyinstaller

Faça suas alterações no app.py ou templates/index.html.

Recompile o executável:

    `pyinstaller --noconsole --onefile --name "Monitor do Sistema" --icon=icon.ico --add-data "templates;templates" app.py`

O novo .exe será gerado em dist/.


---

## 🧭 Em Desenvolvimento

O projeto está em fase de evolução.
Futuras atualizações podem incluir:

Histórico e exportação de métricas

Alertas automáticos de alto consumo

Tema escuro e opções de personalização

Compatibilidade aprimorada com Linux e WSL

Instalação como serviço em segundo plano


---

## 💡 Objetivo

Criar uma ferramenta visual, leve e multiplataforma para monitorar o desempenho do sistema em tempo real — sem depender de softwares pesados ou complexos.


---

## 👨‍💻 Autor

Douglas Alves
- 📅 Projeto em desenvolvimento — melhorias e contribuições são bem-vindas!


---

## 📜 Licença

- Este projeto é licenciado sob a Licença MIT — você pode usar, modificar e distribuir livremente, desde que mantenha os créditos originais.


---

## MIT License

Copyright (c) 2025 Douglas Alves

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


---

## ✨ Status do Projeto: Em desenvolvimento — novas versões trarão mais recursos e melhorias visuais.