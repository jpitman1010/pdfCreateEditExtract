from fpdf import FPDF 
import plotly.express as px
import plotly
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green
from PyPDF2 import PdfFileReader, PdfFileWriter



# https://pythonhosted.org/PyPDF2/

class PDF(FPDF):
     # to draw a line horizontally across center of page
#     def lines(self):
#         self.set_line_width(0.0)
#         self.line(0,pdf_h/2,210,pdf_h/2)

          # to draw a square you need 4 lines
     def lines(self):
        self.set_line_width(0.0)
        self.line(5.0,5.0,205.0,5.0) # top one
        self.line(5.0,292.0,205.0,292.0) # bottom one
        self.line(5.0,5.0,5.0,292.0) # left one
        self.line(205.0,5.0,205.0,292.0) # right one
     # to draw a rectangle
     # def lines(self):
     #      self.rect(5.0, 5.0, 200.0,287.0)
     # double lined rect around edge of page
     # def lines(self):
        self.rect(5.0, 5.0, 200.0,287.0)
        self.rect(8.0, 8.0, 194.0,282.0)
     # filling in outter edge of inside lines with red: 
#     def lines(self):
        self.set_fill_color(32.0, 47.0, 250.0) # color for outer rectangle
        self.rect(5.0, 5.0, 200.0,287.0,'DF')
        self.set_fill_color(255, 255, 255) # color for inner rectangle
        self.rect(8.0, 8.0, 194.0,282.0,'FD')



     # ADDING IMAGES
     def imagex(self):
          self.set_xy(6.0,6.0)
          self.image(sctplt,  link='', type='', w=1586/80, h=1920/80)
          self.set_xy(183.0,6.0)
          self.image(sctplt2,  link='', type='', w=1586/80, h=1920/80)



          df = px.data.iris()
          pltx= px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                         size='petal_length', hover_data=['petal_width'])
          plotly.io.write_image(pltx,file='pltx.png',format='png',width=700, height=450)
          pltx=(os.getcwd()+'/'+"pltx.png")
          ### define a method
          def charts(self):
               self.set_xy(40.0,25.0)
               self.image(plt,  link='', type='', w=700/5, h=450/5)


     # WORKING WITH TEXT
     def titles(self):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt="LORD OF THE PDFS", border=0)


     # USING TEXT FILE 
     def texts(self,name):
        with open(name,'rb') as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,80.0)    
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0,10,txt)





     # pdf = PDF()#pdf object

     # SETTING AUTHOR
     # pdf.set_author('Eser SAYGIN')

     # pdf=PDF(orientation='L') # landscape


     # pdf=PDF(unit='mm') #unit of measurement


     # pdf=PDF(format='A4') #page format. A4 is the default value of the format, you don't have to specify it.
     # full syntax
     # PDF(orientation={'P'(def.) or 'L'}, measure{'mm'(def.),'cm','pt','in'}, format{'A4'(def.),'A3','A5','Letter','Legal')
     #default
pdf = PDF(orientation='P', unit='mm', format='A4')


pdf.add_page()
pdf.output('test.pdf','F')


# assigning height and width dimensions
pdf_w=210
pdf_h=297




def create_simple_checkboxes():
     c = canvas.Canvas('simple_checkboxes.pdf')
     
     c.setFont("Courier", 20)
     c.drawCentredString(300, 700, 'Pets')
     c.setFont("Courier", 14)
     form = c.acroForm
     
     c.drawString(10, 650, 'Dog:')
     form.checkbox(name='cb1', tooltip='Field cb1',
                    x=110, y=645, buttonStyle='check',
                    borderColor=magenta, fillColor=pink, 
                    textColor=blue, forceBorder=True)
     
     c.drawString(10, 600, 'Cat:')
     form.checkbox(name='cb2', tooltip='Field cb2',
                    x=110, y=595, buttonStyle='cross',
                    borderWidth=2, forceBorder=True)
     
     c.drawString(10, 550, 'Pony:')
     form.checkbox(name='cb3', tooltip='Field cb3',
                    x=110, y=545, buttonStyle='star',
                    borderWidth=1, forceBorder=True)
     
     c.drawString(10, 500, 'Python:')
     form.checkbox(name='cb4', tooltip='Field cb4',
                    x=110, y=495, buttonStyle='circle',
                    borderWidth=3, forceBorder=True)
     
     c.drawString(10, 450, 'Hamster:')
     form.checkbox(name='cb5', tooltip='Field cb5',
                    x=110, y=445, buttonStyle='diamond',
                    borderWidth=None,
                    checked=True,
                    forceBorder=True)
     
     c.save()

