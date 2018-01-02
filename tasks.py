from invoke import task


@task
def migrate(ctx):
    ctx.run("docker-compose exec web ./manage.py migrate")


@task
def up(ctx):
    ctx.run("docker-compose up --build -d")


@task
def down(ctx):
    ctx.run("docker-compose down")
