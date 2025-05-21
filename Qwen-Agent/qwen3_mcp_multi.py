# qwen3_mcp_multi.py
from qwen_agent.agents.assistant import Assistant
from qwen_agent.utils.output_beautify import typewriter_print

def init_agent_service():

    # 使用 Ollama 运行的模型
     llm_cfg = {
         'model': 'Qwen3:8B',
         'model_server': 'http://localhost:11434/v1',
         'api_key': 'EMPTY',
     }

    system = ('你是一个数据分析师，具有对本地数据库的增删改查能力，同时具有使用python代码的能力')

    tools = [{
        "mcpServers": {
            "sqlite" : {
                "command": r"C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\uvx.exe",
                "args": [
                    "mcp-server-sqlite",
                    "--db-path",
                    "test.db"
                ]
            },
           
        },
        
        
    },
    # pip install "qwen-agent[code_interpreter]"
    'code_interpreter',
    ]

    bot = Assistant(
        llm=llm_cfg,
        name='数据分析师',
        description='可以对本地数据库进行增删改查，也',
        system_message=system,
        function_list=tools,
    )

    return bot

def run_query(query=None):
    # 定义数据库助手
    bot = init_agent_service()

    # 执行对话逻辑
    messages = []
    messages.append({'role': 'user', 'content': [{'text': query}]})

    # 跟踪前一次的输出，用于增量打印
    previous_text = ""
    
    print('数据库管理员: ', end='', flush=True)

    for response in bot.run(messages):
        previous_text = typewriter_print(response, previous_text)


# 命令行接口，便于直接运行
if __name__ == '__main__':

    query = '帮我随机生成20条学生的成绩数据, 插入到students表中,\
             然后绘制一个折线图展示所有成绩变化趋势'
    
    # 执行查询
    run_query(query)
        