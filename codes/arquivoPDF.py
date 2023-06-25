from fpdf import FPDF

class regPDF:

    # Variáveis globais

    pontu = ""
    expe = ""
    atendi = ""
    proativi = ""
    dina = ""
    tecnol = ""
    assidu = ""
    avaliado = ""
    texto = ""

    # Funções que recebem as avaliações

    def resPontu(pt):
        global pontu
        pontu = pt
    
    def resExpe(ex):
        global expe
        expe = ex
    
    def resAtendi(at):
        global atendi
        atendi = at

    def resProativi(pr):
        global proativi
        proativi = pr

    def resDina(di):
        global dina
        dina = di

    def resTecnol(te):
        global tecnol
        tecnol = te

    def resAssidu(assi):
        global assidu
        assidu = assi

    # Função que geram o arquivo PDF com seu conteúdo pronto
   
    def usuario(nome):
        global avaliado
        avaliado = nome

    def supervisor(txt):
        global texto
        texto = txt
        regPDF.relatorio()

    def relatorio():
        
        global avaliado
        global texto

        titulo = f"Avaliação do Colaborador(a) : {avaliado}" # Inserir o nome do avaliado

        pdf = FPDF('P','mm','A4')

        pdf.add_page()
        pdf.set_font('helvetica','',12)
        pdf.cell(txt=titulo, w=0, align="c")
        pdf.ln(20) # Dentro do ln, podemos colocar um valor inteiro representando quantos linhas pular
        pdf.multi_cell(txt= f"PONTUALIDADE: {pontu}\n\nEXPERIÊNCIA: {expe}\n\nATENDIMENTO: {atendi}\n\nPROATIVIDADE: {proativi}\n\nDINÂMICA: {dina}\n\nTECNOLOGIA: {tecnol}\n\nASSIDUIDADE: {assidu}", w=0, align="j" )
        pdf.ln(20)
        pdf.cell(txt="Considerações do Supervisor(a):", w=0, align="c")
        pdf.ln(10)
        pdf.multi_cell(txt=texto, w=0)
        pdf.ln(20)
        pdf.cell(txt="____________________________", w=0, align="c")
        pdf.ln()
        pdf.cell(txt="Isabel Ribeiro - Supervisora", w=0, align="c")
        pdf.ln(20)
        pdf.cell(txt="____________________________________________", w=0, align="c")
        pdf.ln()
        pdf.cell(txt=f"{avaliado} - Colaborador(a)", w=0, align="c")
        pdf.output(f"./arquivos/{avaliado}.pdf")