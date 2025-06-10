# AutoCodeRover - AI Code Review Agent

An intelligent code review assistant powered by OpenAI's GPT-4. This tool helps developers by providing automated code reviews and generating meaningful commit messages.

## Features

- **Automated Code Review**: Analyzes your git changes and provides:
  - Summary of changes
  - Potential issues and bugs
  - Suggestions for improvement
  - Best practices recommendations
- **Smart Commit Messages**: Generates conventional commit messages based on your changes
- **Beautiful CLI**: Rich terminal output with color-coded messages and progress indicators

## Prerequisites

- Python 3.9+
- Docker (optional)
- OpenAI API Key

## Installation

### Using Docker

1. Build the container:
```bash
docker build -f Dockerfile.minimal -t acr .
```

2. Run the container:
```bash
docker run -it -e OPENAI_KEY="your-api-key" acr
```

### Local Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:
```bash
export OPENAI_KEY="your-api-key"
```

## Usage

### Review Code Changes

```bash
python main.py review
```

### Generate Commit Message

```bash
python main.py suggest-commit-message
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT 