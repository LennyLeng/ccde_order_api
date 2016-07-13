#encoding=utf8
#! /bin/python

from flask import Flask, request
from flask_restful import Resource, Api
import json
import pgdb
import calccpk
import os

#import pdb

app = Flask(__name__)
api = Api(app)

class order_list(Resource):
    def get(self):
        try:
            db = pgdb.postgres_driver()
            begin_range = request.args.get('begin_range', '0001-01-01 00:00:00')
            end_range = request.args.get('end_range', '9999-12-31 00:00:00')
            data = db.read("SELECT id,proposer_name,proposer_work_phone,proposer_private_phone,proposer_vdi_login_name,proposer_mail_login_name,proposer_department,proposer_post,proposer_room_num,service_type,order_type,order_content,recv_unit,recv_operator_name,to_char(begin_time, 'YYYY-MM-DD HH24:MI:SS') AS begin_time ,to_char(end_time, 'YYYY-MM-DD HH24:MI:SS') AS end_time ,EXTRACT(epoch FROM cost_time) AS cost_time FROM orders WHERE begin_time >= %s AND begin_time <= %s", (begin_range, end_range))
            return data
        except pgdb.PostgresDriverException as e:
            return {"code":e.code,"msg":e.msg}
        except Exception as e:
            return {"code":500,"msg":("未知错误:%s" % str(e))}

    def post(self):
        try:
            data = json.loads(request.data)
            db = pgdb.postgres_driver()
            db.write("INSERT INTO orders (proposer_name,proposer_work_phone,proposer_private_phone,proposer_vdi_login_name,proposer_mail_login_name,proposer_department,proposer_post,proposer_room_num,service_type,order_type,order_content,recv_unit,recv_operator_name,begin_time,end_time,deal_content,cost_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, age(%s, %s)) RETURNING id", (data['proposer_name'], data['proposer_work_phone'], data['proposer_private_phone'], data['proposer_vdi_login_name'], data['proposer_mail_login_name'], data['proposer_department'], data['proposer_post'] , data['proposer_room_num'], data['service_type'], data['order_type'], data['order_content'], data['recv_unit'], data['recv_operator_name'], data['begin_time'], data['end_time'], data['deal_content'], data['end_time'], data['begin_time']))
            data = None
            order_id = db.write_ret_val()
            data = db.read("SELECT id,proposer_name,proposer_work_phone,proposer_private_phone,proposer_vdi_login_name,proposer_mail_login_name,proposer_department,proposer_post,proposer_room_num,service_type,order_type,order_content,recv_unit,recv_operator_name,to_char(begin_time, 'YYYY-MM-DD HH24:MI:SS') AS begin_time ,to_char(end_time, 'YYYY-MM-DD HH24:MI:SS') AS end_time ,EXTRACT(epoch FROM cost_time) AS cost_time FROM orders WHERE id = %s", (order_id, ))
            return data
        except pgdb.PostgresDriverException as e:
            return {"code":e.code,"msg":e.msg}
        except Exception as e:
            return {"code":500,"msg":("未知错误:%s" % str(e))}

class order(Resource):
    def get(self, order_id):
        try:
            db = pgdb.postgres_driver()
            data = db.read("SELECT id,proposer_name,proposer_work_phone,proposer_private_phone,proposer_vdi_login_name,proposer_mail_login_name,proposer_department,proposer_post,proposer_room_num,service_type,order_type,order_content,recv_unit,recv_operator_name,to_char(begin_time, 'YYYY-MM-DD HH24:MI:SS') AS begin_time ,to_char(end_time, 'YYYY-MM-DD HH24:MI:SS') AS end_time ,EXTRACT(epoch FROM cost_time) AS cost_time FROM orders WHERE id = %s", (order_id, ))
            return data
        except pgdb.PostgresDriverException as e:
            return {"code":e.code,"msg":e.msg}
        except Exception as e:
            return {"code":500,"msg":("未知错误:%s" % str(e))}

    def put(self, order_id):

        try:
            data = json.loads(request.data)
            db = pgdb.postgres_driver()
            data = db.write("UPDATE orders SET (proposer_name,proposer_work_phone,proposer_private_phone,proposer_vdi_login_name,proposer_mail_login_name,proposer_department,proposer_post,proposer_room_num,service_type,order_type,order_content,recv_unit,recv_operator_name,begin_time,end_time,deal_content,cost_time) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, age(%s, %s)) WHERE id = %s", (data['proposer_name'], data['proposer_work_phone'], data['proposer_private_phone'], data['proposer_vdi_login_name'], data['proposer_mail_login_name'], data['proposer_department'], data['proposer_post'] , data['proposer_room_num'], data['service_type'], data['order_type'], data['order_content'], data['recv_unit'], data['recv_operator_name'], data['begin_time'], data['end_time'], data['deal_content'], data['end_time'], data['begin_time'], order_id))
            data = None
            data = db.read("SELECT id,proposer_name,proposer_work_phone,proposer_private_phone,proposer_vdi_login_name,proposer_mail_login_name,proposer_department,proposer_post,proposer_room_num,service_type,order_type,order_content,recv_unit,recv_operator_name,to_char(begin_time, 'YYYY-MM-DD HH24:MI:SS') AS begin_time ,to_char(end_time, 'YYYY-MM-DD HH24:MI:SS') AS end_time ,EXTRACT(epoch FROM cost_time) AS cost_time FROM orders WHERE id = %s", (order_id, ))
            return data
        except pgdb.PostgresDriverException as e:
            return {"code":e.code,"msg":e.msg}
        except Exception as e:
            return {"code":500,"msg":("未知错误:%s" % str(e))}



class analysis(Resource):
    def get(self):
        try:
            db = pgdb.postgres_driver()
            begin_range = request.args.get('begin_range', '0001-01-01 00:00:00')
            end_range = request.args.get('end_range', '9999-12-31 00:00:00')


            data = db.read("SELECT COUNT(*) AS order_count FROM orders WHERE begin_time >= %s AND begin_time <= %s", (begin_range, end_range))
            order_count = data[0]['order_count']
            data = db.read("SELECT EXTRACT(epoch FROM cost_time) AS cost_time FROM orders WHERE begin_time >= %s AND begin_time <= %s", (begin_range, end_range))
            val_data = []
            for item in data:
                val_data.append(item['cost_time'])

            data = {}
            data['order_count'] = order_count
            data['max_cost_time'] = max(val_data)
            data['min_cost_time'] =  min(val_data)
            data['avg_cost_time'] = sum(val_data) / len(val_data)
            data['mid_cost_time'] = val_data[len(val_data) // 2]

            data['cp_cost_time'] = float(calccpk.cp(val_data, int(os.getenv('CPK_TOPLIMIT_SEC')), 0))
            if data['cp_cost_time'] == float('inf') or data['cp_cost_time'] == float('-inf'):
                data['cp_cost_time'] = str(data['cp_cost_time'])

            data['cpk_cost_time'] = float(calccpk.cpk(val_data, int(os.getenv('CPK_TOPLIMIT_SEC')), 0))
            if data['cpk_cost_time'] == float('inf') or data['cpk_cost_time'] == float('-inf'):
                data['cpk_cost_time'] = str(data['cpk_cost_time'])

            #pdb.set_trace()

            return data

        except pgdb.PostgresDriverException as e:
            return {"code":e.code,"msg":e.msg}
        except Exception as e:
            return {"code":500,"msg":("未知错误:%s" % str(e))}

api.add_resource(order_list, '/orders')
api.add_resource(order, '/orders/<order_id>')
api.add_resource(analysis, '/orders/analysis')

if __name__ == '__main__':
    app.run(debug=True)
