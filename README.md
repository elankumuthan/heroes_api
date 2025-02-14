# HERO API LAB 1

## Overview 
This FastAPI helps to provide Hero Management API, aloowing users to create, read, update and delete heroes. It also supports file uploading and returning an image.


## Features 

### Operations on heroes


|Method | Endpoint | Description|
|--------|---------|------------|
|POST | hero/ | Create a new hero|
|GET | /heroes/ | Get all heroes|
|GET | /heroes/{hero_id} | Get hero by ID|
|PUT | /heroes/{hero_id}	| Update a hero|
|DELETE	| /heroes/{hero_id}	| Delete a hero|

### File Operations

|Method |	Endpoint |	Description|
|------|------------|--------------|
|POST |	/uploadfile/ |	Upload a file|

Uploaded files are stored in the uploads/ directory.

### Return Binary Content

|Method |	Endpoint |	Description|
|--------|------------|------------|
|GET |	/image |	Serve an image (app/spiderman.jpg)|


## Installation

1. Clone the repository

```
git clone <your-repo-url>
cd hero_api
```

2. Run the Docker Container

```
docker compose up
```

3. Send request

You can send a request from post.http which has some test cases.

## Test Cases

### Operations on hero

### 1. Create new hero

```
curl -X POST "http://localhost:8000/hero/" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Ant-man",
        "age": 35,
        "secret_power": "Shrink and Grow",
        "gender": "Male",
        "real_name": "Scott Lang"
    }'
```

### Expected response:

```
{
    "name": "Ant-man",
    "age": 35,
    "secret_power": "Shrink and Grow",
    "gender": "Male",
    "real_name": "Scott Lang"
}
```

### 2. Create new hero with missing name

```
curl -X POST "http://localhost:8000/hero/" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "",
        "age": 54,
        "secret_power": "Superhuman strength, durability, endurance, and healing",
        "gender": "Male",
        "real_name": "Bruce Banner",
        "id": 36
        }'
```

### Expected response:

```
{
    "detail": "Hero name is required"
}
```

### 3. Create new hero with missing id

```
curl -X POST "http://localhost:8000/hero/" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Batman",
        "age": 54,
        "secret_power": "Superhuman strength, durability, endurance, and healing",
        "gender": "Male",
        "real_name": "Bruce Banner"
        }'
```

### Expected response:

```
{
    "detail": "Hero ID is required"
}
```

### 4. Get all heroes

```
curl http://127.0.0.1:8000/heroes/ 
```

### Expected response 

```
[
  {
    "name": "Superman",
    "secret_power": "Flight",
    "age": 35,
    "id": 1,
    "real_name": "Clark Kent",
    "gender": "Male"
  },
  {
    "name": "The Bat-Man",
    "secret_power": "Genius, Ultra-rich, Master Martial Artist",
    "age": 24,
    "id": 2,
    "real_name": "Bruce Wayne",
    "gender": "Male"
  },
  {
    "name": "Wonder Woman",
    "secret_power": "Super Strength",
    "age": 5000,
    "id": 3,
    "real_name": "Diana Prince",
    "gender": "Female"
  },
  {
    "name": "Iron Man",
    "secret_power": "Advanced Armor",
    "age": 45,
    "id": 4,
    "real_name": "Tony Stark",
    "gender": "Male"
  },
  {
    "name": "Spider-Man",
    "secret_power": "Wall Climbing",
    "age": 18,
    "id": 5,
    "real_name": "Peter Parker",
    "gender": "Male"
  },
  {
    "name": "Ant-man",
    "secret_power": "Shrink and Grow",
    "age": 35,
    "id": 40,
    "real_name": "Scott Lang",
    "gender": "Male"
  }
]
```

### 5. Get hero by id

```
curl GET http://127.0.0.1:8000/heroes/2
```

### Expected response

```
{
    "name": "Batman",
    "secret_power": "Genius",
    "age": 40,
    "id": 2,
    "real_name": "Bruce Wayne",
    "gender": "Male"
}

```

### 6. Sort hero by age

```
curl GET http://127.0.0.1:8000/heroes/?sortBy=age
```

Expected response:

```
[
  {
    "name": "Spider-Man",
    "secret_power": "Wall Climbing",
    "age": 18,
    "id": 5,
    "real_name": "Peter Parker",
    "gender": "Male"
  },
  {
    "name": "The Bat-Man",
    "secret_power": "Genius, Ultra-rich, Master Martial Artist",
    "age": 24,
    "id": 2,
    "real_name": "Bruce Wayne",
    "gender": "Male"
  },
  {
    "name": "Superman",
    "secret_power": "Flight",
    "age": 35,
    "id": 1,
    "real_name": "Clark Kent",
    "gender": "Male"
  },
  {
    "name": "Ant-man",
    "secret_power": "Shrink and Grow",
    "age": 35,
    "id": 40,
    "real_name": "Scott Lang",
    "gender": "Male"
  },
  {
    "name": "Iron Man",
    "secret_power": "Advanced Armor",
    "age": 45,
    "id": 4,
    "real_name": "Tony Stark",
    "gender": "Male"
  },
  {
    "name": "Wonder Woman",
    "secret_power": "Super Strength",
    "age": 5000,
    "id": 3,
    "real_name": "Diana Prince",
    "gender": "Female"
  }
]
```

### 7. Sort hero by age and limit to 3

```
curl GET http://127.0.0.1:8000/heroes/?sortBy=age&count=3
```

### Expected response:

```
[
  {
    "name": "Spider-Man",
    "secret_power": "Wall Climbing",
    "age": 18,
    "id": 5,
    "real_name": "Peter Parker",
    "gender": "Male"
  },
  {
    "name": "The Bat-Man",
    "secret_power": "Genius, Ultra-rich, Master Martial Artist",
    "age": 24,
    "id": 2,
    "real_name": "Bruce Wayne",
    "gender": "Male"
  },
  {
    "name": "Superman",
    "secret_power": "Flight",
    "age": 35,
    "id": 1,
    "real_name": "Clark Kent",
    "gender": "Male"
  }
]
```

### 8. Update a hero detail 

```
curl -X PUT "http://127.0.0.1:8000/heroes/2" \
     -H "Content-Type: application/json" \
     -d '{
          "name": "The Bat-Man",
          "age": 24,
          "secret_power": "Genius, Ultra-rich, Master Martial Artist"
     }'
```
### Expected response 

```
{
  "name": "The Bat-Man",
  "secret_power": "Genius, Ultra-rich, Master Martial Artist",
  "age": 24,
  "id": 2,
  "real_name": "Bruce Wayne",
  "gender": "Male"
}
```

### 9. Delete a hero 

```
curl -X DELETE "http://127.0.0.1:8000/heroes/3"
```

### Expected response 

```
{
"ok": true
}

```

### File Operations

### 1. Upload a file 

```
POST http://localhost:8000/uploadfile/
Content-Type: multipart/form-data; boundary=----CustomBoundary123

------CustomBoundary123
Content-Disposition: form-data; name="file"; filename="spiderman.jpg"
Content-Type: image/jpeg

< ../app/spiderman.jpg
------CustomBoundary123--
```

## Expected response

```
{
    "filename": "spiderman.jpg",
    "size": 44148,
    "file_type": "image/jpeg",
    "path": "uploads/spiderman.jpg"
}
```

### Return binary content 

### 1. Return an image

```
curl GET http://127.0.0.1:8000/image
```
### Expected response:
![spiderman](https://github.com/user-attachments/assets/d19b97b6-91db-4ba3-858b-3506c133325b)


