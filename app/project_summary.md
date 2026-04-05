# /docs

Welcome to the API documentation for this project.

This page explains the available routes, access control rules, validation behavior, error handling, and database design in a simple, readable format.

---

## Swagger UI link: [https://fintect-api-production.up.railway.app/docs#/]

## 1) Authentication Routes

These routes handle user authentication and account setup.

### Credentials

#### Admin
- **Username:** [neel.hans97@gmail.com](mailto:neel.hans97@gmail.com)
- **Password:** `admin123`

#### Analyst
- **Username:** [analyst1@example.com](mailto:analyst1@example.com)
- **Password:** `analyst123`

#### Viewer
- **Username:** [viewer1@example.com](mailto:viewer1@example.com)
- **Password:** `viewer123`

---

## 2) Protected Routes with RBAC

Some routes are protected using **Role-Based Access Control (RBAC)**.

### 2.1 User Management

This section allows admins to manage users and roles.

#### Privileges
- Update the role of other users.
- Promote users to **admin**.
- Promote users to **analyst**.

---

## Role Based Access Control

RBAC is enforced using **Enums** for type safety and consistency.

### Roles

1. **Viewer**
   - Default role assigned at registration.

2. **Admin**
   - The first admin is created at startup.
   - Additional users can later be promoted to admin.

3. **Analyst**
   - A viewer can be promoted to analyst by an admin.

---

## User and Role Management

Roles are enforced using enums for type safety.

- RBAC enforced via dependency injection
- New users are assigned the **viewer** role by default.
- Admin-only endpoints are used to update user roles.
- Role changes are controlled through RBAC enforcement in the service layer and route protection.

---

## Financial Records CRUD

The financial records management routes include full CRUD support.

### Permissions

1. **Create**
   - Only admin can create a record.

2. **Retrieve**
   - Open to all authenticated users, and in some cases publicly readable depending on route design.

3. **Update**
   - Only admin can update a record.

4. **Delete**
   - Only admin can delete a record.

---

## Record Filtering

The `get_financial_records` route supports filtering by:

1. **Category**
   - Enforced by enums.
   - Examples: Salary, Investment, Utilities, Rent, etc.

2. **Type**
   - Income or investment.

3. **Date**
   - Records can be filtered by date.

4. **Customer credentials**
   - Records can be filtered by customer-related identifiers such as mobile number.

---

## Dashboard Summary APIs

These APIs provide aggregate views of the financial data.

### Available summaries

1. **Overall summary**
   - Total income.
   - Total expense.
   - Across all customers.

2. **Customer financial summary**
   - Summary for a specific customer.

3. **Financial summary by category**
   - Totals grouped by category.

4. **Monthly income vs expense trends**
   - Shows monthly trend comparisons.

5. **Export all financial records to CSV**
   - Useful for analysts who want to evaluate data beyond the dashboard summary.

---

## Input Validation

Request validation is handled using **Pydantic schemas**.

### Validation features
- Field-level validation is implemented using `field_validator`.
- Response models ensure consistent and structured API outputs.
- Input normalization, such as trimming whitespace, is handled at schema level.

### Examples
- Email format validation.
- Minimum password length checks.
- Cleaned input values before business logic runs.

---

## Error Handling

Business logic errors are handled using `HTTPException` with appropriate status codes.

### Common status codes
- **400 Bad Request**
  - Duplicate or invalid input.
  - Example: email already registered.

- **401 Unauthorized**
  - Authentication failures.
  - Example: invalid credentials.

### Validation errors
Input validation errors are automatically handled by Pydantic schemas:
- Type validation, such as `EmailStr`.
- Field constraints, such as minimum password length.
- Custom validation through `field_validator`.

### Design approach
- Validation is handled at schema level.
- Business logic errors are handled in the service layer.
- Error messages are clear and descriptive to make debugging and testing easier.

---

## Data Persistence

The application uses **PostgreSQL** for persistent storage.

### Storage details
- Database interactions are handled using **SQLAlchemy ORM**.
- Models define the structured schema for users and financial records.
- Data is stored in relational format with proper schema design.
- User data and financial records persist across sessions.
- Relationships are managed at the ORM level.

### Configuration
- The database connection is configured using the `DATABASE_URL` environment variable.
- The same configuration works for both local and deployed environments.
- The app is deployed using **Railway PostgreSQL**.

### Why PostgreSQL
PostgreSQL was chosen for:
- Reliable, structured data storage.
- Strong support for relational data.
- Seamless integration with SQLAlchemy.
- Smooth deployment with Railway.

---

## Quick Summary

- Authentication is available through dedicated auth routes.
- RBAC protects admin-only actions.
- Users start as viewers by default.
- Admins can promote users to analyst or admin.
- Financial records support CRUD and filtering.
- Dashboard APIs provide totals, trends, summaries, and CSV export.
- Validation is handled by Pydantic.
- PostgreSQL is used for durable data persistence.

---