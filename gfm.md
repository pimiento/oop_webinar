- [YaTube Project](#orgcb5fbc2)
  - [Social network for bloggers.](#orgf0ea812)
- [Tech Stack](#org3a31c20)
- [Run project in DEV-Mode](#org7b7baf3)
- [How to check your models](#org772f4dd)



<a id="orgcb5fbc2"></a>

# YaTube Project


<a id="orgf0ea812"></a>

## Social network for bloggers.


<a id="org3a31c20"></a>

# Tech Stack

-   **Client:** Python 3.7, Django 2.2.19
-   **Server:** Windows/Linux/MacOS/FreeBSD


<a id="org7b7baf3"></a>

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


<a id="org772f4dd"></a>

# How to check your models

1.  Go to Django-shell

    ```shell
    source venv/bin/activate
    python manage.py shell
    ```
2.  Check your users models

    ```python
    from posts.models import User

    all_users = User.objects.all()
    ```
