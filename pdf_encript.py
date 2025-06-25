import pikepdf

pdf = pikepdf.Pdf.open("demo.pdf")

no_ext = pikepdf.Permissions(extract=False)
pdf.save("pdf2.pdf",encryption=pikepdf.Encryption(user='@123',
                                                  owner="Sarkar",
                                                  allow=no_ext))
