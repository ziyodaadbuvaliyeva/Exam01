fayl="report.pdf"

if '.pdf' in fayl:
    print("fayl turi:pdf")
elif 'docx' in fayl:
    print('fayl turi:docx')
elif".txt" in fayl:
    print('fayl turi:txt')
else:
    print("fayl turi nomalum")