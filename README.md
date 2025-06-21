# Political Candidates API

A FastAPI backend for managing political candidates with in-memory storage.

## Features

- **CRUD Operations**: Create, Read, Update, Delete candidates
- **Search Functionality**: Search candidates by name, party, or description
- **Party Filtering**: Get candidates by political party
- **Pagination**: Support for paginated results
- **Statistics**: Get basic stats about candidates
- **CORS Support**: Configured for frontend integration

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server**:
   ```bash
   python run.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Access the API**:
   - API Base URL: `http://localhost:8000`
   - Interactive Documentation: `http://localhost:8000/docs`
   - Alternative Documentation: `http://localhost:8000/redoc`

## API Endpoints

### Candidates

- `GET /api/candidates` - Get all candidates (with pagination and search)
- `GET /api/candidates/{id}` - Get a specific candidate
- `POST /api/candidates` - Create a new candidate
- `PUT /api/candidates/{id}` - Update a candidate (full update)
- `PATCH /api/candidates/{id}` - Update a candidate (partial update)
- `DELETE /api/candidates/{id}` - Delete a candidate

### Additional Endpoints

- `GET /api/candidates/party/{party}` - Get candidates by political party
- `GET /api/candidates/search?query={query}` - Search candidates
- `GET /api/stats` - Get statistics about candidates
- `GET /health` - Health check endpoint

## Sample Data

The API comes pre-loaded with 6 sample candidates from different political parties:

1. Sarah Johnson - Progressive Democrats
2. Michael Chen - Conservative Alliance
3. Maria Rodriguez - Green Future Party
4. David Thompson - Independent Coalition
5. Lisa Park - Liberal Reform Party
6. Robert Williams - Traditional Values Party

## Data Model

```python
{
  "id": int,
  "name": str,
  "image": str,
  "political_party": str,
  "description": str,
  "created_at": datetime,
  "updated_at": datetime | null
}
```

## Frontend Integration

The API is configured with CORS to work with frontend applications running on:
- `http://localhost:3000` (React dev server)
- `http://localhost:5173` (Vite dev server)

## Notes

- This is an in-memory implementation - data will be reset when the server restarts
- No authentication is implemented - suitable for development and demo purposes
- The API is designed to work seamlessly with the React frontend in the `mpp-frontend` directory 