from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


class McpConfig:

    def __init__(self):


    def get_mysql_workbench(self):
        mysql_server_params = StdioServerParams(
            command="/Library/Frameworks/Python.framework/Versions/3.14/bin/uv",
            args=[
                "--directory",
                "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages",
                "run",
                "mysql_mcp_server"
            ],
            env= {
                "MYSQL_HOST": "localhost",
                "MYSQL_PORT": "3306",
                "MYSQL_USER": "root",
                "MYSQL_PASSWORD": "sput@6HU",
                "MYSQL_DATABASE": "rahulshettyacademy"
            }
        )
        return McpWorkbench(mysql_server_params)
