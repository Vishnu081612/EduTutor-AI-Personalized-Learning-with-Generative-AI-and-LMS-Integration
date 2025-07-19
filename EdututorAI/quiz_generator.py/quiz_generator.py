from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai import Credentials

creds = Credentials(
    api_key="your_real_ibm_api_key",
    url="your_real_ibm_instance_url"
)
  # Ensure .env file has correct credentials

model = Model("granite-13b-chat-v2", credentials=creds)

topic = input("Enter a topic: ")

prompt = f"Generate 5 multiple-choice questions about: {topic}"

result = model.generate(
    prompt,
    params={"decoding_method": "sample", "max_new_tokens": 500}
)

print("\nGenerated Quiz Questions:\n")
print(result)

from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai import Credentials

creds = Credentials(
    api_key="your_real_ibm_api_key",
    url="your_real_ibm_instance_url"
)
  # Ensure .env file has correct credentials

model = Model("granite-13b-chat-v2", credentials=creds)

topic = input("Enter a topic: ")

prompt = f"Generate 5 multiple-choice questions about: {topic}"

result = model.generate(
    prompt,
    params={"decoding_method": "sample", "max_new_tokens": 500}
)

print("\nGenerated Quiz Questions:\n")
print(result)
