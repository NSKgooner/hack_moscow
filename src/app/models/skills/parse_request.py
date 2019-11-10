class ParseRequest:

    def __init__(self):
        self.email = None
        self.known = []
        self.unknown = []
        self._skills = []

    def _get_data_from_request(self, request):
        try:
            return request['skillsItemUiModel']
        except KeyError:
            return []

    def _set_skills(self, request):
        data = self._get_data_from_request(request)
        for elem in data:
            self._skills.append({'name': elem['name'],
                                 'selected': elem['selected']['mValue'],
                                 })

    def _set_email(self, request):
        self.email = request['email'].lower()

    def set_email_known_unknown(self, request):
        self._set_email(request)
        self._set_skills(request)
        for skill in self._skills:
            if skill['selected']:
                self.known.append(skill['name'])
            else:
                self.unknown.append(skill['name'])
