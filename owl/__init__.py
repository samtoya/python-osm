from core.file_helper import FileWriter


class Owl:
    @classmethod
    def save_country_to_file(cls, filename, data, directory='localized_countries'):
        FileWriter.save(filename=filename, data=data, directory=directory)

    @staticmethod
    def save_output(data, filename, directory='localized_countries'):
        FileWriter.save(filename=filename, data=data, directory=directory)
        pass
