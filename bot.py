from openai import OpenAI
from dotenv import load_dotenv
import os
from cleaner import get_highlighted_properties
import json
load_dotenv()

api_key = os.getenv('API_KEY')
client = OpenAI(api_key=api_key)


tools = [
  {
      "type": "function",
      "function": {

          "name": "get_highlighted_properties",
          "parameters": {
              "type": "object",
              "properties": {
                  "number_of_properties": {"type": "string",
                                           "description": "Number of properties to be returned by this function. Up to 8 properties per type of property."},
                  "type_of_property":{"type": "string",
                                      "description": "This property can either be 'usada', 'nueva' or 'arriendo'"},
              },
              "additionalProperties": False,
          },
      },
  }
]

message = input("send a message for our bot >:)")
completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[{
      "role": "system",
      "content": "You are a helpful customer support assistant for the TOCTOC site. Use the supplied tools to assist the user."
  },
      {"role": "user", "content": message}],

  tools=tools,
)
calls = completion.choices[0].message.tool_calls
arguments = json.loads(calls[0].function.arguments)
print(get_highlighted_properties(int(arguments['number_of_properties']), arguments['type_of_property']))
