# Kaizntree

This is Django project with the RESTful API application.

## Setting Up and Running the Application

1. Clone the Repository: Clone your GitHub repository containing the Django REST API project to your local machine.

```
git clone <repository_url>
```

2. Install Dependencies: Navigate to the project directory and install the required dependencies using pip.

```
cd <project_directory>
pip install -r requirements.txt
```

3. Database Setup: Set up your database according to your Django settings. You may need to run migrations to create the necessary database schema.

```
python manage.py migrate
```

4. Run the Development Server: Start the Django development server to run the API locally.

```
python manage.py runserver
```

5. Access the API: You can now access the API endpoints locally at http://localhost:8000/.

## API Documentation

To consume the endpoints of your Django REST API:

1. Authentication:

    * To authenticate, send a POST request to /auth/login/ with valid credentials (username and password). This will return a token.
    * Use the obtained token in subsequent requests by including it in the Authorization header as Token <your_token>.

2. Making Requests:

    * Use tools like curl, Postman, or Python's requests library to make requests to your API endpoints.
    * Include the required parameters and headers according to the documentation of each endpoint.
  
3. Testing Endpoints:

    * Test each endpoint with different input values and scenarios to ensure they behave as expected.
    * Use the provided unit tests to validate the functionality of the endpoints.

4. Handling Responses:

    * Check the response status codes and body to verify the success or failure of the requests.
    * Handle the response data accordingly in your client application.

## Authentication Endpoints
1. Login
  * URL: /auth/login/
  * Method: POST
  * Request Format:
    * Body:
      
      ```
      {
      "username": "your_username",
      "password": "your_password"
      }
      ```

  * Response Format:
    * Body(on success):
  
       ```
      {
      "token": "your_token"
      }
      ```
       
    * Body(on failure):
      
       ```
      {
      "error": "Error message"
      }

      ```
      
2. Logout
  * URL: /auth/logout/
  * Method: POST
  * Request Format: None
  * Response Format:
    * Body(on success):
  
       ```
      {
      "message": "Logout successful"
      }
      ```
    * Body(on failure):
      
       ```
      {
      "error": "Error message"
      }

      ```

3. Register
  * URL: /auth/register/
  * Method: POST
  * Request Format:
    * Body:
      ```
      {
      "username": "desired_username",
      "password": "desired_password",
      "security_question": "security_question",
      "security_answer": "security_answer"
      }
      ```

   * Response Format:
     * Body (on success):
    
        ```
        {
        "username": "registered_username"
        }
        ```
    
     * Body (on failure):  

        ```
        {
        "error": "Error message"
        }
        ```


4. Forgot Password (Request)
  * URL: /auth/forgot-password/
  * Method: POST
  * Request Format:
    * Body:
      ```
      {
      "username": "your_username",
      "security_question": "security_question",
      "security_answer": "security_answer"
      }
      ```

   * Response Format:
     * Body (on success):
    
        ```
        {
        "message": "Password reset email sent"
        }
        ```
    
     * Body (on failure):  

        ```
        {
        "error": "Error message"
        }
        ```

5. Reset Password
  * URL: /auth/reset-password/
  * Method: POST
  * Request Format:
    * Body:
      ```
      {
      "username": "your_username",
      "new_password": "new_password"
      }
      ```

   * Response Format:
     * Body (on success):
    
        ```
        {
        "message": "Password reset successful"
        }
        ```
    
     * Body (on failure):  

        ```
        {
        "error": "Error message"
        }
        ```

## Dashboard Endpoints

1. Item Dashboard (Retrieve list of items)
  * URL: /dashboard/items/
  * Method: GET
  * Request Format: None
  * Response Format:
     * Body (on success):
    
        ```
        [
          {
            "sku": "item_sku",
            "name": "item_name",
            "category": "item_category",
            "tags": "item_tags",
            "stock_status": "item_stock_status",
            "available_stock": "item_available_stock"
          },
        ]

        ```
    
     * Body (on failure):  

        ```
        {
        "error": "Error message"
        }
        ```
