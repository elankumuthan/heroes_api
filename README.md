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
|DELETE | /heroes/delete_all | Delete all heroes|


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

### Post request

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

### 4. RESET back default heroes

```
curl -X POST "http://localhost:8000/heroes/reset_all" \
     -H "Authorization: Bearer supersecureadminkey"
```

### Expected response 

```
{
  "message": "Default heroes added successfully",
  "added_heroes": [
    1,
    2,
    3,
    4,
    5
  ]
}
```


### Get request 

### 1. Get all heroes

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

### 2. Get hero by id

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

### 3. Sort hero by age

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

### 4. Sort hero by age and limit to 3

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
### 5. Sort hero by id

```
curl GET http://127.0.0.1:8000/heroes/?sortBy=id
```

Expected response:

```
[
  {
    "name": "Superman",
    "secret_power": "Flight",
    "id": 1,
    "age": 35,
    "real_name": "Clark Kent",
    "gender": "Male"
  },
  {
    "name": "Batman",
    "secret_power": "Genius",
    "id": 2,
    "age": 40,
    "real_name": "Bruce Wayne",
    "gender": "Male"
  },
  {
    "name": "Wonder Woman",
    "secret_power": "Super Strength",
    "id": 3,
    "age": 5000,
    "real_name": "Diana Prince",
    "gender": "Female"
  },
  {
    "name": "Iron Man",
    "secret_power": "Advanced Armor",
    "id": 4,
    "age": 45,
    "real_name": "Tony Stark",
    "gender": "Male"
  },
  {
    "name": "Spider-Man",
    "secret_power": "Wall Climbing",
    "id": 5,
    "age": 18,
    "real_name": "Peter Parker",
    "gender": "Male"
  }
]
```

### 6. Sort hero by name

```
curl GET http://127.0.0.1:8000/heroes/?sortBy=name
```

Expected response:

```
[
  {
    "name": "Batman",
    "secret_power": "Genius",
    "id": 2,
    "age": 40,
    "real_name": "Bruce Wayne",
    "gender": "Male"
  },
  {
    "name": "Iron Man",
    "secret_power": "Advanced Armor",
    "id": 4,
    "age": 45,
    "real_name": "Tony Stark",
    "gender": "Male"
  },
  {
    "name": "Spider-Man",
    "secret_power": "Wall Climbing",
    "id": 5,
    "age": 18,
    "real_name": "Peter Parker",
    "gender": "Male"
  },
  {
    "name": "Superman",
    "secret_power": "Flight",
    "id": 1,
    "age": 35,
    "real_name": "Clark Kent",
    "gender": "Male"
  },
  {
    "name": "Wonder Woman",
    "secret_power": "Super Strength",
    "id": 3,
    "age": 5000,
    "real_name": "Diana Prince",
    "gender": "Female"
  }
]
```

### 7. Sort hero by gender

```
curl GET http://127.0.0.1:8000/heroes/?sortBy=gender
```

Expected response:

```
[
  {
    "name": "Wonder Woman",
    "secret_power": "Super Strength",
    "id": 3,
    "age": 5000,
    "real_name": "Diana Prince",
    "gender": "Female"
  },
  {
    "name": "Superman",
    "secret_power": "Flight",
    "id": 1,
    "age": 35,
    "real_name": "Clark Kent",
    "gender": "Male"
  },
  {
    "name": "Batman",
    "secret_power": "Genius",
    "id": 2,
    "age": 40,
    "real_name": "Bruce Wayne",
    "gender": "Male"
  },
  {
    "name": "Iron Man",
    "secret_power": "Advanced Armor",
    "id": 4,
    "age": 45,
    "real_name": "Tony Stark",
    "gender": "Male"
  },
  {
    "name": "Spider-Man",
    "secret_power": "Wall Climbing",
    "id": 5,
    "age": 18,
    "real_name": "Peter Parker",
    "gender": "Male"
  }
]
```
### PUT request
### 1. Update a hero detail 

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

### DELETE request

### 1. Delete a hero WITHOUT authorization

```
curl -X DELETE "http://127.0.0.1:8000/heroes/1"
```

### Expected response 

```
{
  "detail": "Unauthorized"
}

```

### 2. Delete a hero WITH authorization

```
curl -X DELETE "http://localhost:8000/heroes/1" \
     -H "Authorization: Bearer supersecureadminkey"
```

### Expected response 

```
{
  "message": "Hero with ID 1 deleted"
}
```

### 3. Delete all heroes WITH authorization

```
curl -X DELETE "http://localhost:8000/heroes/delete_all" \
     -H "Authorization: Bearer supersecureadminkey"
```

### Expected response 

```
{
  "message": "Deleted heroes with IDs [2, 3, 4, 5]"
}
```

