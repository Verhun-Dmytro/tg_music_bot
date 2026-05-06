# Music Search Bot

A functional search bot for querying a small, localized music database. Restricted to personal and network use.

## Deployment

The application is configured for Docker containerization.

Build the image and execute image:
```bash and powershell
docker-compose up -d --build
```


## Database

Uses a minimalist database architecture designed to handle small volumes of queries.
The database stores user information and music history.

## Development Roadmap

*   **Refactoring:** Complete conversion of the existing synchronous codebase to fully asynchronous execution.
*   **Feature** Saving a music file ID from Telegram and using it.