# qwen3_mcp_sqlite.py
from qwen_agent.agents.assistant import Assistant
from qwen_agent.utils.output_beautify import typewriter_print

def init_agent_service():
    # llm_cfg = {
    #    'model': 'qwen3-235b-a22b',
    #    'model_server': 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    #    'api_key': 'sk-4e17cb482d64',
    # }

    # 使用 deepseek-chat 模型
    # llm_cfg = {
    #     'model': 'deepseek-chat',
    #     'model_server': 'https://api.deepseek.com',
    #     'api_key': 'sk-6d68ae12b',
    #     }
    
    # 使用 Ollama 运行的模型
    llm_cfg = {
         'model': 'Qwen3:8B',
         'model_server': 'http://localhost:11434/v1',
         'api_key': 'EMPTY',
     }

    system = ('你扮演一个数据库助手，你具有查询数据库的能力')

    tools = [{
        "mcpServers": {
            "sqlite" : {
                "command": "uvx",
                "args": [
                    "mcp-server-sqlite",
                    "--db-path",
                    "test.db"
                ]
            }
        }
    }]
    
    bot = Assistant(
        llm=llm_cfg,
        name='数据库管理员',
        description='你是一位数据库管理员，具有对本地数据库的增删改查能力',
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

    query = '帮我创建一个学生表,表名是students,包含id, name, age, gender, score字段,然后插入一条数据,id为1,name为张三,age为20,gender为男,score为95'
    
    # 执行查询
    run_query(query)
        