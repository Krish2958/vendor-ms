# Vendor Management System API

Welcome to the Vendor Management System (VMS) API. This API provides endpoints to manage vendors, purchase orders, and track vendor performance metrics.

## Setup Instructions

1. Clone this repository to your local machine:

```
git clone <repository_url>
```

2. Navigate to the project directory:

```
cd vendor-management-system
```

3. Install dependencies using pip:

```
pip install -r requirements.txt
```

4. Apply database migrations:

```
python manage.py migrate
```

5. Run the development server:

```
python manage.py runserver
```

6. Access the API at `http://127.0.0.1:8000/api/`.

## API Endpoints

### Vendors

- **GET /api/vendors/**: Retrieve a list of all vendors.
- **POST /api/vendors/**: Create a new vendor.
- **GET /api/vendors/{id}/**: Retrieve details of a specific vendor.
- **PUT /api/vendors/{id}/**: Update a specific vendor.
- **DELETE /api/vendors/{id}/**: Delete a specific vendor.
- **GET /api/vendors/{id}/performance/**: Retrieve performance metrics for a specific vendor.

### Purchase Orders

- **GET /api/purchase_orders/**: Retrieve a list of all purchase orders.
- **POST /api/purchase_orders/**: Create a new purchase order.
- **GET /api/purchase_orders/{id}/**: Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{id}/**: Update a specific purchase order.
- **DELETE /api/purchase_orders/{id}/**: Delete a specific purchase order.
- **POST /api/purchase_orders/{id}/acknowledge/**: Acknowledge a purchase order.

### Performance Metrics

- **GET /api/performance/**: Retrieve a list of all historical performance records.
- **POST /api/performance/**: Create a new historical performance record.
- **GET /api/performance/{id}/**: Retrieve details of a specific historical performance record.
- **PUT /api/performance/{id}/**: Update a specific historical performance record.
- **DELETE /api/performance/{id}/**: Delete a specific historical performance record.

## Documentation & Testing

For More Detailed Documentation and Testing visit 
```
http://127.0.0.1:8000/documentation/
```

## Example Usage

1. Retrieve a list of vendors:

```
GET /api/vendors/
```

2. Create a new purchase order:

```
POST /api/purchase_orders/
{
  "po_number": "PO123",
  "vendor": 1,
  "order_date": "2024-05-10T00:00:00Z",
  "delivery_date": "2024-05-20T00:00:00Z",
  "items": [
    {
      "name": "Item 1",
      "quantity": 10
    },
    {
      "name": "Item 2",
      "quantity": 5
    }
  ]
}
```

3. Retrieve performance metrics for a specific vendor:

```
GET /api/vendors/{id}/performance/
```

## Support

For any issues or questions, please contact krishm.km17@gmail.com.

---
