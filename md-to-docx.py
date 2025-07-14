import markdown
from docx import Document
from bs4 import BeautifulSoup

def markdown_to_docx(markdown_file, docx_file):
    # Read the Markdown file
    with open(markdown_file, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=['fenced_code', 'codehilite'])

    # Remove code blocks from HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    for code_block in soup.find_all(['pre', 'code']):
        code_block.decompose()
    cleaned_html = str(soup)

    # Create a Word document
    doc = Document()

    # Add the cleaned HTML content as plain text
    doc.add_paragraph(soup.get_text())

    # Save the Word document
    doc.save(docx_file)

# Example usage
markdown_to_docx('generated_police_report.md', 'report_docx.docx')
