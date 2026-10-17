import streamlit as st
import pymupdf  # Substituiu o antigo 'fitz'
import io

st.set_page_config(page_title="Imposição A5 para A4", layout="centered")

st.title("✂️ Gerador de A4 com Base em A5")
st.write("O sistema ajusta a orientação, cola as artes lado a lado em um A4")

arquivo_pdf = st.file_uploader("Selecione o arquivo PDF (A5)", type=["pdf"])

if arquivo_pdf is not None:
    # Carrega o PDF original na memória
    doc_original = pymupdf.open(stream=arquivo_pdf.read(), filetype="pdf")
    
    # Cria um novo documento PDF em branco (que será o nosso A4)
    doc_saida = pymupdf.open()

    # Medidas de um A4 em Paisagem (em pontos tipográficos)
    a4_width, a4_height = 842.0, 595.0
    meio = a4_width / 2

    total_paginas = len(doc_original)

    for i in range(0, total_paginas, 2):
        pagina_frente = doc_original[i]
        # Verifica se tem verso, se não, retorna None
        pagina_verso = doc_original[i + 1] if i + 1 < total_paginas else None

        # --- PREPARA A FRENTE ---
        rect_f = pagina_frente.rect
        if rect_f.width > rect_f.height:
            pagina_frente.set_rotation(90)

        # Cria a folha A4 física (Paisagem)
        nova_pag_frente = doc_saida.new_page(width=a4_width, height=a4_height)
        
        # Cola a arte A5 do lado esquerdo e do lado direito
        nova_pag_frente.show_pdf_page(pymupdf.Rect(0, 0, meio, a4_height), doc_original, pagina_frente.number)
        nova_pag_frente.show_pdf_page(pymupdf.Rect(meio, 0, a4_width, a4_height), doc_original, pagina_frente.number)
        
        

        # --- PREPARA O VERSO ---
        nova_pag_verso = doc_saida.new_page(width=a4_width, height=a4_height)
        
        if pagina_verso:
            rect_v = pagina_verso.rect
            if rect_v.width > rect_v.height:
                pagina_verso.set_rotation(90)
            
            nova_pag_verso.show_pdf_page(pymupdf.Rect(0, 0, meio, a4_height), doc_original, pagina_verso.number)
            nova_pag_verso.show_pdf_page(pymupdf.Rect(meio, 0, a4_width, a4_height), doc_original, pagina_verso.number)
        
        

    # 5. Salva o arquivo final
    pdf_bytes = doc_saida.write()
    
    st.success("✨ PDF gerado com sucesso!")
    
    st.download_button(
        label="📥 Baixar PDF A4 Pronto para Imprimir",
        data=pdf_bytes,
        file_name="A4_com_linha_de_corte.pdf",
        mime="application/pdf"
    )
