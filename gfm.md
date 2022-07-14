- [YaTube Project](#orgd04f945)
  - [Social network for bloggers.](#orgfee9ae9)
- [Tech Stack](#orgde0c7f3)
- [Run project in DEV-Mode](#org5464be6)
- [How to check your models](#org96403e6)


```shell
    [0;1;31;91mm[0m     [0;1;36;96mm[0m       [0;1;33;93mmm[0;1;32;92mmm[0;1;36;96mmm[0;1;34;94mm[0m        [0;1;32;92m#[0m
     [0;1;33;93m"[0;1;32;92mm[0m [0;1;36;96mm"[0m   [0;1;35;95mm[0;1;31;91mmm[0m     [0;1;36;96m#[0m    [0;1;31;91mm[0m   [0;1;32;92mm[0m  [0;1;36;96m#[0;1;34;94mmm[0;1;35;95mm[0m    [0;1;33;93mm[0;1;32;92mmm[0m
      [0;1;36;96m"#[0;1;34;94m"[0m   [0;1;31;91m"[0m   [0;1;32;92m#[0m    [0;1;34;94m#[0m    [0;1;33;93m#[0m   [0;1;36;96m#[0m  [0;1;34;94m#[0;1;35;95m"[0m [0;1;31;91m"#[0m  [0;1;32;92m#"[0m  [0;1;34;94m#[0m
       [0;1;34;94m#[0m    [0;1;33;93mm"[0;1;32;92m""[0;1;36;96m#[0m    [0;1;35;95m#[0m    [0;1;32;92m#[0m   [0;1;34;94m#[0m  [0;1;35;95m#[0m   [0;1;33;93m#[0m  [0;1;36;96m#"[0;1;34;94m""[0;1;35;95m"[0m
       [0;1;35;95m#[0m    [0;1;32;92m"m[0;1;36;96mm"[0;1;34;94m#[0m    [0;1;31;91m#[0m    [0;1;36;96m"m[0;1;34;94mm"[0;1;35;95m#[0m  [0;1;31;91m#[0;1;33;93m#m[0;1;32;92m#"[0m  [0;1;34;94m"#[0;1;35;95mmm[0;1;31;91m"[0m
```


<a id="orgd04f945"></a>

# YaTube Project


<a id="orgfee9ae9"></a>

## Social network for bloggers.


<a id="orgde0c7f3"></a>

# Tech Stack

-   **Client:** Python 3.7, Django 2.2.19
-   **Server:** Windows/Linux/MacOS/FreeBSD


<a id="org5464be6"></a>

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


<a id="org96403e6"></a>

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
