from textwrap import dedent
import typer

import client as cl

app = typer.Typer()

@app.command(help="create a solution file from a template.")
def create(
        id: str = typer.Argument(..., help="A valid rosalind id."),
        tmpl: cl.Template = typer.Option(
            cl.Template.simple,
            "--template", "-t",
            help="Choose one of the existing templates.")
):
    to_path = f"{cl.Location.package()}/{loc.module()}/{id}.py"
    cl.io.copy_template(tmpl, to_path)
    print(f"Created file: {to_path}")


@app.command(help="create an empty workspace inside current directory.")
def init(dir_name: str = typer.Argument("default")):
    if cl.workspace.validate_workspace(): 
        print(dedent("""Error creating a new workspace inside a 
            valid rosalind-cli workspace"""))
        return 

    d_name = dir_name if dir_name != "default" else None
    cl.workspace.create_workspace(d_name)


@app.command(help="login to rosalind page, and store session data.")
def login(
    username: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., 
        prompt=True, confirmation_prompt= True, hide_input=True),
):
    try:
        data = cl.web.account.login(username,password)
    except cl.web.exceptions.UnauthorizedAccessException as e:
        print(e)
    else:
        print(f"Welcome {username}, you are now succesfully logged in.")
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
        save: bool = typer.Option(
            False,
            "--save", "-s",
            help=dedent("""Set if you want to save the answer to a file,
                        if not print to stdout.""")),
):
    solution = cl.utils.load_solution_module(id, loc) # TODO: modify 
    data = cl.io.parseInput(input)
    solution = solution.main(data)

    if save:
        cl.io.writeCache(f"solutions/{id}.txt", solution)
    else:
        print(solution)

@app.command(help="Submit your solution to rosalind.") 
def submit(
        id: str = typer.Argument(..., help="A valid rosalind id."),
        publish: bool = typer.Option(
            False,
            "--publish", "-p",
            help= "set if you want to publish to rosalind your source file"),
        save: bool = typer.Option(
            False,
            "--save", "-s",
            help=dedent("""Set if you want to save the challenge data from 
                        rosalind web page.""")),
):
    cookies = cl.io.load_cookies(".session/cookies")
    exercise = cl.web.exercises.Exercise(id,cookies)
    data = exercise.problem_dataset()
    
    solution = cl.utils.load_solution_module(id, loc) # TODO: modify
    solution = solution.main(data)
    
    solution_filename = f"solutions/{id}.txt"
    cl.io.writeCache(solution_filename, solution)

    # submit solution and assert if the answer is correct and print to stdout.
    try:
        submit_cookies = exercise.submit(solution_filename)
    except cl.web.exceptions.WrongAnswerException:
        log_data = f"data/{id}_WRONG_ANWER_DATA_LOG.txt" 
        log_solution = f"solutions/{id}_WRONG_ANWER_SOLUTION_LOG.txt" 
        cl.io.writeCache(log_data, data)
        cl.io.writeCache(log_solution, solution)
        print(dedent(f"""\
            Wrong Answer: Modify your answer and try again. You can find
            a data copy in {log_data} and a copy of the output solution 
            at {log_solution}."""))
    except cl.web.exceptions.UnauthorizedAccessException:
        print("You are not logged in. Please login and try again.")
        return
    else:
        print("Congratulations, correct Answer!!")
        cl.io.dump_cookies('.session/cookies', submit_cookies)

    if save:
        cl.io.writeCache(f"data/{id}_SAVED.txt", data)

    if publish: print("Publish is currently unimplemented.")



@app.command(help="""\
test your solution with the default example of the problem page.""")
def test(
        id: str = typer.Argument(..., help="A valid rosalind id."),
        reset: bool = typer.Option(
            False,
            "--remove", "-r",
            help= dedent("""Set this flag to reset the tests of problems 
                         to the default test. useful when you have made 
                         changes to the page and want a clean start.""")),
):
    test = cl.tests.Test(id,loc) # TODO: modify
    if reset:
        test.test_remove()

    if not test.test_exist():
        test.create_test()
    
    test.run_test()


if __name__ == "__main__":
    app()
