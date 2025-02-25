from openai import OpenAI

API_BASE_URL = "https://api.deepseek.com/v1"
API_KEY = "YOUR_API_KEY"

class LLMClient:
    def __init__(self, api_key=API_KEY, base_url=API_BASE_URL):
        """初始化LLM客戶端"""
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
    def chat(self, messages, temperature=0.5, stream=True):
        """與LLM互動"""
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=temperature,
                stream=stream
            )
            
            if stream:
                full_response = ""
                for chunk in response:
                    if chunk.choices[0].delta.content is not None:
                        content = chunk.choices[0].delta.content
                        print(content, end='', flush=True)
                        full_response += content
                print()
                return full_response
            else:
                return response.choices[0].message.content
                
        except Exception as e:
            print(f"LLM Error: {str(e)}")
            raise

# 使用範例
if __name__ == "__main__":
    llm = LLMClient()
    messages = [
        {"role": "user", "content": "你好"}
    ]
    response = llm.chat(messages)
    print(f"Response: {response}")