# OpenAI Chat Completion API Client

This project provides a Python class `LLM` to interact with the OpenAI API for generating chat completions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Installation

1. Clone the repository:

   ```sh
   git clone git@github.com:venkyvajrala/virgo.git
   cd virgo
   ```

2. Create a virtual environment and activate it:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Set the `OPENAI_API_KEY` environment variable with your OpenAI API key:

   ```sh
   export OPENAI_API_KEY="your_openai_api_key"
   ```

## Testing

1. Run the tests using `unittest`:

   ```sh
   python3 -m unittest
   ```
