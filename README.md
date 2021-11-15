#### this is a an API use for face detection and recongnition

### For Getting It Localy

#### Requirements
* python ^3.6
* opencv
* face_recognition
* numpy
* uvicorn 0.15.0 with CPython 3.8.8 on Linux
* fastapi 
##### how to use it ?
1. Puts your known images in the ***knowImage*** folder with persons name as image name
2. Make sure that you are the main folder in your terminal
3. On Linux or Ubuntu run the command bellow
> uvicorn server:app --reload
> You should submit the image that your want to recongnize throught an input file field
### For testing the api with Postman
> Please got to the url localhost:[your port]/docs for more explanations

+ AngeMervaneJdev 