from dto.beneficiario import Beneficiario
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import re
from abc import ABC, abstractmethod


class Pdf:
    def __init__(self, pdf):
        self.pdf = Path(pdf)
        self.__reader = None

    
    def receberPdf(self):
        reader = PdfReader(self.pdf)
        self.__reader = reader
        return self.__reader


    def identificar_beneficiario(self):

        nome = None
        cpf = None
        cnpj_empresa = None
        

        texto_completo = ""

        # Junta texto de todas as páginas
        for page in self.__reader.pages:
            texto = page.extract_text()
            if texto:
                texto_completo += texto + "\n"

        # Nome
        match_nome = re.search(r"beneficiário:\s*(.+)", texto_completo, re.IGNORECASE)
        if match_nome:
            nome = match_nome.group(1).strip()

        # CPF
        match_cpf = re.search(r"cpf:\s*(\d{11})", texto_completo, re.IGNORECASE)

        if match_cpf:
            cpf = match_cpf.group(1)

        # CNPJ
        match_cnpj = re.search(r"(\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2})\s*CNPJ/CPF", texto_completo, re.IGNORECASE)
        if match_cnpj:
            cnpj_empresa = match_cnpj.group(1).strip()

        b = Beneficiario()
        b.nome = nome
        b.cpf = cpf
        b.cnpj_empresa = cnpj_empresa

        return b
    

    def separar_pdf(self, pasta_saida="pdf_separados"):

        Path(pasta_saida).mkdir(exist_ok=True)

        reader = PdfReader(self.pdf)
        arquivos_criados = []

        for i, page in enumerate(reader.pages, start=1):

            writer = PdfWriter()
            writer.add_page(page)

            nome_arquivo = f"{self.pdf.stem}_pagina_{i}.pdf"
            caminho_saida = Path(pasta_saida) / nome_arquivo

            with open(caminho_saida, "wb") as f:
                writer.write(f)

            arquivos_criados.append(caminho_saida)

        return arquivos_criados