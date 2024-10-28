import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Step 1: Send a request to the URL
url = 'https://www.booking.com/resorts/city/vn/quy-nhon.html?aid=356980&label=gog235jc-1BCAMYjwQo9AFCCHF1eS1uaG9uSDNYA2j0AYgBAZgBKrgBF8gBDNgBAegBAYgCAagCA7gC_IzxuAbAAgHSAiQ1NWU3ODhlZS0wYzVlLTRlYzctYTg2ZC0zMmUyZWIwYzhkYznYAgXgAgE&sid=d817f5f95ab5d302a0cf9f9fad922a98&lang=en-us&soz=1&lang_click=other&cdl=vi&lang_changed=1'
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract text content from <p> tags
paragraphs = soup.find_all('p')
page_text = '\n'.join([para.get_text() for para in paragraphs])

# Step 4: Create a PDF using ReportLab
pdf_output = 'data/booking.pdf'
c = canvas.Canvas(pdf_output, pagesize=letter)
width, height = letter

# Step 5: Add the text content to the PDF
text_object = c.beginText(40, height - 40)  # Start 40 points from the top and left
text_object.setFont("Helvetica", 10)

# Split the text into lines and add to the PDF
for line in page_text.split('\n'):
    text_object.textLine(line)

c.drawText(text_object)

# Step 6: Save the PDF
c.save()

print(f"Content saved to {pdf_output}")
