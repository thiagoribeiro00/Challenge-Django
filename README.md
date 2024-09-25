# Emergency Contacts API

This is a simple Django REST API service that allows users to manage their emergency contacts by creating and deleting them.

## **Requirements**

- Python 3.7+
- Django 4.x
- Django REST Framework

## **Setup**

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/emergency_contacts_api.git
    cd emergency_contacts_api
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv myenv
    source myenv/bin/activate   # For Linux/Mac
    myenv\Scripts\activate      # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the SQLite database:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://localhost:8000/`.

## **API Endpoints**

### 1. Create Contact
- **Endpoint:** `/api/contacts/`
- **Method:** `POST`
- **Payload:**
    ```json
    {
      "first_name": "John",
      "last_name": "Doe",
      "phone_number": "+1234567890"
    }
    ```
- **Response:** 
    - `201 Created` with created contact details
    - `400 Bad Request` if validation fails

### 2. Delete Contact
- **Endpoint:** `/api/contacts/<id>/`
- **Method:** `DELETE`
- **Response:**
    - `204 No Content` upon successful deletion
    - `404 Not Found` if the contact does not exist

## **Error Handling**
- Provides meaningful error messages and appropriate status codes for invalid data or non-existent resources.

## **Deployment**

To deploy the project, you can use platforms like Heroku, Render, or Vercel. Refer to their respective documentation for deployment steps.

## **Testing**

You can use tools like Postman or cURL to test the endpoints. Here are some examples:

- **Create a Contact using cURL:**
    ```bash
    curl -X POST http://localhost:8000/api/contacts/ \
    -H "Content-Type: application/json" \
    -d '{"first_name": "John", "last_name": "Doe", "phone_number": "+1234567890"}'
    ```

- **Delete a Contact using cURL:**
    ```bash
    curl -X DELETE http://localhost:8000/api/contacts/1/
    ```

## **License**

This project is licensed under the MIT License.
#   D j a n g o - A P I  
 #   A P I - D j a n g o  
 