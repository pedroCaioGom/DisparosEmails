from utils.pdf import Pdf
from utils.planilha import Planilha
from utils.email import Email


class Disparador:
    def __init__(self, caminho_pdf):
        self.caminho_planilha = r'D:\Python\DepartamentoPessoal\arquivos\planilha\Dados.xlsx'
        self.caminho_pdf = caminho_pdf
        self.beneficiario = None

        #fazer um loop na pasta D:\Python\DepartamentoPessoal\pdf_separados para que consiga passar cada caminho_pdf
        #caminho_pdf = r'D:\Python\DepartamentoPessoal\pdf_separados\JOAO_VITOR_NERES_CABRAL_05420519151_45936979000142.pdf'


    def executar_pdf(self):
        # ==============================
        # 2️⃣ Carregar PDF
        # ==============================
        pdf = Pdf(self.caminho_pdf)
        pdf.receberPdf()

        # ==============================
        # 3️⃣ Extrair beneficiário do PDF
        # ==============================
        self.beneficiario = pdf.identificar_beneficiario()

        print("Beneficiário encontrado:")
        print("CPF:", self.beneficiario.cpf)
        print("Nome:", self.beneficiario.nome)
        print("CNPJ:", self.beneficiario.cnpj_empresa)

        return self.beneficiario
    

    def executar_planilha(self):
        try:
            # ==============================
            # 4️⃣ Carregar planilha
            # ==============================
            planilha = Planilha(planilha=self.caminho_planilha)
            planilha.recebendo_planilha()
        except Exception as e:
            print(f"Erro ao carregar a planilha: {e}")
            return None

        # ==============================
        # 5️⃣ Buscar email pelo CPF
        # ==============================
        print(f"Buscando email pelo CPF: {self.beneficiario.cpf}...")

        email = planilha.buscar_email_por_cpf(self.beneficiario.cpf)

        if not email:  # trata CPF não encontrado ou email vazio
            print(f"⚠️ CPF {self.beneficiario.cpf} não encontrado ou email vazio na planilha")
            self.beneficiario.email = None
            return self.beneficiario

        # Se email encontrado, atualiza o beneficiário
        self.beneficiario.email = email
        print("✅ Email encontrado:", self.beneficiario.email)

        return self.beneficiario
    

    def executar_envio(self):
        # ==============================
        # 6️⃣ (Futuro) enviar email
        # ==============================
        envio = Email(
            destinatario=self.beneficiario.email,
            assunto=r'Informe de rendimentos',
            mensagem=r'Boa tarde, segue informes de rendimento 2026.',
            anexo=self.caminho_pdf
        )
        envio.enviar_email()