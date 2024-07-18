from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
from ibm_watson_machine_learning.foundation_models import Model
from dotenv import load_dotenv
from langchain.chains import LLMChain

from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate
import os
import google.generativeai as genai
import json



# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('gemini_api_key')
genai.configure(api_key=API_KEY)
model_gemini = genai.GenerativeModel('gemini-pro')
# Access the variables
ibm_url = os.getenv('IBM_URL')
ibm_apikey = os.getenv('IBM_APIKEY')
proj_id = os.getenv('project_id')

model_id="meta-llama/llama-3-70b-instruct"
model_id2='ibm/granite-13b-instruct-v2'

gen_parms = {
    "DECODING_METHOD" : "greedy",
    "TEMPERATURE":0,
    "TOP_P":0,
    "TOP_K":1,
    "MIN_NEW_TOKENS" : 1,
    "MAX_NEW_TOKENS" : 40
}
gen_parms2 = {
    "DECODING_METHOD" : "greedy",
    "TEMPERATURE":0,
    "TOP_P":0,
    "TOP_K":1,
    "MIN_NEW_TOKENS" : 1,
    "MAX_NEW_TOKENS" : 100
}

credentials = {
        "url": ibm_url,
        "apikey":ibm_apikey
    }
 
try:
   
    project_id = proj_id    
except KeyError:
    project_id = input("Please enter your project_id (hit enter): ")
    
    

model = Model( model_id, credentials, gen_parms, project_id )
model2 = Model( model_id, credentials, gen_parms2, project_id )
#################  generate llm response ##########################
def generate(augmented_prompt_in):
    generated_response = model.generate(augmented_prompt_in)
    return generated_response["results"][0]["generated_text"]


def generate_address(augmented_prompt_in):
    generated_response = model2.generate(augmented_prompt_in)
    return generated_response["results"][0]["generated_text"]
####################### to extract answer only from llm response using granite############################


def cal_response_gemini(prompt):
    response = model_gemini.generate_content(prompt)
    generated_response = response.text
    return generated_response


def str_jsonify(string_json_data):
    data_dict = json.loads(string_json_data)
    return data_dict