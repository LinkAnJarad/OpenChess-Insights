from flask import Blueprint
from flask import render_template
from flask import request
import os
import chess_review

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template('index.html')

@views.route('/analysis', methods=['POST'])
def analyse():

    roast = False
    config = None

    if request.method == 'POST':
        pgn_data = request.form['pgn']
        print(request.form)
        time_limit = request.form['time-limit']
        depth_limit = request.form['depth-limit']

        config = {
            "limit_type": request.form['limits'],
            "time_limit": time_limit,
            "depth_limit": depth_limit,
            "roast": 'roastmode' in request.form
        }

    (
        san_moves, 
        fens, 
        scores,
        classification_list,
        review_list,
        best_review_list,
        san_best_moves,
        uci_best_moves,
        devs,
        tens,
        mobs,
        conts,
        white_acc,
        black_acc,
        white_elo_est,
        black_elo_est,
        average_cpl_white,
        average_cpl_black
     ) = chess_review.pgn_game_review(pgn_data=pgn_data, **config)

    return render_template('analysis.html',
            move_list = san_moves,
            fen_list = fens,
            score_list = scores,
            cls_list = classification_list,
            review_list = review_list,
            best_review_list = best_review_list,
            best_move_list = san_best_moves,
            best_move_uci_list = uci_best_moves,
            dev_list = devs,
            ten_list = tens,
            mob_list = mobs,
            cont_list = conts,
            acc_pair = [round(white_acc), round(black_acc)],
            elo_pair = [round(white_elo_est), round(black_elo_est)],
            acpl_pair = [round(average_cpl_white), round(average_cpl_black)]
        )