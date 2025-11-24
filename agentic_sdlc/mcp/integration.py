"""MCP function call integration."""

import json
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class MCPFunction:
    """Represents an MCP function callable by agents."""
    
    name: str
    description: str
    mcp_server: str
    parameters: Dict[str, Any]


class MCPIntegration:
    """Integrates MCP endpoints as agent-accessible function calls."""
    
    # Mapping of MCP servers to their available functions
    MCP_FUNCTIONS = {
        "github": [
            {
                "name": "github_search_code",
                "description": "Search code across GitHub repositories",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query"},
                        "language": {"type": "string", "description": "Programming language filter"},
                    },
                    "required": ["query"],
                },
            },
            {
                "name": "github_create_pr",
                "description": "Create a pull request on GitHub",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "PR title"},
                        "body": {"type": "string", "description": "PR description"},
                        "base": {"type": "string", "description": "Base branch"},
                        "head": {"type": "string", "description": "Head branch"},
                    },
                    "required": ["title", "body", "base", "head"],
                },
            },
            {
                "name": "github_create_issue",
                "description": "Create an issue on GitHub",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Issue title"},
                        "body": {"type": "string", "description": "Issue description"},
                        "labels": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["title", "body"],
                },
            },
        ],
        "task-master-ai": [
            {
                "name": "task_master_add_task",
                "description": "Add a new task to Task Master",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Task title"},
                        "tag": {"type": "string", "description": "Task tag"},
                        "status": {"type": "string", "enum": ["deferred", "todo", "in-progress", "done"]},
                        "description": {"type": "string", "description": "Task description"},
                        "priority": {"type": "string", "enum": ["high", "medium", "low"]},
                    },
                    "required": ["title", "tag"],
                },
            },
            {
                "name": "task_master_get_tasks",
                "description": "Retrieve tasks from Task Master",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tag": {"type": "string", "description": "Filter by tag"},
                        "status": {"type": "string", "description": "Filter by status"},
                        "withSubtasks": {"type": "boolean", "description": "Include subtasks"},
                    },
                },
            },
            {
                "name": "task_master_update_task",
                "description": "Update an existing task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Task ID"},
                        "tag": {"type": "string", "description": "Task tag"},
                        "prompt": {"type": "string", "description": "Update instructions"},
                        "status": {"type": "string", "enum": ["deferred", "todo", "in-progress", "done"]},
                    },
                    "required": ["id", "tag", "prompt"],
                },
            },
            {
                "name": "task_master_research",
                "description": "Conduct deep research and save to file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Research query"},
                        "projectRoot": {"type": "string", "description": "Project root directory"},
                        "tag": {"type": "string", "description": "Task tag"},
                        "filePaths": {"type": "string", "description": "Comma-separated file paths"},
                        "saveToFile": {"type": "boolean", "description": "Save results to file"},
                        "detailLevel": {"type": "string", "enum": ["low", "medium", "high"]},
                    },
                    "required": ["query", "projectRoot"],
                },
            },
        ],
        "perplexity": [
            {
                "name": "perplexity_search",
                "description": "Search the web using Perplexity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Search query"},
                    },
                    "required": ["query"],
                },
            },
            {
                "name": "perplexity_reason",
                "description": "Deep reasoning with Perplexity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Reasoning query"},
                        "context": {"type": "string", "description": "Additional context"},
                    },
                    "required": ["query"],
                },
            },
        ],
        "context7": [
            {
                "name": "context7_search_docs",
                "description": "Search library documentation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "library": {"type": "string", "description": "Library name"},
                        "query": {"type": "string", "description": "Search query"},
                    },
                    "required": ["library", "query"],
                },
            },
        ],
        "deepwiki": [
            {
                "name": "deepwiki_analyze_repo",
                "description": "Analyze repository patterns and insights",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_url": {"type": "string", "description": "Repository URL"},
                        "query": {"type": "string", "description": "Analysis query"},
                    },
                    "required": ["repo_url"],
                },
            },
        ],
        "knowledgegraph": [
            {
                "name": "knowledge_graph_store",
                "description": "Store knowledge in the knowledge graph",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity": {"type": "string", "description": "Entity name"},
                        "type": {"type": "string", "description": "Entity type"},
                        "properties": {"type": "object", "description": "Entity properties"},
                    },
                    "required": ["entity", "type"],
                },
            },
            {
                "name": "knowledge_graph_query",
                "description": "Query the knowledge graph",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "Query string"},
                    },
                    "required": ["query"],
                },
            },
        ],
        "sequential-thinking": [
            {
                "name": "sequential_think",
                "description": "Structured reasoning process",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "problem": {"type": "string", "description": "Problem statement"},
                        "steps": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["problem"],
                },
            },
        ],
    }
    
    def __init__(self, mcp_config: Dict[str, Any]):
        """Initialize MCP integration with configuration."""
        self.config = mcp_config
        self.enabled_servers = set(mcp_config.get("mcpServers", {}).keys())
        
    def get_available_functions(self) -> List[Dict[str, Any]]:
        """Get all available MCP functions based on enabled servers."""
        functions = []
        
        for server_name, server_functions in self.MCP_FUNCTIONS.items():
            if server_name in self.enabled_servers:
                for func in server_functions:
                    # Convert to OpenAI function format
                    functions.append({
                        "type": "function",
                        "function": {
                            "name": func["name"],
                            "description": func["description"],
                            "parameters": func["parameters"],
                        }
                    })
        
        return functions
    
    def get_functions_for_agent(self, agent_id: str, phase: str) -> List[Dict[str, Any]]:
        """Get MCP functions relevant to a specific agent/phase."""
        all_functions = self.get_available_functions()
        
        # Phase-specific function filtering
        phase_filters = {
            "planning": ["task_master", "perplexity", "context7", "deepwiki", "sequential"],
            "roles": ["task_master", "context7", "deepwiki"],
            "process": ["task_master", "sequential"],
            "development": ["task_master", "github", "context7"],
            "finalization": ["task_master", "github", "knowledge_graph"],
        }
        
        # Get relevant prefixes for this phase
        relevant_prefixes = phase_filters.get(phase, [])
        
        if not relevant_prefixes:
            return all_functions
        
        # Filter functions by phase
        filtered = []
        for func in all_functions:
            func_name = func["function"]["name"]
            if any(func_name.startswith(prefix) for prefix in relevant_prefixes):
                filtered.append(func)
        
        return filtered
    
    def format_function_call_result(self, function_name: str, result: Any) -> str:
        """Format MCP function call result for agent consumption."""
        return json.dumps({
            "function": function_name,
            "result": result,
        }, indent=2)
