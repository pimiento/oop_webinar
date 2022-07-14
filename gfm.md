- [YaTube Project](#orgaf37616)
  - [Social network for bloggers.](#orgc7f6d7b)
- [Tech Stack](#org2be34b5)
- [Run project in DEV-Mode](#org395a3b2)



<a id="orgaf37616"></a>

# YaTube Project


<a id="orgc7f6d7b"></a>

## Social network for bloggers.


<a id="org2be34b5"></a>

# Tech Stack

-   **Client:** Python 3.7, Django 2.2.19
-   **Server:** Windows/Linux/MacOS/FreeBSD


<a id="org395a3b2"></a>

# Run project in DEV-Mode

1.  Install and activate virtual environment

    ```shell
    python -m venv venv
    # For Linux/MacOS
    source venv/bin/activate
    # For Windows
    source venv/Scripts/activate.sh
    ```
2.  Install dependencies

    ```shell
    pip install -r requirements.txt
    ```
3.  Migrate models to database

    ```shell
    python manage.py migrate
    ```
4.  Create a superuser

    ```shell
    python manage.py createsuperuser
    ```
5.  Run

    ```shell
    python manage.py runserver
    ```
