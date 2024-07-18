# a={
#     "id": "before-getting-started.about-you",
#     "order": 1,
#     "name": "Before getting started : Person taking interview",
#     "endInterview": False,
#     "questions": [
#       {
#         "id": "will.creator",
#         "order": 1,
#         "type": "RADIO",
#         "text": "Who is doing this interview?",
#         "note": None,
#         "multipleChoice": False,
#         "conditions": [
#           "'pre.launch_type' == 'public'"
#         ],
#         "acceptedValues": {
#           "testator": "The person whose Will it is or taking for himself or herself (i.e. the testator)",
#           "solicitor": "A solicitor or will-writer on behalf of a client",
#           "other": "The testator, with assistance from someone else (e.g. a friend or relative)"
#         }
#       }
#     ]
#   }

# # Sample user response
# user_response = "taking for myself with the help of friend"  # This should be dynamically set based on actual user input

# # Constructing the prompt for the LLM
# question = a['questions'][0]['text']

# accepted_values_data=a['questions'][0]['acceptedValues']
# prompt2 = f"""[[INST]]<<SYS>The user responded with -"{user_response}" to the question -"{question}". 
# Based on the following options, determine the most appropriate key:

# {a['questions'][0]['acceptedValues']}

# The output must be a JSON object with the key that best matches the user's response.

# Your response should conform to this JSON format:

# Input:
# {{
#     "input": "The user responded with -\"taking on the behalf of client\" to the question -\"Who is doing this interview?\". \\nBased on the following options, determine the most appropriate key:\\n\\n{{'testator': 'The person whose Will it is himself or herself (i.e. the testator)', 'solicitor': 'A solicitor or will-writer on behalf of a client', 'other': 'The testator, with assistance from someone else (e.g. a friend or relative)'}}\\n\\nPlease provide the key that best matches the user's response."
# }}

# Output:
# {{
#    "output": "solicitor"
# }}
# <<SYS>[[/INST]]
# Output:"""


# from response_calculator import generate,cal_response_gemini,str_jsonify

# ans=generate(prompt2)
# answer=str_jsonify(ans)
# print(answer['output'])


# # Sample user response
dob = "16 may 2002"  # This should be dynamically set based on actual user input

# Constructing the prompt for the LLM
format = 'dd/mm/yyyy'



prompt =f"""
[[INST]]<<SYS>
Convert this date string-{dob} into date format-{format}
Your response should conform to this JSON format:
Input:
{{"input":"Convert this date string- 26 june 1996 into date format-'dd/mm/yyyy'}}
Output:
{{"output":"26/06/1996"}}
<<SYS>[[/INST]]
Output:
"""

from response_calculator import generate,cal_response_gemini,str_jsonify,generate_address

ans=generate(prompt)
answer=str_jsonify(ans)
print(answer)

