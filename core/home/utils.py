from django.template.loader import get_template
from django.http import HttpResponse
from weasyprint import HTML
from io import BytesIO

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html_content = template.render(context_dict)
    
    
    # Crear un objeto HTML a partir del contenido HTML
    html = HTML(string=html_content)
    
    # Generar el PDF en memoria
    pdf_data = html.write_pdf()
    
    # Devolver el PDF como una respuesta HTTP
    response = HttpResponse(pdf_data, content_type='application/pdf')
    
    # Opcional: Establecer el encabezado de descarga si deseas que el navegador ofrezca descargar el PDF
    response['Content-Disposition'] = 'attachment; filename="resultado.pdf"'
    
    return response
