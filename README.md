# ✨ CodeGeneratorGPT ✨

This script, called CodeGeneratorGPT, refactors and improves Python code using OpenAI's GPT-3 model. It takes a large Python file as input, splits it into smaller chunks or code blocks, generates refactored 
code using the GPT-3 model, and combines the refactored chunks into a single output file.

## 🖥 ️ Features

- Splits a large Python file into smaller chunks
- Generates refactored code using OpenAI's GPT-3 model
- Combines refactored chunks into a single output file

## 💿 Installation

1. Clone the repository:

```
git clone https://github.com/sambegui/CodeGeneratorGPT.git
```

2. Change to the project directory:

```
cd CodeGeneratorGPT
```

3. Install required dependencies:

```
pip install -r requirements.txt
```

4. Set up the OpenAI API Key:

```
export OPENAI_API_KEY="your_openai_api_key_here"
```

## 🧑‍💻 Usage

1. Run the script:

```
python CodeGeneratorGPT.py
```
or
```
python3 CodeGeneratorGPT.py
```

2. Provide the path to the large Python file when prompted:

```
Please enter the path to the large Python file: /path/to/your/python/file.py
```

3. The script will generate a refactored output file named `refactored_python_script.py` and a `context.txt` file with summaries for each chunk.

## ⚠ ️ Work in Progress

Here's a list of new functions and their definitions based on the suggested improvements:

1. `def process_input_file_line_by_line(file_path):`
   Processes the input file line by line to improve memory usage.

2. `def generate_code_with_context(prompt, context):`
   Generates code using the OpenAI API based on the given prompt and context, which may include previous chunks or context.txt file.

3. `def split_code_blocks(file_path):`
   Splits the input file into code blocks, taking into account code dependencies, context, and appropriate separation of functions and classes.

4. `def handle_exceptions_during_code_generation():`
   Handles exceptions during code generation, including OpenAI API errors and incorrect input files.

5. `def update_generate_code_function_for_GPT4():`
   Updates the `generate_code` function to use the GPT-4 model engine when it becomes available.

6. `def parallel_code_generation():`
   Implements multithreading for parallel code generation to improve the speed of the script.

7. `def interactive_command_line_menu():`
   Provides an interactive command-line menu for a more user-friendly experience.

8. `def format_generated_code(code):`
   Formats the generated code using code formatting tools like Black, Flake8, or YAPF.

9. `def run_unit_tests():`
   Runs unit tests to ensure the refactored code maintains its functionality and to catch potential bugs.

10. `def setup_version_control():`
    Sets up version control for the script to track changes and enable collaboration on the script's development.

These functions are being implemented in the script to enhance its functionality, reliability, and usability based on the suggested improvements.

## Demo
![CodeGeneratorGPT-Demo](CodeGeneratorGPT-Demo.gif)

## Contributing

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Make changes or add new features based on the list of proposed improvements.
4. Write unit tests for your changes.
5. Submit a pull request to the `main` branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT-3 model and API.
- [Spacy](https://spacy.io/) for token counting in text.
