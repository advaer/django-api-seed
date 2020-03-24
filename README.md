<h1>Growth Simulator API PoC.</h1>


<h5>Setup project:</h5>
<ol>
<li>Install requirements<br>
    <code>$ pip install -r requirements/base.txt</code>
<li>Create .env file from default example<br>
    <code>$ cp .env.default .env</code><br>
    and add your values to .env
<li>Migrate database tables<br>
    <code>$  python manage.py migrate</code>
<li>Populate tables with examples data (optional)<br>
    <code>$ python manage.py loaddata initial</code>
<li>Load user: "localadmin" with password "strongpassword" fixture (optional)<br>
    <code>$ python manage.py loaddata src/apps/core/fixtures/local_admin</code>
<li>OR Create admin user (optional)<br>
    <code>$ python manage.py createsuperuser</code>
</ol>

Enjoy!