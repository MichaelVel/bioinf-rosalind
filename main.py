import typer

import client.utilities as cl
from client.tests import Test

app = typer.Typer()

@app.command()
def create(
        id: str,
        loc: cl.Location = typer.Option(cl.Location.STRONGHOLD, "--location", "-l"),
        tmpl: cl.Template = typer.Option(cl.Template.simple, "--template", "-t")
):
    to_path = f"{cl.Location.package()}/{loc.module()}/{id}.py"
    cl.copy_template(tmpl, to_path)
    print(f"Created file: {to_path}")


@app.command()
def get(source: str, file: str) -> str:
    process_file = cl.get_data_from_source(source)
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

    solution = cl.load_solution_module(id, loc)
    data = cl.parseInput(input)
    solution = solution.main(data)
    if save:
      cl.writeCache(f"solutions/{id}.txt", solution)

    print(solution)

test_help_remove = "replace the current test for exercise."

@app.command()
def test(
        id: str,
        loc: cl.Location = typer.Option(cl.Location.STRONGHOLD, "--location", "-l"),
        remove: bool = typer.Option(False, "--remove", "-r", help= test_help_remove),
):
    test = Test(id,loc)
    if remove:
        test.test_remove()

    if not test.test_exist():
        test.create_test()
    
    test.run_test()


if __name__ == "__main__":
    app()