# if __name__ == '__main__':
#     create_simple_checkboxes()
#     create_simple_radios()
#     create_simple_choices()
#     create_simple_listboxes()
#     create_simple_form()



# simple_radios.py

def create_simple_radios():
     c = canvas.Canvas('simple_radios.pdf')
     
     c.setFont("Courier", 20)
     c.drawCentredString(300, 700, 'Radio demo')
     c.setFont("Courier", 14)
     form = c.acroForm
     
     c.drawString(10, 650, 'Dog:')
     form.radio(name='radio1', tooltip='Field radio1',
                    value='value1', selected=False,
                    x=110, y=645, buttonStyle='check',
                    borderStyle='solid', shape='square',
                    borderColor=magenta, fillColor=pink, 
                    textColor=blue, forceBorder=True)
     form.radio(name='radio1', tooltip='Field radio1',
                    value='value2', selected=True,
                    x=110, y=645, buttonStyle='check',
                    borderStyle='solid', shape='square',
                    borderColor=magenta, fillColor=pink, 
                    textColor=blue, forceBorder=True)    
     
     c.drawString(10, 600, 'Cat:')
     form.radio(name='radio2', tooltip='Field radio2',
                    value='value1', selected=True,
                    x=110, y=595, buttonStyle='cross',
                    borderStyle='solid', shape='circle',
                    borderColor=green, fillColor=blue, 
                    borderWidth=2,
                    textColor=pink, forceBorder=True)
     form.radio(name='radio2', tooltip='Field radio2',
                    value='value2', selected=False,
                    x=110, y=595, buttonStyle='cross',
                    borderStyle='solid', shape='circle',
                    borderColor=green, fillColor=blue, 
                    borderWidth=2,
                    textColor=pink, forceBorder=True)
     
     c.drawString(10, 550, 'Pony:')
     form.radio(name='radio3', tooltip='Field radio3',
                    value='value1', selected=False,
                    x=110, y=545, buttonStyle='star',
                    borderStyle='bevelled', shape='square',
                    borderColor=blue, fillColor=green, 
                    borderWidth=2,
                    textColor=magenta, forceBorder=False)
     form.radio(name='radio3', tooltip='Field radio3',
                    value='value2', selected=True,
                    x=110, y=545, buttonStyle='star',
                    borderStyle='bevelled', shape='circle',
                    borderColor=blue, fillColor=green, 
                    borderWidth=2,
                    textColor=magenta, forceBorder=True)
     
     c.save()
     
     # if __name__ == '__main__':
     #     create_simple_radios()
     #     create_simple_choices()
     #     create_simple_listboxes()
          #     create_simple_form()



def create_simple_choices():
     c = canvas.Canvas('simple_choices.pdf')
     
     c.setFont("Courier", 20)
     c.drawCentredString(300, 700, 'Choices')
     c.setFont("Courier", 14)
     form = c.acroForm
     
     c.drawString(10, 650, 'Choose a letter:')
     options = [('A','Av'),'B',('C','Cv'),('D','Dv'),'E',('F',),('G','Gv')]
     form.choice(name='choice1', tooltip='Field choice1',
                    value='A',
                    x=165, y=645, width=72, height=20,
                    borderColor=magenta, fillColor=pink, 
                    textColor=blue, forceBorder=True, options=options)
     
     c.drawString(10, 600, 'Choose an animal:')
     options = [('Cat', 'cat'), ('Dog', 'dog'), ('Pig', 'pig')]
     form.choice(name='choice2', tooltip='Field choice2',
                    value='Cat',
                    options=options, 
                    x=165, y=595, width=72, height=20,
                    borderStyle='solid', borderWidth=1,
                    forceBorder=True)
     
     c.save()

