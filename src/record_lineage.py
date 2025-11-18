import uuid, json
from datetime import datetime
from pathlib import Path

try:
    from openlineage.client import OpenLineageClient, RunEvent, RunState, Dataset, Job, Run
    CONFIG_PATH = Path(__file__).resolve().parents[1] / "openlineage.yml"
    client = OpenLineageClient.from_yaml(str(CONFIG_PATH))
except:
    client = None

def log_lineage(job_name, input_paths, output_paths, description=""):
    run_id = str(uuid.uuid4())
    event_time = datetime.utcnow().isoformat()

    if client:
        try:
            event = RunEvent(
                eventTime=event_time,
                eventType=RunState.COMPLETE,
                run=Run(runId=run_id),
                job=Job(namespace="training-provenance", name=job_name),
                inputs=[Dataset(namespace="local", name=p) for p in input_paths],
                outputs=[Dataset(namespace="local", name=p) for p in output_paths],
                producer="training-provenance-system"
            )
            client.emit(event)
            return
        except:
            pass

    log_dir = Path(__file__).resolve().parents[1] / "lineage"
    log_dir.mkdir(exist_ok=True)
    with open(log_dir / "events.log", "a") as f:
        f.write(json.dumps({
            "eventTime": event_time,
            "job": job_name,
            "inputs": input_paths,
            "outputs": output_paths,
            "desc": description
        }) + "\n")
