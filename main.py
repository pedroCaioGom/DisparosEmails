from pathlib import Path
from utils.pdf import Pdf
from flow.disparador import Disparador


def main():
    pasta = Path(r"pasta_raiz_dos_pdfs")

    for arquivo in pasta.glob("*.pdf"):
        print(f"\nProcessando arquivo: {arquivo.name}")
        d = Disparador(arquivo)

        beneficiario = d.executar_pdf()  # retorna o objeto Beneficiario ou None

        # Se não encontrou beneficiário, pular para o próximo PDF
        if not beneficiario or not beneficiario.cpf:
            print(f"⚠️ Nenhum beneficiário encontrado em {arquivo.name}. Pulando...")
            continue

        # Executa planilha
        planilha = d.executar_planilha()

        # Se o email não for encontrado, você também pode pular envio
        if not beneficiario.email:
            print(f"⚠️ Email não encontrado para {beneficiario.nome}. Pulando envio...")
            continue

        # Executa envio
        d.executar_envio()


if __name__ == "__main__":
    main()
        