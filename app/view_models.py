class VoteResultViewModel:
    def __init__(self, legislator_name: str,
                 bill_id: str,
                 bill_title: str,
                 vote_type):

        self.legislator_name = legislator_name
        self.bill_id = bill_id
        self.bill_title = bill_title
        self.vote_type = vote_type


class BillVoteViewModel:
    def __init__(self, legislator_name: str,
                 legislator_id: str,
                 vote_type: int):

        self.legislator_name = legislator_name
        self.legislator_id = legislator_id
        self.vote_type = vote_type
