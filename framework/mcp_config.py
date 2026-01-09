from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


class McpConfig:

    @staticmethod
    def get_mysql_workbench():
        mysql_server_params = StdioServerParams(
            command="/Library/Frameworks/Python.framework/Versions/3.14/bin/uv",
            args=[
                "--directory",
                "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages",
                "run",
                "mysql_mcp_server"
            ],
            env={
                "MYSQL_HOST": "localhost",
                "MYSQL_PORT": "3306",
                "MYSQL_USER": "root",
                "MYSQL_PASSWORD": "sput@6HU",
                "MYSQL_DATABASE": "rahulshettyacademy"
            }
        )
        return McpWorkbench(mysql_server_params)

    @staticmethod
    def get_rest_api_workbench():
        rest_api_server_params = StdioServerParams(
            args=[
                "-y",
                "dkmaker-mcp-rest-api"
              ],
            env={
                "REST_BASE_URL": "https://rahulshettyacademy.com/",
                "HEADER_Accept": "application/json"
              }
        )
        return McpWorkbench(rest_api_server_params)

    @staticmethod
    def get_excel_workbench():
        excel_server_params = StdioServerParams(
            args=["--yes", "@negokaz/excel-mcp-server"],
            env={"EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"},
            read_timeout_seconds=60
        )
        return McpWorkbench(excel_server_params)

    @staticmethod
    def get_file_system_workbench():
        file_system_server_params = StdioServerParams(
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "/Users/shashanksharma/Developer/claude_files"
              ],
            read_timeout_seconds=60
        )
        return McpWorkbench(file_system_server_params)