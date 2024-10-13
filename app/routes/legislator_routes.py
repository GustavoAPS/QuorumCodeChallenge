from flask import Blueprint, render_template
from app.view_models import VoteResultViewModel
from app.database_mock import (
    get_legislators,
    get_legislator_by_id,
    get_vote_results_by_legislator_id,
    get_vote_by_id,
    get_bill_by_id,
    count_vote_types
)

legislator_bp = Blueprint('legislator', __name__)


@legislator_bp.route('/')
def index():
    legislator_list = get_legislators()
    amount_of_legislators = len(legislator_list)
    return render_template('index.html',
                           legislator_list=legislator_list,
                           amount_of_legislators=amount_of_legislators)


@legislator_bp.route('/legislators/<int:id>', methods=['GET'])
def legislator(id):

    legislator = get_legislator_by_id(id)
    vote_results = get_vote_results_by_legislator_id(id)
    vote_result_view_models = []

    for vote_result in vote_results:
        vote = get_vote_by_id(vote_result.vote_id)
        bill = get_bill_by_id(vote.bill_id)
        new_view = VoteResultViewModel(legislator_name=legislator.name,
                                       bill_id=bill.id,
                                       bill_title=bill.title,
                                       vote_type=vote_result.vote_type)
        vote_result_view_models.append(new_view)

    return render_template('legislator.html',
                           legislator=legislator,
                           supports=count_vote_types(vote_results, 1),
                           opositions=count_vote_types(vote_results, 2),
                           total_votes=len(vote_results),
                           vote_result_view_models=vote_result_view_models)
