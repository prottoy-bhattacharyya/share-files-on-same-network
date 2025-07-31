# Django File Sharing Application

This is a simple Django application that allows you to share files between devices on the same network.

## Features

*   Upload files through a web interface.
*   Download files from a list of uploaded files.
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

2.  **Install dependencies:**

    ```bash
    pip install uv
    ```
    uv will automatically create a virtual environment and install all the dependencies.


3.  **Start the development server:**

    ```bash
    python -m uv run manage.py runserver 0.0.0.0:8000
    ```

## Accessing the Application

Once the server is running, you can access the application from any device on the same network by navigating to the `Network IP` address followed by the `port number`.
For Example:
<img width="673" height="305" alt="Screenshot 2025-08-01 042422" src="https://github.com/user-attachments/assets/788e0231-bb35-4e6f-a63b-3072e9ab5416" />
for your device the Network IP can be different 
