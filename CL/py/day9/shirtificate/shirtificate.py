from fpdf import FPDF

def main():
    user_name = input("Name: ")
    create_shirtificate(user_name)


def create_shirtificate(name):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica","B", size=45)
    pdf.cell(200, 10, text="CS50 Shirtificate", align='C')



    # Add image
    pdf.image("shirtificate.png", x=10, y=50, w=190, h=180)
    # Text
    pdf.set_font("helvetica", size=16)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 90)  # 设置文本的位置
    pdf.cell(250, 20, f"{name} took CS50", 0, 1, 'C', 0, 0)

    # Save the pdf with name .pdf
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
