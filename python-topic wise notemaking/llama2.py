'''#from langchain.llms import Ollama
from langchain_community.llms import Ollama
# Function to generate a summary using Ollama model
def generate_summary(text):
    # Initialize the Ollama model (make sure the base_url and model name are correct)
    ollama = Ollama(base_url='http://localhost:11434', model='phi3')
    
    # Prompt to ask the model for a summary of the input text
    prompt = f"Please \n{text}\n\n" \
         "**Section 1 - Introduction and Thesis Statement Summary (TOPIC)**\n" \
         "*- Provide the main thesis, purpose of research/study as articulated in the introduction. Describe how this foundational idea is reflected throughout each subsequent section.*\n\n" \
         "**Section 2 - Main Content with Subtopics and Their Descriptions (DESCRIPTION FOR EACH TOPIC)**\n" \
         "*- Identify main sections/subsections within the PDF, highlighting their significance in relation to the overall thesis. Summarize each subtopic's core ideas while maintaining a\n" \
         "clear connection back to central arguments or findings.*\n" \
         "  - For complex concepts: Simplify using definitions that remain faithful to original context without introducing external information not found within the document itself,\n" \
         "ensuring clarity and accessibility for student understanding.\n" \
         "*- When summarizing methods/theories discussed in these sections: Outline their relevance directly tied back to core ideas or arguments provided by author(s). Incorporate\n" \
         "necessary explanations while maintaining academic integrity.*\n" \
         "  - For visual representations (figures, tables): Describe them succinctly as they appear within the document and explain how they contribute to understanding the content. Ensure\n" \
         "that descriptions aid comprehension without misrepresentation of data or figures included in original text.\n" \
         "*- Direct quotes: Include direct citations from key sections with attributions, paraphrasing where appropriate while preserving meaning.*\n" \
         "  - Insert questions at strategic points within these summaries to promote critical thinking and deeper understanding related back to the content discussed herein for each\n" \
         "subtopic. Provide guided answers following these questions directly referring back to text contents as a means of fostering interactive learning experiences without personal\n" \
         "interpretations or external commentary.*\n" \
         "*- Reference details: Present all references, citations included in summaries accurately according to APA/MLA style standards (if provided by author(s) otherwise general academic\n" \
         "standard). Ensure proper attribution is given for any ideas borrowed from the PDF.*\n" \
         "  - Organize this information under consistent and clear headings that reflect logical progression of topics throughout sections, beginning with bold key statements followed by\n" \
         "relevant supporting details to maintain clarity.*\n" \
         "*- Transition phrases: Use these skillfully between summaries drawn from different sections/subsections for seamless navigation across content areas ensuring students are\n" \
         "reminded of prior points when needed as a cohesive narrative unfolds, guiding them through the document's logical structure.\n" \
         "  - Concluding synthesis (DESCRIPTION): Offer concise summarization reflecting back on all key takeaways from this text in relation to its greater context or significance without\n" \
         "introducing new interpretations while highlighting how these insights might relate to further learning and application.*"
    
    # Get the response from the model
    summary = ollama(prompt)
    
    # Return the generated summary
    return summary'''
    
