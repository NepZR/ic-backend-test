import requests
import zipfile

import urllib.request
from bs4 import BeautifulSoup

TARGET_URL = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'

crawledPage = BeautifulSoup(
    requests.get(TARGET_URL).text,
    features='lxml'
)

html_targetList = crawledPage.find_all('a', attrs={
    'data-tippreview-enabled': 'true',
    'class': 'internal-link'
})

attachmentList = [
    item['href'] for item in html_targetList
    if not (item.text.find('Anexo') == -1)
]

file_names = []
for attachment in attachmentList:
    urllib.request.urlretrieve(
        attachment, attachment[attachment.index('Anexo'):]
    )

    file_names.append(
        attachment[attachment.index('Anexo'):]
    )

with zipfile.ZipFile('attachments.zip', 'w') as attZip:
    for file_name in file_names:
        attZip.write(file_name)
    attZip.close()
