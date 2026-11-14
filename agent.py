from strands import Agent
from strands.models.ollama import OllamaModel

model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen3:4b",
)

agent = Agent(model=model, callback_handler=None)

print("Calling Qwen through local Ollama...", flush=True)
result = agent("今天天气如何")
print(result)