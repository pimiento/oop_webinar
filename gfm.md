- [Social network for bloggers.](#orgbcd9b8b)
- [Tech Stack](#org3275bbb)
- [Run project in DEV-Mode](#org84f9291)
- [How to check your models](#org4ecc678)

<div style="font-family: monospace, fixed; font-weight: bold;"> <span style="">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span><br /> <span style=";color:#f55">m</span><span style="">&#160;&#160;&#160;&#160;&#160;</span><span style=";color:#5ff">m</span><span style="">&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span><span style=";color:#ff5">mm</span><span style=";color:#5f5">mm</span><span style=";color:#5ff">mm</span><span style=";color:#55f">m</span><span style="">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span><span style=";color:#5f5">#</span><span style="">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span><br /> <span style="">&#160;</span><span style=";color:#ff5">&quot;</span><span style=";color:#5f5">m</span><span style="">&#160;</span><span style=";color:#5ff">m&quot;</span><span style="">&#160;&#160;&#160;</span><span style=";color:#f5f">m</span><span style=";color:#f55">mm</span><span style="">&#160;&#160;&#160;&#160;&#160;</span><span style=";color:#5ff">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#f55">m</span><span style="">&#160;&#160;&#160;</span><span style=";color:#5f5">m</span><span style="">&#160;&#160;</span><span style=";color:#5ff">#</span><span style=";color:#55f">mm</span><span style=";color:#f5f">m</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#ff5">m</span><span style=";color:#5f5">mm</span><span style="">&#160;&#160;</span><br /> <span style="">&#160;&#160;</span><span style=";color:#5ff">&quot;#</span><span style=";color:#55f">&quot;</span><span style="">&#160;&#160;&#160;</span><span style=";color:#f55">&quot;</span><span style="">&#160;&#160;&#160;</span><span style=";color:#5f5">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#55f">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#ff5">#</span><span style="">&#160;&#160;&#160;</span><span style=";color:#5ff">#</span><span style="">&#160;&#160;</span><span style=";color:#55f">#</span><span style=";color:#f5f">&quot;</span><span style="">&#160;</span><span style=";color:#f55">&quot;#</span><span style="">&#160;&#160;</span><span style=";color:#5f5">#&quot;</span><span style="">&#160;&#160;</span><span style=";color:#55f">#</span><span style="">&#160;</span><br /> <span style="">&#160;&#160;&#160;</span><span style=";color:#55f">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#ff5">m&quot;</span><span style=";color:#5f5">&quot;&quot;</span><span style=";color:#5ff">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#f5f">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#5f5">#</span><span style="">&#160;&#160;&#160;</span><span style=";color:#55f">#</span><span style="">&#160;&#160;</span><span style=";color:#f5f">#</span><span style="">&#160;&#160;&#160;</span><span style=";color:#ff5">#</span><span style="">&#160;&#160;</span><span style=";color:#5ff">#&quot;</span><span style=";color:#55f">&quot;&quot;</span><span style=";color:#f5f">&quot;</span><span style="">&#160;</span><br /> <span style="">&#160;&#160;&#160;</span><span style=";color:#f5f">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#5f5">&quot;m</span><span style=";color:#5ff">m&quot;</span><span style=";color:#55f">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#f55">#</span><span style="">&#160;&#160;&#160;&#160;</span><span style=";color:#5ff">&quot;m</span><span style=";color:#55f">m&quot;</span><span style=";color:#f5f">#</span><span style="">&#160;&#160;</span><span style=";color:#f55">#</span><span style=";color:#ff5">#m</span><span style=";color:#5f5">#&quot;</span><span style="">&#160;&#160;</span><span style=";color:#55f">&quot;#</span><span style=";color:#f5f">mm</span><span style=";color:#f55">&quot;</span><span style="">&#160;</span><br /> <span style="">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span><br /> <span style="">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</span><br /> </div>


<a id="orgbcd9b8b"></a>

## Social network for bloggers.


<a id="org3275bbb"></a>

# Tech Stack

-   **Client:** Python 3.7, Django 2.2.19
-   **Server:** Windows/Linux/MacOS/FreeBSD


<a id="org84f9291"></a>

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


<a id="org4ecc678"></a>

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
