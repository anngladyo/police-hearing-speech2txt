import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

endpoint = os.getenv("OPENAI_ENDPOINT")
model_name = os.getenv("OPENAI_MODEL")
openai_key = os.getenv("OPENAI_API_KEY")
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=openai_key,
)

def generate_police_report(template_path, transcript_data, openai_client=client, output_path="generated_police_report.md"):
    # Read the markdown template file with proper encoding
    with open(template_path, "r", encoding='utf-8') as file:
        template = file.read() 

    with open(transcript_data, 'r', encoding='utf-8') as file:
        transcript_json = json.load(file)

    # Extract the 'DisplayText' from each dictionary and join them into a single string
    transcript_text = ' '.join(item['DisplayText'] for item in transcript_json if 'DisplayText' in item)

    # Debug: Print the first 200 characters of both to verify they're loaded correctly
    print("\nTranscript preview:", transcript_text[:200])
    print(f"\nTemplate length: {len(template)} characters")
    print(f"Transcript length: {len(transcript_text)} characters")

    response = openai_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""You are a helpful assistant who generates police reports based on a transcription of a police hearing. 

    Your task is to:
    1. Analyze the provided transcript carefully
    2. Extract relevant information (names, dates, locations, events, etc.)
    3. Fill in the template placeholders with this extracted information
    4. Return the completed report in markdown format

    Template to follow (replace ALL placeholders in brackets with actual data from the transcript):
    {template}

    IMPORTANT: Replace every placeholder like [Insert Report Number], [Insert Date], etc. with actual information from the transcript. If information is not available in the transcript, mark it as "Not specified in transcript" or make reasonable inferences based on the hearing content.""",
            },
            {
                "role": "user", 
                "content": f"""Please generate a complete police report by filling in the template with information from this hearing transcript. Make sure to replace all placeholders with actual data:

    TRANSCRIPT:
    {transcript_text}

    Generate the complete report with all placeholders filled in.""",
            }
        ],
        max_tokens=4096,
        temperature=0.3,  # Lower temperature for more consistent output
        top_p=1.0,
        model=model_name
    )

    # Get the generated report content
    generated_report = response.choices[0].message.content

    # Save the generated report to a markdown file
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(generated_report)
        print(f"\n✅ Report successfully saved to: {output_path}")
    except Exception as e:
        print(f"\n❌ Error saving report: {e}")
    
    # Print the generated report to console as well
    print("\n" + "="*50)
    print("GENERATED POLICE REPORT")
    print("="*50)
    print(generated_report)
    
    return generated_report
