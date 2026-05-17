# DataSaurus MCP Server

This project makes the DataSaurus sample data available to AI assistants and web pages. The data comes from `myDataSaurus.csv`, a small collection of x/y coordinate datasets that look very different when plotted even though their basic statistics can be similar.

The MCP server is a read-only bridge between an AI assistant and this dataset. Instead of asking someone to download files or write code, you can connect the server to a compatible assistant and ask plain-English questions such as "Which datasets are available?", "Show me the dino points," or "Summarize the x and y ranges." The assistant asks the MCP server for the data, and the server sends back structured results it can explain or analyze.

## Agentic Journalism with MCP

Read the project overview PDF:

[Open Agentic_Journalism_with_MCP.pdf](./Agentic_Journalism_with_MCP.pdf)

## Hosted Server

If you only want to try the MCP server, use this hosted address:

```text
https://yucky-violet-woodpecker.fastmcp.app/mcp
```

[Open Claude connection page](https://horizon.prefect.io/connect/eyJuYW1lIjoieXVja3ktdmlvbGV0LXdvb2RwZWNrZXIiLCJ0aXRsZSI6Inl1Y2t5LXZpb2xldC13b29kcGVja2VyIiwiZGVzY3JpcHRpb24iOiJFeHBvc2VzIERhdGFzYXVSdXMgZGF0YXNldHMgYW5kIHRoZWlyIGRldGFpbHMuIiwiaWNvbiI6Imljb246RGF0YWJhc2U6JTIzM2I4MmY2IiwicmVtb3RlcyI6W3sidXJsIjoiaHR0cHM6Ly95dWNreS12aW9sZXQtd29vZHBlY2tlci5mYXN0bWNwLmFwcC9tY3AiLCJ0eXBlIjoiaHR0cCJ9XX0/claude-web?orgSlug=prospero)

## Start Here

Choose how you want to use the MCP server.

### Use the hosted version

Best for a quick demo. The server is already deployed on FastMCP, so you only need to connect it to Claude.

### Run it locally

Best if you want to inspect or edit the code. You will clone the GitHub repo, install the requirements, and point your MCP client at the local server.

### Deploy your own hosted copy

Best if you want your own FastMCP URL. Connect FastMCP/Horizon to GitHub, select this repo, and deploy it from your account.

## Option 1: Connect the Hosted Server to Claude

1. Click the Claude connection page above.
2. Sign in to Claude if asked.
3. Review the connector named `yucky-violet-woodpecker`. This is the hosted DataSaurus MCP server.
4. Add the connector. If Claude asks for the server address, paste:

```text
https://yucky-violet-woodpecker.fastmcp.app/mcp
```

5. Open a new Claude chat. Click the `+` button, choose `Connectors`, and turn on the DataSaurus connector for that chat.
6. Try this prompt:

```text
List the available DataSaurus datasets and summarize each one.
```

## Option 2: Run the Server on Your Computer

Use this path when you want the MCP server running from your own machine. You only need Python and Git installed.

1. Clone the GitHub repo:

```bash
git clone https://github.com/hqu/MCP_demo_datasaurus.git
```

2. Open the project folder:

```bash
cd MCP_demo_datasaurus
```

3. Install the Python requirements:

```bash
pip install -r requirements.txt
```

4. Test that FastMCP can see the server:

```bash
fastmcp inspect server.py:mcp
```

5. Add the local server to your MCP client. Use this command if your client asks for a command to run:

```bash
python server.py
```

In Claude Desktop, add the server in developer settings or your MCP configuration file. Give it a clear name such as `DataSaurus`, set the command to `python`, and set the argument to the full path of `server.py` on your computer.

## Option 3: Deploy Your Own Hosted Copy with FastMCP

FastMCP runs hosted servers through Prefect Horizon. Horizon can connect to a GitHub repository, build the server, and give you a hosted MCP URL. You will need a GitHub account that can access this repository.

1. Sign in to [Prefect Horizon](https://horizon.prefect.io/) with your GitHub account.
2. Choose the option to create or deploy an MCP server from GitHub.
3. When GitHub asks for permission, authorize Horizon/FastMCP to access the repository. If you can choose specific repositories, select only this repo: `hqu/MCP_demo_datasaurus`.
4. Choose the repository:

```text
https://github.com/hqu/MCP_demo_datasaurus
```

5. Set the FastMCP entrypoint to:

```text
server.py:mcp
```

6. Deploy the server. When the deployment finishes, copy the hosted MCP URL. It should look similar to:

```text
https://your-server-name.fastmcp.app/mcp
```

7. Add that URL to your MCP client as a remote HTTP MCP server.

If your deployment needs GitHub sign-in for users, follow [FastMCP's GitHub OAuth guide](https://gofastmcp.com/v2/integrations/github). For this demo server, the important setup is simply giving Horizon access to the GitHub repo so it can deploy the code.

## Configure Your MCP Client

Choose the instructions for the client you use. Hosted clients use the FastMCP URL. Local coding clients can also run `server.py` directly from the cloned repo.

### Claude Web

Use this for Claude in a browser at `claude.ai`.

1. Open Claude, then go to `Customize` or `Settings` and choose `Connectors`.
2. Click `+` or `Add custom connector`.
3. Name it `DataSaurus` and paste the hosted MCP URL:

```text
https://yucky-violet-woodpecker.fastmcp.app/mcp
```

4. Start a new chat, click `+`, open `Connectors`, and turn on `DataSaurus` for the conversation.

### Claude Desktop

Use this if you prefer Claude's desktop app.

1. For the hosted server, use the same connector flow as Claude Web: `Settings` > `Connectors` > `Add connector`.
2. Add the hosted URL:

```text
https://yucky-violet-woodpecker.fastmcp.app/mcp
```

3. For a local copy, open Claude Desktop's developer settings or MCP configuration file. Add a server named `DataSaurus`.
4. Set the command to `python` and the argument to the full path of `server.py`. Example:

```powershell
python C:\path\to\MCP_demo_datasaurus\server.py
```

5. Restart Claude Desktop, open a new chat, and enable the DataSaurus server from the tools or connectors menu.

### Claude Code

Use this for Anthropic's command-line coding agent.

1. From the cloned repo, add the local server to Claude Code:

```bash
claude mcp add --transport stdio datasaurus -- python server.py
```

2. If you are using your hosted FastMCP server instead, add it as a remote MCP server:

```bash
claude mcp add --transport http datasaurus https://yucky-violet-woodpecker.fastmcp.app/mcp
```

3. In Claude Code, use a plain prompt that tells it which tool data you want:

```text
Use the DataSaurus MCP server to list the available datasets and summarize the dino dataset.
```

4. If the server exposes MCP prompts, type `/` to browse available slash commands. Claude Code shows MCP prompts in this format:

```text
/mcp__datasaurus__prompt_name
```

### ChatGPT

Use this for ChatGPT web with developer mode turned on. Developer mode is a beta feature and may require Plus, Pro, Business, Enterprise, or Edu access.

1. Open ChatGPT settings, then go to `Connectors` > `Advanced` and turn on `Developer mode`.
2. In `Connectors`, choose `Create` or `Add custom connector`.
3. Enter the connector name `DataSaurus`, paste the MCP endpoint, and choose the authentication option requested by your workspace.

```text
https://yucky-violet-woodpecker.fastmcp.app/mcp
```

4. Open a new chat, click the tools or `+` menu, and select the DataSaurus connector. It may appear with a `Dev` label while you are testing it.

If ChatGPT reports that the MCP server does not match its connector requirements, use Claude or Codex for this demo server, or update the MCP server to include ChatGPT-compatible `search` and `fetch` tools before publishing it to a workspace.

### Codex

Use this for OpenAI Codex in the CLI or IDE extension.

1. Add the hosted MCP server with the Codex CLI:

```bash
codex mcp add datasaurus --url https://yucky-violet-woodpecker.fastmcp.app/mcp
```

2. Verify that Codex saved it:

```bash
codex mcp list
```

3. You can also add it manually to `~/.codex/config.toml`:

```toml
[mcp_servers.datasaurus]
url = "https://yucky-violet-woodpecker.fastmcp.app/mcp"
```

4. Use a prompt that clearly asks Codex to consult the server:

```text
Use the DataSaurus MCP server to list the datasets, fetch the dino points, and summarize the x/y ranges.
```

## Good Test Prompts

- `List the available DataSaurus datasets.`
- `Show me the summary for the dino dataset.`
- `Get the x and y points for dino.`
- `Compare the x and y ranges for all datasets.`
- `Use the DataSaurus MCP server and explain what tools are available.`

## Use the JSON API

The same data is published as static JSON, so any browser, script, or notebook can read it without MCP setup. Use the dataset list first, then request a dataset by name.

### Endpoints

```text
GET ./api/datasets.json
```

Lists all datasets.

```text
GET ./api/datasets/dino.json
```

Gets one dataset.

Dataset names currently include `away`, `bullseye`, `dino`, and `star`. Each dataset response includes the dataset name, all `x`/`y` points, and a small summary.

### Browser Example

```js
const dataset = "dino";
const response = await fetch(`./api/datasets/${dataset}.json`);
const data = await response.json();

console.log(data.points);
```

### Python Example

```bash
python get_dino_dataset.py
```

## Build

Run this whenever `myDataSaurus.csv` changes:

```bash
node scripts/build-api.mjs
```

Then commit the generated `api/` files and enable GitHub Pages for the repository.

## MCP Server Tools

Available MCP tools:

- `list_datasets`: list dataset names and point counts
- `get_dataset_points`: get all `x` and `y` points for a dataset name
- `get_dataset_summary`: get count and x/y bounds for one dataset or all datasets

Local MCP development:

```bash
pip install -r requirements.txt
fastmcp inspect server.py:mcp
fastmcp run server.py:mcp
```
