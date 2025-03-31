import PyPDF2
from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient.from_service_account_file("gcp-key.json") # need to create a google key and put the json path here
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Open the PDF file
pdf_file = open('YOUR_PDF_HERE.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from the page number
page = pdf_reader.pages[200]
pdf_text = page.extract_text()
input_text = texttospeech.SynthesisInput(text=pdf_text) # SynthesisInput for google Text to Speech
response = client.synthesize_speech(
    input=input_text,
    voice=voice,
    audio_config=audio_config
)
with open("output.mp3", "wb") as out:
    out.write(response.audio_content) # create the file
    print("Audio has been generated at output.mp3")

pdf_file.close()