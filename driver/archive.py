from typing import Optional


class ArchiveParameter:
    def __init__(self, directory_save: str, title: str = None, mime_type: str = None, query: Optional[str] = None):
        self.directory_save = directory_save
        self.title = title
        self.mime_type = mime_type
        self.query = self.__create_query(query)
        self.__validate(query)

    def __create_query(self, query) -> str:
        if query is not None:
            return query
        return f"title contains '{self.title}' and mimeType = '{self.mime_type}'"

    def __validate(self, query):
        if self.title is None and self.mime_type is None and query is None:
            raise Exception('Invalid parameters!')
