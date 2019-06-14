from flask import current_app as app
from flask import jsonify
from flask import Blueprint

bp_task_sms = Blueprint('task_sms', __name__)

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

@bp_task_sms.route('/calc_fib')
def calc_fib():
    app.executor.submit_stored('calc_fib', fib, 5)
    return jsonify({'result':'success'}), 200


@bp_task_sms.route('/get_fib')
def get_fib():
    if not app.executor.futures.done('calc_fib'):
        return jsonify({'status': app.executor.futures._state('calc_fib')})
    future = app.executor.futures.pop('calc_fib')
    return jsonify({'status': app.executor.futures.done('calc_fib'), 'result': future.result()})


