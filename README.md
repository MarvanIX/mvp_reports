# MVP Reports

A Django-based MVP for company reporting. Employees can submit anonymous or confidential reports through a **magic link**, while managers can track reports, their status, and receive notifications. Includes user management with a master superuser for full access.

---

## Features

### User Management
- Custom user model using email as login.
- Registration allows selecting a company to join.
- Master user automatically created on first setup.
- Login with email and password.

### Companies
- SuperUser can **create, edit, and delete companies** (Managers can only manage their own company and reports).
- Companies have unique **magic links** for report submission.
- Company table shows name, magic link, and number of reports.

### Reports
- Employees submit reports through a **magic link** (no login required).
- Reports can be **anonymous** or submitted with email.
- Managers can view reports for their company, see status, and creation date.
- Reports page uses a table view with color-coded statuses.

### Notifications
- Managers receive notifications for new reports.
- Notifications appear in the navbar with a bell icon.
- Mark notifications as read without page reload.
- Click a notification to mark it as read.

### Frontend
- **Bootstrap 5** for responsive UI.
- Login and registration pages with centered cards.
- Company and report pages have tables with clickable rows and modals for actions.
- Magic link submission page is centered, card-based, with gradient background.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mvp_reports.git
cd mvp_reports
```
2. Install dependencies:

# Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```
# Windows
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install Django:

```bash
pip install django
```
4. Apply Migrations:
```bash
python manage.py makemigrations #if needed
python manage.py migrate
```
5. Create superuser(if first setup didn't auto-create master user):"
```bash
python manage.py createsuperuser
```
6. Run the Server:
```bash
python manage.py runserver
```
7. Access the app in your browser at http://localhost:8000/login/

---