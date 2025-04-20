import json
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


class GeminieWrapper:
    client = None

    def __init__(self):
        API_KEY = os.getenv("API_KEY")
        self.client = genai.Client(api_key=API_KEY)

    def getContent(Self, input_message) -> str:
        data_structure = """
            My mongodb document stucture looks like:
             {
            "_id": {
                "$oid": "6804b92992dfbd27a0da46d7"
            },
            "ApplicationDate": {
                "$date": "2018-01-01T00:00:00.000Z"
            },
            "Age": 45,
            "AnnualIncome": 26032,
            "CreditScore": 467,
            "EmploymentStatus": "Employed",
            "EducationLevel": "Associate",
            "Experience": 24,
            "LoanAmount": 17499,
            "LoanDuration": 36,
            "MaritalStatus": "Divorced",
            "NumberOfDependents": 4,
            "HomeOwnershipStatus": "Mortgage",
            "MonthlyDebtPayments": 581,
            "CreditCardUtilizationRate": 0.23131078399389507,
            "NumberOfOpenCreditLines": 3,
            "NumberOfCreditInquiries": 3,
            "DebtToIncomeRatio": 0.1677948754822763,
            "BankruptcyHistory": 0,
            "LoanPurpose": "Education",
            "PreviousLoanDefaults": 0,
            "PaymentHistory": 25,
            "LengthOfCreditHistory": 14,
            "SavingsAccountBalance": 2540,
            "CheckingAccountBalance": 665,
            "TotalAssets": 30050,
            "TotalLiabilities": 1749,
            "MonthlyIncome": 2169.3333333333335,
            "UtilityBillsPaymentHistory": 0.704785929274909,
            "JobTenure": 7,
            "NetWorth": 28301,
            "BaseInterestRate": 0.268999,
            "InterestRate": 0.2587266314276737,
            "MonthlyLoanPayment": 703.8591139641082,
            "TotalDebtToIncomeRatio": 0.592282935140185,
            "LoanApproved": 0,
            "RiskScore": 52
            }
        """

        prompt = f"""Convert the following natural language query into a MongoDB aggregation pipeline in JSON format. Only output the JSON and nothing else.

            Natural Language Query: {input_message}"""
        return data_structure + prompt

    def getQuery(self, input_message) -> str:
        contents = self.getContent(input_message)
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=contents
        )
        op = response.text
        print(op)
        query = op.split('\n')
        pq = []
        for q in query:
            pq.append(q.strip())

        new_query = "".join(pq[1:-1])
        return new_query


if __name__ == "__main__":
    print("Main")
    ai = GeminieWrapper()
    ip = input("Give me a question: ")
    op = ai.getQuery(ip)
    print(op)
