### A API Sharing Platform with direct integration of events on backend.

#### 1. What We Did
We set up a microservices architecture using FastAPI for two services: `api_events_service` and `api_marketplace`. The `api_events_service` receives POST requests to log events and provides GET requests to retrieve these events. The `api_marketplace` acts as a frontend that lists these events on its home page.

#### 2. Why We Did It
- **Microservices Architecture:** This architecture allows for modular and scalable development, where services like `api_events_service` handle specific functionalities (event logging), and `api_marketplace` serves as a consumer displaying these events.
  
- **FastAPI:** Chosen for its high-performance, asynchronous capabilities, and ease of use in building RESTful APIs, which are crucial for handling the concurrent nature of web applications and microservices.

- **Separation of Concerns:** By separating event logging (`api_events_service`) from event consumption (`api_marketplace`), we ensure clear responsibilities and easier maintenance.

#### 3. How We Did It

- **Implementation Details:**
  - **FastAPI Framework:** Used to build both services (`api_events_service` and `api_marketplace`), leveraging its intuitive API development features, data validation with Pydantic, and async capabilities with `uvicorn`.
  
  - **Endpoints:** Implemented `POST /api/events/` in `api_events_service` to receive events and `GET /api/events/` to retrieve events. `api_marketplace` fetches events from `api_events_service` using HTTP requests.
  
  - **Dockerization:** Dockerfiles were created for each service (`api_events_service` and `api_marketplace`) to containerize the applications, facilitating portability and deployment consistency.

#### Accessing Microservices and Testing

- **Accessing Microservices:**
  - After building Docker images with `docker-compose`, `api_events_service` is accessible at `http://localhost:5000/`, and `api_marketplace` at `http://localhost:8000/`.
  
- **Testing Microservices:**
  - **Postman:** Use Postman to send POST requests to `http://localhost:5000/api/events/` with JSON payloads to log events.
  - **Curl/HTTPie:** Alternatively, use curl or HTTPie for command-line testing.
  - **GET Requests:** Use GET requests to `http://localhost:8000/` to view and verify listed events on `api_marketplace`.
