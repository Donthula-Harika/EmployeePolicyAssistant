# Create sample employee policy PDFs
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

documents = {
    "Employee Handbook.pdf": """
Employee Handbook

Employees must maintain professional conduct.
Office timing is from 9 AM to 6 PM.
Employees should follow company ethics and policies.
""",

    "Leave Policy.pdf": """
Leave Policy

Employees receive 12 casual leaves annually.
Employees receive 15 sick leaves annually.
Unused casual leaves cannot be carried forward.
""",

    "Travel Policy.pdf": """
Travel Policy

Travel expenses are reimbursed within 30 days.
Original receipts must be submitted for reimbursement.
""",

    "Work From Home Policy.pdf": """
Work From Home Policy

Employees may work from home twice per week.
Manager approval is required for additional remote work.
""",

    "Medical Insurance Policy.pdf": """
Medical Insurance Policy

All employees are covered under company medical insurance.
Dependent coverage is available for spouse and children.
"""
}

for filename, content in documents.items():

    doc = SimpleDocTemplate(filename)

    story = []

    for line in content.strip().split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))
        story.append(Spacer(1, 10))

    doc.build(story)

print("PDF files created successfully.")