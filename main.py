import typer

import client.utilities as cl

app = typer.Typer()

@app.command()
def create(name: str):
    return None

@app.command()
def get(source: str, file: str) -> str:
    process_file = cl.get_data_from_source(source)
    return process_file(file)


@app.callback(invoke_without_command=True)
def main(input: str, id: str, source: str =  typer.Option("")):
    if source: 
        input = get(source, input)

    solution = cl.load_solution_module(id)
    data = cl.parseInput(input)
    solution = solution.main(data)

    print(solution)


if __name__ == "__main__":
    app()
