# AI_SlideDeck_Generator
A web application that automatically generates PowerPoint presentations on any topic. This tool uses a local Large Language Model (LLM) via Ollama to generate structured content and builds a downloadable .pptx slide deck.

## Tech Stack

-   **Backend**: Python, Flask
-   **LLM Integration**: Ollama Python Library
-   **Presentation Generation**: `python-pptx`
-   **Frontend**: HTML & CSS

ai-slide-deck-generator/
├── app.py                      # Main Flask application logic
├── generated_presentations/    # Stores the output .pptx files
├── static.css                  # CSS for the web interface
└── templates/
    └── index.html              # HTML for the web interface
