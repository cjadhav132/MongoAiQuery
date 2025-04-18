import json
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# API_KEY = "AIzaSyDIBqPK2O6bO0GsUkZhYKN1Vz_Zq0RJjUk"
# query_object = json.loads(query_strings[1])
# query_object = json.loads(op)
# print(query_object)
# try:
#     query_object = json.loads(op)
#     print(query_object)
# except :
#     print("error")


class GeminieWrapper:
    client = None

    def __init__(self):
        API_KEY = os.getenv("API_KEY")
        self.client = genai.Client(api_key=API_KEY)

    def getContent(Self, input_message) -> str:
        data_structure = """
            My mongodb document stucture looks like: {
            age: 32,
            name: "Chinmay",
            city: "Thane",
            state: "Maha"
            }
        """

        old_msg = "give me only the  query to write inside the find function (without explaination and without any language name), also put the key name in qoutes: "
        msg = "people in city named mumbai"

        # return data_structure + old_msg + msg
        return data_structure + old_msg + input_message

    def getQuery(self, input_message) -> str:
        contents = self.getContent(input_message)
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=contents
        )
        op = response.text
        print(op[1:-2])

        query_object = eval(op)
        print(query_object)


if __name__ == "__main__":
    print("Main")
    ai = GeminieWrapper()
    ip = input()
    op = ai.getContent(ip)
    print(op)
