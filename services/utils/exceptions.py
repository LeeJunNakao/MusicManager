class PersistenceError(Exception):
    def __init__(self, entity):
        self.entity = entity.capitalize()
        self.message = "Não foi possível salvar os dados devido um erro interno."
        super().__init__(self.message)

    def __str__(self):
        return f"{self.entity}: {self.message}"


class LoginError(Exception):
    def __init__(self):
        self.message = "Não foi possível fazer o login. Email ou senha incorretos."
        super().__init__(self.message)

    def __str__(self):
        return self.message


class CustomValidationError(Exception):
    def __init__(self, exception):
        self.exception = exception
        self._get_fields()
        self.get_message()

    def _get_fields(self):
        errors = self.exception.errors()
        self.fields = [error["loc"][0] for error in errors]

    def get_message(self):
        fields = ", ".join(field for field in self.fields)
        self.message = f"O(s) campo(s) {fields} foram informados incorretamente"
