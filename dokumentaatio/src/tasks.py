from invoke import task

@task
def start(ctx):
    ctx.run("python index.py", pty = True)

@task
def coverage(ctx):
    ctx.run("verage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)