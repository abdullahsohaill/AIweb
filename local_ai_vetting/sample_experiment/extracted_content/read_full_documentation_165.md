# Read Full Documentation
**URL:** https://danyqe.github.io/codebase-mcp
**Page Title:** Codebase MCP - Documentation
--------------------


## Codebase MCP

Turn any LLM into your personal coding assistant
Codebase MCP is an open-source, privacy-first AI development assistant that connects your LLM (like Claude) to your codebase through the Model Context Protocol (MCP). Build production-ready applications without expensive coding assistant subscriptions.

## Why Codebase MCP?

### The Problem

Modern AI coding assistants like Cursor and Windsurf are powerful but come with significant costs:
- 💸 Double subscriptions - Pay for Claude AND a separate coding assistant ($20-40/month)
- ☁️ Cloud-dependent - Your code is processed on remote servers
- 🔒 Vendor lock-in - Limited to specific LLM providers
- ⚙️ Limited control - Can't customize or extend functionality

### The Solution

Codebase MCP changes the game by turning YOUR existing LLM into a full-featured coding assistant:
- ✅ Use what you already pay for - Just need Claude subscription (or any MCP-compatible LLM)
- ✅ Privacy-first architecture - Processing happens locally with local embeddings
- ✅ Open source & extensible - Modify, enhance, and contribute
- ✅ LLM-agnostic design - Connect any LLM via Model Context Protocol
- ✅ Production-ready - Quality scoring, auto-formatting, dependency checking

### Perfect For

- 🎯 Solo developers who want AI assistance without breaking the bank
- 🏢 Small teams who need privacy-conscious development tools
- 🔐 Privacy-focused developers working on sensitive codebases
- 🛠️ Python & React developers building production applications
- 📚 Projects under 20,000 lines - optimal performance range

## Quick Start

### Prerequisites

