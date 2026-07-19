from airflow.models import BaseOperator
from hook.twitter_hook import TwitterHook
import json
from pathlib import Path


class TwitterOperator(BaseOperator):

    template_fields = ("query", "file_path", "end_time", "start_time")

    def __init__(self, file_path, end_time, start_time, query, **kwargs):
        super().__init__(**kwargs)
        self.file_path = file_path
        self.end_time = end_time
        self.start_time = start_time
        self.query = query

    def create_parent_folder(self):
        Path(self.file_path).parent.mkdir(parents=True, exist_ok=True)

    def execute(self, context):
        self.create_parent_folder()

        self.log.info(f"Salvando dados em: {self.file_path}")
        self.log.info(f"Query: {self.query}")
        self.log.info(f"Período: {self.start_time} → {self.end_time}")

        with open(self.file_path, "w", encoding="utf-8") as output_file:
            for pg in TwitterHook(
                self.end_time,
                self.start_time,
                self.query
            ).run():
                json.dump(pg, output_file, ensure_ascii=False)
                output_file.write("\n")

        self.log.info("Extração finalizada com sucesso!")