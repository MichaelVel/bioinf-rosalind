import typer

import client as cl

app = typer.Typer()

@app.command()
def create(
        id: str,
        loc: cl.Location = typer.Option(cl.Location.STRONGHOLD, "--location", "-l"),
        tmpl: cl.Template = typer.Option(cl.Template.simple, "--template", "-t")
):
    to_path = f"{cl.Location.package()}/{loc.module()}/{id}.py"
    cl.io.copy_template(tmpl, to_path)
    print(f"Created file: {to_path}")

@app.command()
def login(
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., 
        prompt=True, confirmation_prompt= True, hide_input=True),
):
    data = cl.web.account.login(username,password)
    cl.io.dump_cookies('.session/cookies', data)


@app.command()
def get(source: str, file: str) -> str:
    process_file = cl.utils.get_data_from_source(source)
    return process_file(file)

@app.command()
def run(
        input: str, 
        id: str,
        source: str =  typer.Option("", "--source", "-s"),
        loc: cl.Location = typer.Option(cl.Location.STRONGHOLD, "--location", "-l"),
        save: bool = typer.Option(False, "--save", "-s"),
):
    print("what")
    if source: 
        input = get(source, input)

    solution = cl.utils.load_solution_module(id, loc)
    data = cl.io.parseInput(input)
    solution = solution.main(data)
    if save:
      cl.io.writeCache(f"solutions/{id}.txt", solution)

    print(solution)

test_help_remove = "replace the current test for exercise."

@app.command()
def test(
        id: str,
        loc: cl.Location = typer.Option(cl.Location.STRONGHOLD, "--location", "-l"),
        remove: bool = typer.Option(False, "--remove", "-r", help= test_help_remove),
):
    test = cl.tests.Test(id,loc)
    if remove:
        test.test_remove()

    if not test.test_exist():
        test.create_test()
    
    test.run_test()


if __name__ == "__main__":
    app()
