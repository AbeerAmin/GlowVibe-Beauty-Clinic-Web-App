# GlowVibe-Beauty-Clinic-Web-App
A cutting-edge web platform for booking beauty and wellness services, consultations, and doctor appointments.

### Table of Contents
* Description
* Installation
* Usage
* Team Members
* Scrum
* Features
* Contributing


## Project Overview
**GlowVibe Beauty** is an innovative web platform designed to elevate the beauty and wellness experience. It provides users with a comprehensive system to book beauty treatments, consult with top professionals, and manage appointments for medical procedures. GlowVibe aims to streamline the process of booking and consultation while offering a vibrant and interactive online experience.

### Purpose and Scope
GlowVibe was developed to solve the frustrations that both beauty clinic clients and service providers face when trying to manage appointments, consultations, and reviews. With a smooth and intuitive interface, it allows clients to easily book services, interact with professionals, and read testimonials, while giving admins and service providers the tools to manage everything seamlessly.

### Problem It Solves
Simplifies appointment scheduling.
Prevents double-booking and resolves conflicts.
Offers secure management of consultations and user data.
Enhances customer experience through notifications and reminders.

### What Makes It Stand Out?
Real-time booking with dynamic availability.
Integration with email/SMS notification services.
GDPR/HIPAA-compliant security for personal and medical data.
Analytics dashboards for tracking user activity and revenue.

### Installation

Follow these steps to install and set up GlowVibe locally:

# 1. Clone the Repository

 git clone https://github.com/AbeerAmin/GlowVibe-Beauty-Clinic-Web-App/tree/main
 
 cd GlowVibe-Beauty-Clinic-Web-App
 
### 2. Backend Setup
# 1.Navigate to the backend directory:
   cd backend
# 2. Install dependencies:
   npm install
# 3.Configure environment variables:
  * Create a .env file and add:
    PORT=5000
    MONGO_URI=your_mongodb_connection_string
    JWT_SECRET=your_jwt_secret_key
    SENDGRID_API_KEY=your_sendgrid_api_key
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
# 4.Start the backend server:
  npm start
  
### 3. Frontend Setup
# 1.Navigate to the frontend directory:
  cd ../frontend
# 2.Install dependencies:
  npm install
# 3.Start the development server:
  npm start
  
The application frontend will run at http://localhost:3000, and the backend will run at http://localhost:5000.


### Usage
# For Users
Register a new account and log in.
Explore the catalog of services and choose the desired beauty treatments.
Schedule consultations or appointments with professionals.
Manage bookings and receive email/SMS notifications for reminders.
# For Admins
Log in with admin credentials.
Add, update, or remove services in the catalog.
Monitor appointments and resolve scheduling conflicts.
Access the analytics dashboard for business insights.

## Team Members

- **Abeer, Sarah, Menna, Rofida, Manar** - Product Owner
  - **Responsibilities**: Prioritizing features, defining product vision, managing backlog.
  
- **Menna Sharaf** - Scrum Master
  - **Responsibilities**: Facilitating Scrum ceremonies, ensuring team follows Scrum processes, removing blockers.
  
- **Rofida Ramadan** - Developer
  - **Responsibilities**: Building the frontend, integrating with the backend, handling UI/UX tasks.
 
- **Manar Mamdouh** - Developer
  - **Responsibilities**: Building the frontend, integrating with the backend, handling UI/UX tasks.
- **Abeer Amin** - Developer
  - **Responsibilities**: Backend development, database design, and integrating third-party APIs for appointment management.

- **Sarah Salah** - Developer
  - **Responsibilities**: Backend development, database design, and integrating third-party APIs for appointment management.
 
 - **Menna Sharaf** - Developer
  - **Responsibilities**: Backend development, database design, and integrating third-party APIs for appointment management.


## Scrum Setup

### Product Backlog
The **Product Backlog** is a prioritized list of features, enhancements, bug fixes, and technical debts that need to be completed. The Product Owner is responsible for maintaining and updating this list.

Some items from the Product Backlog:
- User registration and profile management
- Appointment booking and scheduling system
- Doctor profiles and consultation management
- Client reviews and testimonials system
- Admin dashboard for managing appointments, services, and users

### Sprint Backlog
The **Sprint Backlog** contains tasks and stories that have been pulled from the Product Backlog for a specific Sprint. The team commits to delivering these during the current Sprint.

Example Sprint Backlog items:
- Implement registration form (2 days)
- Create user profile page (3 days)
- Develop appointment booking API (4 days)

### Scrum Ceremonies

- **Sprint Planning**: We meet at the start of each Sprint to review the Product Backlog, discuss what can be accomplished, and define the Sprint Goal.
- **Daily Stand-up**: A 15-minute meeting held every day for the team to discuss progress, blockers, and goals for the day.
- **Sprint Review**: At the end of each Sprint, we demonstrate the work completed to stakeholders and gather feedback.
- **Sprint Retrospective**: A meeting to reflect on the Sprint, identify what went well, and discuss opportunities for improvement.

### Features
* Real-Time Booking: Instantly book and confirm appointments.
* Notifications: Automated email and SMS reminders for appointments.
* Dynamic Service Management: Update service availability and pricing in real-time.
* Secure Data Management: Encryption and compliance with data security standards.
* Analytics Dashboard: Track revenue and user activity in real-time.

  
### Contributing

# We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch:
  git checkout -b feature-name

3. Commit your changes:
  git commit -m "Description of changes"
4. Push the branch:
  git push origin feature-name

5. Open a pull request on GitHub.


