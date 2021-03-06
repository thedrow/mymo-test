from invoke import task


@task
def migrate(ctx):
    ctx.run("docker-compose exec web ./manage.py migrate")


@task
def createsuperuser(ctx):
    ctx.run("docker-compose exec web ./manage.py createsuperuser")


@task
def up(ctx):
    ctx.run("docker-compose up --build -d")


@task
def down(ctx):
    ctx.run("docker-compose down")


@task
def test(ctx):
    ctx.run("pipenv run pytest")
