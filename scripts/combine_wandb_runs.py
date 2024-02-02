import wandb
from wandb.wandb_run import Run

dst_entity = "ai2-llm"
dst_project = "OLMo-7B"

# Read CSV dump from "OLMo Runs" spreadsheet.
#  runs_path = Path("~/Downloads/OLMo Runs - mitchish-mcli.csv").expanduser()
#  run_paths_to_copy = []
#  with runs_path.open("r") as f:
#      reader = csv.DictReader(f, delimiter=",")
#      for row in reader:
#          run_paths_to_copy.append(row["W&B URL"].replace("https://wandb.ai/", ""))

#      # Order oldest -> newest.
#      run_paths_to_copy = list(reversed(run_paths_to_copy))

runs_to_copy = [
    ("ai2-llm/olmo-medium/runs/wvc30anm", "OLMo-7B-run-001", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/uhy9bs35", "OLMo-7B-run-002", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/l6v218f4", "OLMo-7B-run-003", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/8fioq3qx", "OLMo-7B-run-004", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/mk9kaqh0", "OLMo-7B-run-005", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/49i87wpn", "OLMo-7B-run-006", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/0j2eqydw", "OLMo-7B-run-007", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/5wkmhkqh", "OLMo-7B-run-008", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/hrshlkzq", "OLMo-7B-run-009", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/eysi0t0y", "OLMo-7B-run-010", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/7gomworq", "OLMo-7B-run-011", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/lyij2l8m", "OLMo-7B-run-012", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/99euueq4", "OLMo-7B-run-013", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/fcn5q3zw", "OLMo-7B-run-014", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/j18wauyq", "OLMo-7B-run-015", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/jtfwv96r", "OLMo-7B-run-016", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/yuc5kl7s", "OLMo-7B-run-017", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/25urleov", "OLMo-7B-run-018", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/obde4w9j", "OLMo-7B-run-019", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/eaqax5ns", "OLMo-7B-run-020", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/cojbrc1o", "OLMo-7B-run-021", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/4xel5n7e", "OLMo-7B-run-022", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/jcs4c32w", "OLMo-7B-run-023", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/x55jyv7k", "OLMo-7B-run-024", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/yv7lgx0i", "OLMo-7B-run-025", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/11uf7gsv", "OLMo-7B-run-026", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/lds6zcog", "OLMo-7B-run-027", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/ho7jy4ey", "OLMo-7B-run-028", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/87shig0a", "OLMo-7B-run-029", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/x6zdcp5j", "OLMo-7B-run-030", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/olocmvn0", "OLMo-7B-run-031", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/xtruaap8", "OLMo-7B-run-032", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/2l070ogq", "OLMo-7B-run-033", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/uy2ydw12", "OLMo-7B-run-034", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/x23ciyv9", "OLMo-7B-run-035", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/67i5mdg0", "OLMo-7B-run-036", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/wrv46m83", "OLMo-7B-run-037", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/wd2gxrza", "OLMo-7B-run-038", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/z4z0x4m9", "OLMo-7B-run-039", "OLMo-7B"),
    ("ai2-llm/olmo-medium/runs/p067ktg9", "OLMo-7B-Tulu", "OLMo-7B-Tulu"),
]

# Set your API key
wandb.login()

# Initialize the wandb API
api = wandb.Api()

# Iterate through the runs and copy them to the destination project
for run_path, new_run_name, new_run_group in runs_to_copy:
    run = api.run(run_path)

    print(f"Copying run '{run_path}' to '{new_run_name}'...")

    # Get the run history and files
    history = run.scan_history()

    # Create a new run in the destination project
    new_run = wandb.init(
        project=dst_project,
        entity=dst_entity,
        config=run.config,
        name=new_run_name,
        resume="allow",
        group=new_run_group,
        settings=wandb.Settings(_disable_stats=True),
    )
    assert isinstance(new_run, Run)

    # Log the history to the new run
    for data in history:
        step = data.pop("_step")
        new_run.log(data, step=step)

    # Finish the new run
    new_run.finish()
