# PDF to MP3 Converter using Google Text-to-Speech

This script extracts text from a specific page of a PDF and converts it into an MP3 audio file using Google Cloud Text-to-Speech.

## Requirements

- Python 3.x
- `google-cloud-texttospeech` library
- `PyPDF2` library
- A Google Cloud project with Text-to-Speech API enabled
- A service account key in JSON format (`gcp-key.json`)

## Installation

Install the required Python packages:

```bash
pip install google-cloud-texttospeech PyPDF2
```

## Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Text-to-Speech API** for your project.
3. Create a **service account key** and download the `.json` credentials file.
4. Save the file as `gcp-key.json` in the same directory as the script (or update the path in the script).

## Usage

1. Replace `'YOUR_PDF_HERE.pdf'` in the script with the name of your actual PDF file.
2. Update the page number (`pdf_reader.pages[200]`) to the desired page index (starting from `0`).
3. Run the script:

```bash
python main.py
```

The script will generate an `output.mp3` file with the spoken text extracted from the specified page of the PDF.

## Output

The final audio file will be saved as:

```bash
output.mp3
```

## Notes

- Make sure the PDF page has extractable text (not just an image).
- Page indices in PyPDF2 are zero-based (i.e., the first page is `0`).

Let me know if you want this saved as a file or adjusted for a GUI version or batch processing.
