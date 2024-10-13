from flask import Blueprint, render_template
from app.view_models import BillVoteViewModel
from app.database_mock import (
    get_bills, get_bill_by_id,
    get_vote_results_by_bill_id,
    get_legislator_by_id,
    count_vote_types
)


bill_bp = Blueprint('bill', __name__)


@bill_bp.route('/bills')
def bills():
    bill_list = get_bills()
    amount_of_bills = len(bill_list)
    return render_template('bills.html',
                           bill_list=bill_list,
                           amount_of_bills=amount_of_bills)


@bill_bp.route('/bill/<int:id>', methods=['GET'])
def bill(id):
    view_models = []
    vote_results = get_vote_results_by_bill_id(id)
    for vote_result in vote_results:
        legislator = get_legislator_by_id(vote_result.legislator_id)
        new_model = BillVoteViewModel(legislator_name=legislator.name,
                                      legislator_id=legislator.id,
                                      vote_type=vote_result.vote_type)
        view_models.append(new_model)
    return render_template('bill_detail.html',
                           bill=get_bill_by_id(id),
                           view_models=view_models,
                           supports=count_vote_types(vote_results, 1),
                           opositions=count_vote_types(vote_results, 2))
