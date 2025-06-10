#AutoCodeRover is not my project.

@inproceedings{zhang2024autocoderover,
    author = {Zhang, Yuntong and Ruan, Haifeng and Fan, Zhiyu and Roychoudhury, Abhik},
    title = {AutoCodeRover: Autonomous Program Improvement},
    year = {2024},
    isbn = {9798400706127},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3650212.3680384},
    doi = {10.1145/3650212.3680384},
    booktitle = {Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis},
    pages = {1592–1604},
    numpages = {13},
    keywords = {automatic program repair, autonomous software engineering, autonomous software improvement, large language model},
    location = {Vienna, Austria},
    series = {ISSTA 2024}
}


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
