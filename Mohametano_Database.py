import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet ['A1'] = "ID"
sheet ['B1'] = "Applicant Name"
sheet['C1'] = "Gender"
sheet['D1'] = "Age"
sheet['E1'] = "Civil Status"
sheet['F1'] = "Home address"
sheet['G1'] = "School name"
sheet['H1'] = "Email address"
sheet['I1'] = "Phone Number"
workbook.save("Mohametano_Database.xlsx")