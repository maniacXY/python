from fpdf import FPDF

# PRE CLASS SETUP
class PDF(FPDF):
    def header(self):
        # Logo
        try:
            self.image('mypdf_creator/assciistandard.png',x=30,w=150, h=20)
        except FileNotFoundError:
            self.ln(20)

            print("Wenn du einen Header möchtest pack ihn in ./mypdfcreator und ändere den Dateinpfad ind ./mypdfcreator/MyCreator.py")
        self.set_font('DejaVu', 'B', 2)   #B - bold; I - italic, U - underline
        self.ln(1)

    # Page footer
    def footer(self):
        # Position at 2 cm from bottom
        self.set_y(-20)
        # DejaVu italic 8
        self.set_font('DejaVu', 'I', 8)
        # Page number
        self.cell(0, 10, 'Created and Design by Patrick Wiebell with PyFPDF', 0, 0, 'C')

class Creator(PDF):
    #190 max Breite ?  eher 180 + 30 margin = 210
    config = {
        "font_family": "DejaVu",
        "font_size_content": 12,
        "line_hight": 7,
        "sign": "mypdf_creator/sample.png",
        "Ausbildungsgruppe": "YOUR GROUP",
        "Name":"Mustermann, Max"
    }

    def __init__(self, author="PW", output="mypdf.pdf", data="") -> None:
        super().__init__()
        self.author = author
        self.data = data
        self.page_setup()
        self.top_table()
        self.spacer()
        self.content_head()
        self.content_body(self.data)
        self.footer()
        self.pdf.output(output, 'F')
        
    def page_setup(self):
        self.pdf = PDF()
        self.pdf.add_font('DejaVu', '','mypdf_creator/fonts/DejaVuSansCondensed.ttf', True)
        self.pdf.add_font('DejaVu','I','mypdf_creator/fonts/DejaVuSansCondensed-Oblique.ttf', True)
        self.pdf.add_font('DejaVu','B','mypdf_creator/fonts/DejaVuSansCondensed-Bold.ttf', True)
        self.pdf.set_author(self.author)
        self.pdf.alias_nb_pages()
        self.pdf.add_page()
        self.pdf.set_left_margin(15)
        self.pdf.set_right_margin(15)
        
    def top_table(self):
        self.pdf.set_font(self.config["font_family"], 'B', 12)
        self.pdf.cell(50, 7,"Ausbildungsgruppe:", 1,0,"C",)
        self.pdf.set_font(self.config["font_family"], '', 12)
        self.pdf.cell(40, 7, self.config["Ausbildungsgruppe"], 1,0, "C")
        self.pdf.set_font(self.config["font_family"], 'B', 12)
        self.pdf.cell(40, 7, "Name:", 1, 0,"C")
        self.pdf.set_font(self.config["font_family"], '', 12)
        self.pdf.cell(50, 7, self.config["Name"], 1,1,"C")
        self.pdf.cell(180,1,"",1,1,fill=True)
        self.pdf.set_font(self.config["font_family"], 'B', 12)
        self.pdf.cell(50, 7,"Ausbildungs- und", "TLR",0,"C")
        self.pdf.cell(130,7,"",1,1,)
        self.pdf.cell(50, 7,"Tätigkeitsnachweis", "LRB",0,"C")
        self.pdf.cell(40, 7, "Kalenderwoche", 1,0, "C")
        self.pdf.cell(40, 7, "Monat", 1, 0,"C")
        self.pdf.cell(50, 7, "Ausbildungsjahr", 1,1,"C")
        self.pdf.set_font(self.config["font_family"], '', 12)
        self.pdf.cell(50, 7,self.data["Tätigkeitsnachweis"], 1,0,"C")
        self.pdf.cell(40, 7, self.data["Kalenderwoche"], 1,0, "C")
        self.pdf.cell(40, 7, self.data["Monat"], 1, 0,"C")
        self.pdf.cell(50, 7, self.data["Ausbildungsjahr"], 1,1,"C")
    
    def spacer(self):
        self.pdf.cell(180,1,"",0,1)
    
    def content_head(self):
        self.pdf.set_font(self.config["font_family"], 'B', 12)
        self.pdf.cell(49.5,8,"Tag",1,0,"C")
        self.pdf.cell(1,8,"",0,0)
        self.pdf.cell(129.5,8,"Ausgeführte Arbeiten, Unterricht, Unterweisungen",1,1,"C")
        self.pdf.cell(49.5,0.5,"",0,0, fill=True)
        self.pdf.cell(1,0.5,"",0,0)
        self.pdf.cell(129.5,0.3,"",1,1,fill=True)
    
    def content_body(self, data):
        tage = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag")
        self.pdf.set_font(self.config["font_family"], "", 8)
        #mitte ist die 3. Zelle -> 2 -1
        mitte = 2
        
        for tag in tage:
            a = 0
            for num in range(5):
                self.pdf.set_font("DejaVu", "B", 12)
                if num == mitte:
                    self.pdf.cell(49.5,7,"{}".format(tag),"LR",0, "C")
                else:
                    self.pdf.cell(49.5,7,"","LR",0, "C")
                self.pdf.set_font("DejaVu", "", 8)
                self.pdf.cell(1,7,"",0,0)
                         
                if a   < len(data[tag]):
                    self.pdf.cell(129.5,7,"{}".format(data[tag][a]),1,1, "C")
                else:
                    self.pdf.cell(129.5,7,"",1,1, "C")
                
                a+=1
            if tag != "Freitag":
                self.pdf.cell(49.5,1,"","TB",0,"")
                self.pdf.cell(1,1,"",0,0)
                self.pdf.cell(129.5,1,"","TB",1,"")
            else:
                self.pdf.cell(49.5,1,"","T",0,"")
                self.pdf.cell(1,1,"",0,0)
                self.pdf.cell(129.5,1,"","T",1,"")
        
    def footer(self):
        self.pdf.cell(180,1,"",0,1)
        self.pdf.set_font(self.config["font_family"], "B", 8)
        self.pdf.cell(90,5,"Für die Richtigkeit:",0)
        self.pdf.cell(90,5,"Gesehen:",0,1)
        self.pdf.cell(90,11,"","TLR",0)
        self.pdf.cell(90,11,"","TR",1)
        self.pdf.set_font(self.config["font_family"], "", 8)
        self.pdf.cell(2,5,"","L",)
        self.pdf.cell(24,5,self.data["sign_date"],"B",0,"C")
        self.pdf.cell(2,5,"",)
        self.pdf.cell(60,5,"","B",0,"C")
        self.pdf.cell(2,5,"", )
        self.pdf.cell(2,5,"", "L")
        self.pdf.cell(24,5,"","B",0,"C")
        self.pdf.cell(2,5,"", "")
        self.pdf.cell(60,5,"","B",0,"C")
        self.pdf.cell(2,5,"","R",1,)
        #zweite runde
        self.pdf.cell(2,5,"","LB")
        self.pdf.cell(24,5,"Datum","B",0,"C")
        self.pdf.cell(2,5,"","B")
        self.pdf.cell(60,5,"Unterschrift des Auszubildenden","B",0,"C")
        self.pdf.cell(2,5,"","B" )
        self.pdf.cell(2,5,"", "BL")
        self.pdf.cell(24,5,"Datum","B",0,"C")
        self.pdf.cell(2,5,"", "B")
        self.pdf.cell(60,5,"Unterschrift des IT-Ausbilders","B",0,"C")
        self.pdf.cell(2,5,"","RB")
        try:
            self.pdf.image(self.config["sign"], 50,256,35,15)
        except FileNotFoundError:
            print("Füge eine Unterschrift  mit dem Format:(392x244) ein, falls gewünscht. SIEHE docs.md ")