# if __name__ == '__main__':
#     create_simple_choices()
#     create_simple_listboxes()
#     create_simple_form()


def create_simple_listboxes():
     c = canvas.Canvas('simple_listboxes.pdf')
     
     c.setFont("Courier", 20)
     c.drawCentredString(300, 700, 'Listboxes')
     c.setFont("Courier", 14)
     form = c.acroForm
     
     c.drawString(10, 650, 'Choose a letter:')
     options = [('A','Av'),'B',('C','Cv'),('D','Dv'),'E',('F',),('G','Gv')]
     form.listbox(name='listbox1', value='A',
                    x=165, y=590, width=72, height=72,
                    borderColor=magenta, fillColor=pink, 
                    textColor=blue, forceBorder=True, options=options,
                    fieldFlags='multiSelect')
     
     c.drawString(10, 500, 'Choose an animal:')
     options = [('Cat', 'cat'), ('Dog', 'dog'), ('Pig', 'pig')]
     form.listbox(name='choice2', tooltip='Field choice2',
                    value='Cat',
                    options=options, 
                    x=165, y=440, width=72, height=72,
                    borderStyle='solid', borderWidth=1,
                    forceBorder=True)
     
     c.save()

# if __name__ == '__main__':
#     create_simple_listboxes()
#     create_simple_form()



def create_simple_form():
     c = canvas.Canvas('simple_form.pdf')
     
     c.setFont("Courier", 20)
     c.drawCentredString(300, 700, 'Employment Form')
     c.setFont("Courier", 14)
     form = c.acroForm
     
     c.drawString(10, 650, 'First Name:')
     form.textfield(name='fname', tooltip='First Name',
                    x=110, y=635, borderStyle='inset',
                    borderColor=magenta, fillColor=pink, 
                    width=300,
                    textColor=blue, forceBorder=True)
     
     c.drawString(10, 600, 'Last Name:')
     form.textfield(name='lname', tooltip='Last Name',
                    x=110, y=585, borderStyle='inset',
                    borderColor=green, fillColor=magenta, 
                    width=300,
                    textColor=blue, forceBorder=True)
     
     c.drawString(10, 550, 'Address:')
     form.textfield(name='address', tooltip='Address',
                    x=110, y=535, borderStyle='inset',
                    width=400, forceBorder=True)
     
     c.drawString(10, 500, 'City:')
     form.textfield(name='city', tooltip='City',
                    x=110, y=485, borderStyle='inset',
                    forceBorder=True)
     
     c.drawString(250, 500, 'State:')
     form.textfield(name='state', tooltip='State',
                    x=350, y=485, borderStyle='inset',
                    forceBorder=True)
     
     c.drawString(10, 450, 'Zip Code:')
     form.textfield(name='zip_code', tooltip='Zip Code',
                    x=110, y=435, borderStyle='inset',
                    forceBorder=True)
     
     c.save()

# if __name__ == '__main__':
#     create_simple_form()




# rotate_pages.py


def rotate_pages(pdf_path):
     pdf_writer = PdfFileWriter()
     pdf_reader = PdfFileReader(pdf_path)
     # Rotate page 90 degrees to the right
     page_1 = pdf_reader.getPage(0).rotateClockwise(90)
     pdf_writer.addPage(page_1)
     # Rotate page 90 degrees to the left
     page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
     pdf_writer.addPage(page_2)
     # Add a page in normal orientation
     pdf_writer.addPage(pdf_reader.getPage(2))

     with open('rotate_pages.pdf', 'wb') as fh:
          pdf_writer.write(fh)

