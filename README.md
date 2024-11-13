# Hospital Management System

## Overview
The **Hospital Management System** is a Django-based web application designed to streamline the various operations in a healthcare facility. It provides functionalities for both admins and patients to manage appointments, view medical history, and handle doctor availability. The system includes features for appointment scheduling, doctor management, and patient records.

## Features
### Admin Features:
- Dashboard to view overall hospital activities.
- Manage doctors, staff, and patients.
- Appointment scheduling and management.
- Payment processing and staff management.

### Patient Features:
- Register, login, and manage personal information.
- Schedule appointments with doctors.
- View previous appointment history and medical records.

### Doctor Features:
- View and manage patient appointments.
- Update personal information and availability.

## Functionalities
1. **Appointment Scheduling**:
   - Patients can book appointments by selecting a doctor, time slot, and date.
   - The available time slots are dynamically generated.
   - Admins and doctors can view and manage the list of appointments.

2. **Doctor Management**:
   - Admins can manage doctor records, including their specialties.
   - Doctors can set their available time slots.

3. **Patient Management**:
   - Admins can add, view, and manage patient records.
   - Patients can register, view their profile, and edit personal details.

4. **Payment System**:
   - Admins can manage patient payments for treatments and appointments.
   
5. **Medical History**:
   - Patients and doctors can view past appointments and medical records.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (for development), PostgreSQL (for production)
- **Authentication**: Django's built-in authentication system
- **Version Control**: Git
- **Deployment**: Heroku or other cloud services (for production)

## Installation
### Prerequisites:
- Python 3.x
- Django
- PostgreSQL (optional, can use SQLite for development)
- Virtual environment (optional but recommended)
