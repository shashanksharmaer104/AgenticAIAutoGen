from autogen_agentchat.agents import AssistantAgent

from framework.mcp_config import McpConfig


class AgentFactory:

    def __init__(self, model_client):
        self.model_client = model_client
        self.McpConfig = McpConfig()

    def create_database_agent(self, system_message):
        database_agent = AssistantAgent(
            name="DatabaseAgent",
            model_client=self.model_client,
            workbench=self.McpConfig.get_mysql_workbench(),
            system_message=system_message
        )
        return database_agent

    def create_rest_api_agent(self, system_message):
        rest_api_agent = AssistantAgent(
            name="RestAPIAgent",
            model_client=self.model_client,
            workbench=[self.McpConfig.get_rest_api_workbench(), self.McpConfig.get_file_system_workbench()],
            system_message=system_message
        )
        return rest_api_agent

    def create_excel_agent(self, system_message):
        excel_agent = AssistantAgent(
            name="ExcelAgent",
            model_client=self.model_client,
            workbench=self.McpConfig.get_excel_workbench(),
            system_message=system_message
        )
        return excel_agent
