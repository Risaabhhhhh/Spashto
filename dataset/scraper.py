import pandas as pd
import uuid

# Dummy data for demonstration purposes. In a real scenario, this script would scrape 
# and parse income tax FAQs and circulars. We explicitly state here that this is 
# mock data and not fully human-reviewed dataset for production.
data = [
    {
        "id": str(uuid.uuid4()),
        "document_id": "faq_income_tax_001",
        "original_text": "An individual is required to furnish a return of income under section 139(1) if his total income exceeds the maximum amount not chargeable to tax.",
        "simplified_text": "You must file an income tax return if your total income is more than the basic exemption limit.",
        "source_language": "en",
        "target_language": "en",
        "document_type": "FAQ",
        "domain": "income-tax",
        "complexity": 2,
        "source_url": "https://incometaxindia.gov.in/faq"
    },
    {
        "id": str(uuid.uuid4()),
        "document_id": "faq_income_tax_001",
        "original_text": "Belated return can be filed at any time before the end of the relevant assessment year or before the completion of the assessment, whichever is earlier.",
        "simplified_text": "You can file a late return before the assessment year ends or before your assessment is completed, whichever comes first.",
        "source_language": "en",
        "target_language": "en",
        "document_type": "FAQ",
        "domain": "income-tax",
        "complexity": 2,
        "source_url": "https://incometaxindia.gov.in/faq"
    },
    {
        "id": str(uuid.uuid4()),
        "document_id": "circular_002",
        "original_text": "Where the Assessing Officer is satisfied that the assessee has concealed the particulars of his income or furnished inaccurate particulars of such income, he may direct that such person shall pay by way of penalty.",
        "simplified_text": "If the tax officer finds you hid your income or provided false details, they can fine you.",
        "source_language": "en",
        "target_language": "en",
        "document_type": "Circular",
        "domain": "income-tax",
        "complexity": 3,
        "source_url": "https://incometaxindia.gov.in/circulars"
    },
    {
        "id": str(uuid.uuid4()),
        "document_id": "circular_002",
        "original_text": "The penalty shall not be less than the amount of tax sought to be evaded by reason of concealment of particulars of his income or the furnishing of inaccurate particulars of such income.",
        "simplified_text": "The fine will be at least equal to the amount of tax you tried to avoid paying.",
        "source_language": "en",
        "target_language": "en",
        "document_type": "Circular",
        "domain": "income-tax",
        "complexity": 2,
        "source_url": "https://incometaxindia.gov.in/circulars"
    },
    {
        "id": str(uuid.uuid4()),
        "document_id": "notice_143_1",
        "original_text": "Intimation under section 143(1) is sent to the assessee detailing the computation of income and tax payable or refundable.",
        "simplified_text": "A notice under section 143(1) tells you how your income and tax were calculated, and if you owe money or get a refund.",
        "source_language": "en",
        "target_language": "en",
        "document_type": "Notice",
        "domain": "income-tax",
        "complexity": 2,
        "source_url": "https://incometaxindia.gov.in/notices"
    },
    {
        "id": str(uuid.uuid4()),
        "document_id": "form_16_inst",
        "original_text": "Form 16 is a certificate issued by an employer certifying the details of tax deducted at source and deposited to the Central Government.",
        "simplified_text": "Form 16 is a document from your employer showing the tax taken from your salary and paid to the government.",
        "source_language": "en",
        "target_language": "en",
        "document_type": "Form Instruction",
        "domain": "income-tax",
        "complexity": 1,
        "source_url": "https://incometaxindia.gov.in/forms"
    },
    {
        "id": str(uuid.uuid4()),
        "document_id": "faq_tds_004",
        "original_text": "Any person responsible for paying any sum representing winnings from any lottery or crossword puzzle or card game and other game of any sort in an amount exceeding ten thousand rupees shall, at the time of payment thereof, deduct income-tax thereon at the rates in force.",
        "simplified_text": "If someone pays you more than ₹10,000 for winning a lottery, crossword, or game, they must deduct tax from it before paying you.",
        "source_language": "en",
        "target_language": "en",
        "document_type": "FAQ",
        "domain": "income-tax",
        "complexity": 2,
        "source_url": "https://incometaxindia.gov.in/faq"
    }
]

def generate_mock_data():
    df = pd.DataFrame(data)
    df.to_csv("dataset/labeled/indian_gov_legal_simplification.csv", index=False)
    print(f"Generated {len(df)} rows in dataset/labeled/indian_gov_legal_simplification.csv")

if __name__ == "__main__":
    generate_mock_data()
