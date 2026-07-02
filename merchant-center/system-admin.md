# System Admin

The System Administration section is the backend hub for platform administrators to perform global configuration, manage users and permissions, manage APIs, and monitor system operations.

## User Management

**Feature Description**: View all platform backend administrator account information and manage account status.

**Operations**:
- Filter: Search by account name, status, and time.
- Add:
  - Account Name: It is recommended that the login username match the email address.
  - Username: Used only to display the user's name.
  - Email: Used for security verification during sensitive operations; a verification code will be sent.
  - Status: When disabled, the user will not be able to log in to the merchant backend.
  - Password: Set the login password.
  - Confirm Password: Re-enter the login password.
  - Google Authenticator Code: Verify the Google Authenticator code of the currently logged-in account for security verification.

- Edit: Edit username and status.
- Delete: After deletion, the user cannot log in to the merchant backend.
- Assign Role: After assigning a role, the user will have the permissions corresponding to that role.

---

## Role Management

**Feature Description**: View all backend role information for the platform and manage role permissions.

**Operations**:
- Add: Create a role name for the role's permissions. Examples: Finance, Operations, etc.
  - Super Administrator: Default to "No".

- Edit: Edit information of created roles.
- Delete: After deleting a role, users bound to that role will have no permissions.
- Bind Menu: Bind menus to a role; users bound to that role will then be able to access and view those menus.

---

## Security Center

This page is primarily for managing basic security information for merchant logins and viewing the latest login history.

### Profile Verification Management

- **Feature Description**: Submit company information for platform review. When no information has been submitted, permissions are limited.
- **Steps**:
  1. Click "Verify"
  2. Fill in business information
  3. Fill in contact person information
  4. Submit for review
  5. After approval, gain more permissions

### Login Password Management

- **Feature Description**: Change the password for logging into the merchant backend.
- **Steps**:
  1. Click "Change Login Password".
  2. Set a **new login password** (8-18 characters, combination of letters, numbers, and symbols).
  3. Re-enter the new password for confirmation.
  4. Enter email verification code / Google Authenticator code for identity verification.
  5. Click "Confirm"; the password change takes effect immediately.

### Fund Password Management

- **Feature Description**: Set or change the secondary verification password used for fund operations such as withdrawals.
- **Steps**:
  1. Click "Change Fund Password".
  2. Set a **new fund password** (8-18 characters, combination of letters, numbers, and symbols).
  3. Re-enter the new password for confirmation.
  4. Enter email verification code / Google Authenticator code for identity verification.
  5. Click "Confirm"; the password change takes effect immediately.

### Google Authenticator Binding

- **Feature Description**: Bind Google Authenticator to add dynamic password (MFA) protection for logins or critical operations. Binding is mandatory upon first login.
- If you have forgotten your original Google Authenticator code, please contact the platform for a reset.
- **Steps**:
  1. Click "Reset Google Authenticator".
  2. Use the Google Authenticator app to scan the **QR code** displayed on the page.
  3. The app will generate a 6-digit dynamic verification code.
  4. Enter this verification code in the input field on the page.
  5. Click "Next" to proceed with security verification.
  6. Enter email verification code / original Google Authenticator code for identity verification.
  7. Upon successful confirmation, the Google Authenticator reset is complete.

### Recent Login History

**Feature Description**: Displays the most recent login locations and IP information for this merchant account. If a login from an unknown location is detected, please change your password and Google Authenticator immediately.
