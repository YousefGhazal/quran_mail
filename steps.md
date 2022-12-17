# reqs

1. create subscribe and unsubscribe pages
    - soft delete in unsubscribe (is active)
2. send the selected aya to all active users in email
    - create tasks file and add a function to it
    - please use django herald <https://github.com/ahmedyasserays/django-herald>
3. get random ayah with tafsir from the api
    - please use
        <https://requests.readthedocs.io/en/latest/>
        requests.get(url).json()
4. create cron job that runs every day
    - celery

        <https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#first-steps>

        <https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html>
        
        <https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html>
5. make unsubscribe button in email have token
6. contact us page
    - create new gmail
