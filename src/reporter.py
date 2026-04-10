from fpdf import FPDF

def duration_report(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Analysis of Media Content Durations", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
    # Simple Elaboration
    pdf.set_y(190) 
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This report shows that movies in the library are usually around 100 minutes long, "
                         "which is a standard film length. On the other hand, TV shows typically last for "
                         "about 2 seasons. This suggests that while there are many movies, the TV shows "
                         "tend to be shorter series rather than long-running multi-season programs.")
    pdf.output("Duration_Report.pdf")


def report_content_distribution(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Global Content Portfolio Distribution", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
    # Simple Elaboration
    pdf.set_y(190)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This chart shows that there are significantly more movies than TV shows in the collection. "
                         "With over 5,000 movies and fewer than 1,000 TV shows, it is clear that the library "
                         "focuses heavily on feature films. This makes the platform better suited for people "
                         "who enjoy watching movies rather than long series.")
    pdf.output("Content_Distribution.pdf")


def report_yearly_trend(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Historical Release Volume Trends", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
    # Simple Elaboration
    pdf.set_y(190)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This graph shows how content production has changed over time. Production was very low "
                         "and steady for many years, but it exploded after 2010, reaching a massive peak in 2018. "
                         "The sharp drop seen after 2019 is likely due to the global pandemic, which caused "
                         "many movie and show productions to stop temporarily.")
    pdf.output("Yearly_Trends.pdf")


def report_top_countries(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Leading Nations in Global Content Production", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
    # Simple Elaboration
    pdf.set_y(190)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This report highlights that the United States and India are the world leaders in making "
                         "movies and shows for this library. The United States has nearly 2,400 titles, while "
                         "India follows with about 1,000. Other countries like the UK and Canada also contribute, "
                         "but the majority of the content comes from these two main countries.")
    pdf.output("top_countries.pdf")


def report_rating_distribution(image_path):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Audience Demographics & Rating Classification", ln=True, align='C')
    
    # Graph
    pdf.image(image_path, x=10, y=30, w=190)
    
    # Simple Elaboration
    pdf.set_y(190)
    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, "This chart shows that most of the content is made for adults and teenagers. The most "
                         "common rating is TV-MA (for mature audiences), followed by TV-14 (for teens). Ratings "
                         "for young children, like TV-G and TV-Y, are much less common. This suggests the library "
                         "is mainly designed for older viewers rather than small kids.")
    pdf.output("rating_distribution.pdf")
