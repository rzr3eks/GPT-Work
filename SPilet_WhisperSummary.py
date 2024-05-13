import whisper
import openai

def transcribe_audio(audio_path):
    # Load the model
    model = whisper.load_model("base")

    # Load and transcribe the audio file
    result = model.transcribe(audio_path)
    return result['text']

def summarize_text(text):
    # OpenAI API key and setup
    openai.api_key = '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'

    # Use GPT-4 to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following conversation:\n\n{text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    audio_file_path = 'whisp.wav'
    transcription = transcribe_audio(audio_file_path)
    summary = summarize_text(transcription)
    
    print("Transcription:", transcription)
    print("Summary:", summary)

if __name__ == "__main__":
    main()
