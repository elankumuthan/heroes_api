# HERO API LAB 1

## Overview 
This FastAPI helps to provide Hero Management API, aloowing users to create, read, update and delete heroes. It also supports file uploading and returning an image.


## Features 

### Operations on heroes


|Method | Endpoint | Description|
|POST | hero/ | Create a new hero|
|GET | /heroes/ | Get all heroes|
|GET | /heroes/{hero_id} | Get hero by ID|
|PUT | /heroes/{hero_id}	| Update a hero|
|DELETE	| /heroes/{hero_id}	| Delete a hero|

### File Operations

Method	Endpoint	Description
POST	/uploadfile/	Upload a file

uploaded files are stored in the uploads/ directory.

### Return Binary Content


Method	Endpoint	Description
GET	/image	Serve an image (app/spiderman.jpg)


## Installation

1. Clone the repository 

git clone <your-repo-url>
cd hero_api

2. Build and Run the Docker Container 

docker compose up --build

3. Send request

You can send request from post.http which has some test cases.

    a. Create new hero

    curl -X POST "http://localhost:8000/hero/" \
     -H "Content-Type: application/json" \
     -d '{
        "name": "Ant-man",
        "age": 35,
        "secret_power": "Shrink and Grow",
        "gender": "Male",
        "real_name": "Scott Lang"
    }'

     expected response:

   {
        "name": "Ant-man",
        "age": 35,
        "secret_power": "Shrink and Grow",
        "gender": "Male",
        "real_name": "Scott Lang"
    }

    b. Create new hero with missing name

    curl -X POST "http://localhost:8000/hero/" \
     -H "Content-Type: application/json" \
     -d '{
        "name": "",
        "age": 54,
        "secret_power": "Superhuman strength, durability, endurance, and healing",
        "gender": "Male",
        "real_name": "Bruce Banner"
    }'

    expected response:

    {
    "detail": "Hero name is required"
    }

    c. Get all heroes

    curl http://127.0.0.1:8000/heroes/ 

    expected response 

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
    "name": "Batman",
    "secret_power": "Genius",
    "age": 40,
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
  }
]


    d. Get hero by id

    curl GET http://127.0.0.1:8000/heroes/2

    {
  "name": "Batman",
  "secret_power": "Genius",
  "age": 40,
  "id": 2,
  "real_name": "Bruce Wayne",
  "gender": "Male"
}

    e. Sort hero by age

    curl GET http://127.0.0.1:8000/heroes/?sortBy=age

    expected response:

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
    "name": "Superman",
    "secret_power": "Flight",
    "age": 35,
    "id": 1,
    "real_name": "Clark Kent",
    "gender": "Male"
  },
  {
    "name": "Batman",
    "secret_power": "Genius",
    "age": 40,
    "id": 2,
    "real_name": "Bruce Wayne",
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
    f. Sort hero by age and limit to 3

    curl GET http://127.0.0.1:8000/heroes/?sortBy=age&count=3

    expected response:

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
    "name": "Superman",
    "secret_power": "Flight",
    "age": 35,
    "id": 1,
    "real_name": "Clark Kent",
    "gender": "Male"
  },
  {
    "name": "Batman",
    "secret_power": "Genius",
    "age": 40,
    "id": 2,
    "real_name": "Bruce Wayne",
    "gender": "Male"
  }
]
    g. Update a hero detail 

    curl -X PUT "http://127.0.0.1:8000/heroes/2" \
     -H "Content-Type: application/json" \
     -d '{
          "name": "The Bat-Man",
          "age": 24,
          "secret_power": "Genius, Ultra-rich, Master Martial Artist",
     }'


    h. Delete a hero 

    curl -X DELETE "http://127.0.0.1:8000/heroes/3"

    {
  "ok": true
}

    i. upload a file 

    POST http://localhost:8000/uploadfile/
Content-Type: multipart/form-data; boundary=----CustomBoundary123

------CustomBoundary123
Content-Disposition: form-data; name="file"; filename="spiderman.jpg"
Content-Type: image/jpeg

< ../app/spiderman.jpg
------CustomBoundary123--

    {
  "filename": "spiderman.jpg",
  "size": 44148,
  "file_type": "image/jpeg",
  "path": "uploads/spiderman.jpg"
}

    j. return a binary content(image)

    curl GET http://127.0.0.1:8000/image

    expected response:
    returns an image

