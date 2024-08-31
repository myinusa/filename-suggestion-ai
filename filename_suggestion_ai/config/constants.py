# Constants
URL = "http://100.116.203.51:1234/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
}
MODEL = "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"
SYSTEM_CONTENT = "From the content of the file, generate a filename. Use snake case, max 25 characters, no file extension or special characters. Only key elements, one word if possible in noun-verb format. Avoid using names that are too general or too wordy. Respond ONLY with filename."
USER_CONTENT = "What is the meaning of life?"
