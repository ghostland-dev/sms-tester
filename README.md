# SMS Tester (Fake SMS REST API & UI)

**Developed by Ismail MOUYAHADA**

---

## What is this project?

This project provides a complete fake SMS REST API and a modern web UI to simulate sending and receiving SMS messages. It is designed for developers who need to test SMS flows in their applications without using a real SMS provider or incurring costs.

---

## Why was it created?

- To allow developers to test SMS notifications, 2FA, and alert flows locally or in CI without sending real messages.
- To provide a simple, persistent, and visual way to inspect all SMS sent by an application during development or automated tests.
- To make it easy to integrate with any backend (Symfony, Laravel, Node, etc.) via a standard HTTP API.

---

## Features

- **REST API (FastAPI, Python):**
  - `POST /sms/send` — Send a fake SMS (fields: `to`, `from`, `message`)
  - `GET /sms/inbox` — List all received SMS
  - `GET /sms/inbox/{phone}` — List SMS sent to a specific number
  - `POST /sms/reset` — Clear the inbox (for test resets)
  - All messages are stored in a JSON file for persistence
- **Modern Web UI (React + Tailwind):**
  - View all SMS in a responsive table
  - Filter by phone number, message content, or date
  - Send SMS from the UI (for manual testing)
  - Copy message content in one click
  - Clear inbox, reset filters, and see API status
  - Auto-refresh every 5 seconds
  - Success/error alerts, loading indicators, and more
- **Dockerized:**
  - One-command startup for both API and UI
  - No need to install Python, Node, or dependencies locally

---

## How does it work?

- The API exposes endpoints to send and list SMS. All data is stored in `sms_storage.json` (mounted as a volume in Docker).
- The React UI queries the API and displays all messages, with advanced filters and actions for developer convenience.
- Both services are orchestrated with Docker Compose for easy startup and isolation.

---

## Important URLs

- **API Docs (Swagger):** [http://localhost:8888/docs](http://localhost:8888/docs)
- **API Endpoints:**
  - `POST http://localhost:8888/sms/send`
  - `GET  http://localhost:8888/sms/inbox`
  - `GET  http://localhost:8888/sms/inbox/{phone}`
  - `POST http://localhost:8888/sms/reset`
- **Web UI:** [http://localhost:3333](http://localhost:3333)

---

## How to start (with Docker)

1. **Clone the repository**
2. **Build and run everything:**
   ```bash
   docker-compose up --build
   ```
3. **Access the UI:**
   - [http://localhost:3333](http://localhost:3333)
4. **Access the API docs:**
   - [http://localhost:8888/docs](http://localhost:8888/docs)

---

## Example: Send a fake SMS (with curl)

```bash
curl -X POST http://localhost:8888/sms/send \
  -H 'Content-Type: application/json' \
  -d '{"to": "+33600000000", "from": "APP", "message": "Your code is 123456"}'
```

---

## Author

Developed by **Ismail MOUYAHADA** 