- Python 3.11 or higher
- Claude Desktop (or any MCP-compatible LLM client)
- Git installed and configured
- Gemini API key (free tier) - Get one here
[LINK: Get one here](https://aistudio.google.com/app/apikey)

### 5-Minute Setup

Add to your claude_desktop_config.json :
Server runs on http://localhost:6789
Restart Claude Desktop to load the MCP server. You should now see Codebase MCP tools available!

## Installation

### System Requirements

### Installation Methods

Docker support is planned for a future release.

### Verify Installation

## Configuration

### Environment Variables

Create a .env file in the project root:

### Claude Desktop Configuration

Windows: %APPDATA%\Claude\claude_desktop_config.json
macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
Linux: ~/.config/Claude/claude_desktop_config.json
- Always use absolute paths
- Windows: Use double backslashes \\ or forward slashes /
- macOS/Linux: Use forward slashes /
- Point to the Python executable in your virtual environment

### Git Configuration

Codebase MCP uses two separate git directories:
- .git/ - Your personal git repository (user-managed)
- .codebase/ - AI-tracked changes (managed by Codebase MCP)

### Rate Limits (Gemini API)

The free Gemini API tier has the following limits:
- 15 requests per minute (RPM)
- 250,000 tokens per minute (TPM)
- 1,000 requests per day (RPD)
Codebase MCP automatically handles rate limiting with exponential backoff.

## Tools Overview

Codebase MCP provides 13+ specialized tools accessible via the Model Context Protocol. Each tool is designed for specific development tasks.

### Tool Categories

- session_tool - Manage isolated development sessions
- git_tool - Full git integration
- project_structure_tool - Understand project organization
- write_tool - Write new code with quality checks
- edit_tool - AI-assisted code editing
- read_code_tool - Read files and symbols
- search_tool - Multi-mode code search
- list_file_symbols_tool - List all symbols in files
- read_symbol_from_database - Find symbols across codebase
- memory_tool - Persistent knowledge storage
- code_analysis_tool - Syntax and lint analysis

### session_tool

Purpose: Manage isolated development sessions with automatic branching
- start - Create new session branch
- end - End session and return to main
- switch - Switch to existing session
- list - List all session branches
- merge - Merge session into main
- current - Show current session status
- delete - Delete a session branch
- Use descriptive session names: feature-X , fix-Y , refactor-Z
- Start a session before making changes to isolate work
- Use auto-merge only for well-tested changes
- Check current session status regularly

### memory_tool

Purpose: Store and retrieve project knowledge across chat sessions
- store - Store new memory
- search - Search memories semantically
- context - Get session startup context
- list - List memories by category
- update - Update existing memory
- stats - Get memory statistics
- progress - Project milestones
- learning - Technical insights
- preference - User preferences
- mistake - Errors and corrections
- solution - Working solutions
- architecture - Design decisions
- integration - Component interactions
- debug - Debugging experiences
- 5 (CRITICAL) - Must always remember
- 4 (HIGH) - Very important
- 3 (MEDIUM) - Standard importance
- 2 (LOW) - Nice to remember
- 1 (MINIMAL) - Archive level
- Store memories immediately after learning
- Use context at start of new sessions
- Search before starting similar work
- Always record mistakes with prevention strategies
- Update importance as patterns prove useful

### write_tool

Purpose: Write new code with automatic formatting, dependency checking, and quality analysis
- Automatic code formatting (Black/Ruff for Python, Prettier for JS/TS)
- Dependency conflict detection
- Quality scoring (0-1 scale)
- Auto-commit when quality ≥ 0.8
- Language auto-detection
- file_path - Path to write
- content - Code content
- purpose - What this code does
- language - python/javascript/typescript (auto-detected)
- save_to_file - Whether to save (default: True)
The quality score is calculated based on:
- ✅ Formatting success (0.3)
- ✅ No missing dependencies (0.3)
- ✅ No duplicate definitions (0.2)
- ✅ No syntax errors (0.2)
Score ≥ 0.8 enables auto-commit

### edit_tool

Purpose: AI-assisted code editing using Gemini API
- Gemini 2.5 Flash-Lite powered editing
- Intelligent diff generation
- Automatic error correction
- Rate limiting with exponential backoff
- Quality validation after edit
- target_file - File to edit
- instructions - What to change (single sentence)
- code_edit - Minimal edit specification
- language - Auto-detected if not provided
- save_to_file - Whether to save (default: True)
- Use // ... existing code ... to skip unchanged sections
- Provide clear, single-sentence instructions
- Include enough context around edits
- Don't specify entire file, only changed parts
If editing takes >30 seconds, you'll receive a timeout message. This prevents Claude Desktop from timing out. Options:
- Wait 30-60 seconds and check if edit completed
- Check for partial changes with git diff
- Break complex edits into smaller parts

### search_tool

Purpose: Multi-mode code search (semantic, fuzzy, text, symbol)
- Semantic search: <1 second for typical codebase
- Uses local AllMiniLM-L6-v2 embeddings
- FAISS vector indexing
- Memory footprint: ~100MB for medium projects

## API Reference

Codebase MCP FastAPI server provides 40+ REST endpoints for direct integration.

### Base URL

http://localhost:6789

### API Categories

- Session Management: /session/*
- Memory System: /memory/*
- Git Operations: /git/*
- File Operations: /file/* , /write , /edit
- Search: /search/*
- Project Analysis: /project/*
- Health & Monitoring: /health , /logs

### Authentication

Currently, the API runs locally without authentication. Future versions may add API key authentication for remote access.

### Example API Calls

### Key Endpoints

## Architecture

### System Overview

Codebase MCP uses a three-tier architecture designed for performance and separation of concerns:

### Component Breakdown

- Lightweight HTTP client
- Converts MCP tool calls to FastAPI requests
- Handles error formatting for LLM consumption
- Keeps Claude Desktop responsive
- ~3,000 lines of Python
- 40+ REST API endpoints
- Async request handling
- Modular router architecture
- Comprehensive error handling
- Real-time logging
- Write Pipeline: Format → Dependency Check → Quality Score
- Edit Pipeline: Gemini API → Error Correction → Format
- Git Manager: Dual directory (.git + .codebase)
- Formatter: Black, Ruff (Python) / Prettier (JS/TS)
- Dependency Checker: AST parsing, conflict detection
- Embeddings: Local AllMiniLM-L6-v2 model
- Vector Store: FAISS indexing
- Metadata: SQLite database
- Chunking: AST-aware code splitting
- Performance: <1s search for typical projects
- Storage: SQLite + FAISS vectors
- Categories: 8 knowledge types
- Persistence: Survives restarts
- Search: Semantic retrieval
- Importance: 1-5 priority levels

### Data Flow

### Storage Structure

- ✅ Clean separation of AI vs human changes
- ✅ Prevents accidental commits of AI experiments
- ✅ Easy rollback of AI-generated code
- ✅ You maintain full control of .git
- ✅ Transparent tracking of AI contributions

### Performance Characteristics

### Scalability

- Optimal: Projects under 20,000 lines
- Storage: ~100MB for medium project (embeddings + metadata)
- Memory: ~500MB RAM during operation
- Indexing: Linear scaling with codebase size

## Prompt Engineering

Codebase MCP includes an optimized system prompt for development workflows. The prompt is exposed as an MCP prompt accessible to Claude.

### System Prompt Philosophy

The system prompt configures Claude as an "Elite Solo Software Developer" with complete autonomy over standard development tasks. Key principles:
- 🎯 Autonomous Execution - Make decisions without asking for permission on standard tasks
- 📚 Context-Driven - Always gather context before acting (memory, git, codebase)
- 🏗️ Architecture-First - Plan before building, following SOLID principles
- ✅ Quality-Obsessed - Production-ready code on first attempt
- 🔄 Memory-Driven - Learn from mistakes, never repeat them

### Workflow Loop

The prompt enforces a 5-phase workflow:
- Load project memory ( memory_tool operation="context" )
- Check git status ( git_tool operation="status" )
- Search for related code ( search_tool )
- Review past mistakes to avoid repetition
- Design data flow: Request → Controller → Service → Repository
- Define DTOs for type-safe boundaries
- Consider scaling (10x, 100x traffic)
- Plan error handling and validation
- Start development session ( session_tool operation="start" )
- Write production-quality code with types
- Follow project patterns and conventions
- Use write_tool for new files
- Use edit_tool for modifications
- Add comprehensive error handling
- Quality score must be ≥ 0.8
- All dependencies resolved
- Type safety complete
- Error handling present
- Tests pass (if test suite exists)
- Commit work (auto-commit if quality ≥ 0.8)
- Store learnings in memory
- Record mistakes with prevention strategies
- Provide clear summary of changes

### Effective Prompts

### Domain-Specific Tips

- "Create a REST API endpoint for [feature]"
- "Add Pydantic validation to [model]"
- "Implement repository pattern for [entity]"
- "Add async database operations to [service]"
- "Build a React component for [feature] with TypeScript"
- "Add form validation using React Hook Form"
- "Create a custom hook for [functionality]"
- "Implement responsive design for [component]"
- "Refactor [file] to follow SOLID principles"
- "Extract reusable logic from [component]"
- "Improve type safety in [module]"
- "Add error boundaries to [components]"
- "Fix the [specific error] in [module]"
- "Debug why [feature] isn't working correctly"
- "Investigate performance issues in [component]"

### Accessing the System Prompt

The system prompt is available as an MCP prompt:

## Best Practices

### Session Management

- ✅ Start a session before making changes
- ✅ Use descriptive session names: feature-X , fix-Y
- ✅ Keep sessions focused on one logical unit of work
- ✅ Check session status regularly
- ❌ Don't leave sessions open indefinitely
- ❌ Don't mix unrelated changes in one session

### Memory System

- ✅ Load context at the start of new chat sessions
- ✅ Store learnings immediately after discovering them
- ✅ Always record mistakes with prevention strategies
- ✅ Search memories before starting similar work
- ✅ Update importance levels as patterns prove useful
- ❌ Don't store trivial information (importance 1-2)
- ❌ Don't forget to use operation="context" in new sessions

### Code Quality

- ✅ Let quality score guide whether to commit (≥ 0.8)
- ✅ Fix formatting/dependency issues before proceeding
- ✅ Add types everywhere (no any in TypeScript)
- ✅ Include error handling in all new code
- ✅ Write descriptive commit messages
- ❌ Don't ignore quality warnings
- ❌ Don't skip dependency checking

### Search & Discovery

- ✅ Use semantic search for conceptual queries
- ✅ Use fuzzy symbol search for approximate names
- ✅ Use text search for exact patterns/TODOs
- ✅ Limit results to relevant files with file_pattern
- ❌ Don't search without purpose
- ❌ Don't ignore search results before writing similar code

### AI-Assisted Editing

- ✅ Read file first to understand context
- ✅ Use clear, single-sentence instructions
- ✅ Mark unchanged code with // ... existing code ...
- ✅ Break complex edits into smaller parts
- ✅ Include context around edited sections
- ❌ Don't specify the entire file content
- ❌ Don't make multiple unrelated edits at once
- ❌ Don't omit existing code markers

### Project Organization

- ✅ Keep projects under 20,000 lines for optimal performance
- ✅ Use meaningful file and directory names
- ✅ Follow consistent code organization patterns
- ✅ Separate concerns (API, business logic, data)
- ❌ Don't mix Python and JavaScript in same directory
- ❌ Don't create deeply nested structures

### Performance Tips

- ✅ Reindex periodically if codebase changes significantly
- ✅ Use file_pattern to limit search scope
- ✅ Keep semantic search queries focused
- ✅ Monitor .data/ directory size
- ❌ Don't index generated/node_modules folders
- ❌ Don't run edit_tool on very large files

## Examples

### Example 1: Create New Feature

### Example 2: Debug Existing Code

### Example 3: Refactor Code

### Example 4: Add Feature to Existing File

### Example 5: Start New Project

### Example 6: Complex Multi-Step Task

## Troubleshooting

### Common Issues

Symptoms: Tools don't appear in Claude Desktop after restart
Solutions:
- Verify claude_desktop_config.json paths are absolute
- Check Python path points to virtual environment python.exe
- Ensure mcp_server.py path is correct
- Try restarting Claude Desktop completely (quit from system tray)
- Check Claude Desktop logs for errors
Symptoms: Error when running python main.py
Solutions:
- Ensure virtual environment is activated
- Verify all dependencies installed: pip install -r requirements.txt
- Check if port 6789 is already in use
- Try a different port: python main.py /path/to/project --port 8000
- Check Python version: python --version (need 3.11+)
Symptoms: Edit tool fails with API errors
Solutions:
- Verify GEMINI_API_KEY in .env file
- Check API key is valid at Google AI Studio
- Verify rate limits not exceeded (15 RPM, 250K TPM, 1K RPD)
- Wait if rate limited (tool has exponential backoff)
- For persistent issues, replace with local LLM
Symptoms: Edit operations take >30 seconds
Solutions:
- Wait 30-60 seconds and check if edit completed
- Check git diff to see partial changes
- Break large edits into smaller chunks
- Edit smaller files (<500 lines)
- Use write_tool instead for major rewrites
Symptoms: Search finds nothing despite code existing
Solutions:
- Check if .data/ directory exists and has files
- Reindex the codebase (restart FastAPI server)
- Verify file patterns in .gitignore don't exclude code
- Try different search query phrasing
- Use text search instead of semantic for exact matches
Symptoms: Write tool reports quality < 0.8
Solutions:
- Check formatting errors (Black/Ruff for Python)
- Ensure all imports are available
- Fix syntax errors
- Remove duplicate definitions
- Add missing dependencies to project
Symptoms: Can't switch or merge session branches
Solutions:
- Check uncommitted changes: git_tool operation="status"
- Commit or stash changes before switching
- Use session_tool operation="list" to see all sessions
- Delete problematic session: session_tool operation="delete"
- Manually resolve conflicts in .codebase/ directory
Symptoms: Memories disappear after restart
Solutions:
- Check if .data/metadata.db exists and has data
- Verify file permissions on .data/ directory
- Ensure no errors when storing memories
- Check SQLite database integrity

### Performance Issues

- Reduce max_results parameter
- Use file_pattern to limit scope
- Ensure project is under 20,000 lines
- Check system RAM availability
- Restart FastAPI server periodically
- Reduce embedding model size (if customized)
- Clear old memory entries
- Limit concurrent operations

### Getting Help

- 📖 Check GitHub Issues
[LINK: GitHub Issues](https://github.com/danyQe/codebase-mcp)
- 💬 Open a new issue with: Operating system and Python version Full error message Steps to reproduce Relevant logs from FastAPI server
- Operating system and Python version
- Full error message
- Steps to reproduce
- Relevant logs from FastAPI server
- 🐛 Include FastAPI server logs: http://localhost:6789/logs

## Contributing

Codebase MCP is open source and welcomes contributions! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

### Ways to Contribute

- Check existing issues first
[LINK: existing issues](https://github.com/danyQe/codebase-mcp/issues)
- Include Python version, OS, and full error messages
- Provide steps to reproduce
- Share relevant logs
- Open an issue with [Feature Request] tag
- Explain the use case and benefits
- Discuss implementation approach
- Fix typos and unclear explanations
- Add examples and tutorials
- Translate documentation
- Create video guides
- Fork the repository
- Create a feature branch
- Write clean, well-documented code
- Add tests if applicable
- Submit pull request

### Priority Areas

We're especially interested in contributions for:
- Add Java, Go, Rust chunkers
- Improve JavaScript/TypeScript parsing
- Add more formatter integrations
- Replace Gemini API with local models
- Add LLM provider options
- Optimize for CPU/GPU inference
- Better chunking algorithms
- Improved embedding models
- Faster indexing
- Multi-language support
- Web dashboard improvements
- Real-time progress indicators
- Better visualizations
- Mobile responsiveness
- Increase test coverage
- Add integration tests
- Performance benchmarks
- CI/CD improvements

### Development Setup

### Code Guidelines

- Follow existing code style (Black formatting)
- Add type hints to all functions
- Write docstrings for public APIs
- Keep functions focused and testable
- Add comments for complex logic
- Update documentation for new features

### Pull Request Process

- Create a descriptive branch name: feature/add-java-support
- Write clear commit messages
- Ensure all tests pass
- Update README/docs if needed
- Submit PR with detailed description
- Respond to review feedback

### Code of Conduct

We're committed to providing a welcoming and inclusive environment. Please be respectful and constructive in all interactions.
See CONTRIBUTING.md for full guidelines.
[LINK: CONTRIBUTING.md](https://github.com/danyQe/codebase-mcp/blob/main/CONTRIBUTING.md)

### Development Setup

Detailed development environment setup for contributors.
- Python 3.11+
- Git
- Virtual environment tool (venv or uv)

### Roadmap

Current Version: v1.0.0-beta
- 🔧 Docker support for easier deployment
- 📚 More language support (Java, Go, Rust)
- 🎨 Web dashboard improvements
- ⚡ Performance optimizations
- 📖 Video tutorials and guides
- 🤖 Local LLM integration (Ollama, LLaMA)
- 🔍 Improved semantic search algorithms
- 🧪 Comprehensive test suite
- 📊 Analytics and insights dashboard
- 🔌 Plugin system for extensibility
- ☁️ Optional cloud sync for memory
- 👥 Team collaboration features
- 🏢 Enterprise support
- 🌐 Multi-LLM orchestration
- 📱 Mobile app support
Want to contribute to the roadmap? Open an issue or join development !
[LINK: Open an issue](https://github.com/danyQe/codebase-mcp/issues)

--------------------