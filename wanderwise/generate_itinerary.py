"""
This module contains the code to generate an itinerary for the user.
"""
import os

from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from .llm_data_structures.itinerary import Itinerary
from .llm_prompts.itinerary_prompt import ITINERARY_PROMPT
from .llm_prompts.system_instructions import ITINERARY_SYSTEM_INSTRUCTIONS

load_dotenv()


def generate_itinerary(destination: str, activities: str, trip_length: str) -> Itinerary:
    # Initialize the LLM.
    chat_model = ChatOpenAI(model_name="gpt-4o",
                            temperature=0.7,
                            openai_api_key=os.environ.get("OPENAI_API_KEY"))

    # Create the parser.
    parser = PydanticOutputParser(pydantic_object=Itinerary)

    # Create the prompt template.
    prompt = PromptTemplate(
        template=ITINERARY_SYSTEM_INSTRUCTIONS,
        input_variables=["itinerary_prompt"],  # The formatted ItineraryPrompt template.
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    # Create the chain to invoke the model.
    chain = prompt | chat_model | parser

    # Create the user prompt, which contains the necessary info to generate the itinerary.
    user_prompt = ITINERARY_PROMPT.format(
        destination=destination,
        activities=activities,
        trip_length=trip_length
    )

    # Generate the itinerary.
    generated_itinerary = chain.invoke({"itinerary_prompt": user_prompt})

    return generated_itinerary  # This is an instance of the Itinerary class.
