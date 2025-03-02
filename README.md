# DeepSeek Master  

A multi-step reasoning workflow for philosophical Q&A based on DeepSeek.  
Now support Traditional Chinese.

![DeekSeep](https://github.com/user-attachments/assets/ef3cf3ac-d8b2-4180-bbea-4867ab80dc89)

## Usage  

Set up the required dependencies:  

```  
python3 -m pip install openai  
```  

Configure the [DeepSeek official API key](https://platform.deepseek.com/api_keys) by setting the `API_KEY` variable in `llm_client.py`.  

In the main program `main.py`, populate the `topics` variable with one or more questions in list format, then run the following command:  

```  
python3 main.py  
```  

## Output Location  

The final results and intermediate reasoning steps will be stored in the `output` folder. The final output for each question will be saved in the `stage3/self_expression.txt` file within a folder named after the question.


## Tests  

```  
python3 -m pip install pytest pytest-mock openai
python3 -m pytest
```  
