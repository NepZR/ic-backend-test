# Testes Back-End Dev. - Intuitive Care
> Repositório dedicado para as implementações dos testes direcionados para o processo seletivo proposto pela IntuitiveCare (Dev. Back-End). As soluções aqui disponibilizadas foram feitas por Lucas D. F. Rodrigues.
---
## • Testes realizados
### T1. Web Scraping
- Linguagem de programação utilizada: **Python 3 (com <a href="https://www.anaconda.com/products/distribution">Anaconda Individual Edition</a>)** 
- Bibliotecas utilizadas:
  - <a href="https://www.crummy.com/software/BeautifulSoup/">BeautifulSoup4</a>
  - <a href="https://requests.readthedocs.io/en/latest/">Requests</a>
  - <a href="https://docs.python.org/3/library/zipfile.html">ZipFile</a>
  - <a href="https://docs.python.org/3/library/urllib.request.html">UrlLib (Request)</a>
- Ambiente de desenvolvimento:
  - **IDE:** Visual Studio Code
  - **Python:** 3.9 - Anaconda Individual Edition
- Formatação do código:
  - **Linters**: ```flake8```, ```pep8```
  - **Code Style Convention:** <a href="https://peps.python.org/pep-0008/">PEP8</a>
- Objetivos:
  1. Acessar a página web alvo para coleta;
  2. Baixar **apenas** os Anexos I, II, III, IV (não há especificação de formato - PDF, CSV, por exemplo);
  3. Criar um arquivo .ZIP contendo todos os Anexos baixados no objetivo anterior.
## • Testes não realizados
  - T2. Transformação de dados
  - T3. Banco de dados
  - T4. API

---

## • How To (T1 - Web Scraping)


I) Clonar o repositório:
   ```
   $ git clone https://github.com/NepZR/ic-backend-test.git 
   ```

II) Acessar a pasta do projeto:
   ```
   $ cd ic-backend-test 
   ```

III) Instalar as dependências necessárias:
   ```
   $ pip install -r requirements.txt
   ```

II) Acessar a pasta do Teste 1:
   ```
   $ cd test_1
   ```

IV) Executar o script de Web Scraping:
   ```
   $ python -u webScraping.py
   ```

> Os arquivos baixados e gerados pelo processo de raspagem de dados do script serão salvos dentro da pasta ```test_1```.

---

## Desenvolvedor
<table style="border: 1px solid gray;">
  <tr>
    <td align="center"><a href="https://github.com/NepZR"><img style="width: 150px; height: 150; border-radius: 100%;" src="https://avatars.githubusercontent.com/u/37887926" width="100px;" alt=""/><br /><sub><b>Lucas Darlindo Freitas Rodrigues</b></sub></a><br /><sub><b>Graduando em Ciência da Computação</sub></a><br /><sub><b>UFOPA</sub></a><br /><a href="https://www.linkedin.com/in/lucasdfr"><sub><b>LinkedIn</b></sub></a></td>
  </tr>
<table>