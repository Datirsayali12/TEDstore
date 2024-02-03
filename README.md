
# TEDStore

This Django project is a web application for managing products.




## Prerequisites:
Python
Django


## Installation

Install dependencies: pip install -r requirements.txt
Apply database migrations: python manage.py migrate
Create a superuser: python manage.py createsuperuser
Run the development server: python manage.py runserver


    
## API Reference

#### app APIS

```http
  GET /api/product
```
Response: Return list of all products

#### Get item

```http
  GET /api/offer
```

 Response: 
 {
        "offer_id": 1,
        "offer_category": "Discount Offer",
        "offer_description": "35 % discount on dell"
    }

#### Get item

```http
  POST /api/newsletter

  Request Body:
  {
  "email": "example@example.com"
  }
```

#### Get item

```http
  POST /api/add_cart

  Request Body:
  {
   user_id:int, 
   product_id:int, 
   quantity:int,
  
  }
```

#### Get item

```http
  GET /api/get_subcategories/${category_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `category_id`      | `number` | **Required**. Id of category to fetch subcategories |


#### Get item

```http
  GET /api/review/${slug}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`      | `string` | **Required**. slug of product to fetch review details of product |

```http
  GET /api/category/${slug}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`      | `string` | **Required**. slug of product to fetch category of product |


```http
    POST /api/likes

    Request body:
    {
    'review_id':1,
    'user_id':1    
    }
```
```http
    POST /api/dislikes

    Request body:
    {
    'review_id':1,
    'user_id':1    
    }
```

```http
  GET /api/related_products/<slug>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`      | `string` | **Required**. slug of product to fetch particular product |


#### Account app APIS

```http
  POST /accounts/register
```
 request body:
 {
  "email": "example@example.com",
  "phone_number": 1234567890,
  "address": "123 Example St, City, Country",
  "password": "example_password",
  "password2": "example_password"
 
}

```http
  POST /accounts/login
```
 request body:
 {
  "email": "example@example.com",
  "password": "example_password"
 
}

```http
  GET /accounts/profile
```
 send access token in header

 ```http
  GET /accounts/change_password
```
 send access token of login user in header