# if __name__ == '__main__':
#     path = 'Jupyter_Notebook_An_Introduction.pdf'
#     rotate_pages(path)
#     create_simple_form()




# rotate_pages.py


def rotate_pages(pdf_path):
     pdf_writer = PdfFileWriter()
     pdf_reader = PdfFileReader(pdf_path)
     # Rotate page 90 degrees to the right
     page_1 = pdf_reader.getPage(0).rotateClockwise(90)
     pdf_writer.addPage(page_1)
     # Rotate page 90 degrees to the left
     page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
     pdf_writer.addPage(page_2)
     # Add a page in normal orientation
     pdf_writer.addPage(pdf_reader.getPage(2))

     with open('rotate_pages.pdf', 'wb') as fh:
          pdf_writer.write(fh)

# if __name__ == '__main__':
#     path = 'Jupyter_Notebook_An_Introduction.pdf'
#     rotate_pages(path)
#     rotate_pages(path)
#     create_simple_form()





# pdf_splitting.py

def split(path, name_of_split):
     pdf = PdfFileReader(path)
     for page in range(pdf.getNumPages()):
          pdf_writer = PdfFileWriter()
          pdf_writer.addPage(pdf.getPage(page))

          output = f'{name_of_split}{page}.pdf'
          with open(output, 'wb') as output_pdf:
               pdf_writer.write(output_pdf)

# if __name__ == '__main__':
#     path = 'Jupyter_Notebook_An_Introduction.pdf'
#     split(path, 'jupyter_page')
     # path = 'Jupyter_Notebook_An_Introduction.pdf'
#     rotate_pages(path)


# pdf_watermarker.py


def create_watermark(input_pdf, output, watermark):
     watermark_obj = PdfFileReader(watermark)
     watermark_page = watermark_obj.getPage(0)

     pdf_reader = PdfFileReader(input_pdf)
     pdf_writer = PdfFileWriter()

     # Watermark all the pages
     for page in range(pdf_reader.getNumPages()):
          page = pdf_reader.getPage(page)
          page.mergePage(watermark_page)
          pdf_writer.addPage(page)

     with open(output, 'wb') as out:
          pdf_writer.write(out)

# if __name__ == '__main__':
#     create_watermark(
#         input_pdf='Jupyter_Notebook_An_Introduction.pdf', 
#         output='watermarked_notebook.pdf',
#         watermark='watermark.pdf')

     #    create_watermark() accepts three arguments:

# input_pdf: the PDF file path to be watermarked
# output: the path you want to save the watermarked version of the PDF
# watermark: a PDF that contains your watermark image or text


# pdf_encrypt.py

# def add_encryption(input_pdf, output_pdf, password):
#      pdf_writer = PdfFileWriter()
#      pdf_reader = PdfFileReader(input_pdf)

#      for page in range(pdf_reader.getNumPages()):
#           pdf_writer.addPage(pdf_reader.getPage(page))

#      pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
#                          use_128bit=True)

#      with open(output_pdf, 'wb') as fh:
#           pdf_writer.write(fh)

if __name__ == '__main__':
     # add_encryption(input_pdf='reportlab-sample.pdf',
     #               output_pdf='reportlab-encrypted.pdf',
     #               password='twofish')
     # create_watermark(input_pdf='Jupyter_Notebook_An_Introduction.pdf', 
     #                  output='watermarked_notebook.pdf',
     #                  watermark='watermark.pdf')
     # path = 'Jupyter_Notebook_An_Introduction.pdf'
     # split(path, 'jupyter_page')
     # path = 'Jupyter_Notebook_An_Introduction.pdf'
     # rotate_pages(path)

     # path = 'Jupyter_Notebook_An_Introduction.pdf'
     # rotate_pages(path)
     # rotate_pages(path)
     create_simple_form()
     create_simple_checkboxes()
     create_simple_radios()
     create_simple_choices()
     create_simple_listboxes()
