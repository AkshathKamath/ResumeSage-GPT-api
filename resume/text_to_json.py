from openai import OpenAI
import os
# from dotenv import load_dotenv

# load_dotenv()

client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

def convert_to_json(text):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role":"system",
                "content":"You are a helpful research assistant."
            },
            {
                "role":"user",
                "content":f"Convert this numbered list: {text} to a json list. Just return the json nothing else. No need to add indexes."
            }
        ]
    )
    return response.choices[0].message.content

# text = """1. Highlight your relevant backend development experience by elaborating on specific projects where you have built and developed backend applications.\n2. Specify your proficiency in modern object-oriented programming languages like Java, Python, or others, as required by the job description.\n3. Emphasize your experience in crafting and implementing highly scalable and performant RESTful microservices.\n4. Include details about your proficiency in database technologies, such as RDBMS like PostgreSQL or NoSQL databases.\n5. Showcase your knowledge and hands-on experience with public cloud offerings like AWS, which aligns with the job requirements.\n6. Strengthen your communication skills and passion for collaboration in the professional experience section.\n7. Provide more specific examples in academic projects related to backend development, scalability, and performance optimization.\n8. Consider restructuring the content to clearly demonstrate how your skills and experiences align with the technical requirements of the desired role."""

# print(convert_to_json(text))