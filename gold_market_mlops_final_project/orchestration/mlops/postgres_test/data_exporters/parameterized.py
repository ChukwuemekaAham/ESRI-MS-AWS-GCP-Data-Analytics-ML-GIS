from mage_ai.io.file import FileIO
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    now = kwargs.get("execution_date")
    print(now)

    print(now.day)

    print(now.strftime("%Y/%m/%d"))

    object_key = f'{now_fpath/daily_data.parquet}'

    print(object_key)