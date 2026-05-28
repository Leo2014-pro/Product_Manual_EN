# System Admin

The System Admin module is the backend hub for platform administrators to perform global configuration, manage users and permissions, manage APIs, and monitor system operations.

### User Management

Description: View all backend administrator account information on the platform and manage account status.

![](.gitbook/assets/image53.png)

Operations:

* Filter: Search by account name, status, time
* Add:
* Account name: The username required for login; it is recommended to use the same as the email
* Display name: Used only to display the user's name
* Email: Used for security verification during sensitive operations; verification codes will be sent here
* Status: When disabled, the user cannot log in to the merchant backend
* Password: Set the login password
* Confirm password: Re-enter the login password
* Google verification code: Verify the Google verification code of the currently logged-in account for security verification

![](.gitbook/assets/image54.png)

* Edit: Edit display name and status

![](.gitbook/assets/image55.png)

* Delete: After deletion, the user cannot log in to the merchant backend
* Assign role: After assigning a role, the user inherits the permissions of that role

![](.gitbook/assets/image56.png)

### Role Management

Description: View all backend role information on the platform and manage role permissions.

![](.gitbook/assets/image57.png)

Operations:

* Add: Create a role name for the role's permissions. For example: Finance, Operations, etc.
* Super admin: Default to "No"

![](.gitbook/assets/image58.png)

* Edit: Edit created role information
* Delete: After deleting a role, users bound to that role will lose all permissions
* Bind menu: Bind menus to a role; only users with the bound role can access and view those menus

![](.gitbook/assets/image59.png)

### API Management

Description: Manage all merchants/applications that have been created and have applied for API permissions.

![](.gitbook/assets/image60.png)

Operations:

* Create API Secret: Create an API key and provide it to the technical team for integration. Please keep this key secure. If there is a risk of leakage, replace it immediately.

![](.gitbook/assets/image61.png)

* Webhooks: Technical parameter configuration. Select corresponding events based on business needs.

![](.gitbook/assets/image62.png)
