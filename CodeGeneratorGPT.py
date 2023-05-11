import os
import re
import openai
from pathlib import Path
import dotenv
import spacy
import shutil

dotenv.load_dotenv()
nlp = spacy.load("en_core_web_sm")

def count_tokens(text):
    doc = nlp(text)
    return len(doc)

def generate_code(prompt, model_engine='text-davinci-003', max_tokens=1024, temperature=0.5, n=1, stop=None):
    """
    Generates code using the OpenAI API based on the given prompt.

    :param prompt: The input prompt for the code generation.
    :param model_engine: The OpenAI model engine to use for code generation (default: 'text-davinci-002').
    :param max_tokens: The maximum number of tokens to generate (default: 1024).
    :param temperature: The sampling temperature for the generated text (default: 0.5).
    :param n: The number of generated texts to return (default: 1).
    :param stop: The stop sequence for the generated text (default: None).
    :return: The generated code as a string.
    """
    
    # Check for API key
    if 'OPENAI_API_KEY' not in os.environ:
        raise ValueError("API key not set. Please set the 'OPENAI_API_KEY' environment variable.")
        
    # Initialize the OpenAI API client
    openai.api_key = os.environ['OPENAI_API_KEY']
    
    try:
        # Generate the code
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            n=n,
            stop=stop,
            frequency_penalty=0,
            presence_penalty=0
        )
        code = response.choices[0].text
        return code
    except Exception as e:
        raise RuntimeError(f"API call failed: {e}")
def split_python_file(file_path, max_tokens=1024):
    function_pattern = re.compile(r"^\s*?def\s.*?\w+\(.*?\):")
    with open(file_path, "r") as file:
        lines = file.readlines()

    chunks = []
    chunk = []
    tokens = 0
    for line in lines:
        if function_pattern.match(line) and tokens > max_tokens:
            chunks.append(chunk)
            chunk = []
            tokens = 0
        chunk.append(line)
        tokens += len(line)
    chunks.append(chunk)

    return chunks

def save_chunks(chunks, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    seq = "aa"
    for chunk in chunks:
        with open(f"{output_dir}/{seq}", "w") as chunk_file:
            chunk_file.writelines(chunk)
        seq = increment_seq(seq)

def increment_seq(s):
    s = list(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'z':
            s[i] = 'a'
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    else:
        s.insert(0, 'a')
    return ''.join(s)

nlp = spacy.load("en_core_web_sm")

def count_tokens(text):
    doc = nlp(text)
    return len(doc)

def generate_modified_chunks(input_file, modified_chunks_dir, max_tokens=1024):
    Path(modified_chunks_dir).mkdir(parents=True, exist_ok=True)
    modified_chunks = []
    
    with open(input_file, "r", encoding="ISO-8859-1") as f:
        content = f.read()
        
    lines = content.splitlines()
    num_lines = len(lines)
    chunk_size = max_tokens // 20  # Estimate average tokens per line
    num_chunks = (num_lines + chunk_size - 1) // chunk_size
    
    context_file = "context.txt"
    
    for i in range(num_chunks):
        start_line = i * chunk_size
        end_line = min((i + 1) * chunk_size, num_lines)
        chunk = "\n".join(lines[start_line:end_line]).lstrip("\n")  # Strip leading newlines
        
        # Generate a summary of the current chunk
        summary_prompt = f"Summarize the purpose of the following python code:\n{chunk}"
        summary = generate_code(summary_prompt).strip()
        
        # Append the summary to the context.txt file
        with open(context_file, "a") as f:
            f.write(f"Chunk {i} summary: {summary}\n\n")
            
        prompt = f"python code:\n{chunk}\n\nRefactor and improve the code above:"
        
        modified_chunk = generate_code(prompt)
        modified_chunks.append({"input_chunk": chunk, "modified_chunk": modified_chunk})
        
        modified_chunk_path = f"{modified_chunks_dir}/chunk_{i}_modified.py"
        with open(modified_chunk_path, "w") as modified_chunk_file:
            modified_chunk_file.write(modified_chunk)
            
        # Remove the leading newline from the modified chunk file
        remove_leading_newline(modified_chunk_path)
        
    return modified_chunks

def combine_chunks(modified_chunks, output_path):
    with open(output_path, "w") as output_file:
        for chunk_data in modified_chunks:
            output_file.write(chunk_data["modified_chunk"])

def remove_leading_newline(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        file.writelines(lines[1:] if lines and lines[0] == "\n" else lines)
        
def remove_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        
def clean_directory(directory):
    shutil.rmtree(directory)
        
if __name__ == "__main__":
    input_file = input("Please enter the path to the large Python file: ")
    
    output_dir = "chunks"
    modified_output_dir = "modified_chunks"
    output_file = "refactored_python_script.py"
    
    context_file = "context.txt"
    remove_file(context_file)  # Remove the context.txt file before each script execution
    
    chunks = split_python_file(input_file)
    save_chunks(chunks, output_dir)
    modified_chunks = generate_modified_chunks(input_file, modified_output_dir)
    combine_chunks(modified_chunks, output_file)
    remove_leading_newline(output_file)
    
    clean_directory(output_dir)
    clean_directory(modified_output_dir)