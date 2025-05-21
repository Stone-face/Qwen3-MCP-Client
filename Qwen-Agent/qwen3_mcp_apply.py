# qwen3_mcp_multi.py
from qwen_agent.agents.assistant import Assistant
from qwen_agent.utils.output_beautify import typewriter_print

def init_agent_service():
    llm_cfg = {
        'model': 'qwen3-235b-a22b',
        'model_server': 'https://dashscope.aliyuncs.com/compatible-mode/v1',
        'api_key': 'sk-4e17fd64',
    }

    tools = [{
       "mcpServers": {
           "time": {
               "command": r"C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\uvx.exe",
               "args": ['mcp-server-time', '--local-timezone=Asia/Shanghai']
           },
           "fetch": {
               "command": r"C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\uvx.exe",
               "args": ["mcp-server-fetch"]
           },
           "sqlite": {
               "command": r"C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\uvx.exe",
               "args": ["mcp-server-sqlite", "--db-path", "test.db"]
           },
            "firecrawl-mcp": {
                "command": r"C:\Program Files\nodejs\npx.cmd",
                "args": ["-y", "firecrawl-mcp"],
                "env": {
                    "FIRECRAWL_API_KEY": "fc-72ad993ba1"
                },
            },
            "amap-mcp-server": {
                "command": r"C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\uvx.exe",
                "args": ["amap-mcp-server"],
                "env": {
                    "AMAP_MAPS_API_KEY": "9b555daff4976"
                }
            }
       }
    },
    "code_interpreter"
    ]

    system = """
    你是一个规划师和数据分析师 \
        你可以调用高德地图规划旅行路线，同时可以提取网页信息进行数据分析
    """

    bot = Assistant(
        llm=llm_cfg,
        name='智能助理',
        description='具备查询高德地图、提取网页信息、数据分析的能力',
        system_message=system,
        function_list=tools,
    )

    return bot

def run_query(query=None):
    # 定义数据库助手
    bot = init_agent_service()

    from qwen_agent.gui import WebUI

    chatbot_config = {
        'prompt.suggestions': [
            '请你帮我写一个关于人工智能的论文',
            "https://github.com/orgs/QwenLM/repositories 提取这一页的Markdown 文档，然后绘制一个柱状图展示每个项目的收藏量",
            '帮我查询从故宫去颐和园的路线',
        ]
    }
    WebUI(
        bot,
        chatbot_config=chatbot_config,
    ).run()


if __name__ == '__main__':
    run_query()
