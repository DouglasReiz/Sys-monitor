# 🖥️ Monitor do Sistema

O **Monitor do Sistema** é uma aplicação leve e interativa para monitorar **uso de CPU, memória, disco e rede** em tempo real, diretamente pelo navegador.  
Desenvolvido em **Python** com **Flask** e **Chart.js**, o projeto tem como objetivo oferecer uma visão simples, visual e intuitiva do desempenho do computador.

---

## 🚀 Funcionalidades

✅ **Painel web interativo**  
Acompanhe as métricas em tempo real através de um gráfico dinâmico no navegador.

✅ **Métricas monitoradas**
- **CPU (%)** – Uso total do processador  
- **Memória RAM (%)** – Percentual de memória em uso  
- **Disco (%)** – Utilização do armazenamento  
- **Rede (KB/s)** – Taxas de upload e download instantâneas  

✅ **Atualização automática**
Os gráficos são atualizados a cada segundo, sem precisar recarregar a página.

✅ **Execução no Windows e Linux**
O projeto é compatível com diferentes sistemas operacionais.  
Pode ser executado via Python ou empacotado em um `.exe` (Windows) usando **PyInstaller**.

✅ **Interface limpa e responsiva**
Feita com **HTML + Chart.js**, adaptada para qualquer resolução de tela.

---

## 🧠 Tecnologias utilizadas

- **Python 3**
- **Flask** (para o servidor web)
- **psutil** (para coletar métricas do sistema)
- **Chart.js** (para os gráficos dinâmicos)
- **HTML5 / JavaScript**

---

## 🧩 Como executar o projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/monitor-sistema.git
cd monitor-sistema
