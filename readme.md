

# NASA API Backend

## How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/nasa-api-backend.git
   cd nasa-api-backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser or Postman to test the API.

---

## Available Endpoints

### 1. **GET /apod**
Fetch Astronomy Picture of the Day (APOD).

**Request example**:
   ```bash
   GET /apod?date=2024-11-22
   ```

**Response example**:
   ```json
   {
     "date": "2024-11-22",
     "explanation": "Astronomy Picture of the Day explanation",
     "url": "https://example.com/picture.jpg"
   }
   ```

---

### 2. **GET /mars-photos**
Fetch photos from Mars rover.

**Request example**:
   ```bash
   GET /mars-photos?sol=1000&rover=curiosity
   ```

**Response example**:
   ```json
   [
     {
       "id": 1,
       "img_src": "https://example.com/photo1.jpg",
       "sol": 1000,
       "rover": "Curiosity"
     }
   ]
   ```

---

### 3. **GET /neo-asteroids**
Fetch Near-Earth Objects (NEOs).

**Request example**:
   ```bash
   GET /neo-asteroids?start_date=2024-11-20&end_date=2024-11-22
   ```

**Response example**:
   ```json
   {
     "near_earth_objects": [
       {
         "name": "Asteroid 12345",
         "date": "2024-11-20",
         "diameter": "1.2 km"
       }
     ]
   }
   ```

---

## API PostMan Documentation  
Access the Postman collection [here](https://web.postman.co/workspace/My-Workspace~c8faef5a-a18c-457d-8e0d-8ce8ffe823f2/overview)