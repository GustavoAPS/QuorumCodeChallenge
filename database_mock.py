from app.models import Legislator, VoteResult, Bill, Vote
import csv


# mock database acess
def get_legislators() -> list[Legislator]:
    legislators = []
    with open('app/data/legislators.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            legislator = Legislator(id=int(row['id']), name=row['name'])
            legislators.append(legislator)
    return legislators


def get_legislator_by_id(id) -> Legislator:
    legislators = get_legislators()
    for legislator in legislators:
        if legislator.id == id:
            return legislator
    return None


def get_vote_results() -> list[VoteResult]:
    vote_results = []
    with open('app/data/vote_results.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote_result = VoteResult(id=int(row['id']),
                                     legislator_id=int(row['legislator_id']),
                                     vote_id=int(row['vote_id']),
                                     vote_type=int(row['vote_type']))
            vote_results.append(vote_result)
    return vote_results


def get_vote_results_by_legislator_id(legislator_id) -> list[VoteResult]:
    legislator_vote_results = []
    vote_results = get_vote_results()
    for vote_result in vote_results:
        if vote_result.legislator_id == legislator_id:
            legislator_vote_results.append(vote_result)
    return legislator_vote_results


def get_vote_by_id(vote_id) -> Vote:
    with open('app/data/votes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vote_result = Vote(id=int(row['id']), bill_id=int(row['bill_id']))
            if vote_result.id == vote_id:
                return vote_result
    return None


def get_bill_by_id(bill_id) -> Bill:
    with open('app/data/bills.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bill_result = Bill(id=int(row['id']),
                               title=str(row['title']),
                               sponsor_id=str(row['sponsor_id']))
            if bill_result.id == bill_id:
                return bill_result
    return None


def get_bills() -> list[Bill]:
    bill_list = []
    with open('app/data/bills.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bill_result = Bill(id=int(row['id']),
                               title=str(row['title']),
                               sponsor_id=str(row['sponsor_id']))
            bill_list.append(bill_result)
    return bill_list


def get_vote_results_by_bill_id(bill_id) -> list[VoteResult]:

    vote_results = get_vote_results()
    filtered_results = []

    for vote_result in vote_results:
        # Get the vote associated with the vote_result
        vote = get_vote_by_id(vote_result.vote_id)
        if vote and vote.bill_id == bill_id:
            filtered_results.append(vote_result)

    return filtered_results


def count_vote_types(vote_results, vote_type):
    return sum(1 for vote_result in vote_results if vote_result.vote_type == vote_type)
