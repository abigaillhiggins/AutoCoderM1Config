import os
import typer
from git import Repo
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from typing import Optional

app = typer.Typer()
console = Console()

def get_diff(repo_path: str = ".", branch: str = "HEAD") -> str:
    """Get the git diff for the latest changes."""
    repo = Repo(repo_path)
    if not repo.is_dirty():
        return ""
    return repo.git.diff()

def analyze_code(client: OpenAI, diff: str) -> str:
    """Analyze code changes using OpenAI API."""
    if not diff:
        return "No changes detected to review."
    
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": "You are an expert code reviewer. Analyze the following git diff and provide:"
                          "\n1. A summary of changes"
                          "\n2. Potential issues or bugs"
                          "\n3. Suggestions for improvement"
                          "\n4. Best practices that could be applied"
                          "\nBe concise but thorough."
            },
            {
                "role": "user",
                "content": f"Here's the diff to review:\n\n{diff}"
            }
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content

@app.command()
def review(path: str = ".", branch: str = "HEAD"):
    """Review code changes in the current directory."""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        console.print("[red]Error: OPENAI_KEY environment variable not set[/red]")
        return

    client = OpenAI(api_key=api_key)
    
    with console.status("Analyzing code changes..."):
        diff = get_diff(path, branch)
        if not diff:
            console.print("[yellow]No changes detected in the working directory.[/yellow]")
            return
        
        analysis = analyze_code(client, diff)
        
    console.print(Panel(
        analysis,
        title="[bold blue]Code Review Analysis[/bold blue]",
        border_style="blue"
    ))

@app.command()
def suggest_commit_message(path: str = ".", branch: str = "HEAD"):
    """Generate a commit message for the current changes."""
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        console.print("[red]Error: OPENAI_KEY environment variable not set[/red]")
        return

    client = OpenAI(api_key=api_key)
    
    with console.status("Generating commit message..."):
        diff = get_diff(path, branch)
        if not diff:
            console.print("[yellow]No changes detected in the working directory.[/yellow]")
            return
        
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": "Generate a concise but descriptive git commit message for the following changes."
                              "\nFollow conventional commits format."
                              "\nFormat: <type>(<scope>): <description>"
                },
                {
                    "role": "user",
                    "content": f"Here's the diff:\n\n{diff}"
                }
            ],
            temperature=0.7
        )
        
        message = response.choices[0].message.content
        
    console.print(Panel(
        message,
        title="[bold green]Suggested Commit Message[/bold green]",
        border_style="green"
    ))

if __name__ == "__main__":
    app() 