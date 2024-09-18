# Release v0.1

## Features

- **Interactive Shell**: Introduced an interactive command line shell using the `cmd` module, allowing users to manage subscriptions and fetch updates interactively.
- **Command Support**:
  - `add owner/repo`: Add a repository subscription.
  - `remove owner/repo`: Remove a repository subscription.
  - `fetch`: Fetch updates for all subscribed repositories.
  - `list`: List all subscribed repositories.
  - `exit`: Exit the shell.

## Improvements

- **Help Messages**: Enhanced command help messages and startup intro messages for better user guidance.
- **Background Scheduler**: Implemented background scheduling using APScheduler for non-blocking periodic update checks.

## Documentation

- **README**: Added detailed instructions for installation, usage, and contribution.
- **Release Notes**: Provided a comprehensive release note for v0.1 detailing all changes and features.

## Miscellaneous

- **Project Structure**: Organized project files and directories for better maintainability.
- **Requirements**: Added `requirements.txt` for easy dependency installation.

## Usage

- Run `python sentinel.py` to start the interactive shell.
- Use `help` or `?` to list available commands and their descriptions.

# Release v0.0.1

## What's New

- Initial release of GitHub Sentinel
- Basic project structure with core modules:
  - Subscription management
  - Update fetching
  - Notification system
  - Report generation

## Installation

- Clone the repository and navigate into the directory.
- Follow the instructions in the README to set up and run the project.