'''from langchain_community.llms import Ollama
from concurrent.futures import ProcessPoolExecutor
import asyncio
from spellchecker import SpellChecker

# Function to generate a summary with spelling correction and parallel processing
def generate_summary(text):
    # Initialize the Ollama model
    ollama = Ollama(base_url='http://localhost:11434', model='phi3')

    # Function to generate a summary using Ollama model
    def _generate_summary(text):
        prompt = f"Please \n{text}\n\n" \
            "**Section 1 - Introduction and Thesis Statement Summary (TOPIC)**\n" \
            "*- Provide the main thesis, purpose of research/study as articulated in the introduction. Describe how this foundational idea is reflected throughout each subsequent section.*\n\n" \
            "**Section 2 - Main Content with Subtopics and Their Descriptions (DESCRIPTION FOR EACH TOPIC)**\n" \
            "*- Identify main sections/subsections within the PDF, highlighting their significance in relation to the overall thesis. Summarize each subtopic's core ideas while maintaining a\n" \
            "clear connection back to central arguments or findings.*\n" \
            "  - For complex concepts: Simplify using definitions that remain faithful to original context without introducing external information not found within the document itself,\n" \
            "ensuring clarity and accessibility for student understanding.\n" \
            "*- When summarizing methods/theories discussed in these sections: Outline their relevance directly tied back to core ideas or arguments provided by author(s). Incorporate\n" \
            "necessary explanations while maintaining academic integrity.*\n" \
            "  - For visual representations (figures, tables): Describe them succinctly as they appear within the document and explain how they contribute to understanding the content. Ensure\n" \
            "that descriptions aid comprehension without misrepresentation of data or figures included in original text.\n" \
            "*- Direct quotes: Include direct citations from key sections with attributions, paraphrasing where appropriate while preserving meaning.*\n" \
            "  - Insert questions at strategic points within these summaries to promote critical thinking and deeper understanding related back to the content discussed herein for each\n" \
            "subtopic. Provide guided answers following these questions directly referring back to text contents as a means of fostering interactive learning experiences without personal\n" \
            "interpretations or external commentary.*\n" \
            "*- Reference details: Present all references, citations included in summaries accurately according to APA/MLA style standards (if provided by author(s) otherwise general academic\n" \
            "standard). Ensure proper attribution is given for any ideas borrowed from the PDF.*\n" \
            "  - Organize this information under consistent and clear headings that reflect logical progression of topics throughout sections, beginning with bold key statements followed by\n" \
            "relevant supporting details to maintain clarity.*\n" \
            "*- Transition phrases: Use these skillfully between summaries drawn from different sections/subsections for seamless navigation across content areas ensuring students are\n" \
            "reminded of prior points when needed as a cohesive narrative unfolds, guiding them through the document's logical structure.\n" \
            "  - Concluding synthesis (DESCRIPTION): Offer concise summarization reflecting back on all key takeaways from this text in relation to its greater context or significance without\n" \
            "introducing new interpretations while highlighting how these insights might relate to further learning and application.*"
        
        summary = ollama(prompt)
        return summary

    # Function to correct spelling using PySpellChecker
    def _correct_spelling(text):
        spell = SpellChecker()
        words = text.split()
        corrected_words = []

        for word in words:
            corrected = spell.correction(word)
            if corrected is None:
                corrected_words.append(word)  # Keep the original word if no correction is found
            else:
                corrected_words.append(corrected)

        return " ".join(corrected_words)  # Fixed indentation here

    # Function to process text concurrently (no need for ProcessPoolExecutor for a single text)
    def _process_text(text):
        # Directly process the text to generate summary after spelling correction
        summary = _generate_summary(text)
        return summary

    # Function to run asynchronous tasks for spelling correction and summary generation
    async def _async_process_text(text):
        loop = asyncio.get_event_loop()
        
        # Correct spelling asynchronously
        corrected_text = await loop.run_in_executor(None, lambda: _correct_spelling(text))
        
        # Generate summary asynchronously
        summary = await loop.run_in_executor(None, lambda: _process_text(corrected_text))
        
        return summary

    # Run the asynchronous tasks
    summary = asyncio.run(_async_process_text(text))

    # Return the generated summary
    return summary
'''

from langchain_community.llms import Ollama
from concurrent.futures import ProcessPoolExecutor
import asyncio
from spellchecker import SpellChecker

# Function to generate a refined summary with parallel processing and spelling correction
def generate_summary(text):
    # Initialize the Ollama model
    ollama = Ollama(base_url='http://localhost:11434', model='phi3')

    # Refined prompt for summary generation
    def _generate_summary(text):
        
        prompt = (
    f"Please \n{text}\n\n"
    "**Section 1 - Introduction and Thesis Statement Summary (TOPIC)**\n"
    "- Summarize the main thesis and purpose of the research or study as outlined in the introduction.\n"
    "- Explain how this foundational idea is reflected throughout the subsequent sections.\n\n"
    "**Section 2 - Main Content with Subtopics and Their Descriptions (DESCRIPTION FOR EACH TOPIC)**\n"
    "- Identify main sections and subsections, summarizing their core ideas and relevance to the thesis.\n"
    "- Simplify complex concepts with clear definitions while staying true to the original context.\n"
    "- Add questions to promote critical thinking with brief answers based on the text.\n"
    "- Use bold headings and transition phrases to create a logical and cohesive flow across topics.\n\n"
    "**Concluding Synthesis (DESCRIPTION)**\n"
    "- Summarize all key takeaways, reflecting on their significance in the broader context.\n"
    "- Avoid introducing new interpretations but highlight how the insights might support further learning or application."
)

        
        return ollama(prompt)

    # Correct spelling using PySpellChecker
    def _correct_spelling(text):
        spell = SpellChecker()
        words = text.split()
        corrected_words = [spell.correction(word) or word for word in words]
        return " ".join(corrected_words)

    # Process text and generate summary
    def _process_text(text):
        corrected_text = _correct_spelling(text)
        summary = _generate_summary(corrected_text)
        return summary

    # Asynchronous wrapper for parallel processing
    async def _async_process_text(text):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, lambda: _process_text(text))

    # Run the asynchronous tasks
    summary = asyncio.run(_async_process_text(text))

    return summary
