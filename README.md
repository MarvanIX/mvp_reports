MVP Reports

A Django-based MVP for company reporting. Employees can submit anonymous or confidential reports through a magic link, while managers can track reports, their status, and receive notifications. Includes user management with a master superuser for full access.

Features
User Management

Custom user model using email as login.

Registration allows selecting a company to join.

Master user automatically created on first setup.

Login with email and password.

Companies

Managers can create, edit, and delete companies.

Companies have unique magic links for report submission.

Company table shows name, magic link, and number of reports.

Reports

Employees submit reports through a magic link (no login required).

Reports can be anonymous or submitted with email.

Managers can view reports for their company, see status, and creation date.

Reports page uses a table view with color-coded statuses.

Notifications

Managers receive notifications for new reports.

Notifications appear in the navbar with a bell icon.

Mark notifications as read without page reload.

Frontend

Bootstrap 5 for responsive UI.

Login and registration pages with centered cards.

Company and report pages have tables with clickable rows and modals for actions.

Magic link submission page is centered, card-based, with gradient background.

Installation

Clone the repository:

git clone https://github.com/yourusername/mvp_reports.git
cd mvp_reports

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser (if first setup didn’t auto-create master user):

python manage.py createsuperuser

Run the development server:

python manage.py runserver
Usage
User Registration

Go to /register/ to sign up.

Select a company from the dropdown to join.

Password confirmation required.

Login

Go to /login/ to authenticate.

Master user has full access and can see all companies and reports.

Company Management

Managers can create, edit, and delete companies from /company/.

Click a company row to select for editing or deletion.

Magic link for report submission is displayed per company.

Report Submission

Employees access the report form via the company magic link (no login needed).

Option to submit anonymously or provide an email.

Managers are notified of new reports.

Notifications

Bell icon in the navbar shows unread notifications.

Click a notification to mark it as read via AJAX (no page reload).

Models

User: Custom user model with email login.

Company: Holds company information and managers.

Report: Reports submitted by employees, linked to a company.

MagicLink: Unique token for each company to submit reports.

Notification: Alerts for managers about new reports.

Project Structure
mvp_reports/
├─ users/                  # User management app
│  ├─ models.py
│  ├─ views.py
│  └─ templates/users/
├─ reports/                # Company and report management app
│  ├─ models.py
│  ├─ views.py
│  └─ templates/reports/
├─ static/                 # CSS, JS, images
├─ templates/              # Base templates
├─ mvp_reports/            # Django settings
└─ manage.py
Technologies

Python 3.13

Django 4.x

Bootstrap 5

JavaScript (vanilla) for modals, row selection, and AJAX notifications

Notes

Master user is automatically created on first setup with email master@example.com and password masterpassword (change in production!).

AJAX is used to update notifications without refreshing the page.

Magic links allow anonymous report submission securely.

Screenshots

Login/Register: Centered cards with Bootstrap styling.

Company Page: Table view with magic link and clickable rows for edit/delete.

Report Submission: Centered card, optional anonymous submission.

Notifications: Bell icon shows unread count, click to mark as read.

License

MIT License
