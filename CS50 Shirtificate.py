from fpdf import FPDF


class ShirtificatePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def create_shirtificate(name):
    pdf = ShirtificatePDF(orientation="P", format="A4")
    pdf.add_page()

    pdf.set_font("Arial", "B", 36)

    shirt_image_path = "shirtificate.png"

    pdf.image(shirt_image_path, x=0, y=50, w=210, h=297, type="PNG")

    pdf.set_xy(0, 130)
    pdf.set_font("Arial", "B", 50)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(210, 20, name, 0, 0, "C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    create_shirtificate(user_name)
