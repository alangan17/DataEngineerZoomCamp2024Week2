import pyarrow as pa
import pyarrow.parquet as pq
import os

if "data_exporter" not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/src/keys/my-creds.json"
    bucket_name = kwargs.get("sink_bucket_name")
    project_id = kwargs.get("sink_gcp_project_id")

    table_name = kwargs.get("sink_table_name")

    root_path = f"{bucket_name}/{table_name}"

    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=kwargs.get("sink_partition_cols_list"),
        filesystem=gcs,
    )

    print(f"Data exported to {root_path}")
