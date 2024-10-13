
class Legislator:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Vote:
    def __init__(self, id, bill_id):
        self.id = id
        self.bill_id = bill_id


class VoteResult:
    def __init__(self, id, legislator_id, vote_id, vote_type):
        self.id = id
        self.legislator_id = legislator_id
        self.vote_id = vote_id
        self.vote_type = vote_type


class Bill:
    def __init__(self, id, title, sponsor_id):
        self.id = id
        self.title = title
        self.sponsor_id = sponsor_id
