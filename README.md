# Django File Sharing Application

This is a simple Django application that allows you to share files between devices on the same network.

## Features

*   Send files to other devices on the same network.
*   Receive/Download files from other devices on the same network.
*   Responsive design for use on different devices.

## Requirements

*   Python 3.x
*   Django

## Setup and Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/prottoy-bhattacharyya/share-files-on-same-network.git
    cd share-files-on-same-network
    ```

    ***Android Devices:***
    <br>
    1.1. Open Termux and type
    ```bash
    pkg install git
    git clone https://github.com/prottoy-bhattacharyya/share-files-on-same-network.git
    ```

2. **Install Python dependencies**
   <br><br>
    Make sure Python is installed: [Download Python](https://www.python.org/downloads/)
    
    ```bash
    pip install uv
    ```
    uv will automatically create a virtual environment and install all the dependencies.

    ***Android Devices :***
    <br>
    2.1. goto the folder you wanted to save the files 

    ```bash
    termux-setup-storage
    cd <directory>
    ```
    2.2. Install Dependencies:
    
    ```bash
    pkg install python
    pip install django
    ```

3.  **Start the development server:**

    ```bash
    python -m uv run manage.py runserver 0.0.0.0:8000
    ```
    ***Android Devices :***
    <br>
    3.1. Find your Network IP Address

    ```bash
    ifconfig
    ```
    <br>
    <br>
    <img width="300" alt="Screenshot 2025-08-01 042422" src="https://github.com/user-attachments/assets/d08fb016-3567-4d11-946b-600861a39147" />
    <br>
    <br>
    
    3.2 Run the Server
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

## Accessing the Application

Once the server is running, you can access the application from any device on the same network by navigating to the `Network IP` address followed by the `port number`. Eg., `192.168.0.103:8000` in your browser
<br>
<br>
**For Example:**
<br>
<br>
<img width="673" height="305" alt="Screenshot 2025-08-01 042422" src="https://github.com/user-attachments/assets/788e0231-bb35-4e6f-a63b-3072e9ab5416" />
<br>
<br>
**For your device the Network IP can be different** 
