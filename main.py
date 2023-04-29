from textwrap import dedent
import typer

import client as cl

app = typer.Typer()

@app.command(help="create a solution file from a template.")
def create(
        id: str = typer.Argument(..., help="A valid rosalind id."),
        loc: cl.Location = typer.Option(
            cl.Location.STRONGHOLD, 
            "--location", "-l",
            help="A valid rosalind location."),
        tmpl: cl.Template = typer.Option(
            cl.Template.simple,
            "--template", "-t",
            help="Choose one of the existing templates.")
):
    to_path = f"{cl.Location.package()}/{loc.module()}/{id}.py"
    cl.io.copy_template(tmpl, to_path)
    print(f"Created file: {to_path}")



@app.command(help="login to rosalind page, and store session data.")
def login(
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., 
        prompt=True, confirmation_prompt= True, hide_input=True),
):
    data = cl.web.account.login(username,password)
    cl.io.dump_cookies('.session/cookies', data)



@app.command(help="get data from a given datasource and cache the query.")
def get(source: str, file: str) -> str:
    process_file = cl.utils.get_data_from_source(source)
    return process_file(file)


@app.command(help="run the given problem with a local input datasource.")
def run(
        id: str = typer.Argument(..., help="A valid rosalind id."),
        input: str = typer.Argument(... , 
            help="input data source to run the solution."),
        loc: cl.Location = typer.Option(
            cl.Location.STRONGHOLD, 
            "--location", "-l",
            help="A valid rosalind location."),
        save: bool = typer.Option(
            False,
            "--save", "-s",
            help=dedent("""Set if you want to save the answer to a file,
                        if not print to stdout.""")),
):
    solution = cl.utils.load_solution_module(id, loc)
    data = cl.io.parseInput(input)
    solution = solution.main(data)

    if save:
        cl.io.writeCache(f"solutions/{id}.txt", solution)
    else:
        print(solution)


@app.command(help="""\
test your solution with the default example of the problem page.""")
def test(
        id: str = typer.Argument(..., help="A valid rosalind id."),
        loc: cl.Location = typer.Option(
            cl.Location.STRONGHOLD, 
            "--location", "-l",
            help="A valid rosalind location."),
        reset: bool = typer.Option(
            False,
            "--remove", "-r",
            help= dedent("""Set this flag to reset the tests of problems 
                         to the default test. useful when you have made 
                         changes to the page and want a clean start.""")),
):
    test = cl.tests.Test(id,loc)
    if reset:
        test.test_remove()

    if not test.test_exist():
        test.create_test()
    
    test.run_test()


if __name__ == "__main__":
    app()
